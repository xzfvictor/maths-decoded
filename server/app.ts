/**
 * Hono app definition — pure Hono, no `process.env`, no `node:` imports.
 * Portable to Node (via `server/index.ts`), Vercel (`api/*.ts` via
 * `@hono/vercel` adapter), and Cloudflare Workers (`worker/index.ts`).
 *
 * Single endpoint in v1: POST /api/regenerate-exercise. The client sends
 * context + the current instance; the server returns either a fresh
 * `ExerciseInstance` or the original instance with an error envelope.
 *
 * Every user click generates a fresh question. Cost is bounded by the
 * per-IP rate limit in `server/ratelimit.ts` (10 tokens, refill 1/36 s);
 * we do not cache results because the user's explicit intent on each
 * click is "give me a different question".
 */

import { Hono } from 'hono'
import type { Difficulty, ExerciseInstance } from '../src/content/types'
import { topicById } from '../src/content/topics'
import { callRegenerate } from './m3'
import { log } from './logger'
import { clientIp, consume } from './ratelimit'

export const app = new Hono().basePath('/api')

interface RegenerateRequest {
  topicId: string
  lessonId: string
  exerciseId: string
  currentInstance: ExerciseInstance
  /** Optional difficulty override. Server defaults to the exercise's
   *  declared difficulty when missing. */
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

// Health probe.
app.get('/health', (c) => c.json({ ok: true, ts: Date.now() }))

// Regenerate endpoint.
app.post('/regenerate-exercise', async (c) => {
  const ip = clientIp(c.req.raw)
  const started = Date.now()
  log('req', { method: 'POST', path: '/api/regenerate-exercise', ip })

  // 1. Rate limit.
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

  // 2. Parse body.
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

  // 3. Lookup topic + lesson + exercise so the server can pass real context to M3.
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

  // 4. Call M3 directly. No cache — every user click = fresh question.
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

  // Failure: surface the reason but do not crash. The original instance
  // is returned so the client can keep showing the existing question and
  // display a small "couldn't generate" message.
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

// Default JSON 404 for unknown /api/* routes.
app.notFound((c) =>
  c.json({ error: 'not_found', path: new URL(c.req.url).pathname }, 404),
)
