/**
 * Build the system + user prompts that ask M3 to regenerate an exercise
 * testing the same syllabus dot points as the original.
 *
 * Inputs are plain `ExerciseInstance` shapes — same as the bundle. The
 * server is allowed to import `src/content/*` because the existing scripts
 * do (see `scripts/check-coverage.ts:6`).
 */

import type { ExerciseInstance, Topic, Lesson } from '../src/content/types'
import { DOT_POINTS } from '../src/content/coverage'

const SYSTEM_PROMPT = [
  'You are a maths exercise writer for an Australian VCE Mathematical Methods revision app.',
  'Write a SINGLE different question that tests the SAME syllabus dot points as the example question provided.',
  'Output via the submit_exercise tool — no prose, no markdown fences, no commentary outside the tool call.',
  '',
  'Hard rules:',
  '- The question must match the example\'s answerType exactly. Do not switch between numeric, polynomial, set, and exact.',
  '- The question must match the REQUESTED DIFFICULTY (intro/core/challenge), not the example\'s difficulty.',
  '  If the requested difficulty is intro, write a routine application of the same idea with no twists.',
  '  If it is core, match the example\'s depth.',
  '  If it is challenge, add an extension, multi-step twist, or a tricky variation of the same concept.',
  '- The answer field is what the student types into a text box and what a strict checker compares against.',
  '  The checker normalises whitespace, case, *, and ^. It does NOT parse LaTeX, TeX commands, \\dfrac, \\frac, \\cdot.',
  '    exact      → plain string ("Tuesday", "x-intercept", "yes").',
  '    numeric    → decimal "0.5" or simple fraction "1/3". NO TeX.',
  '    polynomial → e.g. "2x^2+3x-1", "-x+5". Checker sorts terms; order is irrelevant. NO "=", NO LaTeX.',
  '    set        → values separated by "," or ";", order-independent ("1, 3, 5").',
  '- PROMPT FORMAT — every math expression MUST be wrapped in `$...$` (inline) or `$$...$$` (block). The reader sees raw text for anything outside these delimiters, so unwrapped math like `3x^2` renders as the literal characters `3x^2` instead of a typeset formula.',
  '  GOOD: "Find the roots of $3x^2 - 7x + 2 = 0$."',
  '  BAD:  "Find the roots of 3x^2 - 7x + 2 = 0."  ← reader sees gibberish',
  '  Apply this rule to every variable with a power ($x^2$, $b^2$, $a^n$), every equation ($2x + 3 = 7$), every expression with operators ($x + 1$, $x - 2$), and every discriminant/factor ($b^2 - 4ac$).',
  '- solution is an ordered list of short steps. Each step is a single sentence with math inline in $...$.',
  '- choices (when present) is exactly 4 strings; one must equal answer after normalisation.',
  '- hint is optional, one short sentence.',
  '- Self-check before submitting: (1) the answer you write must, when normalised, equal itself (rewrite out \\frac, \\dfrac, \\cdot, =, or non-ASCII math operators); (2) every math expression in the prompt is wrapped in `$...$` or `$$...$$`.',
].join('\n')

/**
 * Tool schema forcing structured output. Reused exactly by every regeneration
 * call. The model's `tool_use.input` is what we validate.
 */
export const SUBMIT_EXERCISE_TOOL = {
  name: 'submit_exercise',
  description: 'Submit the regenerated exercise as a single JSON object.',
  input_schema: {
    type: 'object',
    required: ['prompt', 'answer', 'answerType', 'solution'],
    properties: {
      prompt: { type: 'string' },
      answer: { type: 'string' },
      answerType: { type: 'string', enum: ['exact', 'numeric', 'polynomial', 'set'] },
      solution: { type: 'array', items: { type: 'string' }, minItems: 1 },
      hint: { type: 'string' },
      choices: { type: 'array', items: { type: 'string' } },
    },
    additionalProperties: false,
  },
} as const

