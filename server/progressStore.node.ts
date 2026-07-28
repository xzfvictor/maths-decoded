/**
 * Node fs implementation of the progress store.
 *
 * - Reads `data/progress.json` on boot into an in-memory cache.
 * - Writes are atomic: write to `progress.json.tmp`, then `rename`.
 * - On boot, if the file is corrupt or unparseable, it's renamed to
 *   `progress.json.bak.<iso>` and the store starts empty.
 *
 * Caveats:
 * - Single-process only. Concurrent processes will see stale reads.
 * - The whole file is rewritten on every PUT. Fine for a small user base;
 *   a serious multi-user deploy wants SQLite/Postgres.
 */

import * as fs from 'node:fs/promises'
import * as path from 'node:path'
import { log } from './logger'
import {
  emptyStore,
  type ProgressStore,
  type ServerStore,
  type UserProgress,
} from './progressStore'

const FILE_NAME = 'progress.json'
const TMP_SUFFIX = '.tmp'
const BAK_SUFFIX = '.bak'

export function makeNodeProgressStore(dataDir: string): ProgressStore {
  const filePath = path.join(dataDir, FILE_NAME)

  async function ensureDir(): Promise<void> {
    await fs.mkdir(dataDir, { recursive: true })
  }

  async function load(): Promise<ServerStore> {
    await ensureDir()
    let raw: string
    try {
      raw = await fs.readFile(filePath, 'utf8')
    } catch (e) {
      // File doesn't exist — first boot is a happy path.
      if ((e as NodeJS.ErrnoException).code === 'ENOENT') {
        return emptyStore()
      }
      log('store.read.error', { error: String(e) })
      return emptyStore()
    }
    try {
      const parsed = JSON.parse(raw) as ServerStore
      if (!parsed || typeof parsed !== 'object' || !parsed.users) return emptyStore()
      // Normalize: drop any malformed user entries rather than crash.
      const users: ServerStore['users'] = {}
      for (const [userId, rec] of Object.entries(parsed.users)) {
        if (!rec || typeof rec !== 'object') continue
        const lessons = (rec.lessons && typeof rec.lessons === 'object') ? rec.lessons : {}
        const exercises = (rec.exercises && typeof rec.exercises === 'object') ? rec.exercises : {}
        users[userId] = {
          lessons,
          exercises,
          updatedAt: typeof rec.updatedAt === 'string' ? rec.updatedAt : new Date().toISOString(),
        }
      }
      return { version: 1, users }
    } catch (e) {
      // Corruption: back up the bad file and start fresh.
      const bakPath = `${filePath}${BAK_SUFFIX}.${new Date().toISOString().replace(/[:.]/g, '-')}`
      try {
        await fs.rename(filePath, bakPath)
        log('store.corrupt.backup', { bakPath, error: String(e) })
      } catch {
        log('store.corrupt.backup_failed', { error: String(e) })
      }
      return emptyStore()
    }
  }

  async function save(store: ServerStore): Promise<void> {
    await ensureDir()
    const tmpPath = `${filePath}${TMP_SUFFIX}`
    await fs.writeFile(tmpPath, JSON.stringify(store, null, 2), 'utf8')
    await fs.rename(tmpPath, filePath)
  }

  let cache: ServerStore | null = null
  let writeChain: Promise<void> = Promise.resolve()

  async function getCache(): Promise<ServerStore> {
    if (cache === null) cache = await load()
    return cache
  }

  return {
    async load() {
      return getCache()
    },

    async save(store) {
      cache = store
      // Serialize writes so a flurry of PUTs doesn't race the rename.
      writeChain = writeChain.then(() => save(store)).catch((e) => {
        log('store.write.error', { error: String(e) })
        throw e
      })
      await writeChain
    },

    async get(userId) {
      const c = await getCache()
      return c.users[userId] ?? null
    },

    async put(userId, patch) {
      const c = await getCache()
      const existing = c.users[userId]
      // Per-topic max(attempted) and max(correct) on the server side too —
      // a defensive merge in case the client forgot. This is what the
      // client's `mergeProgress` already does, but the server is the
      // source of truth, so apply the same rule.
      const lessons: Record<string, string[]> = { ...(existing?.lessons ?? {}) }
      for (const [topicId, ids] of Object.entries(patch.lessons)) {
        const merged = new Set([...(lessons[topicId] ?? []), ...ids])
        lessons[topicId] = [...merged]
      }
      const exercises: Record<string, { attempted: number; correct: number }> = {
        ...(existing?.exercises ?? {}),
      }
      for (const [topicId, next] of Object.entries(patch.exercises)) {
        const cur = exercises[topicId]
        if (!cur) {
          exercises[topicId] = { ...next }
        } else {
          exercises[topicId] = {
            attempted: Math.max(cur.attempted, next.attempted),
            correct: Math.max(cur.correct, next.correct),
          }
        }
      }
      const updated: UserProgress = {
        lessons,
        exercises,
        updatedAt: new Date().toISOString(),
      }
      c.users[userId] = updated
      await this.save(c)
      return updated
    },
  }
}