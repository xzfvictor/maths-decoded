import { Link } from 'react-router-dom'
import { topicsForUnit, strandForTopic, UNIT_TITLES } from '../content/topics'
import { DOT_POINTS, STRANDS } from '../content/coverage'
import type { Unit } from '../content/types'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio } from '../lib/storage'
import { ProgressBar } from '../components/ProgressBar'

const VCE_UNITS: Unit[] = [1, 2]

export function Home() {
  useProgress()
  const totalTopics = topicsForUnit(1).length + topicsForUnit(2).length + topicsForUnit(10).length
  const preVceTopics = topicsForUnit(10)

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
