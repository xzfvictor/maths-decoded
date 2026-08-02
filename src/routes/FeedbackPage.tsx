// Author-facing feedback dashboard. Lists every section a student has
// voted on, lets the author copy or download the raw JSON, and offers
// a destructive "Reset all feedback" action gated by a confirm dialog.
//
// The page is intentionally a "developer view" — it's reachable from
// the header and shows every section, no privacy filtering, so the
// author can spot which parts of the syllabus need rewriting.

import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { topicById } from '../content/topics'
import {
  getAllFeedback,
  resetFeedback,
  type FeedbackEntry,
  type FeedbackStore,
  type SectionType,
} from '../lib/feedback'

type GroupBy = 'topic' | 'lesson' | 'type'

const SECTION_TYPE_LABEL: Record<SectionType, string> = {
  audio: 'Explain to me',
  example: 'Worked example',
  exercise: 'Exercise',
}

const GROUP_LABEL: Record<GroupBy, string> = {
  topic: 'By topic',
  lesson: 'By lesson',
  type: 'By section type',
}

export function FeedbackPage() {
  // Re-read the store whenever a feedback write fires so the page
  // reflects votes made on lesson tabs in the same session.
  const [store, setStore] = useState<FeedbackStore>(() => getAllFeedback())
  const [groupBy, setGroupBy] = useState<GroupBy>('type')
  const [actionMsg, setActionMsg] = useState<string | null>(null)

  useEffect(() => {
    function refresh() {
      setStore(getAllFeedback())
    }
    window.addEventListener('vce-feedback-write', refresh)
    window.addEventListener('storage', refresh)
    return () => {
      window.removeEventListener('vce-feedback-write', refresh)
      window.removeEventListener('storage', refresh)
    }
  }, [])

  const entries = useMemo(() => {
    return Object.entries(store.votes)
      .map(([sectionId, entry]) => ({ sectionId, entry }))
      .sort((a, b) => b.entry.at - a.entry.at)
  }, [store])

  const upCount = entries.filter((e) => e.entry.vote === 'up').length
  const downCount = entries.filter((e) => e.entry.vote === 'down').length

  // Group entries by the selected dimension for display.
  const groups = useMemo(() => {
    const m = new Map<string, { sectionId: string; entry: FeedbackEntry }[]>()
    for (const row of entries) {
      const key = groupKey(row.entry, groupBy)
      const list = m.get(key) ?? []
      list.push(row)
      m.set(key, list)
    }
    return [...m.entries()].sort(([a], [b]) => a.localeCompare(b))
  }, [entries, groupBy])

  async function copyJson() {
    try {
      await navigator.clipboard.writeText(JSON.stringify(store, null, 2))
      setActionMsg('Copied feedback JSON to the clipboard.')
    } catch {
      setActionMsg("Couldn't access the clipboard — try Download JSON instead.")
    }
  }

  function downloadJson() {
    const blob = new Blob([JSON.stringify(store, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `feedback-${new Date().toISOString().slice(0, 10)}.json`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
    setActionMsg('Downloaded feedback JSON.')
  }

  function onReset() {
    if (!confirm('Reset all feedback on this device? This cannot be undone.')) return
    resetFeedback()
    setActionMsg('All feedback cleared.')
  }

  return (
    <article className="mx-auto max-w-3xl">
      <div className="mb-6">
        <Link to="/" className="text-sm text-brand-600 hover:underline">
          ← Modules
        </Link>
        <h1 className="mt-2 text-3xl font-bold text-slate-900 dark:text-white">
          Lesson feedback
        </h1>
        <p className="mt-1 text-sm text-slate-600 dark:text-slate-300">
          Everything collected from the 👍 / 👎 buttons on lesson pages,
          on this device. Use the export to share this data with Claude
          and ask for content improvements.
        </p>
      </div>

      {/* Summary stats + actions. */}
      <section className="mb-6 rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
        <div className="flex flex-wrap items-center gap-4">
          <Stat label="Sections with feedback" value={entries.length} />
          <Stat label="👍 Helpful" value={upCount} tone="emerald" />
          <Stat label="👎 Needs work" value={downCount} tone="rose" />
        </div>
        <div className="mt-4 flex flex-wrap items-center gap-2">
          <button
            type="button"
            onClick={copyJson}
            disabled={entries.length === 0}
            className="rounded-lg bg-brand-600 px-3 py-1.5 text-sm font-semibold text-white transition hover:bg-brand-700 disabled:cursor-not-allowed disabled:opacity-50"
          >
            Copy as JSON
          </button>
          <button
            type="button"
            onClick={downloadJson}
            disabled={entries.length === 0}
            className="rounded-lg border border-slate-300 px-3 py-1.5 text-sm font-medium text-slate-700 transition hover:bg-slate-100 disabled:cursor-not-allowed disabled:opacity-50 dark:border-slate-700 dark:text-slate-200 dark:hover:bg-slate-800"
          >
            Download JSON
          </button>
          <button
            type="button"
            onClick={onReset}
            disabled={entries.length === 0}
            className="ml-auto rounded-lg border border-rose-300 px-3 py-1.5 text-sm font-medium text-rose-700 transition hover:bg-rose-50 disabled:cursor-not-allowed disabled:opacity-50 dark:border-rose-700/60 dark:text-rose-300 dark:hover:bg-rose-950/30"
          >
            Reset all feedback
          </button>
        </div>
        {actionMsg && (
          <p className="mt-2 text-xs text-slate-500 dark:text-slate-400">{actionMsg}</p>
        )}
      </section>

      {/* Grouping tabs. */}
      <div className="mb-3 flex items-center gap-2">
        <span className="text-xs font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400">
          Group by
        </span>
        {(Object.keys(GROUP_LABEL) as GroupBy[]).map((g) => (
          <button
            key={g}
            type="button"
            onClick={() => setGroupBy(g)}
            className={`rounded-lg px-3 py-1 text-sm font-medium transition ${
              groupBy === g
                ? 'bg-brand-600 text-white'
                : 'border border-slate-300 text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800'
            }`}
          >
            {GROUP_LABEL[g]}
          </button>
        ))}
      </div>

      {/* Empty state. */}
      {entries.length === 0 && (
        <div className="rounded-xl border border-dashed border-slate-300 bg-slate-50 p-6 text-sm text-slate-500 dark:border-slate-700 dark:bg-slate-900/40 dark:text-slate-400">
          No feedback yet. As students use the 👍 / 👎 buttons on lesson
          pages, their votes will appear here.
        </div>
      )}

      {/* Grouped list. */}
      {groups.map(([groupLabel, rows]) => (
        <section
          key={groupLabel}
          className="mb-6 rounded-xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900"
        >
          <header className="border-b border-slate-100 px-5 py-3 dark:border-slate-800">
            <h2 className="text-sm font-semibold text-slate-700 dark:text-slate-200">
              {groupLabel}
            </h2>
          </header>
          <ul className="divide-y divide-slate-100 dark:divide-slate-800">
            {rows.map(({ sectionId, entry }) => (
              <li key={sectionId} className="px-5 py-3">
                <div className="flex flex-wrap items-center gap-3">
                  <VoteBadge vote={entry.vote} />
                  <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-medium text-slate-800 dark:text-slate-100">
                      <HumanLabel entry={entry} />
                    </p>
                    <p className="truncate text-xs text-slate-500 dark:text-slate-400">
                      <code className="font-mono text-[11px]">{sectionId}</code>
                    </p>
                  </div>
                  <span className="shrink-0 text-xs text-slate-400 dark:text-slate-500">
                    {formatTimestamp(entry.at)}
                  </span>
                </div>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </article>
  )
}

function Stat({
  label,
  value,
  tone = 'slate',
}: {
  label: string
  value: number
  tone?: 'slate' | 'emerald' | 'rose'
}) {
  const toneClass =
    tone === 'emerald'
      ? 'text-emerald-700 dark:text-emerald-300'
      : tone === 'rose'
        ? 'text-rose-700 dark:text-rose-300'
        : 'text-slate-900 dark:text-white'
  return (
    <div>
      <p className="text-xs font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400">
        {label}
      </p>
      <p className={`text-2xl font-bold tabular-nums ${toneClass}`}>{value}</p>
    </div>
  )
}

function VoteBadge({ vote }: { vote: 'up' | 'down' }) {
  const isUp = vote === 'up'
  return (
    <span
      className={`inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-full text-sm ${
        isUp
          ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/40 dark:text-emerald-200'
          : 'bg-rose-100 text-rose-700 dark:bg-rose-900/40 dark:text-rose-200'
      }`}
      aria-label={isUp ? 'Helpful' : 'Needs improvement'}
    >
      {isUp ? '👍' : '👎'}
    </span>
  )
}

/** Build a human label for an entry: lesson heading + section type. */
function HumanLabel({ entry }: { entry: FeedbackEntry }) {
  const topic = topicById(entry.topicId)
  const lesson = topic?.lessons.find((l) => l.id === entry.lessonId)
  const topicTitle = topic?.title ?? entry.topicId
  const lessonHeading = lesson?.heading ?? entry.lessonId
  const sectionLabel = SECTION_TYPE_LABEL[entry.sectionType]
  if (entry.sectionType === 'audio') {
    return (
      <>
        {topicTitle} · {lessonHeading} · <em>{sectionLabel}</em>
      </>
    )
  }
  return (
    <>
      {topicTitle} · {lessonHeading} · <em>{sectionLabel}</em> ({entry.sectionRef})
    </>
  )
}

function groupKey(entry: FeedbackEntry, by: GroupBy): string {
  if (by === 'topic') {
    const topic = topicById(entry.topicId)
    return topic?.title ?? entry.topicId
  }
  if (by === 'lesson') {
    const topic = topicById(entry.topicId)
    const lesson = topic?.lessons.find((l) => l.id === entry.lessonId)
    return `${topic?.title ?? entry.topicId} — ${lesson?.heading ?? entry.lessonId}`
  }
  return SECTION_TYPE_LABEL[entry.sectionType]
}

function formatTimestamp(ms: number): string {
  try {
    return new Date(ms).toLocaleString()
  } catch {
    return new Date(ms).toISOString()
  }
}
