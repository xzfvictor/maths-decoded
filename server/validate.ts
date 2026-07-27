/**
 * Validate the `submit_exercise` tool_use payload coming back from M3.
 * Same checks `scripts/verify.ts` runs against curated exercises, applied
 * to whatever the model produced. Returns a discriminated union so the
 * caller can tell "model gave malformed JSON" from "model gave a real
 * instance the checker rejects".
 *
 * The `originalInstance` is kept and returned in failure cases so the
 * client can swap it back in without losing state.
 */

import type { ExerciseInstance } from '../src/content/types'
import { checkAnswer } from '../src/lib/answer'

export type ValidationError =
  | { kind: 'malformed'; reason: string }
  | { kind: 'missing_fields'; fields: string[] }
  | { kind: 'bad_answer_type'; got: unknown }
  | { kind: 'empty_answer'; reason: string }
  | { kind: 'checker_self_fail'; got: string; type: string }
  | { kind: 'choices_inconsistent'; reason: string }
  | { kind: 'unparsable_numeric'; got: string }
  | { kind: 'no_solution'; got: number }
  | { kind: 'prompt_too_short'; len: number }
  | { kind: 'naked_math'; examples: string[]; reason: string }

export type ValidationResult =
  | { ok: true; instance: ExerciseInstance }
  | { ok: false; error: ValidationError }

const VALID_TYPES = new Set(['exact', 'numeric', 'polynomial', 'set'])

/** Parse the model's tool input. Tolerates JSON strings. */
export function parseModelInput(raw: unknown): Record<string, unknown> {
  if (raw && typeof raw === 'object' && !Array.isArray(raw)) return raw as Record<string, unknown>
  if (typeof raw === 'string') {
    try {
      const parsed = JSON.parse(raw)
      if (parsed && typeof parsed === 'object' && !Array.isArray(parsed)) {
        return parsed as Record<string, unknown>
      }
    } catch {
      /* fall through */
    }
  }
  throw new Error('model output is not a JSON object')
}

/** Same lenient number parser as `src/lib/answer.ts:14`. */
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

function normalise(s: string): string {
  return s.trim().toLowerCase().replace(/\s+/g, '').replace(/\*/g, '').replace(/\^/g, '')
}

/**
 * Detect math expressions written as plain text instead of being wrapped in
 * `$...$` / `$$...$$` delimiters. Returns null on a clean prompt, or
 * `{ examples, reason }` listing the offending patterns.
 *
 * Patterns we flag (each is overwhelmingly likely to be math):
 *   - variable with exponent: `x^2`, `b^2`, `a^n`
 *   - polynomial coefficient pair: `3x`, `7y` (when not part of a longer word)
 *   - equation terminator: `= 0`
 *   - common algebraic operators between a digit and a variable
 *
 * We split the prompt on math spans first so legit text inside `$$...$$`
 * doesn't get flagged.
 */
export function detectNakedMath(prompt: string): { examples: string[]; reason: string } | null {
  const examples: string[] = []
  // Match either $$...$$ or $...$. The split keeps the matched delimiters
  // as their own elements, so we can drop them.
  const segments = prompt.split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+?\$)/g)
  for (const seg of segments) {
    if (seg.startsWith('$')) continue // Inside math — fine.
    // Variable with exponent: x^2, b^2, a^n, x^{12}.
    const supMatches = seg.match(/[a-zA-Z]\^(\{[^}]+\}|\d+)/g)
    if (supMatches) examples.push(...supMatches.slice(0, 4))
    // Equation terminator: "= 0" (with optional whitespace, optional punctuation).
    const eqZero = seg.match(/=\s*0\b/g)
    if (eqZero) examples.push(...eqZero.slice(0, 2))
    // Discriminant / "b^2 - 4ac" style: a variable followed by a minus and
    // a digit-prefixed expression, after we've already caught `x^2` cases.
    // Skipped here — covered by supMatches via the leading variable power.
    // Polynomial coefficient followed by variable: " 3x", " - 7x", "(2y".
    // Match only when the digit is on the boundary (preceded by space/start,
    // or after an opening paren / comma) and the letter is not part of a
    // longer word.
    const coeff = seg.match(/(?:^|[\s(,])(\-?\s?\d+)\s*([a-zA-Z])(?![a-zA-Z0-9])/g)
    if (coeff) examples.push(...coeff.slice(0, 3).map((s) => s.trim()))
  }
  if (examples.length === 0) return null
  const unique = [...new Set(examples)].slice(0, 5)
  return {
    reason: `unwrapped math in prompt (${unique.join(', ')})`,
    examples: unique,
  }
}

