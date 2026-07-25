import { Link } from 'react-router-dom'
import { topicsForUnit, UNIT_TITLES } from '../content/topics'
import type { Unit } from '../content/types'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio } from '../lib/storage'
import { ProgressBar } from '../components/ProgressBar'

/** VCE module home — shows only Units 1 and 2. */
export function VceHome() {
  useProgress()
  const units: Unit[] = [1, 2]

  return (
    <div className="mx-auto max-w-4xl">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-slate-900 dark:text-white">
          VCE Mathematical Methods — Units 1 &amp; 2
        </h1>
        <p className="mt-2 max-w-2xl text-slate-600 dark:text-slate-300">
          The full VCE study design mapped lesson-by-lesson. Pick a topic, read
          the theory, then practise with worked exercises. Each topic assumes
          the ones before it in the same unit.
        </p>
      </header>

      {units.map((unit) => {
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
                      <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
                        {t.blurb}
                      </p>
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
    </div>
  )
}