import { useState } from 'react'
import type { WorkedExample } from '../content/types'
import { Prose } from './Prose'

/**
 * Interactive worked-example card.
 *
 * The statement is always visible. The solution starts hidden and is
 * revealed **one step at a time** so the student can pause and think
 * before each step. A progress bar shows where they are in the
 * solution. Buttons let them advance, jump to the end, or reset.
 */
export function WorkedExample({ example }: { example: WorkedExample }) {
  const [open, setOpen] = useState(false)
  const [revealed, setRevealed] = useState(0) // 0..steps.length
  const total = example.steps.length
  const done = revealed >= total

  function start() {
    setOpen(true)
    setRevealed(1)
  }
  function next() {
    setRevealed((n) => Math.min(n + 1, total))
  }
  function prev() {
    setRevealed((n) => Math.max(n - 1, 0))
  }
  function showAll() {
    setRevealed(total)
  }
  function reset() {
    setOpen(false)
    setRevealed(0)
  }

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
      {/* Statement (always visible). */}
      <div className="mb-3 flex items-start gap-3">
        <span
          aria-hidden="true"
          className="mt-1 inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-brand-100 text-xs font-bold text-brand-700 dark:bg-brand-900/40 dark:text-brand-200"
        >
          Ex
        </span>
        <div className="min-w-0 flex-1 text-base font-medium text-slate-800 dark:text-slate-100">
          <Prose text={example.statement} className="inline" />
        </div>
      </div>

      {/* Closed state — single "Show solution" button. */}
      {!open && (
        <button
          type="button"
          onClick={start}
          className="inline-flex items-center gap-1 rounded-lg bg-brand-50 px-3 py-1.5 text-sm font-semibold text-brand-700 transition hover:bg-brand-100 dark:bg-brand-900/40 dark:text-brand-200 dark:hover:bg-brand-900/60"
        >
          Show solution
          <span aria-hidden="true">▾</span>
        </button>
      )}

      {/* Open state — progressive reveal. */}
      {open && (
        <div className="mt-4 border-t border-slate-100 pt-4 dark:border-slate-800">
          {/* Progress. */}
          <div className="mb-3 flex items-center gap-3">
            <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
              <div
                className="h-full bg-brand-500 transition-all duration-300 ease-out"
                style={{ width: `${total === 0 ? 0 : (revealed / total) * 100}%` }}
                role="progressbar"
                aria-valuenow={revealed}
                aria-valuemin={0}
                aria-valuemax={total}
              />
            </div>
            <span className="shrink-0 text-xs font-semibold text-slate-500 dark:text-slate-400">
              {done ? `All ${total} steps` : `Step ${revealed} / ${total}`}
            </span>
          </div>

          {/* Steps. */}
          <ol className="list-decimal space-y-3 pl-5 text-sm">
            {example.steps.slice(0, revealed).map((step, i) => (
              <li
                key={i}
                className={
                  // Slight emphasis on the most recent step.
                  i === revealed - 1 && !done
                    ? 'animate-[fadein_300ms_ease-out]'
                    : ''
                }
              >
                <Prose text={step} className="inline" />
              </li>
            ))}
          </ol>

          {/* Controls. */}
          <div className="mt-4 flex flex-wrap items-center gap-2">
            {!done && (
              <>
                <button
                  type="button"
                  onClick={next}
                  className="inline-flex items-center gap-1 rounded-lg bg-brand-600 px-3 py-1.5 text-sm font-semibold text-white transition hover:bg-brand-700"
                >
                  {revealed === 0 ? 'Start solution' : 'Next step →'}
                </button>
                {revealed > 0 && (
                  <button
                    type="button"
                    onClick={prev}
                    className="rounded-lg border border-slate-300 px-3 py-1.5 text-sm text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
                  >
                    ← Previous
                  </button>
                )}
                <button
                  type="button"
                  onClick={showAll}
                  className="rounded-lg border border-slate-300 px-3 py-1.5 text-sm text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
                >
                  Show all
                </button>
              </>
            )}
            <button
              type="button"
              onClick={reset}
              className="ml-auto rounded-lg px-3 py-1.5 text-sm text-slate-500 hover:text-slate-700 dark:hover:text-slate-200"
            >
              Reset
            </button>
          </div>
        </div>
      )}
    </div>
  )
}