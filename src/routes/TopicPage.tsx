import { useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { topicById, topicsForUnit, moduleForUnit, UNIT_TITLES } from '../content/topics'
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

  // The "back" link goes to the student's current module home, not the
  // landing page — they came in via a module, that's where they're working.
  const moduleId = topic ? moduleForUnit(topic.unit) : undefined
  const moduleHomeHref = moduleId ? `/${moduleId}` : '/'

  if (!topic) {
    return (
      <div className="mx-auto max-w-2xl text-center">
        <p className="text-slate-500">Topic not found.</p>
        <Link to="/" className="text-brand-600 hover:underline">
          Back to modules
        </Link>
      </div>
    )
  }

  const ratio = topicLessonRatio(topic.id, topic.lessons.length)
  const dotPointDetails = topic.dotPoints
    .map((dpId) => DOT_POINTS.find((d) => d.id === dpId))
    .filter((d): d is NonNullable<typeof d> => Boolean(d))

  // Surface the topics that come immediately before and after this one in
  // the same unit, plus the first topic in the unit. These are the natural
  // "what should I do next?" suggestions for a beginner working through
  // the syllabus in order.
  const unitTopics = topicsForUnit(topic.unit)
  const idx = unitTopics.findIndex((t) => t.id === topic.id)
  const prevTopic = idx > 0 ? unitTopics[idx - 1] : undefined
  const nextTopic = idx >= 0 && idx < unitTopics.length - 1 ? unitTopics[idx + 1] : undefined
  const firstTopic = unitTopics[0]

  // Human label for the current module, used in the "back" link and the
  // first-topic callout.
  const moduleLabel =
    topic.unit === 10 ? 'Pre-VCE' : topic.unit === 1 ? 'Unit 1' : 'Unit 2'

  return (
    <div className="mx-auto max-w-3xl">
      <div className="mb-6">
        <Link to={moduleHomeHref} className="text-sm text-brand-600 hover:underline">
          ← Back to {moduleLabel} topics
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

        {/* "Before you start" callout — points back at the immediately
            previous topic in the unit so a newcomer knows the assumed
            background. Hidden on the very first topic in a unit. */}
        {prevTopic && idx > 0 && (
          <div className="learner-tip mt-5">
            <span className="font-semibold text-slate-800 dark:text-slate-100">
              Before you start:
            </span>{' '}
            This topic builds on{' '}
            <Link
              to={`/topic/${prevTopic.id}`}
              className="font-medium text-brand-700 underline hover:no-underline dark:text-brand-300"
            >
              Topic {prevTopic.order} — {prevTopic.title}
            </Link>
            . If anything there feels shaky, refresh it first; the exercises
            here assume that earlier material is solid.
          </div>
        )}
        {idx === 0 && topic.unit !== 10 && firstTopic && (
          <div className="learner-tip mt-5">
            <span className="font-semibold text-slate-800 dark:text-slate-100">
              No prior VCE Maths Methods assumed:
            </span>{' '}
            this is the first topic of {UNIT_TITLES[topic.unit]}. If Year 10
            foundations feel shaky, the{' '}
            <Link
              to="/pre-vce"
              className="font-medium text-brand-700 underline hover:no-underline dark:text-brand-300"
            >
              Pre-VCE module
            </Link>{' '}
            has quick refreshers.
          </div>
        )}
      </div>

      <h2 className="mb-3 text-lg font-semibold text-slate-800 dark:text-slate-100">Lessons</h2>
      <p className="mb-3 -mt-2 text-sm text-slate-500 dark:text-slate-400">
        Work through these in order — each lesson assumes you've done the ones
        before it.
      </p>
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

      {/* Up next — the next topic in the same unit, so beginners always
          have an obvious "what's after this?" answer without scrolling the
          sidebar. */}
      {nextTopic && (
        <section className="mt-8 rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
          <p className="text-xs font-semibold uppercase tracking-wide text-slate-400">
            Up next
          </p>
          <Link
            to={`/topic/${nextTopic.id}`}
            className="mt-1 block text-lg font-semibold text-slate-900 hover:text-brand-700 dark:text-white"
          >
            Topic {nextTopic.order} — {nextTopic.title} →
          </Link>
          <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{nextTopic.blurb}</p>
        </section>
      )}

      {/* Study-design coverage note. */}
      <section className="mt-8 rounded-xl border border-dashed border-slate-300 bg-slate-50 p-5 text-sm dark:border-slate-700 dark:bg-slate-900/50">
        <h2 className="mb-2 font-semibold text-slate-700 dark:text-slate-200">
          Study-design coverage
        </h2>
        <p className="mb-2 text-xs text-slate-500 dark:text-slate-400">
          This topic addresses the following syllabus points. You don't need to
          memorise the codes — they're shown so a teacher or tutor can verify
          coverage.
        </p>
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
