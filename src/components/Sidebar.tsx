import { useState } from 'react'
import { NavLink, useParams } from 'react-router-dom'
import {
  topicsForUnit,
  strandForTopic,
  UNIT_TITLES,
} from '../content/topics'
import { STRANDS, type Strand } from '../content/coverage'
import type { Unit } from '../content/types'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio, isLessonDone } from '../lib/storage'

/** Render the VCE (non-Pre-VCE) unit: a flat list of topics. */
function VceUnitSection({
  unit,
  activeTopicId,
  onNavigate,
}: {
  unit: Unit
  activeTopicId?: string
  onNavigate?: () => void
}) {
  const topics = topicsForUnit(unit)
  return (
    <div>
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
}

/** Render the Pre-VCE unit: topics grouped by strand, each strand collapsible. */
function PreVceUnitSection({
  activeTopicId,
  onNavigate,
}: {
  activeTopicId?: string
  onNavigate?: () => void
}) {
  const topics = topicsForUnit(10)
  const activeStrandId = activeTopicId
    ? strandForTopic(topics.find((t) => t.id === activeTopicId)!)?.id
    : undefined

  // All strands start expanded. The user can collapse any of them.
  const [open, setOpen] = useState<Record<Strand['id'], boolean>>(() =>
    Object.fromEntries(STRANDS.map((s) => [s.id, true])) as Record<Strand['id'], boolean>,
  )

  // Whenever the user lands on a topic in a closed strand, open that strand.
  if (activeStrandId && !open[activeStrandId]) {
    setOpen((o) => ({ ...o, [activeStrandId]: true }))
  }

  return (
    <div>
      <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-400">
        {UNIT_TITLES[10]}
      </p>
      <ul className="space-y-2">
        {STRANDS.map((strand) => {
          const strandTopics = topics.filter(
            (t) => strandForTopic(t)?.id === strand.id,
          )
          if (strandTopics.length === 0) return null
          const isOpen = open[strand.id]
          const strandHasActive = activeStrandId === strand.id
          return (
            <li key={strand.id} className="rounded-lg border border-slate-200 dark:border-slate-800">
              <button
                onClick={() => setOpen((o) => ({ ...o, [strand.id]: !o[strand.id] }))}
                className={`flex w-full items-center justify-between gap-2 rounded-lg px-3 py-2 text-left text-sm font-semibold transition ${
                  strandHasActive
                    ? 'bg-brand-50 text-brand-800 dark:bg-brand-900/30 dark:text-brand-100'
                    : 'text-slate-700 hover:bg-slate-100 dark:text-slate-200 dark:hover:bg-slate-800'
                }`}
                aria-expanded={isOpen}
              >
                <span className="flex items-center gap-2">
                  <span
                    className={`inline-block transition-transform ${isOpen ? 'rotate-90' : ''}`}
                    aria-hidden="true"
                  >
                    ▸
                  </span>
                  {strand.name}
                </span>
                <span className="text-[10px] font-normal text-slate-400">
                  {strandTopics.length} topic{strandTopics.length === 1 ? '' : 's'}
                </span>
              </button>
              {isOpen && (
                <ul className="space-y-0.5 px-2 pb-2">
                  {strandTopics.map((t) => {
                    const ratio = topicLessonRatio(t.id, t.lessons.length)
                    const done = ratio >= 1 && t.lessons.length > 0
                    const isActive = t.id === activeTopicId
                    return (
                      <li key={t.id}>
                        <NavLink
                          to={`/topic/${t.id}`}
                          onClick={onNavigate}
                          className={({ isActive: linkActive }) =>
                            `flex items-center gap-2 rounded-md px-2.5 py-1.5 text-sm transition ${
                              linkActive
                                ? 'bg-brand-100 font-semibold text-brand-800 dark:bg-brand-900/50 dark:text-brand-100'
                                : 'text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800'
                            }`
                          }
                        >
                          <span
                            className={`flex h-3.5 w-3.5 shrink-0 items-center justify-center rounded-full border text-[10px] ${
                              done
                                ? 'border-emerald-500 bg-emerald-500 text-white'
                                : 'border-slate-300 dark:border-slate-600'
                            }`}
                          >
                            {done ? '✓' : ''}
                          </span>
                          <span className="flex-1">{t.title}</span>
                        </NavLink>

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
                </ul>
              )}
            </li>
          )
        })}
      </ul>
    </div>
  )
}

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

      <VceUnitSection unit={1} activeTopicId={activeTopicId} onNavigate={onNavigate} />
      <VceUnitSection unit={2} activeTopicId={activeTopicId} onNavigate={onNavigate} />
      <PreVceUnitSection activeTopicId={activeTopicId} onNavigate={onNavigate} />
    </nav>
  )
}
