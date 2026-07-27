import { Link } from 'react-router-dom'
import { MODULES, topicsForModule, UNIT_TITLES, homePathForModule } from '../content/topics'
import { DOT_POINTS, STRANDS } from '../content/coverage'
import { useProgress } from '../lib/useProgress'

/**
 * The first page the student sees. They pick a module here — VCE Unit 1,
 * VCE Unit 2, or Pre-VCE Year 10 — and the rest of the app narrows itself
 * to that module until they come back here and choose a different one.
 */
export function LandingPage() {
  useProgress()
  const totalLessons = MODULES.reduce(
    (n, m) => n + topicsForModule(m.id).reduce((a, t) => a + t.lessons.length, 0),
    0,
  )

  return (
    <div className="mx-auto max-w-5xl">
      <header className="mb-10">
        <h1 className="text-3xl font-bold text-slate-900 dark:text-white sm:text-4xl">
          MathsDecoded
        </h1>
        <p className="mt-2 text-lg text-slate-600 dark:text-slate-300">
          What would you like to learn?
        </p>
        <p className="mt-3 max-w-2xl text-base text-slate-600 dark:text-slate-300">
          Pick the module that matches what you're studying. Each one covers
          the full syllabus with short lessons, worked examples, and exercises.
          Your progress is saved on this device — you can come back here any
          time to switch modules.
        </p>
        <p className="mt-3 text-sm text-slate-400">
          {MODULES.length} modules · {totalLessons} lessons · {DOT_POINTS.length} syllabus points
          covered
        </p>
      </header>

      <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {MODULES.map((m) => (
          <Link
            key={m.id}
            to={homePathForModule(m.id)}
            className="group flex flex-col rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-0.5 hover:border-brand-400 hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
          >
            <span
              className={`mb-3 inline-flex w-fit items-center rounded-full px-3 py-1 text-xs font-semibold uppercase tracking-wide ${badgeClass(m.id)}`}
            >
              {badgeLabel(m.id)}
            </span>
            <h2 className="text-xl font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white">
              {m.title}
            </h2>
            <p className="mt-2 flex-1 text-sm text-slate-600 dark:text-slate-300">
              {description(m.id)}
            </p>
            <ul className="mt-4 space-y-1 text-xs text-slate-500 dark:text-slate-400">
              {m.units.map((u) => (
                <li key={u}>• {UNIT_TITLES[u]}</li>
              ))}
              {m.id === 'pre-vce' &&
                STRANDS.map((s) => <li key={s.id}>• {s.name} strand</li>)}
            </ul>
            <span className="mt-5 inline-flex items-center gap-1 text-sm font-semibold text-brand-600 group-hover:underline dark:text-brand-300">
              {openLabel(m.id)} →
            </span>
          </Link>
        ))}
      </div>

      <p className="mt-10 text-xs text-slate-400">
        Switch modules any time using{' '}
        <span className="font-semibold">Switch module</span> in the sidebar.
      </p>
    </div>
  )
}

function badgeClass(id: string): string {
  if (id === 'maths-methods-unit1')
    return 'bg-sky-100 text-sky-800 dark:bg-sky-900/40 dark:text-sky-200'
  if (id === 'maths-methods-unit2')
    return 'bg-violet-100 text-violet-800 dark:bg-violet-900/40 dark:text-violet-200'
  return 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-200'
}

function badgeLabel(id: string): string {
  if (id === 'maths-methods-unit1') return 'Unit 1'
  if (id === 'maths-methods-unit2') return 'Unit 2'
  return 'Pre-VCE'
}

function description(id: string): string {
  if (id === 'maths-methods-unit1')
    return 'Functions, algebra, calculus and probability — the first half of VCE Mathematical Methods. Eleven topics that build on each other in order.'
  if (id === 'maths-methods-unit2')
    return 'Transcendental functions, calculus and probability — the second half. Eleven topics covering circular functions, exponentials, logs, calculus and more.'
  return 'Year 10 foundations organised into the six strands (Number, Algebra, Measurement, Space, Statistics, Probability). Use as a refresher before VCE, or on its own.'
}

function openLabel(id: string): string {
  if (id === 'maths-methods-unit1') return 'Open Unit 1'
  if (id === 'maths-methods-unit2') return 'Open Unit 2'
  return 'Open Pre-VCE'
}