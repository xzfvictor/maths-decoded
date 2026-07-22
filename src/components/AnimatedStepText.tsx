import { Fragment } from 'react'
import katex from 'katex'

/**
 * A single chunk of a step's text. Either a stretch of plain prose, or a
 * math expression. Block-math vs inline-math is also tracked so KaTeX
 * renders with the right display mode.
 */
type Segment = { text: string; kind: 'text' | 'math-inline' | 'math-block' }

/**
 * Split a markdown-ish step string into segments at $...$ and $$...$$
 * boundaries. We do this at the string level (rather than walking the
 * rendered DOM) so the math expressions stay atomic — a single math
 * formula never gets split into multiple animatable tokens.
 */
function splitToSegments(step: string): Segment[] {
  const out: Segment[] = []
  let i = 0
  while (i < step.length) {
    // Block math: $$ ... $$ (single line — the worked-example steps
    // are short and don't span multi-line block math).
    if (step.startsWith('$$', i)) {
      const end = step.indexOf('$$', i + 2)
      if (end === -1) {
        out.push({ text: step.slice(i + 2), kind: 'math-block' })
        break
      }
      out.push({ text: step.slice(i + 2, end), kind: 'math-block' })
      i = end + 2
      continue
    }
    if (step[i] === '$') {
      // Inline math: $ ... $
      const end = step.indexOf('$', i + 1)
      if (end === -1) {
        out.push({ text: step.slice(i), kind: 'text' })
        break
      }
      out.push({ text: step.slice(i + 1, end), kind: 'math-inline' })
      i = end + 1
      continue
    }
    // Plain text up to the next $.
    const next = step.indexOf('$', i)
    const slice = next === -1 ? step.slice(i) : step.slice(i, next)
    if (slice.length > 0) out.push({ text: slice, kind: 'text' })
    i = next === -1 ? step.length : next
  }
  return out
}

/** Split a plain-text segment into word tokens. Each non-whitespace run
 *  grabs its trailing whitespace so the rendered HTML never has a
 *  whitespace-only token (those collapse to zero width inside an
 *  inline-block). */
function tokenize(text: string): string[] {
  return text.match(/\s+|\S+\s*/g) ?? []
}

/** Per-step animation tuning. */
const PER_TOKEN_MS = 45 // ms between successive tokens within a step
const TOKEN_DURATION_MS = 280 // per-token fade duration
const MATH_PULSE_MS = 650 // halo outline that fades after each math token
const POST_MATH_PAUSE_MS = 220 // "look at this formula" pause after math
const POST_TEXT_PAUSE_MS = 60 // tiny breath between prose segments

/** Brand primary in rgba, so the pulse halo matches the site theme. */
const BRAND_RGB = '49, 109, 255' // #316dff (brand-500)

/**
 * Render a step's text as a stream of animated tokens — words and
 * inline math appear one after another with a tiny fade-up.
 *
 * Two extras on top of the basic fade-up:
 *   • Math tokens get a brand-coloured "halo" pulse after they appear
 *     (just a quick outline that fades — gives the eye a hint of
 *     "look at this").
 *   • Smart pacing: a slightly longer pause is inserted at boundaries
 *     between math and prose so the student has a beat to absorb the
 *     formula before the surrounding text catches up.
 *
 * The animation only fires when `triggerKey` changes, so re-rendering
 * the same step (e.g. from a state change elsewhere) doesn't replay
 * the tokens.
 */
