// Helpers for building TeX fragments in parameterised questions. Keeping these
// centralised means every generated question renders signs/coefficients the same way.

/** Format a signed term to append after an existing term, e.g. 3 -> "+ 3", -2 -> "- 2". */
export function signed(n: number): string {
  return n < 0 ? `- ${Math.abs(n)}` : `+ ${n}`
}

/** Coefficient in front of a variable: 0 -> "", 1 -> "x", -1 -> "-x", 3 -> "3x". */
export function coeff(n: number, variable = 'x'): string {
  if (n === 0) return ''
  if (n === 1) return variable
  if (n === -1) return `-${variable}`
  return `${n}${variable}`
}

/** A signed term to append after an existing term. With a variable, drops a unit
 *  coefficient (appendTerm(-1,'x') -> "- x"); with variable '' it is a constant
 *  (appendTerm(1,'') -> "+ 1"). Zero contributes nothing. */
export function appendTerm(n: number, variable: string): string {
  if (n === 0) return ''
  const abs = Math.abs(n)
  const body = variable === '' ? `${abs}` : abs === 1 ? variable : `${abs}${variable}`
  return n < 0 ? ` - ${body}` : ` + ${body}`
}

/** Render a linear expression ax + b, dropping zero/one coefficients cleanly. */
export function linear(a: number, b: number, variable = 'x'): string {
  if (a === 0) return `${b}`
  const lead = coeff(a, variable)
  if (b === 0) return lead
  return `${lead}${appendTerm(b, '')}`
}

/** Render a monic-or-not quadratic ax^2 + bx + c, dropping 1-coefficients and zero terms.
 *  e.g. quadratic(1, 1, -4) -> "x^2 + x - 4"; quadratic(1, 2, 0) -> "x^2 + 2x". */
export function quadratic(a: number, b: number, c: number): string {
  const lead = a === 1 ? 'x^2' : a === -1 ? '-x^2' : `${a}x^2`
  return `${lead}${appendTerm(b, 'x')}${appendTerm(c, '')}`
}

/** Greatest common divisor for reducing fractions in answers. */
export function gcd(a: number, b: number): number {
  a = Math.abs(a)
  b = Math.abs(b)
  while (b) {
    ;[a, b] = [b, a % b]
  }
  return a || 1
}

/** Render a possibly-improper fraction as an exact TeX value, reducing first. */
export function frac(num: number, den: number): string {
  if (den === 0) return '\\text{undefined}'
  let n = num
  let d = den
  if (d < 0) {
    n = -n
    d = -d
  }
  const g = gcd(n, d)
  n /= g
  d /= g
  if (d === 1) return `${n}`
  const sign = n < 0 ? '-' : ''
  return `${sign}\\dfrac{${Math.abs(n)}}{${d}}`
}
