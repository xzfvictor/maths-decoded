/**
 * Server-side M3 wrapper. Builds the prompt + tools, calls M3, validates
 * the result against the existing checker. One retry on validation failure.
 *
 * Pure async function: no `process.env` reads here (caller passes config
 * in). Lets the test harness inject deterministic config.
 */

import { callM3 } from '../scripts/lib/m3'
import type { ExerciseInstance, Lesson, Topic } from '../src/content/types'
import { log } from './logger'
import {
  SUBMIT_EXERCISE_TOOL,
  buildRepairPrompt,
  buildSystemPrompt,
  buildUserPrompt,
} from './prompt'
import { validate, type ValidationResult } from './validate'

export interface M3Config {
  baseUrl: string
  authToken: string
  model: string
  signal?: AbortSignal
}

export interface RegenerateArgs {
  topic: Topic
  lesson: Lesson
  difficulty: 'intro' | 'core' | 'challenge'
  original: ExerciseInstance
}

/**
 * Returns a validated instance OR a structured failure describing why.
 * Caller chooses whether to cache, retry, or fall back to the original.
 */
export async function callRegenerate(
  args: RegenerateArgs,
  cfg: M3Config,
): Promise<ValidationResult> {
  if (!cfg.authToken) {
    return {
      ok: false,
      error: { kind: 'malformed', reason: 'ANTHROPIC_AUTH_TOKEN is not set on the server' },
    }
  }

  const userPrompt = buildUserPrompt(args.topic, args.lesson, args.original, args.difficulty)
  const systemPrompt = buildSystemPrompt()

  const start = Date.now()
  let firstResult: ValidationResult | null = null

  try {
    const first = await callM3(userPrompt, {
      baseUrl: cfg.baseUrl,
      authToken: cfg.authToken,
      model: cfg.model,
      maxTokens: 1500,
      system: systemPrompt,
      tools: [SUBMIT_EXERCISE_TOOL],
      toolChoice: { type: 'tool', name: SUBMIT_EXERCISE_TOOL.name },
      signal: cfg.signal,
    })

    if (first.kind !== 'tool') {
      firstResult = {
        ok: false,
        error: { kind: 'malformed', reason: 'model did not invoke submit_exercise tool' },
      }
      log('m3.validate', { status: 'reject', reason: 'no_tool_call', ms: Date.now() - start })
      return firstResult
    }

    firstResult = validate(first.input)
    log('m3.validate', {
      status: firstResult.ok ? 'ok' : 'reject',
      reason: firstResult.ok ? undefined : firstResult.error.kind,
      ms: Date.now() - start,
    })

    if (firstResult.ok) return firstResult
  } catch (err) {
    log('m3.error', { ms: Date.now() - start, message: (err as Error).message })
    return {
      ok: false,
      error: { kind: 'malformed', reason: `M3 call failed: ${(err as Error).message}` },
    }
  }

  // One retry with repair feedback.
  try {
    const lastAttempt = firstResult && !firstResult.ok ? firstResult.error : null
    const reason =
      lastAttempt && 'kind' in lastAttempt
        ? JSON.stringify(lastAttempt)
        : 'unknown validation failure'

    const repairUser = buildRepairPrompt(args.original, reason, 'see last error above')
    const second = await callM3(repairUser, {
      baseUrl: cfg.baseUrl,
      authToken: cfg.authToken,
      model: cfg.model,
      maxTokens: 1500,
      system: systemPrompt,
      tools: [SUBMIT_EXERCISE_TOOL],
      toolChoice: { type: 'tool', name: SUBMIT_EXERCISE_TOOL.name },
      signal: cfg.signal,
    })

    if (second.kind !== 'tool') {
      const result: ValidationResult = {
        ok: false,
        error: { kind: 'malformed', reason: 'retry: model did not invoke submit_exercise tool' },
      }
      log('m3.retry.validate', { status: 'reject', reason: 'no_tool_call' })
      return result
    }

    const validated = validate(second.input)
    log('m3.retry.validate', {
      status: validated.ok ? 'ok' : 'reject',
      reason: validated.ok ? undefined : validated.error.kind,
    })
    return validated
  } catch (err) {
    log('m3.retry.error', { message: (err as Error).message })
    return {
      ok: false,
      error: { kind: 'malformed', reason: `M3 retry failed: ${(err as Error).message}` },
    }
  }
}
