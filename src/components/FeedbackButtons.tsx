// Inline thumb-up / thumb-down pair rendered in the corner of every
// lesson section card. Click semantics: clicking the active thumb
// clears the vote (toggle off). A "Thanks!" label appears briefly after
// a fresh vote, then fades so the buttons return to their resting state.

import { useEffect, useRef, useState } from 'react'
import {
  clearVote,
  setVote,
  useFeedback,
  type SectionType,
  type Vote,
} from '../lib/feedback'

interface Props {
  /** Stable id built by audioSectionId / exampleSectionId / exerciseSectionId. */
  sectionId: string
  topicId: string
  lessonId: string
  sectionType: SectionType
  /** exerciseId / exampleId / 'audio'. */
  sectionRef: string
  /** Compact mode hides the "Helpful?" caption — used inside dense
   *  exercise cards where the buttons sit beside other controls. */
  compact?: boolean
}

const THANKS_MS = 1400

export function FeedbackButtons({
  sectionId,
  topicId,
  lessonId,
  sectionType,
  sectionRef,
  compact = false,
}: Props) {
  const entry = useFeedback(sectionId)
  const [thanks, setThanks] = useState<Vote | null>(null)
  const thanksTimer = useRef<ReturnType<typeof setTimeout> | null>(null)

  useEffect(() => {
    return () => {
      if (thanksTimer.current) clearTimeout(thanksTimer.current)
    }
  }, [])

  function showThanks(v: Vote) {
    setThanks(v)
    if (thanksTimer.current) clearTimeout(thanksTimer.current)
    thanksTimer.current = setTimeout(() => setThanks(null), THANKS_MS)
  }

  function onVote(v: Vote) {
    if (entry?.vote === v) {
      // Toggle off — clicking the already-active thumb clears the vote.
      clearVote(sectionId)
    } else {
      setVote(sectionId, v, { topicId, lessonId, sectionType, sectionRef })
      showThanks(v)
    }
  }

  const upActive = entry?.vote === 'up'
  const downActive = entry?.vote === 'down'

  return (
    <div
      className={`flex items-center gap-1 ${compact ? '' : 'rounded-lg border border-slate-200 bg-slate-50 px-2 py-1 dark:border-slate-800 dark:bg-slate-900/60'}`}
      role="group"
      aria-label={compact ? 'Feedback' : 'Was this section helpful?'}
    >
      {!compact && (
        <span className="mr-1 text-[11px] font-semibold uppercase tracking-wide text-slate-400">
          {thanks === 'up' ? 'Thanks!' : thanks === 'down' ? 'Noted — thanks!' : 'Helpful?'}
        </span>
      )}
      <button
        type="button"
        onClick={() => onVote('up')}
        aria-pressed={upActive}
        aria-label="Helpful"
        title="This section was helpful"
        className={`inline-flex h-7 w-7 items-center justify-center rounded-md text-sm transition ${
          upActive
            ? 'bg-emerald-100 text-emerald-700 ring-1 ring-emerald-300 dark:bg-emerald-900/50 dark:text-emerald-200 dark:ring-emerald-700/60'
            : 'text-slate-500 hover:bg-slate-100 hover:text-slate-700 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-slate-200'
        }`}
      >
        <span aria-hidden="true">👍</span>
      </button>
      <button
        type="button"
        onClick={() => onVote('down')}
        aria-pressed={downActive}
        aria-label="Needs improvement"
        title="This section needs improvement"
        className={`inline-flex h-7 w-7 items-center justify-center rounded-md text-sm transition ${
          downActive
            ? 'bg-rose-100 text-rose-700 ring-1 ring-rose-300 dark:bg-rose-900/50 dark:text-rose-200 dark:ring-rose-700/60'
            : 'text-slate-500 hover:bg-slate-100 hover:text-slate-700 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-slate-200'
        }`}
      >
        <span aria-hidden="true">👎</span>
      </button>
    </div>
  )
}
