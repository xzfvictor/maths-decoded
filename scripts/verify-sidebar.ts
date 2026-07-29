// Verify that the Sidebar's useActiveModule logic resolves the correct
// module for every topic URL. Mirrors the regex + topicById lookup
// in src/components/Sidebar.tsx so a regression in either place fails here.

import { TOPICS, moduleForUnit } from '../src/content/topics'

const TOPIC_RE = /^\/topic\/([^/]+)/

const year7 = TOPICS.filter((t) => t.unit === 7)
const year8 = TOPICS.filter((t) => t.unit === 8)
const year9 = TOPICS.filter((t) => t.unit === 9)
const year10 = TOPICS.filter((t) => t.unit === 10)
const year10a = TOPICS.filter((t) => t.unit === ('10A' as unknown as number))
const vceUnit1 = TOPICS.filter((t) => t.unit === 1)
const vceUnit2 = TOPICS.filter((t) => t.unit === 2)

function resolveActiveModule(pathname: string): { id: string; unit: number; module: string } {
  // Order matters: /year-10a must precede /year-10.
  if (pathname.startsWith('/year-10a')) return { id: pathname, unit: -1, module: 'year-10a' }
  if (pathname.startsWith('/year-10')) return { id: pathname, unit: -1, module: 'year-10' }
  if (pathname.startsWith('/year-9')) return { id: pathname, unit: -1, module: 'year-9' }
  if (pathname.startsWith('/year-8')) return { id: pathname, unit: -1, module: 'year-8' }
  if (pathname.startsWith('/year-7')) return { id: pathname, unit: -1, module: 'year-7' }
  if (pathname.startsWith('/maths-methods-unit2')) return { id: pathname, unit: -1, module: 'maths-methods-unit2' }
  if (pathname.startsWith('/maths-methods-unit1')) return { id: pathname, unit: -1, module: 'maths-methods-unit1' }
  const m = pathname.match(TOPIC_RE)
  if (m) {
    const t = TOPICS.find((x) => x.id === m[1])
    if (!t) return { id: m[1], unit: -1, module: 'unknown-id' }
    const mod = moduleForUnit(t.unit)
    if (!mod) return { id: t.id, unit: t.unit as unknown as number, module: 'unknown-unit' }
    return { id: t.id, unit: t.unit as unknown as number, module: mod }
  }
  return { id: '', unit: -1, module: 'year-7' }
}

let failed = 0
const checks: { label: string; url: string; expectModule: string; actual: string; ok: boolean }[] = []

const buckets: { topics: typeof TOPICS; expected: string }[] = [
  { topics: year7, expected: 'year-7' },
  { topics: year8, expected: 'year-8' },
  { topics: year9, expected: 'year-9' },
  { topics: year10, expected: 'year-10' },
  { topics: year10a, expected: 'year-10a' },
  { topics: vceUnit1, expected: 'maths-methods-unit1' },
  { topics: vceUnit2, expected: 'maths-methods-unit2' },
]

for (const { topics, expected } of buckets) {
  for (const t of topics) {
    const url = `/topic/${t.id}`
    const r = resolveActiveModule(url)
    const ok = r.module === expected
    checks.push({ label: t.id, url, expectModule: expected, actual: r.module, ok })
    if (!ok) failed++
  }
}

// Module home routes.
const homeRoutes = [
  '/year-7',
  '/year-8',
  '/year-9',
  '/year-10',
  '/year-10a',
  '/maths-methods-unit1',
  '/maths-methods-unit2',
  '/year-7/anything',
  '/year-10a/anything',
]
for (const url of homeRoutes) {
  const r = resolveActiveModule(url)
  let expected = 'year-7'
  if (url.startsWith('/year-10a')) expected = 'year-10a'
  else if (url.startsWith('/year-10')) expected = 'year-10'
  else if (url.startsWith('/year-9')) expected = 'year-9'
  else if (url.startsWith('/year-8')) expected = 'year-8'
  else if (url.startsWith('/year-7')) expected = 'year-7'
  else if (url === '/maths-methods-unit2') expected = 'maths-methods-unit2'
  else if (url === '/maths-methods-unit1') expected = 'maths-methods-unit1'
  const ok = r.module === expected
  checks.push({ label: url, url, expectModule: expected, actual: r.module, ok })
  if (!ok) failed++
}

// Lesson URL format /topic/:id/:lessonId — same regex must still capture id.
const sampleTopic = year7[0] ?? year8[0] ?? year9[0] ?? year10[0] ?? year10a[0] ?? vceUnit1[0]
if (sampleTopic) {
  const lessonUrl = `/topic/${sampleTopic.id}/some-lesson`
  const r2 = resolveActiveModule(lessonUrl)
  const expected = moduleForUnit(sampleTopic.unit)
  const ok = r2.module === expected
  checks.push({
    label: 'lesson URL',
    url: lessonUrl,
    expectModule: expected ?? 'unknown',
    actual: r2.module,
    ok,
  })
  if (!ok) failed++
}

console.log(`\nTotal checks: ${checks.length}`)
const failedRows = checks.filter((c) => !c.ok)
if (failedRows.length === 0) {
  console.log(`✓ All ${checks.length} URL resolutions match expected module.`)
} else {
  console.log(`✗ ${failedRows.length} mismatches:`)
  for (const c of failedRows) {
    console.log(`  ${c.label}: ${c.url}  expected=${c.expectModule}  got=${c.actual}`)
  }
}
console.log()
console.log(`Year 7 topics checked: ${year7.length}`)
console.log(`Year 8 topics checked: ${year8.length}`)
console.log(`Year 9 topics checked: ${year9.length}`)
console.log(`Year 10 topics checked: ${year10.length}`)
console.log(`Year 10A topics checked: ${year10a.length}`)
console.log(`VCE Unit 1 topics checked: ${vceUnit1.length}`)
console.log(`VCE Unit 2 topics checked: ${vceUnit2.length}`)
process.exit(failed === 0 ? 0 : 1)
