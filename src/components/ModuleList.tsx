import { Link } from 'react-router-dom'
import { MODULES, topicsForModule, homePathForModule, UNIT_TITLES } from '../content/topics'
import { useProgress } from '../lib/useProgress'
import { useSession } from '../lib/auth'

/**
 * Numbered module list on the landing page. One row per registered
 * module, with a per-module colour number, tagline, topic count, and
 * (when the user is signed in) a progress bar.
 *
 * Designed to read as a curriculum progression rather than three
 * interchangeable products.
 */
export function ModuleList() {
  const auth = useSession()
  const progress = useProgress()
  const showProgress = auth.status === 'authed'

  return (
    <ol className="space-y-3">
      {MODULES.map((m, idx) => {
        const topics = topicsForModule(m.id)
        const totalLessons = topics.reduce((n, t) => n + t.lessons.length, 0)
        const completedLessons = topics.reduce(
          (n, t) => n + (progress.lessons[t.id]?.length ?? 0),
          0,
        )
        const pct = totalLessons === 0 ? 0 : Math.min(1, completedLessons / totalLessons)
        const num = String(idx + 1).padStart(2, '0')
        const colour = moduleColour(m.id)
        return (
          <li key={m.id}>
            <Link
              to={homePathForModule(m.id)}
              className="group flex items-center gap-4 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm transition hover:-translate-y-0.5 hover:border-brand-400 hover:shadow-md dark:border-slate-800 dark:bg-slate-900 sm:p-5"
            >
              <span
                className={`inline-flex h-10 w-10 shrink-0 items-center justify-center rounded-full text-sm font-bold ${colour.bg} ${colour.text}`}
                aria-hidden="true"
              >
                {num}
              </span>
              <div className="min-w-0 flex-1">
                <p className="truncate text-base font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white dark:group-hover:text-brand-300 sm:text-lg">
                  {m.title}
                </p>
                <p className="mt-0.5 truncate text-xs text-slate-500 dark:text-slate-400 sm:text-sm">
                  {tagline(m.id)}
                </p>
                <p className="mt-1 text-xs text-slate-500 dark:text-slate-400">
                  {topics.length} topic{topics.length === 1 ? '' : 's'}
                  {totalLessons > 0 && ` · ${totalLessons} lessons`}
                </p>
                {showProgress && completedLessons > 0 && (
                  <div className="mt-3 h-1.5 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
                    <div
                      className="h-full rounded-full bg-brand-500 transition-[width] duration-300"
                      style={{ width: `${Math.round(pct * 100)}%` }}
                    />
                  </div>
                )}
              </div>
              <span
                className="shrink-0 text-slate-300 transition group-hover:translate-x-0.5 group-hover:text-brand-500 dark:text-slate-600"
                aria-hidden="true"
              >
                →
              </span>
            </Link>
          </li>
        )
      })}
    </ol>
  )
}

function moduleColour(id: string): { bg: string; text: string } {
  if (id === 'maths-methods-unit1') {
    return { bg: 'bg-sky-100 dark:bg-sky-900/40', text: 'text-sky-700 dark:text-sky-200' }
  }
  if (id === 'maths-methods-unit2') {
    return { bg: 'bg-violet-100 dark:bg-violet-900/40', text: 'text-violet-700 dark:text-violet-200' }
  }
  if (id === 'year-7') {
    return { bg: 'bg-amber-100 dark:bg-amber-900/40', text: 'text-amber-700 dark:text-amber-200' }
  }
  if (id === 'year-8') {
    return { bg: 'bg-rose-100 dark:bg-rose-900/40', text: 'text-rose-700 dark:text-rose-200' }
  }
  if (id === 'year-9') {
    return { bg: 'bg-teal-100 dark:bg-teal-900/40', text: 'text-teal-700 dark:text-teal-200' }
  }
  if (id === 'year-10') {
    return { bg: 'bg-emerald-100 dark:bg-emerald-900/40', text: 'text-emerald-700 dark:text-emerald-200' }
  }
  // year-10a
  return { bg: 'bg-indigo-100 dark:bg-indigo-900/40', text: 'text-indigo-700 dark:text-indigo-200' }
}

function tagline(id: string): string {
  if (id === 'maths-methods-unit1')
    return 'Functions, algebra, calculus and probability — the first half of VCE Methods.'
  if (id === 'maths-methods-unit2')
    return 'Transcendentals, calculus and probability — the second half.'
  if (id === 'year-7')
    return 'Foundations across number, algebra, measurement, space, statistics & probability.'
  if (id === 'year-8')
    return 'Linear algebra, geometry, Pythagoras, sampling, and complementary events.'
  if (id === 'year-9')
    return 'Real numbers, quadratics, trigonometry, scientific notation, and bivariate statistics.'
  if (id === 'year-10')
    return 'Factorisation, simultaneous equations, modelling, and statistical investigations.'
  // year-10a
  return 'Surds, logarithms, polynomials, trigonometry, and standard deviation — extension into VCE.'
}

// Re-export for any callers that still want the unit-titles map.
export { UNIT_TITLES }