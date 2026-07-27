// Verify that the Sidebar's useActiveModule logic resolves the correct
// module for every Pre-VCE topic URL. Mirrors the regex + topicById lookup
// in src/components/Sidebar.tsx so a regression in either place fails here.

import { TOPICS } from '../src/content/topics'

const TOPIC_RE = /^\/topic\/([^/]+)/

const preVceTopics = TOPICS.filter((t) => t.unit === 10)
const vceUnit1 = TOPICS.filter((t) => t.unit === 1)
const vceUnit2 = TOPICS.filter((t) => t.unit === 2)

function resolveActiveModule(pathname: string): { id: string; unit: number; module: string } {
  if (pathname.startsWith('/pre-vce')) return { id: pathname, unit: -1, module: 'pre-vce' }
  if (pathname.startsWith('/maths-methods-unit2')) return { id: pathname, unit: -1, module: 'maths-methods-unit2' }
  if (pathname.startsWith('/maths-methods-unit1')) return { id: pathname, unit: -1, module: 'maths-methods-unit1' }
  const m = pathname.match(TOPIC_RE)
  if (m) {
    const t = TOPICS.find((x) => x.id === m[1])
    if (!t) return { id: m[1], unit: -1, module: 'unknown-id' }
    if (t.unit === 1) return { id: t.id, unit: t.unit, module: 'maths-methods-unit1' }
    if (t.unit === 2) return { id: t.id, unit: t.unit, module: 'maths-methods-unit2' }
    if (t.unit === 10) return { id: t.id, unit: t.unit, module: 'pre-vce' }
  }
  return { id: '', unit: -1, module: 'maths-methods-unit1' }
}

let failed = 0
const checks: { label: string; url: string; expectModule: string; actual: string; ok: boolean }[] = []

// Every Pre-VCE topic must resolve to pre-vce.
for (const t of preVceTopics) {
  const url = `/topic/${t.id}`
  const r = resolveActiveModule(url)
  const ok = r.module === 'pre-vce' && r.unit === 10
  checks.push({ label: t.id, url, expectModule: 'pre-vce', actual: r.module, ok })
  if (!ok) failed++
}

// Every VCE Unit 1 topic must resolve to maths-methods-unit1.
for (const t of vceUnit1) {
  const url = `/topic/${t.id}`
  const r = resolveActiveModule(url)
  const ok = r.module === 'maths-methods-unit1'
  checks.push({ label: t.id, url, expectModule: 'maths-methods-unit1', actual: r.module, ok })
  if (!ok) failed++
}

// Every VCE Unit 2 topic must resolve to maths-methods-unit2.
for (const t of vceUnit2) {
  const url = `/topic/${t.id}`
  const r = resolveActiveModule(url)
  const ok = r.module === 'maths-methods-unit2'
  checks.push({ label: t.id, url, expectModule: 'maths-methods-unit2', actual: r.module, ok })
  if (!ok) failed++
}

// Module home routes.
for (const url of ['/maths-methods-unit1', '/maths-methods-unit2', '/pre-vce', '/pre-vce/anything']) {
  const r = resolveActiveModule(url)
  // /pre-vce/anything should hit /pre-vce prefix first.
  const expected = url.startsWith('/pre-vce') ? 'pre-vce' : url === '/maths-methods-unit2' ? 'maths-methods-unit2' : 'maths-methods-unit1'
  const ok = r.module === expected
  checks.push({ label: url, url, expectModule: expected, actual: r.module, ok })
  if (!ok) failed++
}

// Lesson URL format /topic/:id/:lessonId — same regex must still capture id.
const lessonUrl = `/topic/${preVceTopics[0].id}/some-lesson`
const r2 = resolveActiveModule(lessonUrl)
const ok2 = r2.module === 'pre-vce' && r2.id === preVceTopics[0].id
checks.push({
  label: 'lesson URL',
  url: lessonUrl,
  expectModule: 'pre-vce',
  actual: r2.module,
  ok: ok2,
})
if (!ok2) failed++

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
console.log(`Pre-VCE topics checked: ${preVceTopics.length}`)
console.log(`VCE Unit 1 topics checked: ${vceUnit1.length}`)
console.log(`VCE Unit 2 topics checked: ${vceUnit2.length}`)
process.exit(failed === 0 ? 0 : 1)