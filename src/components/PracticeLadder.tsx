/**
 * Per-lesson "practice ladder" panel. Sits at the bottom of the lesson's
 * exercises section and replaces the per-card regenerate buttons with two
 * lesson-level actions: **Similar question** and **Harder question**.
 *
 * Difficulty progression (capped at 2 levels above intro):
 *   intro (0) → core (1) → challenge (2)
 *
 *   - **Similar** generates a question at the user's currently-cleared
 *     level so they can re-roll at the same difficulty.
 *   - **Harder** generates a question one level up, capped at `challenge`.
 *     Once the user solves *any* challenge card (static or generated),
 *     the button disappears and shows the celebration message.
 *
 * The lesson's existing curated + param exercises still render above the
 * ladder (sorted by difficulty, intro → core → challenge). When one of
 * those is solved, the onSolved callback feeds the cleared-level state so
 * a student can climb by solving the static cards alone if they want.
 */

import { useEffect, useMemo, useRef, useState } from 'react'
import type { CuratedExercise, Difficulty, Exercise, ExerciseInstance } from '../content/types'
import { ExerciseCard } from './ExerciseCard'
import { regenerateExercise } from '../lib/regenerateExercise'

const LEVEL_ORDER: Difficulty[] = ['intro', 'core', 'challenge']
const LEVEL_INDEX: Record<Difficulty, 0 | 1 | 2> = {
  intro: 0,
  core: 1,
  challenge: 2,
}
const MAX_LEVEL: 0 | 1 | 2 = 2 // 2 levels up from intro.

/** Hard cap on a single generation. The countdown UI ticks down from
 *  this value; at 0 the in-flight request is aborted. */
const TIMEOUT_MS = 30_000
const TIMEOUT_SEC = TIMEOUT_MS / 1000

/**
 * Find the best exercise to use as the prompt base when regenerating.
 * Prefer a curated entry — its instance is fixed and gives M3 the
 * canonical example. Fall back to the first param exercise's `build(0)`
 * when a lesson has only param exercises; the seeded instance is
 * representative enough for the model to anchor on the same family of
 * problems.
 */
function pickBaseInstance(
  exercises: readonly Exercise[],
): { id: string; instance: ExerciseInstance } | null {
  for (const e of exercises) {
    if (e.kind === 'curated') return { id: e.id, instance: e.instance }
  }
  for (const e of exercises) {
    if (e.kind === 'param') return { id: e.id, instance: e.build(0) }
  }
  return null
}

interface GeneratedItem {
  /** Stable React key. */
  key: string
  difficulty: Difficulty
  instance: ExerciseInstance
}

