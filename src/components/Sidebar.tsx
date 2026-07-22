import { NavLink, useParams } from 'react-router-dom'
import { topicsForUnit, UNIT_TITLES } from '../content/topics'
import type { Unit } from '../content/types'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio, isLessonDone } from '../lib/storage'

const UNITS: Unit[] = [1, 2, 10]

export function Sidebar({ onNavigate }: { onNavigate?: () => void }) {
  useProgress() // re-render on progress changes so ticks update live
  const { id: activeTopicId } = useParams<{ id: string; lessonId: string }>()

  return (
    <nav className="flex h-full flex-col gap-6 overflow-y-auto p-4">
      <NavLink
        to="/"
        onClick={onNavigate}
        className="text-lg font-bold text-slate-900 dark:text-white"
      >
        VCE Maths Methods
        <span className="block text-xs font-normal text-slate-500">Units 1, 2 &amp; Pre-VCE</span>
      </NavLink>

      {UNITS.map((unit) => {
        const topics = topicsForUnit(unit)
        return (
          <div key={unit}>
            <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-400">
              {UNIT_TITLES[unit]}
            </p>
            <ul className="space-y-1">
              {topics.map((t) => {
                const ratio = topicLessonRatio(t.id, t.lessons.length)
                const done = ratio >= 1 && t.lessons.length > 0
                const isActive = t.id === activeTopicId
                return (
                  <li key={t.id}>
                    <NavLink
                      to={`/topic/${t.id}`}
                      onClick={onNavigate}
                      className={({ isActive: linkActive }) =>
                        `flex items-center gap-2 rounded-lg px-3 py-2 text-sm transition ${
                          linkActive
                            ? 'bg-brand-100 font-semibold text-brand-800 dark:bg-brand-900/50 dark:text-brand-100'
                            : 'text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800'
                        }`
                      }
                    >
                      <span
                        className={`flex h-4 w-4 shrink-0 items-center justify-center rounded-full border text-[10px] ${
                          done
                            ? 'border-emerald-500 bg-emerald-500 text-white'
                            : 'border-slate-300 dark:border-slate-600'
                        }`}
                      >
                        {done ? '✓' : ''}
                      </span>
                      <span className="flex-1">{t.title}</span>
                    </NavLink>

                    {/* Expand the active topic into its lessons. */}
                    {isActive && (
                      <ul className="ml-4 mt-1 space-y-0.5 border-l border-slate-200 pl-3 dark:border-slate-700">
                        {t.lessons.map((l, i) => {
                          const lessonDone = isLessonDone(t.id, l.id)
                          return (
                            <li key={l.id}>
                              <NavLink
                                to={`/topic/${t.id}/${l.id}`}
                                onClick={onNavigate}
                                className={({ isActive: la }) =>
                                  `flex items-center gap-2 rounded-md px-2 py-1.5 text-xs transition ${
                                    la
                                      ? 'bg-brand-50 font-semibold text-brand-700 dark:bg-brand-900/30 dark:text-brand-200'
                                      : 'text-slate-500 hover:bg-slate-100 dark:text-slate-400 dark:hover:bg-slate-800'
                                  }`
                                }
                              >
                                <span
                                  className={`text-[10px] ${lessonDone ? 'text-emerald-500' : 'text-slate-300 dark:text-slate-600'}`}
                                >
                                  {lessonDone ? '✓' : '○'}
                                </span>
                                <span className="flex-1">
                                  {i + 1}. {l.heading}
                                </span>
                              </NavLink>
                            </li>
                          )
                        })}
                      </ul>
                    )}
                  </li>
                )
              })}
              {topics.length === 0 && (
                <li className="px-3 py-2 text-xs italic text-slate-400">Coming soon</li>
              )}
            </ul>
          </div>
        )
      })}
    </nav>
  )
}
