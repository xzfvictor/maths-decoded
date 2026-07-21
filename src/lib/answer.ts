import type { AnswerType } from '../content/types'

/** Normalise a free-text answer for tolerant comparison. */
function normalise(s: string): string {
  return s
    .trim()
    .toLowerCase()
    .replace(/\s+/g, '')
    .replace(/\*/g, '') // treat 3*x and 3x the same
    .replace(/\^/g, '') // x^2 vs x2 — normalised away for exact/poly text compare
}

/** Parse a number allowing simple fractions like "3/4" and unicode minus. */
function parseNumber(s: string): number | null {
  const cleaned = s.trim().replace(/−/g, '-').replace(/\s+/g, '')
  if (/^-?\d+(\.\d+)?$/.test(cleaned)) return parseFloat(cleaned)
  const frac = cleaned.match(/^(-?\d+)\/(-?\d+)$/)
  if (frac) {
    const d = parseFloat(frac[2])
    if (d === 0) return null
    return parseFloat(frac[1]) / d
  }
  return null
}

/** Normalise a polynomial-ish answer: sort terms, strip spaces & explicit multiplication. */
function normalisePolynomial(s: string): string {
  const cleaned = s
    .toLowerCase()
    .replace(/\s+/g, '')
    .replace(/\*/g, '')
    .replace(/−/g, '-')
  // Split into signed terms and sort so "x^2+2x" === "2x+x^2".
  const withLeadingSign = cleaned.startsWith('-') ? cleaned : `+${cleaned}`
  const terms = withLeadingSign.match(/[+-][^+-]+/g)
  if (!terms) return cleaned
  return terms.sort().join('')
}

export function checkAnswer(type: AnswerType, correct: string, given: string): boolean {
  if (given.trim() === '') return false
  switch (type) {
    case 'numeric': {
      const a = parseNumber(correct)
      const b = parseNumber(given)
      if (a === null || b === null) return normalise(correct) === normalise(given)
      return Math.abs(a - b) < 1e-6
    }
    case 'polynomial':
      return normalisePolynomial(correct) === normalisePolynomial(given)
    case 'set': {
      const split = (s: string) =>
        s
          .split(/[,;]/)
          .map((x) => {
            const n = parseNumber(x)
            return n === null ? normalise(x) : String(n)
          })
          .filter((x) => x !== '')
          .sort()
      const a = split(correct)
      const b = split(given)
      return a.length === b.length && a.every((v, i) => v === b[i])
    }
    case 'exact':
    default:
      return normalise(correct) === normalise(given)
  }
}
