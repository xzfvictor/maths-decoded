import { Link } from 'react-router-dom'
import { topicsForUnit, strandForTopic, UNIT_TITLES } from '../content/topics'
import { DOT_POINTS, STRANDS } from '../content/coverage'
import type { Unit } from '../content/types'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio } from '../lib/storage'
import { ProgressBar } from '../components/ProgressBar'

const VCE_UNITS: Unit[] = [1, 2]

/** Returns true if the student has completed at least one lesson anywhere. */
function hasAnyProgress(): boolean {
  if (typeof localStorage === 'undefined') return false
  try {
    const raw = localStorage.getItem('vce-mm-progress-v1')
    if (!raw) return false
    const parsed = JSON.parse(raw) as { lessons?: Record<string, string[]> }
    return Object.values(parsed.lessons ?? {}).some((arr) => arr.length > 0)
  } catch {
    return false
  }
}

export function Home() {
  useProgress()
  const totalTopics = topicsForUnit(1).length + topicsForUnit(2).length + topicsForUnit(10).length
  const preVceTopics = topicsForUnit(10)
  const unit1Topics = topicsForUnit(1)
  const firstTopic = unit1Topics[0]

  // The "where to start" panel: a newcomer-friendly nudge that points to the
  // Pre-VCE strand index if the student has no progress yet, otherwise to the
  // first Unit 1 topic. We avoid being prescriptive about *what* they should
  // study — just give them an obvious entry point.
  const showOnboarding = !hasAnyProgress()

  return (
    <div className="mx-auto max-w-4xl">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-slate-900 dark:text-white">
          VCE Mathematical Methods — Units 1 &amp; 2
        </h1>
        <p className="mt-2 max-w-2xl text-slate-600 dark:text-slate-300">
          A complete self-study companion mapped to every point of the VCE Mathematics Study
          Design (2023–2027) and the Victorian Curriculum Level 10 (Pre-VCE) Mathematics
          syllabus. Pick a topic, read the theory, then practise with worked exercises. Your
          progress is saved on this device.
        </p>
        <p className="mt-2 text-sm text-slate-400">
          {totalTopics} topics available · {DOT_POINTS.length} study-design points tracked
        </p>
      </header>

      {showOnboarding && (
        <section className="learner-tip mb-8">
          <p className="font-semibold text-slate-800 dark:text-slate-100">
            👋 New here? Start wherever feels right.
          </p>
          <p className="mt-1 text-slate-700 dark:text-slate-300">
            You don't need any prior VCE Maths Methods knowledge — every lesson begins with a
            short theory recap and walks you through a worked example before the exercises.
            If you want to brush up on Year 10 foundations first, jump to the{' '}
            <Link to="/topic/m-algebra-linear-eq" className="font-medium text-brand-700 underline hover:no-underline dark:text-brand-300">
              Pre-VCE algebra strand
            </Link>
            ; otherwise start at the top of{' '}
            <Link to={`/topic/${firstTopic.id}`} className="font-medium text-brand-700 underline hover:no-underline dark:text-brand-300">
              Unit 1, Topic 1
            </Link>
            .
          </p>
        </section>
      )}

      <HowItWorks />

      {VCE_UNITS.map((unit) => {
        const topics = topicsForUnit(unit)
        return (
          <section key={unit} className="mb-10">
            <h2 className="mb-3 text-xl font-semibold text-slate-800 dark:text-slate-100">
              {UNIT_TITLES[unit]}
            </h2>
            {topics.length === 0 ? (
              <p className="text-sm italic text-slate-400">Topics coming soon.</p>
            ) : (
              <div className="grid gap-4 sm:grid-cols-2">
                {topics.map((t) => {
                  const ratio = topicLessonRatio(t.id, t.lessons.length)
                  return (
                    <Link
                      key={t.id}
                      to={`/topic/${t.id}`}
                      className="group rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:border-brand-400 hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
                    >
                      <div className="mb-1 flex items-center justify-between">
                        <span className="text-xs font-semibold uppercase tracking-wide text-brand-500">
                          Topic {t.order}
                        </span>
                        <span className="text-xs text-slate-400">
                          {t.lessons.length} lessons
                        </span>
                      </div>
                      <h3 className="text-lg font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white">
                        {t.title}
                      </h3>
                      <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{t.blurb}</p>
                      <div className="mt-3">
                        <ProgressBar ratio={ratio} />
                      </div>
                    </Link>
                  )
                })}
              </div>
            )}
          </section>
        )
      })}

      <section className="mb-10">
        <h2 className="mb-1 text-xl font-semibold text-slate-800 dark:text-slate-100">
          {UNIT_TITLES[10]}
        </h2>
        <p className="mb-5 text-sm text-slate-500 dark:text-slate-400">
          Foundation topics organised into the six curriculum strands. Each strand contains
          one or more topics.
        </p>
        <div className="space-y-5">
          {STRANDS.map((strand) => {
            const strandTopics = preVceTopics.filter(
              (t) => strandForTopic(t)?.id === strand.id,
            )
            if (strandTopics.length === 0) return null
            return (
              <div
                key={strand.id}
                className="rounded-xl border border-slate-200 bg-slate-50 p-4 dark:border-slate-800 dark:bg-slate-900/40"
              >
                <div className="mb-3 flex items-baseline justify-between">
                  <h3 className="text-lg font-semibold text-slate-800 dark:text-slate-100">
                    {strand.name}
                  </h3>
                  <span className="text-xs text-slate-400">
                    {strandTopics.length} topic{strandTopics.length === 1 ? '' : 's'}
                  </span>
                </div>
                <p className="mb-3 text-sm text-slate-500 dark:text-slate-400">
                  {strand.description}
                </p>
                <div className="grid gap-3 sm:grid-cols-2">
                  {strandTopics.map((t) => {
                    const ratio = topicLessonRatio(t.id, t.lessons.length)
                    return (
                      <Link
                        key={t.id}
                        to={`/topic/${t.id}`}
                        className="group rounded-lg border border-slate-200 bg-white p-4 shadow-sm transition hover:border-brand-400 hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
                      >
                        <div className="mb-1 flex items-center justify-between">
                          <span className="text-[10px] font-semibold uppercase tracking-wide text-brand-500">
                            {strand.name}
                          </span>
                          <span className="text-xs text-slate-400">
                            {t.lessons.length} lesson{t.lessons.length === 1 ? '' : 's'}
                          </span>
                        </div>
                        <h4 className="text-base font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white">
                          {t.title}
                        </h4>
                        <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
                          {t.blurb}
                        </p>
                        <div className="mt-2">
                          <ProgressBar ratio={ratio} />
                        </div>
                      </Link>
                    )
                  })}
                </div>
              </div>
            )
          })}
        </div>
      </section>
    </div>
  )
}

