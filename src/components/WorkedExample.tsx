import { useEffect, useRef, useState } from 'react'
import type { WorkedExample } from '../content/types'
import { Prose } from './Prose'
import { AnimatedStepText } from './AnimatedStepText'

/**
 * Interactive worked-example card.
 *
 * Steps reveal **one at a time**, with smooth fade/slide CSS animations,
 * an optional **auto-play** mode that cycles through steps at a chosen
 * speed, keyboard shortcuts (Space = play/pause, ←/→ = step), and a
 * pulse highlight on the most recently revealed step so the eye lands
 * where it should. The cumulative effect is a video-like walkthrough
 * without needing pre-rendered media.
 */
export function WorkedExample({ example }: { example: WorkedExample }) {
  const [open, setOpen] = useState(false)
  const [revealed, setRevealed] = useState(0) // 0..steps.length
  const [playing, setPlaying] = useState(false)
  // Speed = ms per step.
  const SPEEDS = [5000, 3000, 1500] // slow, normal, fast
  const [speedIdx, setSpeedIdx] = useState(1)
  const speed = SPEEDS[speedIdx]
  const total = example.steps.length
  const done = revealed >= total

  // Auto-play timer.
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  useEffect(() => {
    if (!playing) return
    if (done) {
      setPlaying(false)
      return
    }
    timerRef.current = setTimeout(() => {
      setRevealed((n) => Math.min(n + 1, total))
    }, speed)
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
    }
  }, [playing, revealed, speed, done, total])

  // Keyboard shortcuts (active when the card is open).
  function onKeyDown(e: React.KeyboardEvent<HTMLDivElement>) {
    if (e.key === ' ' || e.key === 'Spacebar') {
      e.preventDefault()
      if (!open) start()
      else if (done) reset()
      else setPlaying((p) => !p)
    } else if (e.key === 'ArrowRight' || e.key === 'l') {
      e.preventDefault()
      if (open && !done) setRevealed((n) => Math.min(n + 1, total))
    } else if (e.key === 'ArrowLeft' || e.key === 'h') {
      e.preventDefault()
      if (open) setRevealed((n) => Math.max(n - 1, 0))
    } else if (e.key === 'Escape') {
      e.preventDefault()
      setPlaying(false)
      reset()
    }
  }

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
    setPlaying(false)
  }
  function reset() {
    setOpen(false)
    setRevealed(0)
    setPlaying(false)
  }
  function togglePlay() {
    if (!open) {
      start()
      setPlaying(true)
      return
    }
    if (done) {
      reset()
      return
    }
    setPlaying((p) => !p)
  }

  return (
    <div
      tabIndex={0}
      onKeyDown={onKeyDown}
      className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm outline-none focus:ring-2 focus:ring-brand-200 dark:border-slate-800 dark:bg-slate-900 dark:focus:ring-brand-900"
    >
      {/* Statement (always visible). */}
      <div className="mb-3 flex items-start gap-3">
        <span
          aria-hidden="true"
          className="mt-1 inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-brand-100 text-xs font-bold text-brand-700 dark:bg-brand-900/40 dark:text-brand-200"
        >
          Ex
        </span>
        <div className="min-w-0 flex-1">
          <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-400">
            Worked example
          </p>
          <div className="text-base font-medium text-slate-800 dark:text-slate-100">
            <Prose text={example.statement} className="inline" />
          </div>
        </div>
      </div>

      {/* Closed state — encourage attempting the problem first instead of
          just revealing the worked solution. */}
      {!open && (
        <div className="flex flex-wrap items-center gap-2">
          <button
            type="button"
            onClick={start}
            className="inline-flex items-center gap-1 rounded-lg bg-brand-50 px-3 py-1.5 text-sm font-semibold text-brand-700 transition hover:bg-brand-100 dark:bg-brand-900/40 dark:text-brand-200 dark:hover:bg-brand-900/60"
          >
            Show solution
            <span aria-hidden="true">▾</span>
          </button>
          <span className="text-xs text-slate-500 dark:text-slate-400">
            Tip: have a go on paper first — the steps reveal one at a time so you
            can pace yourself.
          </span>
        </div>
      )}

      {/* Open state — progressive reveal. */}
      {open && (
        <div className="mt-4 border-t border-slate-100 pt-4 dark:border-slate-800">
          {/* Progress bar + step counter. */}
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
              {done ? `All ${total} steps ✓` : `Step ${revealed} / ${total}`}
            </span>
          </div>

          {/* Steps list. */}
          <ol className="list-decimal space-y-3 pl-5 text-sm">
            {example.steps.slice(0, revealed).map((step, i) => {
              const isActive = i === revealed - 1 && !done
              return (
                <li
                  key={i}
                  className={[
                    'rounded-md px-3 py-2 transition-all duration-300 ease-out',
                    isActive
                      ? 'animate-[fadeup_350ms_ease-out] bg-brand-50 ring-1 ring-brand-200 dark:bg-brand-900/30 dark:ring-brand-700/40'
                      : '',
                  ].join(' ')}
                  style={
                    isActive
                      ? { animation: 'fadeup 350ms ease-out' }
                      : undefined
                  }
                >
                  <AnimatedStepText text={step} triggerKey={i} />
                </li>
              )
            })}
          </ol>

          {/* Hint: keyboard shortcuts. */}
          <p className="mt-3 text-xs text-slate-400 dark:text-slate-500">
            Tip: <kbd className="rounded border border-slate-200 px-1 text-[10px] dark:border-slate-700">Space</kbd> play/pause · <kbd className="rounded border border-slate-200 px-1 text-[10px] dark:border-slate-700">←</kbd>/<kbd className="rounded border border-slate-200 px-1 text-[10px] dark:border-slate-700">→</kbd> step · <kbd className="rounded border border-slate-200 px-1 text-[10px] dark:border-slate-700">Esc</kbd> reset
          </p>

          {/* Controls. */}
          <div className="mt-3 flex flex-wrap items-center gap-2">
            <button
              type="button"
              onClick={togglePlay}
              className={`inline-flex items-center gap-1 rounded-lg px-3 py-1.5 text-sm font-semibold transition ${
                done
                  ? 'border border-slate-300 text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800'
                  : playing
                    ? 'bg-amber-500 text-white hover:bg-amber-600'
                    : 'bg-brand-600 text-white hover:bg-brand-700'
              }`}
              aria-label={playing ? 'Pause' : done ? 'Restart' : 'Play'}
            >
              {playing ? (
                <>❚❚ Pause</>
              ) : done ? (
                <>↺ Restart</>
              ) : (
                <>▶ {revealed === 0 ? 'Play' : 'Play'}</>
              )}
            </button>

            {!done && (
              <>
                <button
                  type="button"
                  onClick={next}
                  className="rounded-lg border border-slate-300 px-3 py-1.5 text-sm text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
                >
                  Next step →
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

            {/* Speed selector (visible when playing or about to play). */}
            <div className="ml-auto flex items-center gap-1 text-xs text-slate-500 dark:text-slate-400">
              <span>Speed</span>
              {SPEEDS.map((ms, i) => {
                const labels = ['Slow', 'Normal', 'Fast']
                return (
                  <button
                    key={ms}
                    type="button"
                    onClick={() => setSpeedIdx(i)}
                    className={`rounded px-2 py-0.5 transition ${
                      i === speedIdx
                        ? 'bg-brand-600 text-white'
                        : 'border border-slate-300 hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800'
                    }`}
                  >
                    {labels[i]}
                  </button>
                )
              })}
            </div>

            <button
              type="button"
              onClick={reset}
              className="rounded-lg px-3 py-1.5 text-sm text-slate-500 hover:text-slate-700 dark:hover:text-slate-200"
            >
              Reset
            </button>
          </div>
        </div>
      )}

      {/* Local keyframes — kept in-component via <style> to avoid touching tailwind config. */}
      <style>{`
        @keyframes fadeup {
          from { opacity: 0; transform: translateY(6px); }
          to   { opacity: 1; transform: translateY(0); }
        }
      `}</style>
    </div>
  )
}