# CLAUDE.md

Guidance for working in this repository.

## What this is

A static web app that helps a student study **all of VCE Mathematical Methods
Units 1 & 2**, covering every VCAA study-design dot point, plus the
**Victorian Curriculum Level 10 (Pre-VCE) Mathematics** syllabus as a
foundation module. A student picks a module on the landing page, navigates
to a topic, works through short lessons (theory + worked examples), and does
exercises with worked solutions. No backend; progress is stored in the browser.

**Status:** Both modules are fully authored. **52 topics, 157 lessons, 383
exercises** (281 curated + 102 randomised) covering **73/73 syllabus dot
points** — 19 in Unit 1, 24 in Unit 2, and 30 in Pre-VCE Year 10. Unit 1 has
11 topics; Unit 2 has 11 topics (each one is a separate file in
`src/content/topics/` registered in the `TOPICS` array). Pre-VCE adds 30 more
topics grouped into 6 strands.

## Stack

Vite 5 + React 18 + TypeScript (strict) + Tailwind CSS 3 (`darkMode: 'class'`) +
KaTeX 0.16 for maths. Routing is `react-router-dom` 6 with **HashRouter** and Vite
`base: './'`, so the built app runs from any static host or the filesystem.

## Commands

```
npm run dev              # local dev server
npm run build            # tsc -b && vite build (must pass before committing)
npm run check:coverage   # assert every syllabus dot point is claimed by >=1 topic
npm run check:exercises  # instantiate every param exercise over 300 seeds and validate
```

Always run all three before considering content work done. `check:coverage` must
stay green — that means no dot point, in any module, is ever unmapped.

## App structure

```
/                LandingPage — pick Unit 1, Unit 2, or Pre-VCE
/unit-1          UnitHome — Unit 1 topics
/unit-2          UnitHome — Unit 2 topics
/pre-vce         PreVceHome — Year 10 topics grouped by strand
/topic/:id       TopicPage — lessons in a single topic
/topic/:id/:lessonId
                 LessonPage — theory, worked examples, exercises
```

Once a student picks a module on `/`, the sidebar narrows to that module's
topics (it can resolve `/topic/:id` to the right module by looking up the
topic). The sidebar always shows a `← Switch module` link that returns to the
landing page. Topic and lesson URLs are unchanged across modules, so a
bookmarked lesson keeps working.

Unit 1's home page shows a "Continue to Unit 2" card once the student has
finished it, making the natural VCE progression one click away.

## Content model (`src/content/types.ts`)

Content is authored as plain data, not JSX, so the whole site is static and the
checkers can reason about it.

```
Module → Topic → Lessons → WorkedExamples + Exercises
Exercise = CuratedExercise (fixed) | ParamExercise (build(seed) => ExerciseInstance)
```

- **Modules** are defined in `src/content/topics/index.ts` (`MODULES`). The
  three modules are `unit-1` (unit 1), `unit-2` (unit 2), and `pre-vce`
  (unit 10). Helpers `moduleForUnit`, `moduleForTopic`, `topicsForModule`,
  `homePathForModule` resolve the mapping.
- A **Lesson** is one short study session. Keep its theory, examples, and
  exercises self-contained.
- `body` and all solution/example strings are lightweight markdown + TeX.
  Supported markdown (see `src/components/Prose.tsx`): `$...$` / `$$...$$`,
  `**bold**`, `*italic*`, `` `code` ``, `###` headings, `-`/`*` and `1.`
  lists, `>` blockquotes (optionally tagged `> [!definition]` /
  `> [!warning]` for coloured left-rail callouts), and `| pipe | tables |`.
  Don't use markdown Prose doesn't support — it renders literally.

### Lesson UI conventions

Lessons are framed for first-time learners. `LessonPage`:

- Opens with a **"What you'll learn"** panel showing the `summary` plus the
  list of `###` headings extracted from the theory.
- Inline encouragement under Worked Examples ("predict the next line") and
  Exercises ("have a go on paper first").
- Closes with a **"Key takeaways"** recap, also derived from the `###`
  headings.

TopicPage surfaces prerequisites ("Before you start") and the next topic
("Up next") so a beginner always knows where they are in the syllabus.

### Answer checking (`src/lib/answer.ts`)

`checkAnswer(type, correct, given)`. Types: `exact` (normalised string), `numeric`
(tolerance + simple fractions like `3/4`), `polynomial` (order-independent terms),
`set` (order-independent, comma/semicolon-separated). The declared `answer` must be a
plain string the checker accepts — **not** TeX. e.g. for a `numeric` fraction answer
write `"1/3"`, never `"\\dfrac{1}{3}"`.

## Authoring conventions

- **Parameterised exercises must be pure functions of `seed`.** Never use
  `Date.now()` / `Math.random()`. Use only arithmetic on `seed` (and the seeded RNG
  in `src/exercises/engine.ts` if needed). `check:exercises` enforces purity.
