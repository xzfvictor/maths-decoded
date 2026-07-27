import type { Difficulty, ExerciseInstance } from '../content/types'

export type RegenerateDifficulty = Difficulty

export interface RegenerateRequest {
  topicId: string
  lessonId: string
  exerciseId: string
  currentInstance: ExerciseInstance
  /** Optional difficulty override. "Similar question" omits this; "Easier"
   *  sends 'intro'; "Harder" sends 'challenge'. Omit → use the exercise's
   *  declared difficulty. */
  difficulty?: RegenerateDifficulty
}

export type RegenResult =
  | { ok: true; instance: ExerciseInstance }
  | {
      ok: false
      error: 'rate_limited' | 'model_failed' | 'malformed' | 'network' | 'timeout'
      instance: ExerciseInstance | null
    }

interface CallOpts {
  timeoutMs?: number
  signal?: AbortSignal
}

/**
 * POST `/api/regenerate-exercise` and return a tagged union. Never throws —
 * callers can rely on the discriminated result for control flow.
 */
export async function regenerateExercise(
  req: RegenerateRequest,
  opts: CallOpts = {},
): Promise<RegenResult> {
  const { timeoutMs = 20_000, signal: externalSignal } = opts
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), timeoutMs)

  // Chain an external abort into our internal one.
  if (externalSignal) {
    if (externalSignal.aborted) controller.abort()
    else externalSignal.addEventListener('abort', () => controller.abort(), { once: true })
  }

  try {
    const res = await fetch('/api/regenerate-exercise', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(req),
      signal: controller.signal,
    })

    if (!res.ok) {
      // 5xx: server bug. 4xx: client bug. Either way, fall through with
      // a "model_failed" envelope so the UI keeps the original instance.
      return { ok: false, error: 'model_failed', instance: req.currentInstance }
    }

    const data = (await res.json()) as {
      regenerated?: boolean
      instance?: ExerciseInstance
      error?: string
    }

    if (data.regenerated && data.instance) {
      return {
        ok: true,
        instance: data.instance,
      }
    }

    // Server returned a structured error envelope — map to our union.
    const err = data.error
    if (err === 'rate_limited') return { ok: false, error: 'rate_limited', instance: null }
    if (err && typeof err === 'string') {
      return {
        ok: false,
        error: err === 'model_failed' ? 'model_failed' : 'malformed',
        instance: data.instance ?? req.currentInstance,
      }
    }
    return { ok: false, error: 'malformed', instance: req.currentInstance }
  } catch (err) {
    if ((err as Error).name === 'AbortError') {
      return { ok: false, error: 'timeout', instance: req.currentInstance }
    }
    return { ok: false, error: 'network', instance: req.currentInstance }
  } finally {
    clearTimeout(timer)
  }
}
