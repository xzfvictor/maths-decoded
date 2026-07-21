import { useParams, Link } from 'react-router-dom'
import { topicById } from '../content/topics'
import { Prose } from '../components/Prose'
import { ExerciseCard } from '../components/ExerciseCard'
import { isLessonDone, setLessonDone } from '../lib/storage'
import { useProgress } from '../lib/useProgress'

export function LessonPage() {
  const { id, lessonId } = useParams<{ id: string; lessonId: string }>()
  useProgress()
  const topic = id ? topicById(id) : undefined
  const lessonIdx = topic ? topic.lessons.findIndex((l) => l.id === lessonId) : -1
  const lesson = topic && lessonIdx >= 0 ? topic.lessons[lessonIdx] : undefined

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
      </div>

      {/* Theory. */}
      <section className="mb-8 rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
        <Prose text={lesson.body} />
      </section>

      {/* Worked examples. */}
      {lesson.examples.length > 0 && (
        <section className="mb-8">
          <h2 className="mb-4 text-2xl font-bold text-slate-900 dark:text-white">Worked examples</h2>
          <div className="space-y-4">
            {lesson.examples.map((ex) => (
              <details
                key={ex.id}
                className="group rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900"
              >
                <summary className="cursor-pointer list-none">
                  <span className="font-medium text-slate-800 dark:text-slate-100">
                    <Prose text={ex.statement} className="inline" />
                  </span>
                  <span className="ml-2 text-xs text-brand-500 group-open:hidden">
                    Show solution ▾
                  </span>
                </summary>
                <ol className="mt-4 list-decimal space-y-2 border-t border-slate-100 pl-5 pt-4 text-sm dark:border-slate-800">
                  {ex.steps.map((step, i) => (
                    <li key={i}>
                      <Prose text={step} className="inline" />
                    </li>
                  ))}
                </ol>
              </details>
            ))}
          </div>
        </section>
      )}

      {/* Exercises. */}
      {lesson.exercises.length > 0 && (
        <section className="mb-8">
          <h2 className="mb-4 text-2xl font-bold text-slate-900 dark:text-white">Exercises</h2>
          <div className="space-y-4">
            {lesson.exercises.map((ex) => (
              <ExerciseCard key={ex.id} topicId={topic.id} exercise={ex} />
            ))}
          </div>
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