export function AnimatedStepText({
  text,
  triggerKey,
  delayMs = 0,
}: {
  text: string
  /** Bump this number (e.g. step index) whenever the step should re-animate. */
  triggerKey: number | string
  /** Extra delay before the first token animates (e.g. when stepping through). */
  delayMs?: number
}) {
  const segments = splitToSegments(text)

  // Plan token schedule first so each token knows its absolute delay.
  type Plan =
    | { kind: 'text'; tokens: string[]; startAt: number }
    | { kind: 'math'; html: string; startAt: number; isBlock: boolean }
  const plan: Plan[] = []

  let cursor = delayMs // absolute "time when this token starts animating"
  let lastKind: 'text' | 'math' | null = null
  segments.forEach((seg) => {
    // Smart-pacing pause at the boundary between kinds.
    if (lastKind !== null && lastKind !== (seg.kind === 'text' ? 'text' : 'math')) {
      const pause =
        lastKind === 'math' ? POST_MATH_PAUSE_MS : POST_TEXT_PAUSE_MS
      cursor += pause
    }
    if (seg.kind === 'text') {
      const tokens = tokenize(seg.text)
      plan.push({ kind: 'text', tokens, startAt: cursor })
      cursor += (tokens.length - 1) * PER_TOKEN_MS + TOKEN_DURATION_MS
      lastKind = 'text'
    } else {
      const html = katex.renderToString(seg.text, {
        displayMode: seg.kind === 'math-block',
        throwOnError: false,
        strict: false,
      })
      plan.push({
        kind: 'math',
        html,
        startAt: cursor,
        isBlock: seg.kind === 'math-block',
      })
      cursor += TOKEN_DURATION_MS
      lastKind = 'math'
    }
  })

  return (
    <span className="animated-step-text">
      {plan.map((seg, i) => {
        if (seg.kind === 'text') {
          return (
            <Fragment key={i}>
              {seg.tokens.map((tok, j) => (
                <span
                  key={j}
                  className="anim-token"
                  style={{
                    animationDelay: `${seg.startAt + j * PER_TOKEN_MS}ms`,
                    animationDuration: `${TOKEN_DURATION_MS}ms`,
                  }}
                >
                  {tok}
                </span>
              ))}
            </Fragment>
          )
        }
        // Math: one animatable span wrapping the rendered KaTeX HTML.
        // Two animations: the regular fade-up, then the brand-halo pulse
        // that fires as soon as the token is fully visible.
        return (
          <span
            key={i}
            className={`anim-token anim-math${seg.isBlock ? ' anim-math-block' : ''}`}
            style={{
              animationDelay: `${seg.startAt}ms, calc(${seg.startAt}ms + ${TOKEN_DURATION_MS - 60}ms)`,
              animationDuration: `${TOKEN_DURATION_MS}ms, ${MATH_PULSE_MS}ms`,
            }}
            dangerouslySetInnerHTML={{ __html: seg.html }}
          />
        )
      })}
      {/* Per-step keyframe + token CSS, scoped under the class. */}
      <style>{`
        @keyframes animTokenIn {
          from { opacity: 0; transform: translateY(4px); }
          to   { opacity: 1; transform: translateY(0); }
        }
        /* Brand-coloured halo that briefly outlines the math so the eye
           lands on it. The halo grows and fades, like a ping. */
        @keyframes animMathPulse {
          0%   { box-shadow: 0 0 0 3px rgba(${BRAND_RGB}, 0.45); }
          60%  { box-shadow: 0 0 0 6px rgba(${BRAND_RGB}, 0.10); }
          100% { box-shadow: 0 0 0 8px rgba(${BRAND_RGB}, 0); }
        }
        .animated-step-text .anim-token {
          display: inline-block;
          /* Preserve trailing whitespace inside the token; otherwise the
             browser trims it and words run together. */
          white-space: pre;
          opacity: 0;
          animation-name: animTokenIn, animMathPulse;
          /* Two animations need two delays and two durations (comma-
           separated). Plain-text tokens get a no-op pulse (the second
           animation is animation-name: animTokenIn only — see below). */
          animation-timing-function: ease-out, ease-out;
          animation-fill-mode: forwards, forwards;
          animation-duration: 280ms, 0s;
        }
        /* Math: re-declare two real animations. */
        .animated-step-text .anim-math {
          vertical-align: baseline;
          padding: 0 4px;
          border-radius: 4px;
          /* Override the no-op durations above. */
          animation-duration: 280ms, 650ms;
        }
        .animated-step-text .anim-math-block {
          display: block;
        }
      `}</style>
      {/* The triggerKey is included to give React a stable identity but
          not rendered — its only effect is to remount the children when
          it changes, re-firing the animations. */}
      <span hidden>{String(triggerKey)}</span>
    </span>
  )
}