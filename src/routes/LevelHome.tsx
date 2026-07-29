import { Link } from 'react-router-dom'
import { topicsForUnit, strandForTopic, UNIT_TITLES } from '../content/topics'
import { STRANDS } from '../content/coverage'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio } from '../lib/storage'
import { ProgressBar } from '../components/ProgressBar'
import type { Unit } from '../content/types'

/**
 * Foundation module home — shows topics for a single year level (7, 8, 9, 10,
 * or 10A), grouped by strand. All Foundation levels share the same six-strand
 * taxonomy, so the same component handles each level with a `unit` prop.
 */
export function LevelHome({ unit }: { unit: Unit }) {
  useProgress()
  const levelTopics = topicsForUnit(unit)

  return (
    <div className="mx-auto max-w-4xl">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-slate-900 dark:text-white">
          {UNIT_TITLES[unit]}
        </h1>
        <p className="mt-2 max-w-2xl text-slate-600 dark:text-slate-300">
          {levelSubtitle(unit)}
        </p>
        {unit === '10A' && (
          <p className="learner-tip mt-4">
            <span className="font-semibold text-slate-800 dark:text-slate-100">
              No achievement standard:
            </span>{' '}
            Level 10A topics are organised for extension into VCE Mathematical
            Methods.
          </p>
        )}
      </header>

      <div className="space-y-5">
        {STRANDS.map((strand) => {
          const strandTopics = levelTopics.filter(
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

function levelSubtitle(unit: Unit): string {
  switch (unit) {
    case 7:
      return 'Year 7 foundation topics organised into the six curriculum strands. Work through them in order; each topic builds on the ones before it.'
    case 8:
      return 'Year 8 topics organised by strand — extending Year 7 with linear algebra, geometry, Pythagoras, sampling, and complementary probability.'
    case 9:
      return 'Year 9 topics organised by strand — extending Year 8 with real numbers, quadratics, trigonometry, and bivariate statistics.'
    case 10:
      return 'Year 10 topics organised into the six curriculum strands. Use this on its own, or as a bridge into VCE Mathematical Methods.'
    case '10A':
      return 'Year 10A extension topics — surds, logarithms, polynomials, trig, and standard deviation — preparing you for VCE Mathematical Methods.'
    default:
      return ''
  }
}
