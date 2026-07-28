/**
 * The decode demo shown on the landing page.
 *
 * One tangled-looking system of linear equations that resolves through
 * four steps into a clean solution. Each step is rendered with KaTeX
 * and animated in token-by-token by `DecodeHero.tsx`.
 *
 * The content lives here (rather than inside the component) so it can be
 * reused for a static screenshot in marketing copy without coupling.
 */

export interface DecodeStep {
  /** Tiny label rendered above the math, e.g. "Substitute". */
  label: string
  /** KaTeX expression. Use \\\\ for line breaks inside the math block. */
  tex: string
}

/** The "before" expression shown when the hero is idle. */
export const TANGLED = String.raw`\begin{cases} 3x + 2y = 16 \\ x - y = 1 \end{cases}`

export const DECODE_STEPS: DecodeStep[] = [
  { label: 'Rearrange',  tex: String.raw`x = y + 1` },
  { label: 'Substitute', tex: String.raw`3(y + 1) + 2y = 16` },
  { label: 'Collect',    tex: String.raw`5y + 3 = 16` },
  { label: 'Solve',      tex: String.raw`y = \tfrac{13}{5},\ \ x = \tfrac{18}{5}` },
]