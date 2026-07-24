import { useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { topicById } from '../content/topics'
import { DOT_POINTS } from '../content/coverage'
import { ProgressBar } from '../components/ProgressBar'
import { isLessonDone, topicLessonRatio } from '../lib/storage'
import { useProgress } from '../lib/useProgress'

export function TopicPage() {
  const { id } = useParams<{ id: string }>()
  useProgress()
  const topic = id ? topicById(id) : undefined

  // Scroll the right pane to the top whenever the topic changes.
  useEffect(() => {
    if (typeof window !== 'undefined') {
      window.scrollTo({ top: 0, left: 0, behavior: 'auto' })
    }
  }, [id])

  if (!topic) {
    return (
      <div className="mx-auto max-w-2xl text-center">
        <p className="text-slate-500">Topic not found.</p>
        <Link to="/" className="text-brand-600 hover:underline">
          Back to home
        </Link>
      </div>
    )
  }

  const ratio = topicLessonRatio(topic.id, topic.lessons.length)
  const dotPointDetails = topic.dotPoints
    .map((dpId) => DOT_POINTS.find((d) => d.id === dpId))
    .filter((d): d is NonNullable<typeof d> => Boolean(d))

  return (
    <div className="mx-auto max-w-3xl">
      <div className="mb-6">
        <Link to="/" className="text-sm text-brand-600 hover:underline">
          ← All topics
        </Link>
        <h1 className="mt-2 text-3xl font-bold text-slate-900 dark:text-white">{topic.title}</h1>
        <p className="mt-1 text-slate-600 dark:text-slate-300">{topic.blurb}</p>
        <div className="mt-4">
          <ProgressBar ratio={ratio} />
          <p className="mt-1 text-xs text-slate-400">
            {topic.lessons.filter((l) => isLessonDone(topic.id, l.id)).length} of{' '}
            {topic.lessons.length} lessons complete
          </p>
        </div>
      </div>

      <h2 className="mb-3 text-lg font-semibold text-slate-800 dark:text-slate-100">Lessons</h2>
      <ol className="space-y-3">
        {topic.lessons.map((lesson, i) => {
          const done = isLessonDone(topic.id, lesson.id)
          return (
            <li key={lesson.id}>
              <Link
                to={`/topic/${topic.id}/${lesson.id}`}
                className="group flex items-start gap-3 rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition hover:border-brand-400 hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
              >
                <span
                  className={`mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full border text-xs font-semibold ${
                    done
                      ? 'border-emerald-500 bg-emerald-500 text-white'
                      : 'border-slate-300 text-slate-400 dark:border-slate-600'
                  }`}
                >
                  {done ? '✓' : i + 1}
                </span>
                <span className="min-w-0 flex-1">
                  <span className="block font-semibold text-slate-900 group-hover:text-brand-700 dark:text-white">
                    {lesson.heading}
                  </span>
                  {lesson.summary && (
                    <span className="block text-sm text-slate-500 dark:text-slate-400">
                      {lesson.summary}
                    </span>
                  )}
                  <span className="mt-1 block text-xs text-slate-400">
                    {lesson.examples.length} example{lesson.examples.length === 1 ? '' : 's'} ·{' '}
                    {lesson.exercises.length} exercise
                    {lesson.exercises.length === 1 ? '' : 's'}
                  </span>
                </span>
              </Link>
            </li>
          )
        })}
      </ol>

      {/* Study-design coverage note. */}
      <section className="mt-8 rounded-xl border border-dashed border-slate-300 bg-slate-50 p-5 text-sm dark:border-slate-700 dark:bg-slate-900/50">
        <h2 className="mb-2 font-semibold text-slate-700 dark:text-slate-200">
          VCAA study-design coverage
        </h2>
        <ul className="list-disc space-y-1 pl-5 text-slate-500 dark:text-slate-400">
          {dotPointDetails.map((d) => (
            <li key={d.id}>
              <span className="font-medium text-slate-600 dark:text-slate-300">
                Unit {d.unit}, AoS {d.aos} ({d.aosName}):
              </span>{' '}
              {d.text}
            </li>
          ))}
        </ul>
      </section>
    </div>
  )
}
