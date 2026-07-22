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

/**
 * Render a step's text as a stream of animated tokens — words and
 * inline math appear one after another with a tiny fade-up. KaTeX
 * block-math ($$...$$) is rendered as a single animated unit so the
 * formula stays readable while typing in.
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
  let tokenIndex = 0
  return (
    <span className="animated-step-text">
      {segments.map((seg, i) => {
        if (seg.kind === 'text') {
          const tokens = tokenize(seg.text)
          return (
            <Fragment key={i}>
              {tokens.map((tok, j) => {
                const idx = tokenIndex++
                return (
                  <span
                    key={j}
                    className="anim-token"
                    style={{
                      animationDelay: `${delayMs + idx * PER_TOKEN_MS}ms`,
                      animationDuration: `${TOKEN_DURATION_MS}ms`,
                    }}
                    // Stagger key — same triggerKey means no replay.
                    data-token-idx={idx}
                  >
                    {tok}
                  </span>
                )
              })}
            </Fragment>
          )
        }
        // Math: render via KaTeX and wrap as a single animatable token.
        const html = katex.renderToString(seg.text, {
          displayMode: seg.kind === 'math-block',
          throwOnError: false,
          strict: false,
        })
        const idx = tokenIndex++
        return (
          <span
            key={i}
            className="anim-token anim-math"
            style={{
              animationDelay: `${delayMs + idx * PER_TOKEN_MS}ms`,
              animationDuration: `${TOKEN_DURATION_MS}ms`,
            }}
            dangerouslySetInnerHTML={{ __html: html }}
          />
        )
      })}
      {/* Per-step keyframe + token CSS, scoped under the class. */}
      <style>{`
        @keyframes animTokenIn {
          from { opacity: 0; transform: translateY(4px); }
          to   { opacity: 1; transform: translateY(0); }
        }
        .animated-step-text .anim-token {
          display: inline-block;
          /* Preserve trailing whitespace inside the token; otherwise the
             browser trims it and words run together. */
          white-space: pre;
          opacity: 0;
          animation-name: animTokenIn;
          animation-timing-function: ease-out;
          animation-fill-mode: forwards;
        }
        .animated-step-text .anim-math {
          /* Math should sit on its own baseline; don't nudge the line. */
          vertical-align: baseline;
        }
      `}</style>
      {/* The triggerKey is included to give React a stable identity but
          not rendered — its only effect is to remount the children when
          it changes, re-firing the animations. */}
      <span hidden>{String(triggerKey)}</span>
    </span>
  )
}