export function validate(raw: unknown): ValidationResult {
  let input: Record<string, unknown>
  try {
    input = parseModelInput(raw)
  } catch (e) {
    return { ok: false, error: { kind: 'malformed', reason: (e as Error).message } }
  }

  // Required fields present and non-empty.
  const required = ['prompt', 'answer', 'answerType', 'solution'] as const
  const missing: string[] = []
  for (const k of required) {
    const v = input[k]
    if (v === undefined || v === null) {
      missing.push(k)
      continue
    }
    if (typeof v === 'string' && v.trim() === '') missing.push(k)
    if (Array.isArray(v) && v.length === 0) missing.push(k)
  }
  if (missing.length > 0) {
    return { ok: false, error: { kind: 'missing_fields', fields: missing } }
  }

  const answerType = String(input.answerType)
  if (!VALID_TYPES.has(answerType)) {
    return { ok: false, error: { kind: 'bad_answer_type', got: input.answerType } }
  }

  const answer = String(input.answer).trim()
  if (answer === '') {
    return { ok: false, error: { kind: 'empty_answer', reason: 'answer is whitespace' } }
  }

  const prompt = String(input.prompt)
  if (prompt.length < 20) {
    return { ok: false, error: { kind: 'prompt_too_short', len: prompt.length } }
  }

  // Prompt must wrap math in `$...$` / `$$...$$` so KaTeX renders it.
  // The model occasionally emits ASCII math (e.g. `3x^2 - 7x + 2 = 0`)
  // outside delimiters, which the student sees as plain characters. We
  // detect that here and reject the instance so the retry path can
  // prompt the model again with explicit feedback.
  const naked = detectNakedMath(prompt)
  if (naked) {
    return { ok: false, error: { kind: 'naked_math', examples: naked.examples, reason: naked.reason } }
  }

  const solutionRaw = input.solution as unknown[]
  if (!Array.isArray(solutionRaw) || solutionRaw.length === 0) {
    return { ok: false, error: { kind: 'no_solution', got: solutionRaw?.length ?? -1 } }
  }
  // Scrub stray HTML/markup and trim. Models occasionally emit a closing
  // tag or escaped character that doesn't belong in student-facing text.
  const cleanedStrings = solutionRaw
    .map((s) => String(s).replace(/<[^>]+>/g, '').trim())
    .filter((s) => s.length > 0)
  if (cleanedStrings.length === 0) {
    return { ok: false, error: { kind: 'no_solution', got: solutionRaw.length } }
  }
  // If the model emitted a single-element array with internal `||` or
  // newline separators, split it back into ordered steps so the UI sees
  // a real ordered list.
  const solution = cleanedStrings.flatMap((s) => {
    if (cleanedStrings.length > 1) return [s]
    if (s.includes('||')) return s.split(/\s*\|\|\s*/).map((p) => p.trim()).filter(Boolean)
    if (s.includes('\n')) return s.split(/\n+/).map((p) => p.trim()).filter(Boolean)
    return [s]
  })

  // Self-check: the declared answer must pass its own checker.
  if (!checkAnswer(answerType as 'exact' | 'numeric' | 'polynomial' | 'set', answer, answer)) {
    return {
      ok: false,
      error: { kind: 'checker_self_fail', got: answer, type: answerType },
    }
  }

  // Type-specific extras.
  if (answerType === 'numeric') {
    if (parseNumber(answer) === null) {
      return { ok: false, error: { kind: 'unparsable_numeric', got: answer } }
    }
  }

  // Optional choices: must include answer (normalised) and have 2..6 entries.
  let choices: string[] | undefined
  const choicesRaw = input.choices
  if (choicesRaw !== undefined && choicesRaw !== null) {
    if (!Array.isArray(choicesRaw) || choicesRaw.length < 2 || choicesRaw.length > 6) {
      return {
        ok: false,
        error: { kind: 'choices_inconsistent', reason: 'choices must be an array of 2..6 strings' },
      }
    }
    choices = choicesRaw.map((c) => String(c))
    const normAnswer = normalise(answer)
    const hasAnswer = choices.some((c) => normalise(c) === normAnswer)
    if (!hasAnswer) {
      return {
        ok: false,
        error: {
          kind: 'choices_inconsistent',
          reason: 'one choice must equal answer after normalisation',
        },
      }
    }
  }

  // Optional hint: trim, drop empty.
  let hint: string | undefined
  const hintRaw = input.hint
  if (typeof hintRaw === 'string' && hintRaw.trim().length > 0) {
    hint = hintRaw.trim()
  }

  const instance: ExerciseInstance = {
    prompt,
    answer,
    answerType: answerType as ExerciseInstance['answerType'],
    solution,
    ...(hint !== undefined ? { hint } : {}),
    ...(choices !== undefined ? { choices } : {}),
  }

  return { ok: true, instance }
}
