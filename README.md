# MathsDecoded

A self-study platform that breaks down a syllabus into short lessons, walks you
through worked examples, and tests you with exercises that give full worked
solutions. The landing page lets you pick a **module** — currently the full
**Victorian Curriculum F-10 Version 2.0 Mathematics** for Levels 7, 8, 9, 10,
and 10A, plus **VCE Mathematical Methods Units 1 & 2** — and the rest of the
app narrows to that module so the student isn't distracted by material outside
their course.

The app is named **MathsDecoded** because the core promise is the same for any
subject: take the syllabus, demystify it, and meet a beginner where they are.
More subjects (Physics, Chemistry, …) can be plugged in as new modules without
touching the rest of the codebase.

- **Module-aware.** Pick a module on the landing page; the sidebar, home page,
  and progress tracking all scope themselves to that module until you switch.
- **Learn in small sessions.** Each topic is split into lessons that fit a
  single sitting, each with its own theory, worked examples, and exercises.
- **Built for first-time learners.** Every lesson opens with a "What you'll
  learn" summary and closes with a "Key takeaways" recap, so a student with no
  prior knowledge knows where the lesson is going and what to walk away knowing.
- **Practise with feedback.** Exercises check your answer, offer a hint, and
  reveal a step-by-step solution. Many are randomised, so you get a fresh
  question each time.
- **Refresh with AI variants.** Stumped or bored by a question? Use the
  lesson-level **AI Generated Questions** panel at the bottom of the exercises section.
  Two buttons — **Similar question** (re-roll at the same difficulty) and
  **Harder question** (climb one level up) — generate fresh practice from
  the dot points you've already learned. Cap at `challenge`; once you
  clear the hardest card, the **Harder** button disappears with a
  congratulatory note. See "Self-hosting the regenerate server" below for
  what runs that endpoint.
- **Listen before you read.** Each lesson has an "Explain to me" button that
  plays a short AI-narrated overview, with a transcript you can read along to.
- **Track your progress.** Completed lessons and exercise scores are saved
  locally in your browser — no account, no server.
- **Complete coverage, guaranteed.** A build-time check asserts that every
  syllabus dot point is covered by a topic.

> **Status:** Seven modules are registered — **162 topics** covering
> **183/183 syllabus dot points** (19 VCE Unit 1, 24 VCE Unit 2, 31 Year 7,
> 29 Year 8, 24 Year 9, 30 Year 10, 26 Year 10A). All topics are now fully
> authored: **363 lessons** (157 from VCE/Year 10, 206 new across
> Year 7–10A) and **729 exercises** (630 curated + 99 parameterised). Each
> lesson has a body with `###` headings, 3 worked examples, and 1+ curated
> intro exercises; core and challenge variants are generated on demand from
> the `/api/regenerate-exercise` endpoint. The `check:coverage` and
> `check:exercises` scripts assert the contract stays green.

## Modules

The landing page (`/`) asks the student to choose between the current
modules. New modules (other subjects) plug into the same picker with no
code changes outside `src/content/topics/index.ts`.

- **Year 7 Mathematics** — `/year-7`. 31 topics across the six Victorian
  Curriculum strands — currently stubs.
- **Year 8 Mathematics** — `/year-8`. 29 topics — currently stubs.
- **Year 9 Mathematics** — `/year-9`. 24 topics — currently stubs.
- **Year 10 Mathematics** — `/year-10`. 30 fully authored topics across the
  six strands; use as a refresher before VCE, or on its own.
- **Year 10A Mathematics** — `/year-10a`. 26 topics — currently stubs (no
  achievement standard; topics extend into VCE Methods).
- **VCE Mathematical Methods — Unit 1** — `/maths-methods-unit1`. Functions, algebra,
  calculus and probability. Eleven topics covering all Unit 1 dot points.
- **VCE Mathematical Methods — Unit 2** — `/maths-methods-unit2`. Transcendental functions,
  calculus and probability. Eleven topics covering all Unit 2 dot points.

