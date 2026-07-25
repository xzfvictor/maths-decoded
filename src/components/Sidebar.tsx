import { useState } from 'react'
import { NavLink, useLocation, useParams } from 'react-router-dom'
import {
  topicsForUnit,
  strandForTopic,
  topicById,
  UNIT_TITLES,
  moduleById,
  type ModuleId,
} from '../content/topics'
import { STRANDS, type Strand } from '../content/coverage'
import type { Unit } from '../content/types'
import { useProgress } from '../lib/useProgress'
import { topicLessonRatio, isLessonDone } from '../lib/storage'

/**
 * Render the active topic's lessons inline in the sidebar so the student
 * can jump back into any lesson without scrolling back to the topic page.
 * Shared between the VCE and Pre-VCE sidebar trees.
 */
function ActiveTopicLessons({
  topicId,
  onNavigate,
}: {
  topicId: string
  onNavigate?: () => void
}) {
  const topic = topicById(topicId)
  if (!topic) return null

  return (
    <ul className="ml-4 mt-1 space-y-0.5 border-l border-slate-200 pl-3 dark:border-slate-700">
      {topic.lessons.map((l, i) => {
        const lessonDone = isLessonDone(topic.id, l.id)
        return (
          <li key={l.id}>
            <NavLink
              to={`/topic/${topic.id}/${l.id}`}
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
  )
}

/**
 * Render the VCE module's two units (1 and 2) as a flat list of topics.
 */
function VceSidebarSection({
  activeTopicId,
  onNavigate,
}: {
  activeTopicId?: string
  onNavigate?: () => void
}) {
  const units: Unit[] = [1, 2]
  return (
    <div className="space-y-4">
      {units.map((unit) => {
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
                      <span className="flex-1">
                        <span className="mr-1 text-[10px] text-slate-400">#{t.order}</span>
                        {t.title}
                      </span>
                    </NavLink>
                    {isActive && (
                      <ActiveTopicLessons topicId={t.id} onNavigate={onNavigate} />
                    )}
                  </li>
                )
              })}
            </ul>
          </div>
        )
      })}
    </div>
  )
}

/**
 * Render the Pre-VCE module: topics grouped by strand, each strand collapsible.
 */
function PreVceSidebarSection({
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

  const [open, setOpen] = useState<Record<Strand['id'], boolean>>(() =>
    Object.fromEntries(STRANDS.map((s) => [s.id, true])) as Record<Strand['id'], boolean>,
  )

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
            <li
              key={strand.id}
              className="rounded-lg border border-slate-200 dark:border-slate-800"
            >
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
                          <ActiveTopicLessons topicId={t.id} onNavigate={onNavigate} />
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

/**
 * Derive which module to show in the sidebar from the current route.
 * - /vce* → VCE topics
 * - /pre-vce* → Pre-VCE topics
 * - /topic/:id → look up the topic and pick the module that contains it
 * - / (landing) → default to VCE
 */
function useActiveModule(): ModuleId {
  const location = useLocation()
  const params = useParams<{ id: string }>()
  if (location.pathname.startsWith('/pre-vce')) return 'pre-vce'
  if (location.pathname.startsWith('/vce')) return 'vce'
  if (location.pathname.startsWith('/topic/') && params.id) {
    const t = topicById(params.id)
    if (t?.unit === 10) return 'pre-vce'
  }
  return 'vce'
}

export function Sidebar({ onNavigate }: { onNavigate?: () => void }) {
  useProgress()
  const { id: activeTopicId } = useParams<{ id: string; lessonId: string }>()
  const activeModule = useActiveModule()
  const m = moduleById(activeModule)

  return (
    <nav className="flex h-full flex-col gap-4 overflow-y-auto p-4">
      <div>
        <NavLink
          to="/"
          onClick={onNavigate}
          className="text-lg font-bold text-slate-900 dark:text-white"
        >
          {m?.title ?? 'VCE Maths Methods'}
          <span className="block text-xs font-normal text-slate-500">{m?.tagline}</span>
        </NavLink>
      </div>

      {/* Always-available switch-module link — the way back to the landing
          page from anywhere in the app. */}
      <NavLink
        to="/"
        onClick={onNavigate}
        className="inline-flex w-fit items-center gap-1 rounded-lg border border-slate-200 px-2.5 py-1 text-xs font-semibold text-slate-600 transition hover:border-brand-400 hover:text-brand-700 dark:border-slate-700 dark:text-slate-300 dark:hover:text-brand-200"
        title="Back to module selection"
      >
        ← Switch module
      </NavLink>

      {activeModule === 'vce' ? (
        <VceSidebarSection activeTopicId={activeTopicId} onNavigate={onNavigate} />
      ) : (
        <PreVceSidebarSection activeTopicId={activeTopicId} onNavigate={onNavigate} />
      )}
    </nav>
  )
}