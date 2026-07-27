/**
 * Server-side progress store: interface + types only.
 *
 * The actual Node implementation lives in `progressStore.node.ts`. Keeping
 * the interface portable (no `node:` imports here) means the Vercel and
 * Cloudflare adapters can substitute a different store later (Durable
 * Object, KV, D1, Postgres) without changing `server/app.ts`.
 *
 * Schema on disk (and in memory):
 *   {
 *     "version": 1,
 *     "users": {
 *       "<userId>": {
 *         "lessons":   { "<topicId>": ["<lessonId>", ...] },
 *         "exercises": { "<topicId>": { "attempted": N, "correct": N } },
 *         "updatedAt": "2026-07-27T..."
 *       }
 *     }
 *   }
 *
 * This mirrors `src/lib/storage.ts` Progress shape so the client can
 * PUT its local progress verbatim. Merge semantics are the client's job
 * (union of lessons, max of per-topic counters).
 */

export interface ProgressBody {
  lessons: Record<string, string[]>
  exercises: Record<string, { attempted: number; correct: number }>
}

export interface UserProgress extends ProgressBody {
  /** ISO timestamp of the last successful PUT. */
  updatedAt: string
}

export interface ServerStore {
  version: 1
  users: Record<string, UserProgress>
}

export interface ProgressStore {
  /** Read the entire store. Used on boot and by handlers that need
   *  fresh data; subsequent reads should use `get`. */
  load(): Promise<ServerStore>
  /** Write the entire store. Atomic on Node (temp + rename). */
  save(store: ServerStore): Promise<void>
  /** Read one user's progress, or `null` if they have none yet. */
  get(userId: string): Promise<UserProgress | null>
  /** Merge `patch` into the user's record and persist. */
  put(userId: string, patch: ProgressBody): Promise<UserProgress>
}

/** Validate an incoming progress PUT body. Returns the parsed shape or null. */
export function parseProgressBody(x: unknown): ProgressBody | null {
  if (!x || typeof x !== 'object') return null
  const r = x as Record<string, unknown>
  if (!r.lessons || typeof r.lessons !== 'object') return null
  if (!r.exercises || typeof r.exercises !== 'object') return null
  const lessons: Record<string, string[]> = {}
  for (const [topicId, arr] of Object.entries(r.lessons as Record<string, unknown>)) {
    if (!Array.isArray(arr)) return null
    const cleaned: string[] = []
    for (const item of arr) if (typeof item === 'string') cleaned.push(item)
    if (cleaned.length > 0) lessons[topicId] = cleaned
  }
  const exercises: Record<string, { attempted: number; correct: number }> = {}
  for (const [topicId, counters] of Object.entries(r.exercises as Record<string, unknown>)) {
    if (!counters || typeof counters !== 'object') return null
    const c = counters as Record<string, unknown>
    const attempted = typeof c.attempted === 'number' && c.attempted >= 0 ? Math.floor(c.attempted) : null
    const correct = typeof c.correct === 'number' && c.correct >= 0 ? Math.floor(c.correct) : null
    if (attempted === null || correct === null) return null
    if (attempted === 0 && correct === 0) continue // skip empty topics
    exercises[topicId] = { attempted, correct: Math.min(correct, attempted) }
  }
  return { lessons, exercises }
}

/** Empty store, used when the on-disk file is missing or corrupt. */
export function emptyStore(): ServerStore {
  return { version: 1, users: {} }
}