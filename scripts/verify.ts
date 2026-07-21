// Self-check for authored content. For every parameterised exercise across all
// registered topics, instantiate it over many seeds and assert that:
//   1. the declared `answer` passes its own checkAnswer (i.e. a student typing the
//      stated answer would be marked correct);
//   2. `answer` and `solution` are non-empty;
//   3. `build(seed)` is a pure function of seed (same seed → identical instance).
// Also checks curated exercises for self-consistency. Exits non-zero on any failure.

import { TOPICS } from '../src/content/topics'
import { checkAnswer } from '../src/lib/answer'
import type { ExerciseInstance } from '../src/content/types'

const SEEDS = 300
let failures = 0
let paramChecked = 0
let curatedChecked = 0

function validateInstance(where: string, inst: ExerciseInstance): void {
  if (!inst.prompt || inst.prompt.trim() === '') {
    console.error(`✗ ${where}: empty prompt`)
    failures++
  }
  if (inst.answer === undefined || inst.answer === null || String(inst.answer).trim() === '') {
    console.error(`✗ ${where}: empty answer`)
    failures++
    return
  }
  if (!inst.solution || inst.solution.length === 0) {
    console.error(`✗ ${where}: empty solution`)
    failures++
  }
  if (!checkAnswer(inst.answerType, inst.answer, inst.answer)) {
    console.error(
      `✗ ${where}: declared answer "${inst.answer}" (${inst.answerType}) does not pass its own checkAnswer`,
    )
    failures++
  }
}

for (const topic of TOPICS) {
  for (const lesson of topic.lessons) {
    for (const ex of lesson.exercises) {
      const base = `${topic.id}/${lesson.id}/${ex.id}`
      if (ex.kind === 'curated') {
        curatedChecked++
        validateInstance(base, ex.instance)
      } else {
        paramChecked++
        for (let seed = 0; seed < SEEDS; seed++) {
          const inst = ex.build(seed)
          validateInstance(`${base} [seed ${seed}]`, inst)
          // Purity: same seed must give an identical prompt+answer.
          const again = ex.build(seed)
          if (again.prompt !== inst.prompt || again.answer !== inst.answer) {
            console.error(`✗ ${base} [seed ${seed}]: build() is not pure (differs on re-run)`)
            failures++
          }
        }
      }
    }
  }
}

console.log(`Topics: ${TOPICS.length}`)
console.log(`Curated exercises checked: ${curatedChecked}`)
console.log(`Param exercises checked:   ${paramChecked} (× ${SEEDS} seeds)`)

if (failures > 0) {
  console.error(`\n✗ ${failures} problem(s) found.`)
  process.exit(1)
}
console.log('\n✓ All exercises validate: declared answers pass, no empties, builds are pure.')
process.exit(0)
