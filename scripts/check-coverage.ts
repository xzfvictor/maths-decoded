// Build-time guarantee that every VCAA study-design dot point is claimed by at least
// one topic. Run with `npm run check:coverage`. Exits non-zero if anything is unmapped
// or if a topic references an unknown dot-point id.

import { DOT_POINTS, DOT_POINT_IDS } from '../src/content/coverage'
import { TOPICS } from '../src/content/topics'

const claimed = new Set<string>()
let hadError = false

for (const topic of TOPICS) {
  for (const dp of topic.dotPoints) {
    if (!DOT_POINT_IDS.includes(dp)) {
      console.error(`✗ Topic "${topic.id}" references unknown dot point "${dp}"`)
      hadError = true
    }
    claimed.add(dp)
  }
}

const unclaimed = DOT_POINTS.filter((d) => !claimed.has(d.id))

console.log(`Topics registered: ${TOPICS.length}`)
console.log(`Dot points total:  ${DOT_POINTS.length}`)
console.log(`Dot points mapped: ${claimed.size}`)

if (unclaimed.length > 0) {
  console.error(`\n✗ ${unclaimed.length} dot point(s) not yet covered by any topic:`)
  for (const d of unclaimed) {
    console.error(`   [${d.id}] Unit ${d.unit} AoS ${d.aos}: ${d.text}`)
  }
  hadError = true
} else {
  console.log('\n✓ Every study-design dot point is claimed by at least one topic.')
}

process.exit(hadError ? 1 : 0)
