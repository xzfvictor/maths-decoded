# VCE Maths Methods

A study web app covering **all of VCE Mathematical Methods Units 1 & 2**, plus the
**Victorian Curriculum Level 10 (Pre-VCE) Mathematics** syllabus as a foundation
module. Navigate to a topic, work through short lessons of theory and worked
examples, then practise with exercises that give full worked solutions. Every
question is mapped to the official syllabus, so the app covers the whole course —
not just a sample.

- **Three modules, one app.** Pick VCE Unit 1, VCE Unit 2, or Pre-VCE Year 10
  on the landing page; the rest of the app narrows to that module so the
  student isn't distracted by material outside their course.
- **Learn in small sessions.** Each topic is split into lessons that fit a single
  sitting, each with its own theory, worked examples, and exercises.
- **Built for first-time learners.** Every lesson opens with a "What you'll
  learn" summary and closes with a "Key takeaways" recap, so a student with no
  prior knowledge knows where the lesson is going and what to walk away knowing.
- **Practise with feedback.** Exercises check your answer, offer a hint, and
  reveal a step-by-step solution. Many are randomised, so you get a fresh
  question each time.
- **Listen before you read.** Each lesson has an "Explain to me" button that
  plays a short AI-narrated overview, with a transcript you can read along to.
- **Track your progress.** Completed lessons and exercise scores are saved
  locally in your browser — no account, no server.
- **Complete coverage, guaranteed.** A build-time check asserts that every
  syllabus dot point is covered by a topic.

> **Status:** Both modules are fully authored. **52 topics, 157 lessons, 383
> exercises** (281 curated + 102 randomised) covering **73/73 syllabus dot
> points** (43 VCE + 30 Pre-VCE). The `check:coverage` script asserts every dot
> point is claimed and stays green.

## Modules

The landing page (`/`) asks the student to choose between three modules:

- **VCE Mathematical Methods — Unit 1** — `/unit-1`. Functions, algebra,
  calculus and probability. Eleven topics covering all Unit 1 dot points.
- **VCE Mathematical Methods — Unit 2** — `/unit-2`. Transcendental functions,
  calculus and probability. Eleven topics covering all Unit 2 dot points.
- **Pre-VCE Year 10 Maths** — `/pre-vce`. Year 10 foundations organised into the
  six Victorian Curriculum strands (Number, Algebra, Measurement, Space,
  Statistics, Probability). Use as a refresher before VCE, or on its own.

Once a module is picked, the sidebar narrows to that module's topics and the
app keeps that focus until the student returns to the landing page. Unit 1's
home page offers a "Continue to Unit 2" card so the natural progression is
one click away when Unit 1 is finished.

Topic and lesson URLs (`/topic/:id`, `/topic/:id/:lessonId`) are shared across
modules — a bookmarked lesson opens in whichever module the sidebar thinks you
came from. A `← Switch module` link is always pinned to the top of the sidebar
for a one-click return to the landing page.

## Tech stack

Static single-page app — no backend.

- [Vite](https://vitejs.dev/) + [React](https://react.dev/) + TypeScript
- [Tailwind CSS](https://tailwindcss.com/) (light/dark mode)
- [KaTeX](https://katex.org/) for maths rendering
- [React Router](https://reactrouter.com/) (hash routing, so it runs from any static host)

## Getting started

Requires [Node.js](https://nodejs.org/) 18+.

```bash
npm install       # install dependencies
npm run dev       # start the dev server (http://localhost:5173)
```

## Scripts

| Command | What it does |
| --- | --- |
| `npm run dev` | Start the local development server. |
| `npm run build` | Type-check and build the production site into `dist/`. |
| `npm run preview` | Serve the built site locally. |
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

## Course map

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

### Pre-VCE — Year 10 Mathematics

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
  (`MODULES`). The three modules are `unit-1`, `unit-2`, and `pre-vce` —
  each VCE unit is its own module, plus the Pre-VCE Year 10 strand; the rest
  of the code is module-aware.
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

## Disclaimer

This is an independent study resource and is not affiliated with or endorsed by
the VCAA. Study-design content points are referenced for the purpose of
curriculum alignment.