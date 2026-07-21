// Local-only progress tracking via localStorage. One namespaced key holds the whole
// progress object. All access goes through here so the shape stays consistent.

const KEY = 'vce-mm-progress-v1'

export interface Progress {
  /** topicId -> set of completed lesson ids. */
  lessons: Record<string, string[]>
  /** topicId -> { attempted, correct } across its exercises. */
  exercises: Record<string, { attempted: number; correct: number }>
}

const empty: Progress = { lessons: {}, exercises: {} }

function read(): Progress {
  if (typeof localStorage === 'undefined') return structuredClone(empty)
  try {
    const raw = localStorage.getItem(KEY)
    if (!raw) return structuredClone(empty)
    const parsed = JSON.parse(raw) as Partial<Progress> & { sections?: Record<string, string[]> }
    return {
      // Accept the older `sections` key so existing progress isn't lost.
      lessons: parsed.lessons ?? parsed.sections ?? {},
      exercises: parsed.exercises ?? {},
    }
  } catch {
    return structuredClone(empty)
  }
}

function write(p: Progress) {
  if (typeof localStorage === 'undefined') return
  try {
    localStorage.setItem(KEY, JSON.stringify(p))
    // Notify listeners in the same tab (storage event only fires cross-tab).
    window.dispatchEvent(new Event('vce-progress'))
  } catch {
    /* quota or privacy mode — progress simply won't persist */
  }
}

export function getProgress(): Progress {
  return read()
}

export function isLessonDone(topicId: string, lessonId: string): boolean {
  return read().lessons[topicId]?.includes(lessonId) ?? false
}

export function setLessonDone(topicId: string, lessonId: string, done: boolean) {
  const p = read()
  const cur = new Set(p.lessons[topicId] ?? [])
  if (done) cur.add(lessonId)
  else cur.delete(lessonId)
  p.lessons[topicId] = [...cur]
  write(p)
}

export function recordExercise(topicId: string, correct: boolean) {
  const p = read()
  const cur = p.exercises[topicId] ?? { attempted: 0, correct: 0 }
  cur.attempted += 1
  if (correct) cur.correct += 1
  p.exercises[topicId] = cur
  write(p)
}

/** Fraction (0..1) of a topic's lessons that are complete. */
export function topicLessonRatio(topicId: string, totalLessons: number): number {
  if (totalLessons === 0) return 0
  const done = read().lessons[topicId]?.length ?? 0
  return Math.min(done, totalLessons) / totalLessons
}

export function resetProgress() {
  if (typeof localStorage === 'undefined') return
  localStorage.removeItem(KEY)
  window.dispatchEvent(new Event('vce-progress'))
}
