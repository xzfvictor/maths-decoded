// Lesson-section feedback (👍 / 👎) storage. One localStorage key
// (`vce-mm-feedback-v1`) holds the whole store. All access goes through
// here so the shape stays consistent and the React layer can subscribe
// via a CustomEvent — same pattern as `src/lib/storage.ts`.

import { useEffect, useState } from 'react'

const KEY = 'vce-mm-feedback-v1'
const WRITE_EVENT = 'vce-feedback-write'

export type Vote = 'up' | 'down'
export type SectionType = 'audio' | 'example' | 'exercise'

export interface FeedbackEntry {
  vote: Vote
  /** Epoch ms of the most recent vote. */
  at: number
  topicId: string
  lessonId: string
  sectionType: SectionType
  /** The exerciseId / exampleId / 'audio' for the section. */
  sectionRef: string
}

export interface FeedbackStore {
  /** Keyed by sectionId. Re-voting overwrites; clicking the active
   *  thumb removes the entry. */
  votes: Record<string, FeedbackEntry>
}

function read(): FeedbackStore {
  if (typeof localStorage === 'undefined') return { votes: {} }
  try {
    const raw = localStorage.getItem(KEY)
    if (!raw) return { votes: {} }
    const parsed = JSON.parse(raw) as Partial<FeedbackStore>
    if (!parsed || typeof parsed !== 'object' || !parsed.votes) return { votes: {} }
    return { votes: parsed.votes }
  } catch {
    return { votes: {} }
  }
}

function write(s: FeedbackStore) {
  if (typeof localStorage === 'undefined') return
  try {
    localStorage.setItem(KEY, JSON.stringify(s))
    // Same-tab subscribers (FeedbackButtons, FeedbackPage) listen for
    // this event so they re-render without polling.
    window.dispatchEvent(new Event(WRITE_EVENT))
  } catch {
    /* quota or privacy mode — feedback simply won't persist */
  }
}

export function getAllFeedback(): FeedbackStore {
  return read()
}

export function getVote(sectionId: string): FeedbackEntry | undefined {
  return read().votes[sectionId]
}

export function setVote(
  sectionId: string,
  vote: Vote,
  meta: { topicId: string; lessonId: string; sectionType: SectionType; sectionRef: string },
) {
  const s = read()
  s.votes[sectionId] = {
    vote,
    at: Date.now(),
    topicId: meta.topicId,
    lessonId: meta.lessonId,
    sectionType: meta.sectionType,
    sectionRef: meta.sectionRef,
  }
  write(s)
}

export function clearVote(sectionId: string) {
  const s = read()
  if (sectionId in s.votes) {
    delete s.votes[sectionId]
    write(s)
  }
}

export function resetFeedback() {
  write({ votes: {} })
}

/** Returns the current vote (if any) for `sectionId`. Re-renders when
 *  any feedback mutation fires the write event. */
export function useFeedback(sectionId: string): FeedbackEntry | undefined {
  const [vote, setLocalVote] = useState<FeedbackEntry | undefined>(() => getVote(sectionId))
  useEffect(() => {
    function refresh() {
      setLocalVote(getVote(sectionId))
    }
    refresh()
    window.addEventListener(WRITE_EVENT, refresh)
    // The localStorage 'storage' event only fires cross-tab, but we
    // still listen for it in case the user opens two tabs of the app
    // and votes in one — the other tab should reflect that.
    window.addEventListener('storage', refresh)
    return () => {
      window.removeEventListener(WRITE_EVENT, refresh)
      window.removeEventListener('storage', refresh)
    }
  }, [sectionId])
  return vote
}

// ---------------------------------------------------------------------------
// Section-id helpers. One source of truth so every callsite agrees on the
// format. Section ids are stable, content-derived strings — they don't
// include timestamps or random values, so the same lesson always maps
// to the same id and a vote survives page reloads.
// ---------------------------------------------------------------------------

export function audioSectionId(topicId: string, lessonId: string): string {
  return `audio:${topicId}/${lessonId}`
}

export function exampleSectionId(
  topicId: string,
  lessonId: string,
  exampleId: string,
): string {
  return `example:${topicId}/${lessonId}/${exampleId}`
}

export function exerciseSectionId(
  topicId: string,
  lessonId: string,
  exerciseRef: string,
): string {
  return `exercise:${topicId}/${lessonId}/${exerciseRef}`
}
