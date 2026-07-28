import { useProgress } from '../lib/useProgress'
import { MODULES, topicsForModule } from '../content/topics'
import { DOT_POINTS } from '../content/coverage'
import { DecodeHero } from '../components/DecodeHero'
import { ModuleList } from '../components/ModuleList'
import { AuthBadge } from '../components/AuthBadge'
import { ThemeToggle } from '../components/ThemeToggle'

/**
 * The first page the student sees.
 *
 * Hero-led layout:
 *   - Top-right theme toggle (the global header is hidden on `/`).
 *   - "AI-powered" pill, headline, sub-paragraph.
 *   - Interactive decode demo.
 *   - "Pick a module" numbered list with progress bars.
 *   - Auth state panel (sign-in or welcome card).
 *   - Trust strip + stats footer.
 */
export function LandingPage() {
  useProgress()
  const totalLessons = MODULES.reduce(
    (n, m) => n + topicsForModule(m.id).reduce((a, t) => a + t.lessons.length, 0),
    0,
  )

  return (
    <div className="relative mx-auto max-w-4xl px-2 sm:px-0">
      {/* Top-right dark-mode toggle (the global header chrome is hidden
          on the landing page — see App.tsx's onLanding check). */}
      <div className="absolute right-0 top-0">
        <ThemeToggle />
      </div>

      <header className="mb-8 sm:mb-10">
        <span className="inline-flex items-center gap-1.5 rounded-full bg-brand-50 px-3 py-1 text-xs font-semibold text-brand-700 dark:bg-brand-900/30 dark:text-brand-200">
          <span aria-hidden="true">✨</span> AI-powered
        </span>
        <h1 className="mt-3 text-3xl font-bold text-slate-900 dark:text-white sm:text-4xl lg:text-5xl">
          Decode the syllabus.
        </h1>
        <p className="mt-3 max-w-2xl text-base text-slate-600 dark:text-slate-300 sm:text-lg">
          Short lessons, worked examples, and exercises that meet you where
          you are. AI narrates each lesson and generates fresh practice
          questions on demand.
        </p>
      </header>

      <DecodeHero />

      <section className="mt-12">
        <h2 className="mb-4 text-lg font-semibold text-slate-900 dark:text-white sm:text-xl">
          Pick a module
        </h2>
        <ModuleList />
      </section>

      <section className="mt-10">
        <AuthBadge />
      </section>

      <section className="mt-10">
        <p className="text-center text-xs text-slate-500 dark:text-slate-400">
          <span className="inline-flex flex-wrap items-center justify-center gap-x-2 gap-y-1">
            <span className="inline-flex items-center gap-1">
              <span aria-hidden="true">✨</span> AI decoding
            </span>
            <span aria-hidden="true">·</span>
            <span className="inline-flex items-center gap-1">
              <span aria-hidden="true">🎯</span> Full VCE coverage
            </span>
            <span aria-hidden="true">·</span>
            <span className="inline-flex items-center gap-1">
              <span aria-hidden="true">⏱</span> Self-paced
            </span>
          </span>
        </p>
      </section>

      <footer className="mt-8 border-t border-slate-200 pt-6 text-center text-xs text-slate-400 dark:border-slate-800">
        {DOT_POINTS.length} syllabus points · {MODULES.length} modules · {totalLessons} lessons covered
      </footer>
    </div>
  )
}