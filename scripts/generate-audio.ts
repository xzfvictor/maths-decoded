/**
 * Generate AI "Explain to me" audio assets for every lesson.
 *
 * For each lesson, this script:
 *   1. Asks minimax M3 (via the Anthropic-compatible surface at
 *      $ANTHROPIC_BASE_URL) to write a 30–60s conversational script.
 *   2. Persists the script as JSON next to where the audio would live.
 *   3. Probes common TTS routes on the same host; if any returns
 *      audio, converts the script to MP3 and writes it alongside.
 *
 * The output is committed to the repo so the browser just plays the
 * resulting MP3 with no runtime AI or API keys.
 *
 * Usage:
 *   tsx scripts/generate-audio.ts                              # all lessons
 *   tsx scripts/generate-audio.ts --topic functions-relations  # one topic
 *   tsx scripts/generate-audio.ts --topic ... --lesson ...     # one lesson
 *   tsx scripts/generate-audio.ts --dry-script                 # scripts only, no TTS
 *   tsx scripts/generate-audio.ts --force                      # re-generate even if cached
 *
 * Required env:
 *   ANTHROPIC_BASE_URL   — Anthropic-compatible endpoint (defaults to https://api.minimaxi.com/anthropic)
 *   ANTHROPIC_AUTH_TOKEN — bearer token
 *
 * Optional env:
 *   ANTHROPIC_MODEL — model name (defaults to $ANTHROPIC_MODEL, then "MiniMax-M3")
 */

import { TOPICS } from '../src/content/topics'
import type { Topic, Lesson } from '../src/content/types'
import { callM3 } from './lib/m3'
import * as fs from 'node:fs/promises'
import * as path from 'node:path'

const ROOT = process.cwd()
const OUT_DIR = path.join(ROOT, 'public', 'audio', 'lessons')
const ENDPOINT_CACHE = path.join(ROOT, '.audio-tts-endpoint')

const BASE_URL = process.env.ANTHROPIC_BASE_URL ?? 'https://api.minimaxi.com/anthropic'
const AUTH_TOKEN = process.env.ANTHROPIC_AUTH_TOKEN ?? ''
const MODEL = process.env.ANTHROPIC_MODEL ?? 'MiniMax-M3'

// --- CLI flags ------------------------------------------------------------

const argv = process.argv.slice(2)
function flag(name: string): string | undefined {
  const i = argv.indexOf(`--${name}`)
  return i === -1 ? undefined : argv[i + 1]
}
function has(name: string): boolean {
  return argv.includes(`--${name}`)
}
const TOPIC_FILTER = flag('topic')
const LESSON_FILTER = flag('lesson')
const DRY_SCRIPT = has('dry-script')
const FORCE = has('force')

// --- Helpers --------------------------------------------------------------

function lessonOutPath(t: Topic, l: Lesson, ext: 'json' | 'mp3'): string {
  return path.join(OUT_DIR, t.id, `${l.id}.${ext}`)
}

async function readIfExists(p: string): Promise<string | null> {
  try {
    return await fs.readFile(p, 'utf8')
  } catch {
    return null
  }
}

/** Strip markdown/TeX to a short, plain-text form for the prompt to M3. */
function bodyForPrompt(body: string): string {
  return body
    .replace(/```[\s\S]*?```/g, '') // code blocks
    .replace(/\$\$[\s\S]*?\$\$/g, '') // block math
    .replace(/\$[^$]+\$/g, (m) => m.replace(/[$]/g, '').trim()) // inline math → keep as plain text
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/^#{1,6}\s+/gm, '')
    .replace(/^>\s?!?(definition|warning)?\s*/gim, '')
    .replace(/^[-*]\s+/gm, '')
    .replace(/^\d+\.\s+/gm, '')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 4000) // safety bound for the prompt
}

function buildPrompt(topic: Topic, lesson: Lesson): string {
  return [
    `You are a friendly tutor recording a 30–60 second audio explainer for a student who is about to start this VCE Mathematical Methods lesson.`,
    ``,
    `Module: ${topic.title}`,
    `Lesson heading: ${lesson.heading}`,
    lesson.summary ? `One-line summary: ${lesson.summary}` : '',
    ``,
    `Lesson theory (markdown with TeX stripped for you):`,
    bodyForPrompt(lesson.body),
    ``,
    `Write the SPOKEN SCRIPT the tutor will say aloud. Constraints:`,
    `- Aim for 130–170 words (reads in roughly 30–60 seconds at a calm pace).`,
    `- Conversational, friendly, second-person ("you"). Imagine explaining to a classmate who has never seen the topic before.`,
    `- Open with one short sentence that frames the lesson ("In this lesson we'll look at...").`,
    `- Walk through the main ideas in order. If the theory has ### headings, cover each one briefly.`,
    `- Skip equations and code notation entirely — describe them in words ("the square of x plus three").`,
    `- End with a single sentence that primes them for the worked example or exercise ("Now let's see it in action").`,
    `- Output ONLY the spoken script, no preamble, no headings, no stage directions.`,
  ]
    .filter(Boolean)
    .join('\n')
}