function dotPointLookup(id: string): { id: string; text: string } | null {
  const dp = DOT_POINTS.find((d) => d.id === id)
  return dp ? { id: dp.id, text: dp.text } : null
}

/** Strip $$ block math and inline $math$ markers to readable form for the model. */
function promptify(p: string): string {
  return p
    .replace(/```[\s\S]*?```/g, '')
    .replace(/\$\$[\s\S]*?\$\$/g, '[equation]')
    .replace(/\$[^$]+\$/g, (m) => m.replace(/[$]/g, '').trim())
}

/** Strip bold/italic/code markers so the inline JSON example stays readable. */
function flattenInline(s: string): string {
  return s
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\s+/g, ' ')
    .trim()
}

export function buildSystemPrompt(): string {
  return SYSTEM_PROMPT
}

export function buildUserPrompt(
  topic: Topic,
  lesson: Lesson,
  original: ExerciseInstance,
  difficulty: 'intro' | 'core' | 'challenge',
): string {
  const dotPoints = topic.dotPoints
    .map((id) => dotPointLookup(id))
    .filter((d): d is { id: string; text: string } => d !== null)

  const dotPointBlock = dotPoints.length
    ? dotPoints.map((d) => `- ${d.id}: "${d.text}"`).join('\n')
    : '- (no dot points declared for this topic — write to the lesson heading)'

  const choicesLine = original.choices && original.choices.length > 0
    ? original.choices.map((c) => promptify(c)).join(' | ')
    : '(none — open response)'

  const hintLine = original.hint ? flattenInline(promptify(original.hint)) : '(none)'

  const solutionLine = original.solution
    .map((s) => flattenInline(promptify(s)))
    .join(' || ')

  return [
    'Syllabus dot points the regenerated question MUST test:',
    dotPointBlock,
    '',
    `Topic:            ${topic.title}`,
    `Lesson:           ${lesson.heading}`,
    `Requested difficulty: ${difficulty}`,
    '',
    'Example exercise (the one being replaced — its difficulty is shown for context only):',
    `prompt:     ${promptify(original.prompt)}`,
    `answer:     ${flattenInline(original.answer)}`,
    `answerType: ${original.answerType}`,
    `solution:   ${solutionLine}`,
    `hint:       ${hintLine}`,
    `choices:    ${choicesLine}`,
    '',
    `Write a different question at the REQUESTED difficulty (${difficulty}), testing the same dot points, with the same answerType.`,
    'Use the submit_exercise tool.',
  ].join('\n')
}

/** A repair prompt appended when the model's first attempt fails validation. */
export function buildRepairPrompt(
  original: ExerciseInstance,
  reason: string,
  lastAttempt: unknown,
): string {
  const isNakedMath = reason.includes('naked_math')
  const nakedDetail = isNakedMath
    ? 'Wrap EVERY math expression in $...$ (inline) or $$...$$ (block). Without these delimiters, the student sees raw characters — `3x^2` shows as literal `3x^2`, not a typeset formula. Re-read your previous prompt and check every variable power (`x^2`, `b^2`, `a^n`), every equation, every algebraic expression.'
    : null

  return [
    'Your previous attempt was rejected by the validation gate.',
    `Reason: ${reason}`,
    'Last attempt (truncated):',
    JSON.stringify(lastAttempt).slice(0, 800),
    '',
    `Original answer was: "${original.answer}" (${original.answerType}).`,
    '',
    ...(nakedDetail ? [nakedDetail, ''] : []),
    'Resubmit via the submit_exercise tool. Remember:',
    '- answer field must be plain text the checker can normalize. NO \\frac, NO \\dfrac, NO \\cdot, NO "=].',
    '- If answerType is polynomial, terms may be in any order (the checker sorts them).',
    '- If answerType is numeric, write decimals or simple fractions like "1/3".',
    '- If answerType is set, separate values with "," or ";".',
    '- choices (when present) must include answer exactly (after normalisation).',
    '- prompt and solution math must be wrapped in `$...$` / `$$...$$`.',
  ].join('\n')
}