- **Render polynomials through the helpers in `src/exercises/format.ts`**
  (`linear`, `quadratic`, `coeff`, `appendTerm`, `signed`, `frac`, `gcd`) — never
  hand-build coefficient strings. Manual building produces artifacts like `1x`,
  `-1x`, `+ 0`, `(x + 0)^2`. When a coefficient/constant could be 0 or ±1 and would
  render badly, either use the helpers or constrain the seed range to avoid the
  degenerate value (common idiom: `const c = (... ) || -3` to skip 0).
- Every param exercise needs a non-empty `answer` and `solution`, and the declared
  `answer` must pass its own `checkAnswer`. `check:exercises` verifies this over 300
  seeds; run it after any content change.

## Coverage contract

`src/content/coverage.ts` lists all 73 syllabus dot points (19 Unit 1, 24 Unit 2,
30 Pre-VCE Year 10) with stable ids like `u1-al-6` and `m10-a-3`. Each `Topic`
declares the dot-point ids it covers in its `dotPoints` array.
`scripts/check-coverage.ts` asserts every id is claimed by at least one topic.
This is what makes "covers all study requirements" verifiable rather than a
promise.

## Registering a new topic

1. Create `src/content/topics/NN-slug.ts` exporting a `Topic` (order `NN` within
   its unit, `dotPoints` from `coverage.ts`).
2. Import and add it to the `TOPICS` array in
   `src/content/topics/index.ts` — that array is the single source of truth for
   the sidebar, routing, and both checkers.
3. If it's a new module, add a module entry to `MODULES` in the same file and
   wire `moduleForUnit` / `topicsForModule` to recognise the new unit.
4. Run `npm run build`, `npm run check:coverage`, `npm run check:exercises`.

## Progress storage (`src/lib/storage.ts`)

localStorage key `vce-mm-progress-v1`, tracking completed lessons and per-exercise
attempt/correct counts. Updates fire a same-tab `vce-progress` event so the UI
refreshes (`src/lib/useProgress.ts`). A legacy `sections` key is read for
migration. Progress is shared across both modules — a student switching from
VCE to Pre-VCE keeps their completion ticks.

## AI "Explain to me" audio (`scripts/generate-audio.ts`, `src/components/LessonAudio.tsx`)

Every lesson page renders an **Explain to me** audio card between the
"What you'll learn" panel and the theory block. The card plays a short
spoken narration of the lesson and shows a collapsible transcript.

The audio is **pre-generated offline** by `scripts/generate-audio.ts` and
committed to `public/audio/lessons/{topic-id}/{lesson-id}.mp3` (plus a
matching `.json` sidecar with the script text). The browser just plays
the MP3 with a native `<audio>` element — no runtime AI or API keys in
the bundle.

### Generating audio

```
npm run generate:audio                                # every lesson
npm run generate:audio -- --topic functions-relations # one topic
npm run generate:audio -- --topic <t> --lesson <l>    # one lesson
npm run generate:audio -- --dry-script                # scripts only, skip TTS
npm run generate:audio -- --force                     # regenerate even if cached
```

Required env:

- `ANTHROPIC_BASE_URL` — Anthropic-compatible endpoint (defaults to
  `https://api.minimaxi.com/anthropic`).
- `ANTHROPIC_AUTH_TOKEN` — bearer token.
- `ANTHROPIC_MODEL` — model name (defaults to `$ANTHROPIC_MODEL` from
  the shell, else `MiniMax-M3`).

The generator does, in order:

1. For each lesson, build a prompt that asks minimax M3 to write a
   a spoken script (markdown/TeX stripped to plain text, math
   described in words). The script is persisted to
   `public/audio/lessons/{topic}/{lesson}.json`.
2. Probe common TTS routes on the same host (`/v1/audio/speech`,
   `/v1/tts`, `/v1/t2a_v2`, etc.). The first that returns `200` with
   `audio/*` content wins; the result is cached in
   `.audio-tts-endpoint` (gitignored).
3. POST the script to the discovered TTS endpoint and write the
   response to `public/audio/lessons/{topic}/{lesson}.mp3`.

**Graceful degradation:** if no TTS endpoint responds, the generator
still writes the JSON scripts and the UI shows "Audio not generated
yet — run `npm run generate:audio`" instead of a broken player. No
silent failures.

### Re-running

Already-generated assets are skipped unless `--force` is passed. Edit
`scripts/generate-audio.ts` to change the prompt, voice, or TTS
probing; the rest of the app reads only the assets on disk.

## Next up

Both modules are complete. Likely next directions (when one comes up):
enrich existing topics with more curated exercises, or add a Unit 3/4 study
strand when the user asks. Any new topic follows the same registration pattern
(`Topic` shape, registered in the `TOPICS` array) — `check:coverage` will
fail loudly if a `dotPoints` id is unknown or unmapped.