// --- TTS probe ------------------------------------------------------------

interface TTSEndpoint {
  url: string
  /** Acceptable audio content-type prefixes (lowercased). */
  accepts: string[]
  /** Body shape to send. */
  buildBody: (text: string) => unknown
  /** Decode the raw response (or JSON wrapper) into a binary audio buffer. */
  decode: (res: Response) => Promise<Buffer>
}

/**
 * Build the T2A v2 (synchronous TTS) request body used by minimax's
 * `/v1/t2a_v2` route. Returns hex-encoded MP3 inside `data.audio`,
 * decoded by `decodeHexAudio`.
 */
function t2aV2Body(text: string) {
  return {
    model: 'speech-2.6-turbo',
    text,
    stream: false,
    voice_setting: {
      voice_id: 'English_Graceful_Lady',
      speed: 1,
      vol: 1,
      pitch: 0,
    },
    audio_setting: {
      sample_rate: 32000,
      bitrate: 128000,
      format: 'mp3',
      channel: 1,
    },
    output_format: 'hex',
  }
}

async function decodeHexAudio(res: Response): Promise<Buffer> {
  const j = (await res.json()) as {
    data?: { audio?: string }
    base_resp?: { status_code?: number; status_msg?: string }
  }
  if (j.base_resp && j.base_resp.status_code && j.base_resp.status_code !== 0) {
    throw new Error(`TTS base_resp ${j.base_resp.status_code}: ${j.base_resp.status_msg ?? 'unknown'}`)
  }
  const hex = j.data?.audio
  if (!hex) throw new Error('TTS response missing data.audio')
  return Buffer.from(hex, 'hex')
}

/** OpenAI-compatible `/v1/audio/speech` body — fallback for other providers. */
function openAITTSBody(text: string) {
  return { model: 'speech-1', input: text, voice: 'alloy' }
}

async function decodeRawAudio(res: Response): Promise<Buffer> {
  const ab = await res.arrayBuffer()
  return Buffer.from(ab)
}

function candidateEndpoints(): TTSEndpoint[] {
  const root = new URL(BASE_URL).origin
  return [
    // minimax T2A v2 — JSON response with hex-encoded MP3 in data.audio.
    {
      url: `${root}/v1/t2a_v2`,
      accepts: ['application/json'],
      buildBody: t2aV2Body,
      decode: decodeHexAudio,
    },
    // OpenAI-compatible /v1/audio/speech — raw audio body.
    {
      url: `${root}/v1/audio/speech`,
      accepts: ['audio/mpeg', 'audio/mp3', 'audio/wav', 'audio/x-wav', 'audio/octet-stream'],
      buildBody: openAITTSBody,
      decode: decodeRawAudio,
    },
    // Other plausible TTS paths.
    ...['/v1/tts', '/v1/text_to_speech', '/api/v1/audio/speech'].map((p) => ({
      url: `${root}${p}`,
      accepts: ['audio/mpeg', 'audio/mp3', 'audio/wav', 'audio/x-wav', 'audio/octet-stream'],
      buildBody: openAITTSBody,
      decode: decodeRawAudio,
    })),
  ]
}

async function probeTTS(): Promise<TTSEndpoint | null> {
  const cached = await readIfExists(ENDPOINT_CACHE)
  if (cached && !FORCE) {
    try {
      const ep = JSON.parse(cached) as TTSEndpoint
      // sanity-check the cached endpoint still answers.
      const res = await fetch(ep.url, {
        method: 'POST',
        headers: {
          authorization: `Bearer ${AUTH_TOKEN}`,
          'content-type': 'application/json',
        },
        body: JSON.stringify(ep.buildBody('ping')),
      })
      if (res.ok) {
        try {
          await ep.decode(res.clone())
          return ep
        } catch {
          /* cached endpoint no longer decodes correctly — re-probe */
        }
      }
    } catch {
      /* fall through and re-probe */
    }
  }
  const testText = 'Audio generation ready.'
  for (const ep of candidateEndpoints()) {
    try {
      const res = await fetch(ep.url, {
        method: 'POST',
        headers: {
          authorization: `Bearer ${AUTH_TOKEN}`,
          'content-type': 'application/json',
        },
        body: JSON.stringify(ep.buildBody(testText)),
      })
      if (!res.ok) continue
      const ct = (res.headers.get('content-type') ?? '').toLowerCase()
      if (!ep.accepts.some((p) => ct.startsWith(p))) continue
      try {
        await ep.decode(res.clone())
      } catch {
        continue
      }
      await fs.writeFile(ENDPOINT_CACHE, JSON.stringify(ep, null, 2))
      return ep
    } catch {
      /* try next */
    }
  }
  return null
}

