/**
 * Hono app definition — pure Hono, no `node:` imports.
 * Portable to Node (via `server/index.ts`), Vercel (`api/*.ts` via
 * `@hono/vercel` adapter), and Cloudflare Workers (`worker/index.ts`).
 *
 * Note: the regenerate-exercise handler still reads `process.env.ANTHROPIC_*`
 * directly because Hono's `process.env` access pattern is shared with the
 * existing pre-change behaviour; everything new (auth, progress, dev-login)
 * is injected via `createApp({ auth, store })` so deploys without env
 * (Vercel Edge, Cloudflare Workers) can substitute their own values.
 *
 * Endpoints:
 *   GET  /api/health
 *   POST /api/regenerate-exercise           — AI exercise regeneration
 *   POST /api/auth/dev-login                — mock SSO (dev only, 404 in prod)
 *   POST /api/auth/logout
 *   GET  /api/auth/me                       — current session or 401
 *   GET  /api/progress                      — server progress for current user
 *   PUT  /api/progress                      — write-through (CSRF-guarded)
 *
 * Session strategy: HMAC-SHA256 signed cookie (`md_sid`), payload
 * {userId, displayName, email, iat}. Verification accepts an ordered list
 * of secrets so rotation is graceful.
 *
 * Every user click of "Sign in with Google" mints a brand-new identity.
 * The eventual swap to real Google OAuth replaces only `dev-login` with a
 * Google-token-verifying endpoint that calls the same `signSession` +
 * `buildSetCookie` helpers. Everything downstream stays unchanged.
 */

import { Hono } from 'hono'
import type { Difficulty, ExerciseInstance } from '../src/content/types'
import { topicById } from '../src/content/topics'
import { callRegenerate } from './m3'
import { log } from './logger'
import { clientIp, consume } from './ratelimit'
import {
  type AuthConfig,
  buildClearCookie,
  buildSetCookie,
  isSafeCsrf,
  parseCookies,
  randomDisplayName,
  randomEmail,
  randomUserId,
  readSessionCookie,
  signSession,
  verifySession,
  type Session,
} from './auth'
import {
  parseProgressBody,
  type ProgressStore,
} from './progressStore'

export interface AppDeps {
  auth: AuthConfig
  store: ProgressStore
}

