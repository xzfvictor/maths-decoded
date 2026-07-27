import { useEffect, useMemo } from 'react'
import { useParams, Link } from 'react-router-dom'
import { topicById } from '../content/topics'
import { Prose } from '../components/Prose'
import { PracticeLadder } from '../components/PracticeLadder'
import { WorkedExample } from '../components/WorkedExample'
import { LessonAudio } from '../components/LessonAudio'
import { isLessonDone, setLessonDone } from '../lib/storage'
import { useProgress } from '../lib/useProgress'

export function LessonPage() {
  const { id, lessonId } = useParams<{ id: string; lessonId: string }>()
  useProgress()
  const topic = id ? topicById(id) : undefined
  const lessonIdx = topic ? topic.lessons.findIndex((l) => l.id === lessonId) : -1
  const lesson = topic && lessonIdx >= 0 ? topic.lessons[lessonIdx] : undefined

  // Scroll the right pane to the top whenever the topic or lesson changes.
  useEffect(() => {
    if (typeof window !== 'undefined') {
      window.scrollTo({ top: 0, left: 0, behavior: 'auto' })
    }
  }, [id, lessonId])

  // Extract `### heading` lines from the theory body so we can build an in-page
  // outline AND a "Key takeaways" recap. We only render ### headings that
  // exist in the authored theory — no fabricated summaries.
  const sectionHeadings = useMemo(() => {
    if (!lesson) return []
    return lesson.body
      .split('\n')
      .filter((line) => line.trim().startsWith('### '))
      .map((line) => line.trim().slice(4).trim())
  }, [lesson])

  if (!topic || !lesson) {
    return (
      <div className="mx-auto max-w-2xl text-center">
        <p className="text-slate-500">Lesson not found.</p>
        <Link to="/" className="text-brand-600 hover:underline">
          Back to home
        </Link>
      </div>
    )
  }

  const prev = lessonIdx > 0 ? topic.lessons[lessonIdx - 1] : undefined
  const next = lessonIdx < topic.lessons.length - 1 ? topic.lessons[lessonIdx + 1] : undefined
  const done = isLessonDone(topic.id, lesson.id)

  return (
    <article className="mx-auto max-w-3xl">
      <div className="mb-6">
        <Link to={`/topic/${topic.id}`} className="text-sm text-brand-600 hover:underline">
          ← {topic.title}
        </Link>
        <p className="mt-2 text-xs font-semibold uppercase tracking-wide text-brand-500">
          Lesson {lessonIdx + 1} of {topic.lessons.length}
        </p>
        <h1 className="mt-1 text-3xl font-bold text-slate-900 dark:text-white">{lesson.heading}</h1>

        {/* "What you'll learn" — derived from the lesson summary (and the
            auto-generated outline if no summary was provided). Showing this
            upfront gives a newcomer an at-a-glance picture of where the lesson
            is going before they commit to reading the theory. */}
        {(lesson.summary || sectionHeadings.length > 0) && (
          <div className="mt-4 rounded-xl border border-slate-200 bg-slate-50 p-4 dark:border-slate-800 dark:bg-slate-900/60">
            <p className="text-xs font-semibold uppercase tracking-wide text-brand-600 dark:text-brand-300">
              What you'll learn
            </p>
            {lesson.summary && (
              <p className="mt-1 text-sm text-slate-700 dark:text-slate-200">{lesson.summary}</p>
            )}
            {sectionHeadings.length > 0 && (
              <ul className="mt-2 list-disc space-y-0.5 pl-5 text-sm text-slate-600 dark:text-slate-300">
                {sectionHeadings.map((h) => (
                  <li key={h}>{h}</li>
                ))}
              </ul>
            )}
          </div>
        )}
      </div>

      {/* AI explainer audio — sits between the lesson summary and the theory
          card so a student can choose to listen first, read along, or skip. */}
      <LessonAudio topicId={topic.id} lessonId={lesson.id} />

      {/* Theory. */}
      <section className="mb-8 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
        <Prose text={lesson.body} />
      </section>

      {/* Worked examples. */}
      {lesson.examples.length > 0 && (
        <section className="mb-8">
          <h2 className="mb-4 text-2xl font-bold text-slate-900 dark:text-white">Worked examples</h2>
          <p className="mb-3 -mt-2 text-sm text-slate-500 dark:text-slate-400">
            Each example reveals one step at a time. Try to predict the next line before
            you click <span className="font-semibold">Next step</span>.
          </p>
          <div className="space-y-4">
            {lesson.examples.map((ex) => (
              <WorkedExample key={ex.id} example={ex} />
            ))}
          </div>
        </section>
      )}

      {/* Exercises + the AI Generated Questions panel. The panel renders the
          existing exercises (just the intro by default) plus a section
          with two buttons that generate fresh questions as the student
          climbs the difficulty ladder. */}
      {lesson.exercises.length > 0 && (
        <section className="mb-8">
          <h2 className="mb-4 text-2xl font-bold text-slate-900 dark:text-white">
            Exercises
          </h2>
          <p className="mb-2 text-sm text-slate-500 dark:text-slate-400">
            Have a go on paper first — it's the difference between "I can follow a worked
            solution" and "I can solve it myself". Use the hint if you're stuck, and
            reveal the worked solution only after you've genuinely tried.
          </p>
          <p className="mb-4 text-xs text-slate-500 dark:text-slate-400">
            Each lesson opens with one{' '}
            <span className="font-semibold text-emerald-700 dark:text-emerald-300">Intro</span>{' '}
            question. Solve it, then click{' '}
            <span className="font-semibold text-amber-700 dark:text-amber-300">Harder</span>{' '}
            below to generate a Core variant, then a Challenge. The Harder button greys
            out until the current level is solved; the ladder caps at Challenge with a
            celebration message.
          </p>
          <PracticeLadder
            key={`${topic.id}/${lesson.id}`}
            topicId={topic.id}
            lessonId={lesson.id}
            exercises={lesson.exercises}
          />
        </section>
      )}

      {/* Key takeaways — auto-derived from the ### headings in the theory.
          Acts as a final summary card so the student walks away with the
          main points, not just the experience of having scrolled past them. */}
      {sectionHeadings.length > 0 && (
        <section className="mb-8 rounded-xl border border-emerald-300 bg-emerald-50 p-5 dark:border-emerald-700/60 dark:bg-emerald-950/30">
          <p className="text-xs font-semibold uppercase tracking-wide text-emerald-700 dark:text-emerald-300">
            Key takeaways
          </p>
          <p className="mt-1 text-sm text-emerald-900/80 dark:text-emerald-100/80">
            You should be able to explain each of these in your own words before
            moving on:
          </p>
          <ul className="mt-2 list-disc space-y-0.5 pl-5 text-sm text-emerald-900 dark:text-emerald-100">
            {sectionHeadings.map((h) => (
              <li key={h}>{h}</li>
            ))}
          </ul>
        </section>
      )}

      {/* Mark complete. */}
      <div className="mb-8 flex justify-center">
        <button
          onClick={() => setLessonDone(topic.id, lesson.id, !done)}
          className={`rounded-lg px-5 py-2.5 text-sm font-semibold transition ${
            done
              ? 'bg-emerald-100 text-emerald-800 hover:bg-emerald-200 dark:bg-emerald-900/40 dark:text-emerald-200'
              : 'bg-brand-600 text-white hover:bg-brand-700'
          }`}
        >
          {done ? '✓ Lesson complete — click to unmark' : 'Mark lesson complete'}
        </button>
      </div>

      {/* Prev / next lesson navigation. */}
      <nav className="flex items-center justify-between border-t border-slate-200 pt-4 dark:border-slate-800">
        {prev ? (
          <Link
            to={`/topic/${topic.id}/${prev.id}`}
            className="text-sm text-brand-600 hover:underline"
          >
            ← {prev.heading}
          </Link>
        ) : (
          <span />
        )}
        {next ? (
          <Link
            to={`/topic/${topic.id}/${next.id}`}
            className="text-right text-sm text-brand-600 hover:underline"
          >
            {next.heading} →
          </Link>
        ) : (
          <Link to={`/topic/${topic.id}`} className="text-sm text-brand-600 hover:underline">
            Back to topic overview →
          </Link>
        )}
      </nav>
    </article>
  )
}
