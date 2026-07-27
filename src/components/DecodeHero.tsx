import { useEffect, useRef, useState } from 'react'
import katex from 'katex'
import { AnimatedStepText } from './AnimatedStepText'
import { DECODE_STEPS, TANGLED } from '../content/decodeDemo'

type Phase = 'idle' | 'decoding' | 'revealed'

/**
 * The interactive decode demo on the landing page.
 *
 * State machine:
 *   idle      — tangled expression wobbles; "Decode it" button glows.
 *   decoding  — steps animate in one after another (~700 ms apart).
 *   revealed  — all four steps visible; button says "Reset".
 *
 * Animation timing matches the in-lesson worked examples so the brand's
 * motion vocabulary stays consistent (uses the same global keyframes).
 */
export function DecodeHero() {
  const [phase, setPhase] = useState<Phase>('idle')
  const [revealedCount, setRevealedCount] = useState(0)
  // Bumped on every transition into `decoding` so AnimatedStepText
  // remounts and re-fires its token-by-token reveal.
  const [runKey, setRunKey] = useState(0)

  function start() {
    if (phase === 'decoding') return
    setRevealedCount(0)
    setRunKey((k) => k + 1)
    setPhase('decoding')
  }

  function reset() {
    setPhase('idle')
    setRevealedCount(0)
  }

  // Render the tangled expression once, memoised.
  const tangledHtml = katex.renderToString(TANGLED, {
    displayMode: true,
    throwOnError: false,
    strict: false,
  })

  return (
    <section
      className="decode-hero relative overflow-hidden rounded-3xl border border-slate-200 bg-gradient-to-br from-slate-50 via-white to-brand-50/40 p-6 shadow-sm dark:border-slate-800 dark:from-slate-900 dark:via-slate-900 dark:to-brand-900/20 sm:p-8"
      aria-label="Interactive decode demo"
    >
      {/* Tangled expression — always visible, wobbles when idle, dims when decoding. */}
      <div
        className={`decode-tangled transition-opacity duration-300 ${
          phase === 'idle' ? 'opacity-60' : 'opacity-25'
        }`}
        aria-hidden="true"
      >
        <div
          className="mx-auto inline-block rounded-xl bg-white/60 px-4 py-3 dark:bg-slate-950/40"
          dangerouslySetInnerHTML={{ __html: tangledHtml }}
        />
      </div>

      {/* Resolved steps — stack below the tangled expression once decoded. */}
      {phase !== 'idle' && (
        <ol className="mt-6 space-y-4">
          {DECODE_STEPS.slice(0, revealedCount).map((step, i) => (
            <li
              key={`${runKey}-${i}`}
              className="decode-step rounded-xl border border-slate-200 bg-white/70 p-4 dark:border-slate-700 dark:bg-slate-900/60"
              style={{ animationDelay: `${i * 40}ms` }}
            >
              <div className="mb-1 text-xs font-semibold uppercase tracking-wide text-brand-600 dark:text-brand-300">
                Step {i + 1} · {step.label}
              </div>
              <div className="theory overflow-x-auto">
                {/* Each step uses AnimatedStepText for the token-by-token
                    reveal. Stagger via `delayMs` so steps cascade. */}
                <AnimatedStepText
                  text={`$$${step.tex}$$`}
                  triggerKey={`${runKey}-${i}`}
                  delayMs={i * 350}
                />
              </div>
            </li>
          ))}
        </ol>
      )}

      {/* Drives the per-step reveal cadence while `phase === 'decoding'`. */}
      {phase === 'decoding' && (
        <StepRevealDriver
          target={DECODE_STEPS.length}
          onTick={(n) => setRevealedCount(n)}
          onDone={() => setPhase('revealed')}
          // Reset whenever a fresh decode starts.
          resetKey={runKey}
        />
      )}

      {/* Action button — context switches with phase. */}
      <div className="mt-6 flex justify-center">
        {phase !== 'revealed' ? (
          <button
            type="button"
            onClick={start}
            disabled={phase === 'decoding'}
            className="decode-button-idle inline-flex items-center gap-2 rounded-full bg-brand-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-brand-700 disabled:cursor-not-allowed disabled:opacity-70 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 focus-visible:ring-offset-2 dark:focus-visible:ring-offset-slate-900"
          >
            <span aria-hidden="true">✨</span>
            {phase === 'decoding' ? 'Decoding…' : 'Decode it'}
          </button>
        ) : (
          <button
            type="button"
            onClick={reset}
            className="inline-flex items-center gap-2 rounded-full border border-slate-300 bg-white px-5 py-2.5 text-sm font-semibold text-slate-700 shadow-sm transition hover:border-brand-400 hover:text-brand-700 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200 dark:hover:border-brand-400 dark:hover:text-brand-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 focus-visible:ring-offset-2 dark:focus-visible:ring-offset-slate-900"
          >
            ↺ Reset
          </button>
        )}
      </div>

      <p className="mt-4 text-center text-xs text-slate-500 dark:text-slate-400">
        Click <span className="font-semibold">Decode it</span> to see the maths broken into steps.
      </p>
    </section>
  )
}

/**
 * Effect-only component that owns the timed reveal cadence. Calls
 * `onTick(n)` whenever the next step should appear; `onDone()` once
 * the final step is revealed.
 */
function StepRevealDriver({
  target,
  onTick,
  onDone,
  resetKey,
}: {
  target: number
  onTick: (n: number) => void
  onDone: () => void
  resetKey: number
}) {
  const nRef = useRef(0)
  useEffect(() => {
    nRef.current = 0
    let cancelled = false
    function step() {
      if (cancelled) return
      nRef.current += 1
      onTick(nRef.current)
      if (nRef.current >= target) {
        onDone()
        return
      }
      setTimeout(step, 700)
    }
    // First step appears almost immediately; the rest every 700 ms.
    setTimeout(step, 250)
    return () => {
      cancelled = true
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [resetKey])
  return null
}