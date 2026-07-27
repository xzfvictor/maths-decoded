/**
 * End-to-end test for `/api/regenerate-exercise`. Requires a running
 * server on $PORT (default 8787).
 *
 * Usage:
 *   npm run dev:server            # in one terminal
 *   npm run test:regenerate       # in another
 *
 * Asserts:
 *   - HTTP 200 response
 *   - regenerated === true
 *   - instance.answerType matches the original
 *   - instance.solution.length >= 1
 *   - instance.prompt.length > 20
 *   - checkAnswer(self) === true (the regenerated instance passes its own checker)
 *   - difficulty override is accepted (a 'challenge' exercise can be regenerated
 *     as 'intro')
 *   - invalid difficulty string is rejected (400)
 */

import { TOPICS } from '../src/content/topics'
import type { ExerciseInstance } from '../src/content/types'
import { checkAnswer } from '../src/lib/answer'
import { detectNakedMath } from '../server/validate'

const BASE = process.env.TEST_BASE_URL ?? 'http://localhost:8787'

const failures: string[] = []
function assert(cond: unknown, msg: string): void {
  if (!cond) failures.push(msg)
}

// Find the first curated exercise. Prefer one with 'challenge' difficulty so
// we can also exercise the Easier override flow.
type Fixture = {
  topicId: string
  lessonId: string
  exercise: Extract<typeof TOPICS[number]['lessons'][number]['exercises'][number], { kind: 'curated' }>
}

let challengeFixture: Fixture | null = null
let anyFixture: Fixture | null = null

for (const topic of TOPICS) {
  for (const lesson of topic.lessons) {
    for (const ex of lesson.exercises) {
      if (ex.kind !== 'curated') continue
      if (!anyFixture) anyFixture = { topicId: topic.id, lessonId: lesson.id, exercise: ex }
      if (ex.difficulty === 'challenge' && !challengeFixture) {
        challengeFixture = { topicId: topic.id, lessonId: lesson.id, exercise: ex }
      }
    }
  }
}

const fixture: Fixture | null = challengeFixture ?? anyFixture
if (!fixture) {
  console.error('no curated exercise found in TOPICS — cannot run test')
  process.exit(1)
}

const { topicId, lessonId, exercise }: Fixture = fixture
const original: ExerciseInstance = exercise.instance

console.log(`fixture: ${topicId} / ${lessonId} / ${exercise.id} (${exercise.difficulty})`)
console.log(`answer:  ${original.answer} (${original.answerType})`)

interface Response {
  regenerated?: boolean
  instance?: ExerciseInstance
  error?: string
}

async function assertValidRegen(label: string, body: Record<string, unknown>): Promise<void> {
  const res = await fetch(`${BASE}/api/regenerate-exercise`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(body),
  })
  console.log(`\n[${label}] HTTP ${res.status}`)
  assert(res.status === 200, `expected HTTP 200, got ${res.status}`)
  assert(
    res.headers.get('content-type')?.includes('application/json'),
    'expected JSON content-type',
  )

  const data = (await res.json()) as Response
  assert(data.regenerated === true, `[${label}] expected regenerated=true, got error=${data.error}`)
  assert(!!data.instance, `[${label}] missing instance in response`)

  if (data.instance) {
    const ins = data.instance
    assert(
      ins.answerType === original.answerType,
      `[${label}] answerType drift: original=${original.answerType} got=${ins.answerType}`,
    )
    assert(ins.solution.length >= 1, `[${label}] solution must have >= 1 step, got ${ins.solution.length}`)
    assert(ins.prompt.length > 20, `[${label}] prompt must be > 20 chars, got ${ins.prompt.length}`)
    assert(
      checkAnswer(ins.answerType, ins.answer, ins.answer),
      `[${label}] regenerated answer "${ins.answer}" (${ins.answerType}) fails self-check`,
    )
    // Every math expression in the prompt must be wrapped in `$...$` so
    // KaTeX renders it. The server's naked-math detector should have caught
    // and rejected any prompt that didn't comply — so by the time the
    // instance reaches us, this must hold.
    const naked = detectNakedMath(ins.prompt)
    assert(
      naked === null,
      `[${label}] prompt has unwrapped math (${naked?.reason}) — must be wrapped in $...$`,
    )
    console.log(`[${label}] got: ${ins.answer} (${ins.answerType})`)
    console.log(`[${label}] prompt: ${ins.prompt.slice(0, 80)}…`)
  }
}

await assertValidRegen('default difficulty', {
  topicId,
  lessonId,
  exerciseId: exercise.id,
  currentInstance: original,
})

// Override difficulty to 'intro' regardless of the exercise's declared
// difficulty. This exercises the "Easier" / "Harder" path.
if (exercise.difficulty !== 'intro') {
  await assertValidRegen('override intro', {
    topicId,
    lessonId,
    exerciseId: exercise.id,
    currentInstance: original,
    difficulty: 'intro',
  })
}

// Invalid difficulty should be rejected with 400 (not silently coerced).
{
  const bad = await fetch(`${BASE}/api/regenerate-exercise`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({
      topicId,
      lessonId,
      exerciseId: exercise.id,
      currentInstance: original,
      difficulty: 'impossible',
    }),
  })
  console.log(`\n[bad difficulty] HTTP ${bad.status}`)
  assert(bad.status === 400, `[bad difficulty] expected HTTP 400, got ${bad.status}`)
}

if (failures.length > 0) {
  console.error(`\n✗ ${failures.length} test failure(s):`)
  for (const f of failures) console.error(`  - ${f}`)
  process.exit(1)
}
console.log('\n✓ Regenerate endpoint returns valid instances across default and override paths.')
process.exit(0)