async function callTTS(ep: TTSEndpoint, text: string): Promise<Buffer> {
  const res = await fetch(ep.url, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${AUTH_TOKEN}`,
      'content-type': 'application/json',
    },
    body: JSON.stringify(ep.buildBody(text)),
  })
  if (!res.ok) throw new Error(`TTS ${res.status}: ${(await res.text()).slice(0, 200)}`)
  return ep.decode(res)
}

// --- Main loop ------------------------------------------------------------

async function processLesson(t: Topic, l: Lesson, tts: TTSEndpoint | null): Promise<'generated' | 'cached' | 'script-only'> {
  const jsonPath = lessonOutPath(t, l, 'json')
  const mp3Path = lessonOutPath(t, l, 'mp3')

  await fs.mkdir(path.dirname(jsonPath), { recursive: true })

  const existingScript = await readIfExists(jsonPath)
  let script = existingScript

  if (!script || FORCE) {
    process.stdout.write(`  · M3 → ${t.id}/${l.id} … `)
    const result = await callM3(buildPrompt(t, l), {
      baseUrl: BASE_URL,
      authToken: AUTH_TOKEN,
      model: MODEL,
      maxTokens: 600,
    })
    if (result.kind !== 'text') {
      throw new Error('M3 returned unexpected tool output for audio script')
    }
    script = result.text
    await fs.writeFile(jsonPath, script, 'utf8')
    process.stdout.write(`script saved (${script.length} chars) `)
  } else {
    process.stdout.write(`  · cached script (${script.length} chars) `)
  }

  if (DRY_SCRIPT) {
    process.stdout.write('\n')
    return 'script-only'
  }

  if (!tts) {
    process.stdout.write(`(no TTS endpoint — audio skipped)\n`)
    return 'script-only'
  }

  if ((await readIfExists(mp3Path)) && !FORCE) {
    process.stdout.write(`(mp3 cached)\n`)
    return 'cached'
  }

  process.stdout.write(`→ TTS … `)
  const buf = await callTTS(tts, script)
  await fs.writeFile(mp3Path, buf)
  process.stdout.write(`mp3 saved (${buf.length} bytes)\n`)
  return 'generated'
}

async function main() {
  console.log(`generate-audio`)
  console.log(`  base:  ${BASE_URL}`)
  console.log(`  model: ${MODEL}`)
  console.log(`  out:   ${path.relative(ROOT, OUT_DIR)}/`)
  console.log(`  flags: ${JSON.stringify({ TOPIC_FILTER, LESSON_FILTER, DRY_SCRIPT, FORCE })}`)

  if (!AUTH_TOKEN) {
    console.error('ANTHROPIC_AUTH_TOKEN is not set; aborting.')
    process.exit(2)
  }

  const tts = await probeTTS()
  if (tts) {
    console.log(`  tts:   ${tts.url}`)
  } else {
    console.log(`  tts:   none reachable — will generate scripts only`)
  }

  let total = 0
  let generated = 0
  let cached = 0
  let scriptOnly = 0

  for (const t of TOPICS) {
    if (TOPIC_FILTER && t.id !== TOPIC_FILTER) continue
    console.log(`\n[${t.id}] ${t.title}`)
    for (const l of t.lessons) {
      if (LESSON_FILTER && l.id !== LESSON_FILTER) continue
      total++
      try {
        const result = await processLesson(t, l, tts)
        if (result === 'generated') generated++
        else if (result === 'cached') cached++
        else scriptOnly++
      } catch (err) {
        console.error(`  ! ${l.id} failed: ${(err as Error).message}`)
      }
    }
  }

  console.log(`\ndone. ${total} lesson(s): ${generated} generated, ${cached} cached, ${scriptOnly} script-only.`)
}

main().catch((err) => {
  console.error(err)
  process.exit(1)
})