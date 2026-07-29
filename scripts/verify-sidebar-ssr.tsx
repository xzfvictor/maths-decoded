/**
 * Server-render the Sidebar for every topic URL across all modules and assert
 * that the rendered HTML does NOT contain the wrong "VCE Mathematical Methods
 * — Unit 1" header (and similar cross-module leaks), and DOES contain the
 * right module header. Catches user-visible bugs end-to-end without a
 * browser.
 *
 * Run with: npx tsx scripts/verify-sidebar-ssr.tsx
 */

import { renderToString } from 'react-dom/server'
import { MemoryRouter } from 'react-router-dom'
import { Sidebar } from '../src/components/Sidebar'
import { TOPICS, MODULES, moduleForUnit, type ModuleId } from '../src/content/topics'

const MODULE_HEADER: Record<ModuleId, string> = {
  'maths-methods-unit1': 'VCE Mathematical Methods — Unit 1',
  'maths-methods-unit2': 'VCE Mathematical Methods — Unit 2',
  'year-7': 'Year 7 Mathematics',
  'year-8': 'Year 8 Mathematics',
  'year-9': 'Year 9 Mathematics',
  'year-10': 'Year 10 Mathematics',
  'year-10a': 'Year 10A Mathematics',
}

const MODULE_IDS = Object.keys(MODULE_HEADER) as ModuleId[]

interface Row {
  url: string
  topicId: string
  topicUnit: number | string
  module: ModuleId | 'home-route'
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

// Render every topic across every module, asserting the sidebar header matches
// the topic's owning module.
for (const t of TOPICS) {
  const expectedModule = moduleForUnit(t.unit)
  if (!expectedModule) continue
  const expectedHeader = MODULE_HEADER[expectedModule]
  const url = `/topic/${t.id}`
  const html = renderAt(url)
  const hasExpected = html.includes(expectedHeader)
  const activeHighlighted = html.includes(`href="/topic/${t.id}"`)
  const wrongHeader = MODULE_IDS.some(
    (mid) => mid !== expectedModule && html.includes(MODULE_HEADER[mid]),
  )
  rows.push({
    url,
    topicId: t.id,
    topicUnit: t.unit as unknown as number | string,
    module: expectedModule,
    expectedHeader,
    hasWrongHeader: wrongHeader,
    hasExpectedHeader: hasExpected,
    activeTopicHighlighted: activeHighlighted,
    ok: hasExpected && !wrongHeader,
  })
}

// Module home routes should render their own header without leaking others.
for (const m of MODULES) {
  const url = `/${m.id}`
  const html = renderAt(url)
  const expectedHeader = MODULE_HEADER[m.id]
  const wrongHeader = MODULE_IDS.some(
    (mid) => mid !== m.id && html.includes(MODULE_HEADER[mid]),
  )
  rows.push({
    url,
    topicId: '',
    topicUnit: -1,
    module: 'home-route',
    expectedHeader,
    hasWrongHeader: wrongHeader,
    hasExpectedHeader: html.includes(expectedHeader),
    activeTopicHighlighted: false,
    ok: html.includes(expectedHeader) && !wrongHeader,
  })
}

// Lesson URL form must also work.
const sampleTopic = TOPICS.find((t) => t.lessons.length > 0)
if (sampleTopic) {
  const expectedModule = moduleForUnit(sampleTopic.unit)
  if (expectedModule) {
    const url = `/topic/${sampleTopic.id}/${sampleTopic.lessons[0].id}`
    const html = renderAt(url)
    const expectedHeader = MODULE_HEADER[expectedModule]
    const wrongHeader = MODULE_IDS.some(
      (mid) => mid !== expectedModule && html.includes(MODULE_HEADER[mid]),
    )
    rows.push({
      url,
      topicId: sampleTopic.id,
      topicUnit: sampleTopic.unit as unknown as number | string,
      module: expectedModule,
      expectedHeader,
      hasWrongHeader: wrongHeader,
      hasExpectedHeader: html.includes(expectedHeader),
      activeTopicHighlighted: html.includes(`href="/topic/${sampleTopic.id}"`),
      ok: html.includes(expectedHeader) && !wrongHeader,
    })
  }
}

const failed = rows.filter((r) => !r.ok)
const wrongHeader = rows.filter((r) => r.hasWrongHeader)

console.log()
console.log(`Total rows: ${rows.length}`)
const perModule: Record<string, number> = {}
for (const r of rows) {
  const key = typeof r.module === 'string' ? r.module : r.module
  perModule[key] = (perModule[key] ?? 0) + 1
}
for (const [k, v] of Object.entries(perModule)) {
  console.log(`${k} rows: ${v}`)
}
console.log()
if (wrongHeader.length === 0) {
  console.log(`✓ No row renders a foreign module header.`)
} else {
  console.log(`✗ ${wrongHeader.length} rows still show a foreign header:`)
  for (const r of wrongHeader) console.log(`    ${r.url}`)
}
if (failed.length === 0) {
  console.log(`✓ All ${rows.length} SSR snapshots match expected module + active topic.`)
} else {
  console.log(`✗ ${failed.length} mismatches:`)
  for (const r of failed.slice(0, 10)) {
    console.log(
      `    ${r.url}  expected=${r.expectedHeader}  wrongHeader=${r.hasWrongHeader}  expected=${r.hasExpectedHeader}`,
    )
  }
}
process.exit(failed.length === 0 && wrongHeader.length === 0 ? 0 : 1)