/**
 * A short "how a lesson works" explainer. Newcomers often don't know what
 * to expect; spelling out the lesson structure upfront removes friction.
 */
function HowItWorks() {
  const items = [
    {
      label: '1. Read the theory',
      body: 'Each lesson opens with a short, plain-English explanation of the idea — no assumed background.',
    },
    {
      label: '2. Follow a worked example',
      body: 'A complete example reveals one step at a time. Try to predict the next line before you click.',
    },
    {
      label: '3. Practise with exercises',
      body: 'Questions are graded intro → core → challenge. New questions generate a fresh variant on demand.',
    },
    {
      label: '4. Mark complete and move on',
      body: 'When you can do the exercises confidently, mark the lesson complete and progress to the next one.',
    },
  ]
  return (
    <section className="mb-10 rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
      <h2 className="mb-3 text-base font-semibold text-slate-800 dark:text-slate-100">
        How a lesson works
      </h2>
      <ol className="grid gap-3 sm:grid-cols-2">
        {items.map((it) => (
          <li key={it.label} className="rounded-lg bg-slate-50 p-3 dark:bg-slate-900/60">
            <p className="text-sm font-semibold text-slate-800 dark:text-slate-100">{it.label}</p>
            <p className="mt-1 text-sm text-slate-600 dark:text-slate-300">{it.body}</p>
          </li>
        ))}
      </ol>
    </section>
  )
}
