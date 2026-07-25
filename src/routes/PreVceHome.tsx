import { Link } from 'react-router-dom'
import { topicsForUnit, strandForTopic, UNIT_TITLES } from '../content/topics'
import { STRANDS } from '../content/coverage'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio } from '../lib/storage'
import { ProgressBar } from '../components/ProgressBar'

/** Pre-VCE module home — shows only Year 10 topics, grouped by strand. */
export function PreVceHome() {
  useProgress()
  const preVceTopics = topicsForUnit(10)

  return (
    <div className="mx-auto max-w-4xl">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-slate-900 dark:text-white">
          {UNIT_TITLES[10]}
        </h1>
        <p className="mt-2 max-w-2xl text-slate-600 dark:text-slate-300">
          Year 10 foundation topics organised into the six curriculum strands.
          Use this as a refresher before tackling VCE Mathematical Methods, or on
          its own to consolidate Year 10 work.
        </p>
      </header>

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
                <h2 className="text-lg font-semibold text-slate-800 dark:text-slate-100">
                  {strand.name}
                </h2>
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
                      <h3 className="text-base font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white">
                        {t.title}
                      </h3>
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
    </div>
  )
}