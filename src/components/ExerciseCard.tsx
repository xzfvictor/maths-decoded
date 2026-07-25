import { useMemo, useState } from 'react'
import type { Exercise, ExerciseInstance } from '../content/types'
import { checkAnswer } from '../lib/answer'
import { recordExercise } from '../lib/storage'
import { Prose } from './Prose'

const DIFFICULTY_LABEL: Record<string, string> = {
  intro: 'Intro',
  core: 'Core',
  challenge: 'Challenge',
}
const DIFFICULTY_CLASS: Record<string, string> = {
  intro: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-200',
  core: 'bg-sky-100 text-sky-800 dark:bg-sky-900/50 dark:text-sky-200',
  challenge: 'bg-amber-100 text-amber-800 dark:bg-amber-900/50 dark:text-amber-200',
}

/** Instantiate an exercise: curated ones are fixed, param ones use the seed. */
function instantiate(ex: Exercise, seed: number): ExerciseInstance {
  return ex.kind === 'curated' ? ex.instance : ex.build(seed)
}

export function ExerciseCard({ topicId, exercise }: { topicId: string; exercise: Exercise }) {
  // Seed advances when the student asks for a new version of a param question.
  const [seed, setSeed] = useState(() => (exercise.id.length * 2654435761) >>> 0)
  const instance = useMemo(() => instantiate(exercise, seed), [exercise, seed])

  const [response, setResponse] = useState('')
  const [result, setResult] = useState<'correct' | 'wrong' | null>(null)
  const [showSolution, setShowSolution] = useState(false)
  const [showHint, setShowHint] = useState(false)

  const isParam = exercise.kind === 'param'

  function submit() {
    if (response.trim() === '') return
    const ok = checkAnswer(instance.answerType, instance.answer, response)
    setResult(ok ? 'correct' : 'wrong')
    recordExercise(topicId, ok)
    if (!ok) setShowSolution(true)
  }

  function reset(newSeed: boolean) {
    if (newSeed) setSeed((s) => (s * 1664525 + 1013904223) >>> 0)
    setResponse('')
    setResult(null)
    setShowSolution(false)
    setShowHint(false)
  }

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-900">
      <div className="mb-2 flex items-center gap-2">
        <span
          className={`rounded-full px-2 py-0.5 text-xs font-semibold ${DIFFICULTY_CLASS[exercise.difficulty]}`}
        >
          {DIFFICULTY_LABEL[exercise.difficulty]}
        </span>
        {isParam && (
          <span className="text-xs text-slate-400">Parameterised — try "New question"</span>
        )}
      </div>

      {/* "Your turn" header — a small nudge that frames the prompt as a
          question to attempt, not a fact to skim. */}
      <p className="mb-1 text-[11px] font-semibold uppercase tracking-wide text-slate-400">
        Your turn
      </p>
      <div className="mb-3">
        <Prose text={instance.prompt} />
      </div>

      {instance.choices ? (
        <div className="mb-3 flex flex-col gap-2">
          {instance.choices.map((choice) => (
            <button
              key={choice}
              onClick={() => setResponse(choice)}
              className={`rounded-lg border px-3 py-2 text-left text-sm transition ${
                response === choice
                  ? 'border-brand-500 bg-brand-50 dark:bg-brand-900/40'
                  : 'border-slate-200 hover:border-brand-300 dark:border-slate-700'
              }`}
            >
              <Prose text={choice} />
            </button>
          ))}
        </div>
      ) : (
        <input
          type="text"
          value={response}
          onChange={(e) => setResponse(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && submit()}
          placeholder="Your answer…"
          className="mb-3 w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm outline-none focus:border-brand-500 focus:ring-2 focus:ring-brand-200 dark:border-slate-700 dark:bg-slate-950 dark:focus:ring-brand-900"
        />
      )}

      <div className="flex flex-wrap items-center gap-2">
        <button
          onClick={submit}
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-semibold text-white hover:bg-brand-700 disabled:opacity-50"
          disabled={response.trim() === ''}
        >
          Check answer
        </button>
        {instance.hint && !showHint && result !== 'correct' && (
          <button
            onClick={() => setShowHint(true)}
            className="rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
          >
            Hint
          </button>
        )}
        {!showSolution && (
          <button
            onClick={() => setShowSolution(true)}
            className="rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
          >
            Show solution
          </button>
        )}
        {isParam && (
          <button
            onClick={() => reset(true)}
            className="rounded-lg border border-slate-300 px-3 py-2 text-sm text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
          >
            New question
          </button>
        )}
        {result && (
          <button
            onClick={() => reset(false)}
            className="rounded-lg px-3 py-2 text-sm text-slate-500 hover:text-slate-700 dark:hover:text-slate-200"
          >
            Try again
          </button>
        )}
      </div>

      {showHint && instance.hint && (
        <div className="mt-3 rounded-lg bg-slate-100 p-3 text-sm dark:bg-slate-800">
          <span className="font-semibold">Hint: </span>
          <Prose text={instance.hint} className="inline" />
        </div>
      )}

      {result && (
        <div
          className={`mt-3 rounded-lg p-3 text-sm font-medium ${
            result === 'correct'
              ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-200'
              : 'bg-rose-100 text-rose-800 dark:bg-rose-900/40 dark:text-rose-200'
          }`}
        >
          {result === 'correct' ? '✓ Correct!' : '✗ Not quite — see the worked solution below.'}
        </div>
      )}

      {showSolution && (
        <div className="mt-3 rounded-lg border border-slate-200 bg-slate-50 p-3 dark:border-slate-700 dark:bg-slate-800/50">
          <p className="mb-2 text-sm font-semibold text-slate-700 dark:text-slate-200">
            Worked solution
          </p>
          <ol className="list-decimal space-y-2 pl-5 text-sm">
            {instance.solution.map((step, i) => (
              <li key={i}>
                <Prose text={step} className="inline" />
              </li>
            ))}
          </ol>
          {result !== 'correct' && (
            <p className="mt-3 text-sm text-slate-500">
              Answer:{' '}
              <span className="font-semibold text-slate-700 dark:text-slate-200">
                <Prose text={instance.answer} className="inline" />
              </span>
            </p>
          )}
        </div>
      )}
    </div>
  )
}
