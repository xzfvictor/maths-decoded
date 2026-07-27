/**
 * Server-render the Sidebar for every Pre-VCE topic URL and assert that
 * the rendered HTML does NOT contain the wrong "VCE Mathematical Methods
 * — Unit 1" header, and DOES contain the right "Pre-VCE Year 10 Maths"
 * header. Catches the actual user-visible bug end-to-end (or rather,
 * end-to-render), without needing a browser.
 *
 * Run with: npx tsx scripts/verify-sidebar-ssr.tsx
 */

import { renderToString } from 'react-dom/server'
import { MemoryRouter } from 'react-router-dom'
import { Sidebar } from '../src/components/Sidebar'
import { TOPICS } from '../src/content/topics'

const PRE_VCE_HEADER = 'Pre-VCE Year 10 Maths'
const UNIT_1_HEADER = 'VCE Mathematical Methods — Unit 1'
const UNIT_2_HEADER = 'VCE Mathematical Methods — Unit 2'

interface Row {
  url: string
  topicId: string
  topicUnit: number
  module: string
  expectedHeader: string
  hasWrongHeader: boolean
  hasExpectedHeader: boolean
  activeTopicHighlighted: boolean
  ok: boolean
}

function renderAt(pathname: string): string {
  return renderToString(
    <MemoryRouter initialEntries={[pathname]}>
      <Sidebar />
    </MemoryRouter>,
  )
}

const rows: Row[] = []

// Every Pre-VCE topic must render the Pre-VCE sidebar.
for (const t of TOPICS.filter((x) => x.unit === 10)) {
  const url = `/topic/${t.id}`
  const html = renderAt(url)
  const hasExpected = html.includes(PRE_VCE_HEADER)
  const activeHighlighted = html.includes(`href="/topic/${t.id}"`)
  const ok = hasExpected && !html.includes(UNIT_1_HEADER) && activeHighlighted
  rows.push({
    url,
    topicId: t.id,
    topicUnit: t.unit,
    module: 'pre-vce',
    expectedHeader: PRE_VCE_HEADER,
    hasWrongHeader: html.includes(UNIT_1_HEADER),
    hasExpectedHeader: hasExpected,
    activeTopicHighlighted: activeHighlighted,
    ok,
  })
}

// Spot-check VCE Unit 1.
for (const t of TOPICS.filter((x) => x.unit === 1).slice(0, 3)) {
  const url = `/topic/${t.id}`
  const html = renderAt(url)
  rows.push({
    url,
    topicId: t.id,
    topicUnit: t.unit,
    module: 'maths-methods-unit1',
    expectedHeader: UNIT_1_HEADER,
    hasWrongHeader: html.includes(PRE_VCE_HEADER),
    hasExpectedHeader: html.includes(UNIT_1_HEADER),
    activeTopicHighlighted: html.includes(`href="/topic/${t.id}"`),
    ok: html.includes(UNIT_1_HEADER) && !html.includes(PRE_VCE_HEADER),
  })
}

// Spot-check VCE Unit 2.
for (const t of TOPICS.filter((x) => x.unit === 2).slice(0, 3)) {
  const url = `/topic/${t.id}`
  const html = renderAt(url)
  rows.push({
    url,
    topicId: t.id,
    topicUnit: t.unit,
    module: 'maths-methods-unit2',
    expectedHeader: UNIT_2_HEADER,
    hasWrongHeader: html.includes(PRE_VCE_HEADER),
    hasExpectedHeader: html.includes(UNIT_2_HEADER),
    activeTopicHighlighted: html.includes(`href="/topic/${t.id}"`),
    ok: html.includes(UNIT_2_HEADER) && !html.includes(PRE_VCE_HEADER),
  })
}

// Lesson URL form must also work.
const sampleLessonTopic = TOPICS.find((t) => t.unit === 10 && t.lessons.length > 0)
if (sampleLessonTopic) {
  const url = `/topic/${sampleLessonTopic.id}/${sampleLessonTopic.lessons[0].id}`
  const html = renderAt(url)
  rows.push({
    url,
    topicId: sampleLessonTopic.id,
    topicUnit: sampleLessonTopic.unit,
    module: 'pre-vce',
    expectedHeader: PRE_VCE_HEADER,
    hasWrongHeader: html.includes(UNIT_1_HEADER),
    hasExpectedHeader: html.includes(PRE_VCE_HEADER),
    activeTopicHighlighted: html.includes(`href="/topic/${sampleLessonTopic.id}"`),
    ok: html.includes(PRE_VCE_HEADER) && !html.includes(UNIT_1_HEADER),
  })
}

const failed = rows.filter((r) => !r.ok)
const wrongHeader = rows.filter((r) => r.hasWrongHeader)

console.log()
console.log(`Total rows: ${rows.length}`)
console.log(`Pre-VCE rows: ${rows.filter((r) => r.module === 'pre-vce').length}`)
console.log(`VCE Unit 1 rows: ${rows.filter((r) => r.module === 'maths-methods-unit1').length}`)
console.log(`VCE Unit 2 rows: ${rows.filter((r) => r.module === 'maths-methods-unit2').length}`)
console.log()
if (wrongHeader.length === 0) {
  console.log(`✓ No row renders the wrong "VCE Mathematical Methods — Unit 1" header.`)
} else {
  console.log(`✗ ${wrongHeader.length} rows still show the wrong header:`)
  for (const r of wrongHeader) console.log(`    ${r.url}`)
}
if (failed.length === 0) {
  console.log(`✓ All ${rows.length} SSR snapshots match expected module + active topic.`)
} else {
  console.log(`✗ ${failed.length} mismatches:`)
  for (const r of failed) {
    console.log(
      `    ${r.url}  expected=${r.expectedHeader}  wrongHeader=${r.hasWrongHeader}  expected=${r.hasExpectedHeader}  active=${r.activeTopicHighlighted}`,
    )
  }
}
process.exit(failed.length === 0 && wrongHeader.length === 0 ? 0 : 1)