export function createApp(deps: AppDeps): Hono {
  const { auth, store } = deps
  const app = new Hono().basePath('/api')

  // -----------------------------------------------------------------------
  // Session middleware — runs on every request. Reads `md_sid`, verifies,
  // attaches `userId` and `session` to context for downstream handlers.
  // -----------------------------------------------------------------------
  app.use('*', async (c, next) => {
    const cookies = parseCookies(c.req.header('cookie'))
    const token = readSessionCookie(cookies)
    const session = token ? await verifySession(token, auth.secrets) : null
    c.set('userId', session?.userId)
    c.set('session', session)
    await next()
  })

  // -----------------------------------------------------------------------
  // Health probe.
  // -----------------------------------------------------------------------
  app.get('/health', (c) => c.json({ ok: true, ts: Date.now() }))

  // -----------------------------------------------------------------------
  // Mock SSO — exists in dev mode so the client can ship the "Sign in with
  // Google" UI without waiting for real Google OAuth integration. Returns
  // 404 when `auth.devMode` is false so prod deploys never expose it.
  // -----------------------------------------------------------------------
  app.post('/auth/dev-login', async (c) => {
    if (!auth.devMode) {
      return c.json({ error: 'not_found' }, 404)
    }
    const displayName = randomDisplayName()
    const session: Session = {
      userId: randomUserId(),
      displayName,
      email: randomEmail(displayName),
      iat: Date.now(),
    }
    const token = await signSession(session, auth.secrets[0])
    return c.json(
      { userId: session.userId, displayName: session.displayName, email: session.email },
      200,
      {
        'Set-Cookie': buildSetCookie(token, {
          maxAgeSec: auth.cookieMaxAgeSec,
          secure: auth.secureCookies,
        }),
        'Cache-Control': 'no-store',
      },
    )
  })

  app.post('/auth/logout', (c) =>
    c.json(
      { ok: true },
      200,
      {
        'Set-Cookie': buildClearCookie(),
        'Cache-Control': 'no-store',
      },
    ),
  )

  app.get('/auth/me', (c) => {
    const session = c.get('session')
    if (!session) return c.json({ error: 'unauthorized' }, 401)
    return c.json(
      { userId: session.userId, displayName: session.displayName, email: session.email },
      200,
      { 'Cache-Control': 'no-store' },
    )
  })

  // -----------------------------------------------------------------------
  // Server-side progress store — gated by the session middleware.
  // -----------------------------------------------------------------------
  app.get('/progress', async (c) => {
    const userId = c.get('userId')
    if (!userId) return c.json({ error: 'unauthorized' }, 401)
    const stored = await store.get(userId)
    return c.json(
      {
        progress: stored
          ? { lessons: stored.lessons, exercises: stored.exercises }
          : { lessons: {}, exercises: {} },
        updatedAt: stored?.updatedAt ?? null,
      },
      200,
      { 'Cache-Control': 'no-store' },
    )
  })

  app.put('/progress', async (c) => {
    const userId = c.get('userId')
    if (!userId) return c.json({ error: 'unauthorized' }, 401)
    if (!isSafeCsrf(c.req.raw.headers)) {
      return c.json({ error: 'csrf' }, 403)
    }
    const ip = clientIp(c.req.raw)
    if (!consume(ip)) {
      return c.json({ error: 'rate_limited' }, 429)
    }
    let body: unknown
    try {
      body = await c.req.json()
    } catch {
      return c.json({ error: 'bad_request', detail: 'body must be JSON' }, 400)
    }
    const parsed = parseProgressBody(body)
    if (!parsed) {
      return c.json({ error: 'bad_request', detail: 'expected { lessons, exercises }' }, 400)
    }
    const updated = await store.put(userId, parsed)
    return c.json(
      { progress: { lessons: updated.lessons, exercises: updated.exercises }, updatedAt: updated.updatedAt },
      200,
      { 'Cache-Control': 'no-store' },
    )
  })

  // -----------------------------------------------------------------------
  // Regenerate endpoint (pre-existing).
  // -----------------------------------------------------------------------
  interface RegenerateRequest {
    topicId: string
    lessonId: string
    exerciseId: string
    currentInstance: ExerciseInstance
    difficulty?: Difficulty
  }

  const VALID_DIFFICULTIES: Difficulty[] = ['intro', 'core', 'challenge']

  function difficultyOrNull(x: unknown): Difficulty | null {
    return typeof x === 'string' && (VALID_DIFFICULTIES as string[]).includes(x)
      ? (x as Difficulty)
      : null
  }

  function isRegenerateRequest(x: unknown): x is RegenerateRequest {
    if (!x || typeof x !== 'object') return false
    const r = x as Record<string, unknown>
    const baseShape =
      typeof r.topicId === 'string' &&
      typeof r.lessonId === 'string' &&
      typeof r.exerciseId === 'string' &&
      r.currentInstance !== undefined &&
      r.currentInstance !== null &&
      typeof r.currentInstance === 'object'
    if (!baseShape) return false
    if (r.difficulty !== undefined && difficultyOrNull(r.difficulty) === null) {
      return false
    }
    return true
  }

  app.post('/regenerate-exercise', async (c) => {
    const ip = clientIp(c.req.raw)
    const started = Date.now()
    log('req', { method: 'POST', path: '/api/regenerate-exercise', ip })

    if (!consume(ip)) {
      log('res', { status: 200, regenerated: false, reason: 'rate_limited', ms: Date.now() - started })
      return c.json(
        {
          regenerated: false,
          error: 'rate_limited',
          instance: null,
          detail: 'Per-IP request budget exhausted. Try again later.',
        },
        200,
      )
    }

    let body: unknown
    try {
      body = await c.req.json()
    } catch (e) {
      log('res', { status: 400, error: 'bad_json', ms: Date.now() - started })
      return c.json({ error: 'bad_request', detail: 'body must be JSON' }, 400)
    }
    if (!isRegenerateRequest(body)) {
      log('res', { status: 400, error: 'bad_shape', ms: Date.now() - started })
      return c.json(
        { error: 'bad_request', detail: 'expected { topicId, lessonId, exerciseId, currentInstance }' },
        400,
      )
    }
    const req = body
    log('req.parsed', {
      topicId: req.topicId,
      lessonId: req.lessonId,
      exerciseId: req.exerciseId,
      difficulty: req.difficulty ?? '(default)',
    })

    const topic = topicById(req.topicId)
    if (!topic) {
      log('res', { status: 404, error: 'topic_not_found', ms: Date.now() - started })
      return c.json({ error: 'topic_not_found' }, 404)
    }
    const lesson = topic.lessons.find((l) => l.id === req.lessonId)
    if (!lesson) {
      log('res', { status: 404, error: 'lesson_not_found', ms: Date.now() - started })
      return c.json({ error: 'lesson_not_found' }, 404)
    }
    const exercise = lesson.exercises.find((e) => e.id === req.exerciseId)
    if (!exercise) {
      log('res', { status: 404, error: 'exercise_not_found', ms: Date.now() - started })
      return c.json({ error: 'exercise_not_found' }, 404)
    }
    const requestedDifficulty = req.difficulty ?? exercise.difficulty

    const cfg = {
      baseUrl: process.env.ANTHROPIC_BASE_URL ?? 'https://api.minimaxi.com/anthropic',
      authToken: process.env.ANTHROPIC_AUTH_TOKEN ?? '',
      model: process.env.ANTHROPIC_MODEL ?? 'MiniMax-M3',
    }
    const result = await callRegenerate(
      { topic, lesson, difficulty: requestedDifficulty, original: req.currentInstance },
      cfg,
    )

    if (result.ok) {
      log('res', { status: 200, regenerated: true, ms: Date.now() - started })
      return c.json(
        { regenerated: true, instance: result.instance },
        200,
        { 'Cache-Control': 'no-store' },
      )
    }

    log('res', {
      status: 200,
      regenerated: false,
      reason: result.error.kind,
      ms: Date.now() - started,
    })
    return c.json(
      {
        regenerated: false,
        error: result.error.kind,
        instance: req.currentInstance,
      },
      200,
      { 'Cache-Control': 'no-store' },
    )
  })

  app.notFound((c) =>
    c.json({ error: 'not_found', path: new URL(c.req.url).pathname }, 404),
  )

  return app
}

// ---------------------------------------------------------------------------
// Module augmentation: attach session info to every Hono context.
// ---------------------------------------------------------------------------
declare module 'hono' {
  interface ContextVariableMap {
    userId?: string
    session?: Session | null
  }
}