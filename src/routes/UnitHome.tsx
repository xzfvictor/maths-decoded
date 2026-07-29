import { Link } from 'react-router-dom'
import {
  topicsForUnit,
  UNIT_TITLES,
  topicsForModule,
  MODULE_PROGRESSION,
  moduleById,
  type ModuleId,
} from '../content/topics'
import type { Unit } from '../content/types'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio } from '../lib/storage'
import { ProgressBar } from '../components/ProgressBar'

/**
 * Home page for a single VCE unit (1 or 2). Shows only the topics in that
 * unit — sibling topics from the other VCE unit are hidden so the student
 * isn't tempted to jump ahead.
 *
 * `nextModuleId` is derived from `MODULE_PROGRESSION` so the "Finished this
 * unit?" card automatically follows the curriculum order (Year 7 → 8 → 9 →
 * 10 → 10A → VCE Unit 1 → VCE Unit 2). Unit 2 is the last module, so the
 * card doesn't render for it.
 */
export function UnitHome({
  unit,
  moduleId,
}: {
  unit: Unit
  moduleId: ModuleId
}) {
  useProgress()
  const topics = topicsForUnit(unit)

  const idx = MODULE_PROGRESSION.indexOf(moduleId)
  const nextModuleId: ModuleId | undefined =
    idx >= 0 && idx < MODULE_PROGRESSION.length - 1
      ? MODULE_PROGRESSION[idx + 1]
      : undefined
  const nextModule = nextModuleId ? moduleById(nextModuleId) : undefined

  return (
    <div className="mx-auto max-w-4xl">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-slate-900 dark:text-white">
          {UNIT_TITLES[unit]}
        </h1>
        <p className="mt-2 max-w-2xl text-slate-600 dark:text-slate-300">
          Every dot point in this unit, in curriculum order. Each topic assumes
          the ones before it, so work in order. The lessons here are short —
          theory, one or two worked examples, and exercises with full solutions.
        </p>
      </header>

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
                <h2 className="text-lg font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white">
                  {t.title}
                </h2>
                <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{t.blurb}</p>
                <div className="mt-3">
                  <ProgressBar ratio={ratio} />
                </div>
              </Link>
            )
          })}
        </div>
      )}

      {nextModule && (
        <section className="mt-10 rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
          <p className="text-xs font-semibold uppercase tracking-wide text-slate-400">
            Finished this unit?
          </p>
          <Link
            to={`/${nextModule.id}`}
            className="mt-1 block text-lg font-semibold text-slate-900 hover:text-brand-700 dark:text-white"
          >
            Continue to {nextModule.title} →
          </Link>
          <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
            {topicsForModule(nextModule.id).length} topics, {''}
            {topicsForModule(nextModule.id).reduce((n, t) => n + t.lessons.length, 0)} lessons
          </p>
        </section>
      )}
    </div>
  )
}