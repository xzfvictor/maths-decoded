import { useEffect, useRef, useState } from 'react'

/**
 * "Explain to me" audio card. Plays a pre-generated spoken narration
 * of the lesson theory. The MP3 is generated offline by
 * `scripts/generate-audio.ts` and shipped in `public/audio/lessons/`.
 *
 * Three states the UI must handle gracefully:
 *   - MP3 missing (audio not yet generated): button is disabled with a hint.
 *   - MP3 present, transcript missing: player still works, no caption.
 *   - MP3 and transcript both present: player + collapsible transcript.
 */
export function LessonAudio({
  topicId,
  lessonId,
}: {
  topicId: string
  lessonId: string
}) {
  const audioRef = useRef<HTMLAudioElement | null>(null)
  const [status, setStatus] = useState<'checking' | 'missing' | 'ready'>('checking')
  const [playing, setPlaying] = useState(false)
  const [time, setTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const [transcript, setTranscript] = useState<string | null>(null)
  const [showTranscript, setShowTranscript] = useState(false)
  const [rate, setRate] = useState(1)

  // Probe whether the audio file exists. We use a HEAD-style trick: load
  // the metadata only and react to onError / onLoadedMetadata.
  useEffect(() => {
    setStatus('checking')
    setPlaying(false)
    setTime(0)
    setDuration(0)
    const a = new Audio()
    a.preload = 'metadata'
    const onMeta = () => {
      setDuration(Number.isFinite(a.duration) ? a.duration : 0)
      setStatus('ready')
    }
    const onErr = () => setStatus('missing')
    a.addEventListener('loadedmetadata', onMeta)
    a.addEventListener('error', onErr)
    a.src = audioUrl(topicId, lessonId)

    // Sidecar transcript (best-effort).
    fetch(transcriptUrl(topicId, lessonId), { cache: 'force-cache' })
      .then((r) => (r.ok ? r.text() : null))
      .then((t) => setTranscript(t))
      .catch(() => setTranscript(null))

    return () => {
      a.removeEventListener('loadedmetadata', onMeta)
      a.removeEventListener('error', onErr)
      a.src = ''
    }
  }, [topicId, lessonId])

  // Keep the visible time in sync while playing.
  useEffect(() => {
    const a = audioRef.current
    if (!a) return
    const onTime = () => setTime(a.currentTime)
    const onPlay = () => setPlaying(true)
    const onPause = () => setPlaying(false)
    const onEnd = () => setPlaying(false)
    a.addEventListener('timeupdate', onTime)
    a.addEventListener('play', onPlay)
    a.addEventListener('pause', onPause)
    a.addEventListener('ended', onEnd)
    return () => {
      a.removeEventListener('timeupdate', onTime)
      a.removeEventListener('play', onPlay)
      a.removeEventListener('pause', onPause)
      a.removeEventListener('ended', onEnd)
    }
  }, [status])

  // Apply the selected playback speed to the audio element. Runs when the
  // rate changes and once the player becomes ready (element mounts).
  useEffect(() => {
    const a = audioRef.current
    if (a) a.playbackRate = rate
  }, [rate, status])

  function togglePlay() {
    const a = audioRef.current
    if (!a) return
    if (a.paused) {
      void a.play().catch(() => setPlaying(false))
    } else {
      a.pause()
    }
  }

  function stop() {
    const a = audioRef.current
    if (!a) return
    a.pause()
    a.currentTime = 0
  }

  return (
    <section className="mb-8 rounded-xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900">
      <div className="flex items-start gap-3">
        <span
          aria-hidden="true"
          className="mt-1 inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-brand-100 text-base dark:bg-brand-900/40"
        >
          🔊
        </span>
        <div className="min-w-0 flex-1">
          <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-400">
            Explain to me
          </p>
          <p className="text-sm text-slate-600 dark:text-slate-300">
            A short spoken overview of this lesson — useful if you want to listen
            before reading.
          </p>
        </div>
      </div>

      {/* Player area — only when audio is ready. */}
      {status === 'ready' && (
        <div className="mt-4">
          <audio
            ref={audioRef}
            src={audioUrl(topicId, lessonId)}
            preload="metadata"
          />
          <div className="flex flex-wrap items-center gap-3">
            <button
              type="button"
              onClick={togglePlay}
              className={`inline-flex items-center gap-1 rounded-lg px-3 py-1.5 text-sm font-semibold transition ${
                playing
                  ? 'bg-amber-500 text-white hover:bg-amber-600'
                  : 'bg-brand-600 text-white hover:bg-brand-700'
              }`}
              aria-label={playing ? 'Pause' : 'Play'}
            >
              {playing ? <>❚❚ Pause</> : <>▶ Play</>}
            </button>
            <button
              type="button"
              onClick={stop}
              className="rounded-lg border border-slate-300 px-3 py-1.5 text-sm text-slate-600 hover:bg-slate-100 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800"
            >
              ◼ Stop
            </button>
            <div className="flex min-w-0 flex-1 items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
              <span className="tabular-nums">{fmt(time)}</span>
              <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
                <div
                  className="h-full bg-brand-500 transition-[width] duration-200"
                  style={{
                    width: duration > 0 ? `${Math.min(100, (time / duration) * 100)}%` : '0%',
                  }}
                  role="progressbar"
                  aria-valuemin={0}
                  aria-valuemax={duration || 0}
                  aria-valuenow={time}
                />
              </div>
              <span className="tabular-nums">{fmt(duration)}</span>
            </div>
          </div>

          {/* Playback speed control. */}
          <div className="mt-3 flex items-center gap-3">
            <label
              htmlFor={`speed-${topicId}-${lessonId}`}
              className="text-xs font-semibold text-slate-500 dark:text-slate-400"
            >
              Speed
            </label>
            <input
              id={`speed-${topicId}-${lessonId}`}
              type="range"
              min={1}
              max={2}
              step={0.1}
              value={rate}
              onChange={(e) => setRate(Number(e.target.value))}
              className="h-1.5 max-w-[10rem] flex-1 cursor-pointer accent-brand-600"
              aria-label="Playback speed"
              aria-valuetext={`${rate.toFixed(1)}x`}
            />
            <span className="w-10 shrink-0 text-xs font-semibold tabular-nums text-slate-600 dark:text-slate-300">
              {rate.toFixed(1)}x
            </span>
          </div>

          {transcript && (
            <div className="mt-3">
              <button
                type="button"
                onClick={() => setShowTranscript((s) => !s)}
                className="text-xs font-semibold text-brand-600 hover:underline dark:text-brand-300"
              >
                {showTranscript ? 'Hide transcript' : 'Show transcript'}
              </button>
              {showTranscript && (
                <p className="mt-2 rounded-lg bg-slate-50 p-3 text-sm leading-6 text-slate-700 dark:bg-slate-900/60 dark:text-slate-200">
                  {transcript}
                </p>
              )}
            </div>
          )}
        </div>
      )}

      {/* Audio not generated yet. */}
      {status === 'missing' && (
        <div className="mt-4 rounded-lg border border-dashed border-slate-300 bg-slate-50 p-3 text-xs text-slate-500 dark:border-slate-700 dark:bg-slate-900/60 dark:text-slate-400">
          Audio not generated yet. Run{' '}
          <code className="rounded bg-slate-200 px-1 py-0.5 font-mono text-[11px] dark:bg-slate-800">
            npm run generate:audio
          </code>{' '}
          to create it.
        </div>
      )}
    </section>
  )
}

function audioUrl(topicId: string, lessonId: string): string {
  return `audio/lessons/${topicId}/${lessonId}.mp3`
}
function transcriptUrl(topicId: string, lessonId: string): string {
  return `audio/lessons/${topicId}/${lessonId}.json`
}

function fmt(seconds: number): string {
  if (!Number.isFinite(seconds) || seconds < 0) return '0:00'
  const m = Math.floor(seconds / 60)
  const s = Math.floor(seconds % 60)
  return `${m}:${s.toString().padStart(2, '0')}`
}