Once a module is picked, the sidebar narrows to that module's topics and the
app keeps that focus until the student returns to the landing page. Each
module home shows a "Continue to …" card pointing at the next module in
curriculum order (Year 7 → 8 → 9 → 10 → 10A → VCE Unit 1 → VCE Unit 2), so the
natural Foundation → VCE progression is one click away.

Topic and lesson URLs (`/topic/:id`, `/topic/:id/:lessonId`) are shared across
modules — a bookmarked lesson opens in whichever module the sidebar thinks you
came from. A `← Switch module` link is always pinned to the top of the sidebar
for a one-click return to the landing page.

### Adding a new module

Adding another subject (e.g. Physics) is mostly a content exercise:

1. Add a `ModuleId` entry to `MODULES` in `src/content/topics/index.ts` and
   wire it into `moduleForUnit` / `topicsForModule`.
2. Add a route for the module's home page in `src/App.tsx`.
3. Add a syllabus catalog (dot points + strands) to `src/content/coverage.ts`
   and write the topics.

The sidebar, lesson framing, AI audio, progress storage, and checkers all
work as-is for the new module. See `CLAUDE.md` for the full register-a-new-
topic walkthrough.

## Tech stack

Static single-page app — content and coverage are bundled into the
client. A small [Hono](https://hono.dev/) Node server (`server/`) handles
the one runtime call (regenerating exercises on thumb-down) so the API
key never reaches the browser. Self-hostable today; portable to Vercel
or Cloudflare later.

- [Vite](https://vitejs.dev/) + [React](https://react.dev/) + TypeScript
- [Tailwind CSS](https://tailwindcss.com/) (light/dark mode)
- [KaTeX](https://katex.org/) for maths rendering
- [React Router](https://reactrouter.com/) (hash routing, so it runs from any static host)
- [Hono](https://hono.dev/) + `@hono/node-server` for the regenerate API

## Getting started

Requires [Node.js](https://nodejs.org/) 18+.

```bash
npm install       # install dependencies
npm run dev:all   # start the Vite dev server + the API server (http://localhost:5173, http://localhost:8787)
```

For the Vite dev server only (static UI without the regenerate API):

```bash
npm run dev
```

## Scripts

| Command | What it does |
| --- | --- |
| `npm run dev` | Start the Vite dev server (port 5173). |
| `npm run dev:server` | Start only the Hono API server (port 8787). |
| `npm run dev:all` | Start both via `concurrently` — the typical dev workflow. |
| `npm run start:server` | Production start of the API server (run behind nginx/caddy). |
| `npm run build` | Type-check and build the production site into `dist/`. |
| `npm run preview` | Serve the built site locally. |
| `npm run test:regenerate` | End-to-end test against a running server. Requires `npm run dev:server` in another shell. |
| `npm run check:coverage` | Verify every syllabus dot point is claimed by a topic. |
| `npm run check:exercises` | Validate every randomised exercise across 300 seeds. |
| `npm run generate:audio` | Pre-generate AI "Explain to me" audio for every lesson (writes to `public/audio/lessons/`). |

## AI lesson audio

Each lesson page includes an **Explain to me** card that plays a short
spoken overview of the theory. Audio is **pre-generated offline**
by `npm run generate:audio` and committed to the repo at
`public/audio/lessons/{topic}/{lesson}.mp3` (with a matching `.json`
transcript). The browser plays the MP3 with a native `<audio>` element
— there is no runtime AI call and no API key in the bundle.

Required env when generating:

```
ANTHROPIC_BASE_URL=https://api.minimaxi.com/anthropic
ANTHROPIC_AUTH_TOKEN=***
ANTHROPIC_MODEL=MiniMax-M3
```

The script first asks minimax M3 to write a conversational script for
each lesson, then probes the same host for a TTS endpoint
(`/v1/audio/speech`, `/v1/tts`, `/v1/t2a_v2`, etc.). If no TTS route is
reachable, only the JSON scripts are written and the UI degrades to a
clear "audio not generated yet" hint. See `CLAUDE.md` for the full
flow.

## Course map — VCE Mathematical Methods

### Unit 1 — Functions, algebra, calculus & probability
1. Functions, relations, domain & range
2. Inverse functions & their graphs
3. Linear & quadratic functions
4. Cubic & quartic functions
5. Power functions
6. Transformations of the plane
7. Solving polynomials
8. Simultaneous equations
9. Rates of change
10. Probability foundations
11. Counting techniques

### Unit 2 — Transcendental functions, calculus & probability
12. Circular functions
13. Periodicity, symmetry & transformed circular functions
14. Exponential functions & their graphs
15. Logarithms
16. Solving transcendental equations
17. Newton's method
18. Limits & the derivative from first principles
19. Differentiation rules & applications
20. Anti-differentiation
21. Probability of compound events
22. Conditional probability & independence

### Year 10 Mathematics (Victorian Curriculum F-10 V2.0)

Organised into the six curriculum strands:

- **Number** — real numbers, approximations, and the effect of repeated
  calculations on final results.
- **Algebra** — factorisation, exponent laws, equations, inequalities,
  functions, and modelling.
- **Measurement** — surface area, volume, logarithmic scales, Pythagoras and
  right-angled trigonometry.
- **Space** — geometric proofs in the plane and network diagrams of practical
  situations.
- **Statistics** — distributions, boxplots, scatterplots, two-way tables, and
  statistical investigations.
- **Probability** — conditional probability, multi-step chance experiments, and
  independence.

See [`src/content/coverage.ts`](./src/content/coverage.ts) for the full
dot-point catalog and which topics cover each one.

## How content is organised

Lessons and exercises are authored as plain data (not markup), which keeps the
site static and lets the app verify its own coverage and correctness.

```
Module → Topic → Lessons → Worked examples + Exercises
```

- **Modules** are defined in [`src/content/topics/index.ts`](./src/content/topics/index.ts)
  (`MODULES`). The current modules are `year-7`, `year-8`, `year-9`, `year-10`,
  `year-10a`, `maths-methods-unit1`, and `maths-methods-unit2`. New modules
  (other subjects or year levels) are added by appending to `MODULES` and
  wiring their home route.
- **Topics** live in [`src/content/topics/`](./src/content/topics/) and are
  registered in the `TOPICS` array.
- **Coverage** is defined in [`src/content/coverage.ts`](./src/content/coverage.ts):
  every syllabus dot point has a stable id, and each topic declares which ids
  it covers.
- **Exercises** are either hand-written or randomised. Randomised exercises
  are pure functions of a seed, so a given question always has the same answer
  and solution — which is what `check:exercises` verifies.

Contributor guidance and authoring conventions are in
[`CLAUDE.md`](./CLAUDE.md).

## Building for deployment

```bash
npm run build     # outputs a static site to dist/
```

The `dist/` folder can be served by any static host (GitHub Pages, Netlify,
Vercel, or a plain file server). Because routing uses hash URLs and asset
paths are relative, no special server configuration is needed.

## Self-hosting the regenerate server

The regenerate API is in `server/`. The same `Hono` app definition is
portable to Vercel and Cloudflare Workers with a one-file adapter.

For self-host:

1. Copy `.env.example` to `.env` and fill in `ANTHROPIC_AUTH_TOKEN`.
2. Build the static bundle:
   ```bash
   npm run build
   ```
3. Run the API as a long-lived process:
   ```bash
   npm run start:server
   ```
4. Front both with nginx or caddy. The static site serves at `/`;
   `/api/*` proxies to `http://127.0.0.1:8787`. Example caddyfile:
   ```
   maths.example.com {
       root * /var/www/maths-decoded/dist
       file_server
       reverse_proxy /api/* 127.0.0.1:8787
   }
   ```

The API holds the token — it is **never** sent to the browser. Each request
is rate-limited per IP (10 tokens, refills 1 / 36 s) and identical exercise
regenerations are cached for 24 h. Migrations to Vercel or Cloudflare
Workers are documented in `CLAUDE.md`.

## Disclaimer

This is an independent study resource and is not affiliated with or endorsed by
the VCAA. Study-design content points are referenced for the purpose of
curriculum alignment.