export function PracticeLadder({
  topicId,
  lessonId,
  exercises,
}: {
  topicId: string
  lessonId: string
  exercises: readonly Exercise[]
}) {
  // 0/1/2 = highest level cleared. The lesson's static intro is the
  // implicit starting point, so we begin at `intro` (0). That way the very
  // first "Harder question" click correctly generates at `core` instead
  // of an extra intro.
  const [clearedLevel, setClearedLevel] = useState<0 | 1 | 2>(0)
  // Whether the student has solved at least one card at the *current*
  // level. Gates Harder before they engage with the current difficulty
  // at all.
  const [hasSolvedAtCurrentLevel, setHasSolvedAtCurrentLevel] = useState(false)
  // Difficulty of the most recently Harder-generated card that hasn't
  // been solved yet. While set, Harder stays greyed so the student
  // engages with the harder card they just got rather than piling up
  // unanswered generated cards.
  const [awaitingHarderDifficulty, setAwaitingHarderDifficulty] =
    useState<Difficulty | null>(null)
  const [generated, setGenerated] = useState<GeneratedItem[]>([])
  const [loading, setLoading] = useState<'similar' | 'harder' | null>(null)
  const [error, setError] = useState<string | null>(null)
  // Countdown (whole seconds) for the current generation. Starts at
  // TIMEOUT_SEC and ticks toward 0; when it reaches 0 the in-flight
  // request is aborted. Reset each time a new `loading` starts.
  const [remainingSec, setRemainingSec] = useState(TIMEOUT_SEC)
  // AbortController for the in-flight request. Held in a ref so the
  // countdown effect (and the unmount cleanup) can reach it without
  // re-creating it on every render.
  const abortRef = useRef<AbortController | null>(null)

  const baseExercise = useMemo(() => pickBaseInstance(exercises), [exercises])
  const atMax = clearedLevel >= MAX_LEVEL

  // Drive the countdown and abort in lockstep with `loading`.
  useEffect(() => {
    if (loading === null) return
    const start = performance.now()
    setRemainingSec(TIMEOUT_SEC)
    const id = window.setInterval(() => {
      const elapsed = performance.now() - start
      const remainingMs = TIMEOUT_MS - elapsed
      const next = Math.max(0, Math.ceil(remainingMs / 1000))
      setRemainingSec(next)
      if (remainingMs <= 0) {
        // Trigger the abort exactly when the countdown hits 0. The
        // regenerate call resolves with `{ ok: false, error: 'timeout' }`.
        if (abortRef.current && !abortRef.current.signal.aborted) {
          abortRef.current.abort()
        }
        window.clearInterval(id)
      }
    }, 100)
    return () => window.clearInterval(id)
  }, [loading])

  // Cancel any in-flight request if the component unmounts (route change).
  useEffect(() => {
    return () => {
      abortRef.current?.abort()
    }
  }, [])

  function onCardSolved(difficulty: Difficulty) {
    const lvl = LEVEL_INDEX[difficulty]
    setHasSolvedAtCurrentLevel(true)
    if (lvl > clearedLevel) {
      setClearedLevel(lvl as 0 | 1 | 2)
    }
    // Solving the harder card that Harder just produced clears the gate
    // — whether the card is the generated one or a static counterpart
    // at the same level.
    if (difficulty === awaitingHarderDifficulty) {
      setAwaitingHarderDifficulty(null)
    }
  }

  async function generateAt(difficulty: Difficulty, kind: 'similar' | 'harder') {
    if (!baseExercise) return
    setLoading(kind)
    setError(null)

    // Share the AbortController between `generateAt` (the request) and
    // the countdown effect (which fires `abort()` at TIMEOUT_MS).
    const controller = new AbortController()
    abortRef.current = controller

    let res
    try {
      res = await regenerateExercise(
        {
          topicId,
          lessonId,
          exerciseId: baseExercise.id,
          currentInstance: baseExercise.instance,
          difficulty,
        },
        { timeoutMs: TIMEOUT_MS, signal: controller.signal },
      )
    } finally {
      abortRef.current = null
      setLoading(null)
    }
    if (res.ok) {
      setGenerated((g) => [
        ...g,
        {
          key: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
          difficulty,
          instance: res.instance,
        },
      ])
      if (kind === 'harder') {
        // A new harder card is on screen — gate Harder until it's solved.
        setHasSolvedAtCurrentLevel(false)
        setAwaitingHarderDifficulty(difficulty)
      }
    } else if (res.error === 'rate_limited') {
      setError("You've hit the rate limit. Try again in a minute.")
    } else if (res.error === 'timeout') {
      setError('Generation took longer than 30s — try again.')
    } else {
      setError("Couldn't generate a fresh question — try again later.")
    }
  }

  // Render only the intro exercise from each lesson's static data.
  // Higher-difficulty static cards (core / challenge) are *not* shown by
  // default — the student generates them on demand via the Harder button.
  // This keeps each lesson's entry view compact and consistent: one
  // question at a time, more on demand.
  const initialExercises = useMemo(
    () =>
      [...exercises]
        .filter((e) => e.difficulty === 'intro')
        .sort((a, b) => LEVEL_INDEX[a.difficulty] - LEVEL_INDEX[b.difficulty]),
    [exercises],
  )

  const similarDifficulty: Difficulty = LEVEL_ORDER[clearedLevel]
  const harderDifficulty: Difficulty | null =
    clearedLevel < MAX_LEVEL ? LEVEL_ORDER[clearedLevel + 1] : null

  const awaitingHarderSolve = awaitingHarderDifficulty !== null
  const harderBlockedBySolve = !hasSolvedAtCurrentLevel
  const harderBlockedByPending = awaitingHarderSolve
  const hardBlockedReason: string | null = harderBlockedBySolve
    ? 'Solve a current-level question first'
    : harderBlockedByPending
      ? 'Solve the harder card on screen first'
      : null

  return (
    <>
      {initialExercises.map((ex) => (
        <ExerciseCard
          key={ex.id}
          topicId={topicId}
          lessonId={lessonId}
          exercise={ex}
          hideRegenerate
          onSolved={onCardSolved}
        />
      ))}

      {generated.length > 0 && (
        <div className="mt-6 space-y-4">
          <h3 className="text-sm font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400">
            Generated practice
          </h3>
          {generated.map((item) => {
            // Build an Exercise shape so ExerciseCard's prop typing is satisfied.
            const ex: CuratedExercise = {
              kind: 'curated',
              id: item.key,
              difficulty: item.difficulty,
              instance: item.instance,
            }
            return (
              <ExerciseCard
                key={item.key}
                topicId={topicId}
                lessonId={lessonId}
                exercise={ex}
                hideRegenerate
                onSolved={onCardSolved}
              />
            )
          })}
        </div>
      )}

      <div className="mt-6 rounded-xl border border-brand-200 bg-brand-50 p-4 shadow-sm dark:border-brand-700/40 dark:bg-brand-950/20">
        <p className="text-xs font-semibold uppercase tracking-wide text-brand-700 dark:text-brand-300">
          AI Generated Questions
        </p>
        {atMax ? (
          <div className="mt-2 rounded-lg bg-emerald-100 p-3 text-sm font-medium text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-200">
            🎉 You've solved the hardest questions on this lesson.
          </div>
        ) : (
          <>
            <p className="mt-1 text-xs text-slate-600 dark:text-slate-400">
              Highest cleared:{' '}
              <span className="font-semibold text-slate-800 dark:text-slate-200">
                {LEVEL_ORDER[clearedLevel]}
              </span>
              . Harder takes you one level up — capped at{' '}
              <span className="font-semibold">challenge</span>.
            </p>
            <div className="mt-3 flex flex-wrap items-start gap-2">
              <button
                type="button"
                onClick={() => generateAt(similarDifficulty, 'similar')}
                disabled={loading !== null || !baseExercise}
                className="rounded-lg border border-slate-300 px-4 py-2 text-sm font-semibold text-slate-700 transition hover:border-slate-400 hover:bg-slate-100 disabled:cursor-not-allowed disabled:opacity-50 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
              >
                {loading === 'similar' ? `Generating… ${remainingSec}s` : 'Similar question'}
              </button>
              {harderDifficulty !== null && (
                <div className="flex flex-col">
                  <button
                    type="button"
                    onClick={() => generateAt(harderDifficulty, 'harder')}
                    disabled={
                      loading !== null ||
                      !baseExercise ||
                      harderBlockedBySolve ||
                      harderBlockedByPending
                    }
                    title={
                      hardBlockedReason !== null
                        ? hardBlockedReason
                        : 'Generate a question one level up'
                    }
                    className="rounded-lg border border-amber-300 px-4 py-2 text-sm font-semibold text-amber-700 transition hover:border-amber-400 hover:bg-amber-50 disabled:cursor-not-allowed disabled:opacity-50 dark:border-amber-700/60 dark:text-amber-300 dark:hover:bg-amber-950/30"
                  >
                    {loading === 'harder' ? `Generating… ${remainingSec}s` : 'Harder question'}
                  </button>
                  {hardBlockedReason !== null && (
                    <span className="mt-1 text-xs text-slate-500 dark:text-slate-400">
                      {hardBlockedReason}
                    </span>
                  )}
                </div>
              )}
            </div>
            {error && (
              <p className="mt-2 text-xs text-rose-600 dark:text-rose-300">{error}</p>
            )}
          </>
        )}
      </div>
    </>
  )
}
