import { Link } from 'react-router-dom'
import { MODULES, topicsForModule, UNIT_TITLES } from '../content/topics'
import { DOT_POINTS, STRANDS } from '../content/coverage'
import { useProgress } from '../lib/useProgress'

/**
 * The first page the student sees. They pick a module here — VCE Units 1 & 2
 * or Pre-VCE Year 10 — and the rest of the app narrows itself to that module
 * until they come back here and choose a different one.
 */
export function LandingPage() {
  useProgress()
  const totalLessons = MODULES.reduce(
    (n, m) => n + topicsForModule(m.id).reduce((a, t) => a + t.lessons.length, 0),
    0,
  )

  return (
    <div className="mx-auto max-w-4xl">
      <header className="mb-10">
        <h1 className="text-3xl font-bold text-slate-900 dark:text-white sm:text-4xl">
          What would you like to learn?
        </h1>
        <p className="mt-3 max-w-2xl text-base text-slate-600 dark:text-slate-300">
          Pick the module that matches what you're studying. Each one covers the
          full syllabus with short lessons, worked examples, and exercises. Your
          progress is saved on this device — you can come back here any time to
          switch modules.
        </p>
        <p className="mt-3 text-sm text-slate-400">
          {MODULES.length} modules · {totalLessons} lessons · {DOT_POINTS.length} syllabus points
          covered
        </p>
      </header>

      <div className="grid gap-5 sm:grid-cols-2">
        {MODULES.map((m) => (
          <Link
            key={m.id}
            to={m.id === 'vce' ? '/vce' : '/pre-vce'}
            className="group flex flex-col rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-0.5 hover:border-brand-400 hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
          >
            <span
              className={`mb-3 inline-flex w-fit items-center rounded-full px-3 py-1 text-xs font-semibold uppercase tracking-wide ${
                m.id === 'vce'
                  ? 'bg-brand-100 text-brand-800 dark:bg-brand-900/40 dark:text-brand-200'
                  : 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-200'
              }`}
            >
              {m.tagline}
            </span>
            <h2 className="text-xl font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white">
              {m.title}
            </h2>
            <p className="mt-2 flex-1 text-sm text-slate-600 dark:text-slate-300">
              {m.id === 'vce' ? (
                <>
                  The full VCE Mathematical Methods study design — functions, algebra,
                  calculus, and probability across Units 1 and 2. Each lesson assumes
                  the previous ones, so work in order.
                </>
              ) : (
                <>
                  Year 10 foundations organised into the six strands (Number, Algebra,
                  Measurement, Space, Statistics, Probability). Use this to brush up
                  before tackling VCE, or on its own.
                </>
              )}
            </p>
            <ul className="mt-4 space-y-1 text-xs text-slate-500 dark:text-slate-400">
              {m.units.map((u) => (
                <li key={u}>• {UNIT_TITLES[u]}</li>
              ))}
              {m.id === 'pre-vce' &&
                STRANDS.map((s) => <li key={s.id}>• {s.name} strand</li>)}
            </ul>
            <span className="mt-5 inline-flex items-center gap-1 text-sm font-semibold text-brand-600 group-hover:underline dark:text-brand-300">
              {m.id === 'vce' ? 'Open VCE modules' : 'Open Pre-VCE'} →
            </span>
          </Link>
        ))}
      </div>

      <p className="mt-10 text-xs text-slate-400">
        Switch modules any time using <span className="font-semibold">Switch module</span> in
        the sidebar.
      </p>
    </div>
  )
}