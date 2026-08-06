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
- **Watch before you read.** Many lessons also include a short **AI-generated
  video** that visualises the lesson content while the narration plays. The
  video sits in the same "Explain to me" card above the transcript and the
  audio is muxed onto the video itself, so the student only sees one
  player. If the video is missing, the audio player + transcript still
  show. Videos are produced offline by `scripts/` in this repo (see
  "Learn with a video" below).
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
> `check:exercises` scripts assert the contract stays green. Year 8, Year 10A,
> and Year 10 have **183 narrated video lessons** in `public/video/lessons/`
> (49 for Year 8 + 57 for Year 10A + 77 for Year 10, see "Learn with a video"
> below).

## Modules

The landing page (`/`) asks the student to choose between the current
modules. New modules (other subjects) plug into the same picker with no
code changes outside `src/content/topics/index.ts`.

- **Year 7 Mathematics** — `/year-7`. 31 topics across the six Victorian
  Curriculum strands.
- **Year 8 Mathematics** — `/year-8`. 29 fully authored topics across the
  six strands, with 49 narrated video lessons.
- **Year 9 Mathematics** — `/year-9`. 24 topics.
- **Year 10 Mathematics** — `/year-10`. 30 fully authored topics across the
  six strands, with 77 narrated video lessons; use as a refresher before VCE,
  or on its own.
- **Year 10A Mathematics** — `/year-10a`. 26 fully authored topics
  extending into VCE Methods, with 57 narrated video lessons.
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

## Learn with a video

Many lessons also include a **short narrated video** that animates the
content on screen while the narration plays — the same `Explain to me`
audio, just visualised. Videos live at
`public/video/lessons/{topic}/{lesson}.mp4` (mirroring the audio
folder). If the MP4 is missing, the card gracefully falls back to
audio-only + transcript. As of this writing, **183 lessons have videos**:
49 for Year 8, 57 for Year 10A, and 77 for Year 10. More modules to come.

The video pipeline lives in `scripts/videos/`:

- `scripts/videos/_common.py` — shared helpers (safe-area constants,
  `beat_group()` VGroup cleaner, `make_term_card()`, `make_equation_card()`,
  `animate_intro()`, `animate_final_definition()`).
- `scripts/videos/<lesson>.py` — one Manim `Scene` per lesson, each
  following a 5-beat structure (title → concrete example →
  generalisation → contrast → final takeaway).
- The `manimcommunity/manim:latest` Docker image renders the scenes;
  `ffmpeg` muxes the narration and trims the final MP4 to the measured audio
  duration. Run `scripts/videos/verify_year10.sh` to check Year 10 coverage,
  duration alignment, and 1-fps frame extraction.

There is **one mandatory workflow step** before any video is declared
done: extract intermediate frames at 1 fps and inspect **at least 10–15
of them** to verify no overlap, no content covering the title or
subtitle, and no shapes extending past the safe area
`y ∈ [-1.5, 1.8]`. Last-frame-only checks hide most mid-video issues.
A reusable playbook of safe-area rules, scaling limits, beat_group
usage, and intermediate-frame verification is in the
`~/.claude/skills/math-videos/SKILL.md` skill (used by the agents that
authored the videos).

## Course map

Seven modules form the Foundation → VCE progression: **Year 7 → Year 8 →
Year 9 → Year 10 → Year 10A → VCE Methods Unit 1 → VCE Methods Unit 2**.
Every topic below is registered with a stable kebab-case id and a
Victorian-Curriculum dot-point code (for the Foundation levels) or VCE AoS
reference (for the two VCE units).

Total coverage: **162 topics, 363 lessons, 729 exercises** (602 curated + 99
parameterised, × 300 seeds each), **183/183 syllabus dot points** claimed.
The five Foundation modules share the same six-strand taxonomy, while the two
VCE modules use the four Areas of Study.

### Year 7 Mathematics (Victorian Curriculum F-10 V2.0)

31 dot points across the six strands. Topic titles below; the bracketed
prefix is the coverage code (`l7-n-N`, `l7-a-N`, etc.).

#### Number
1. `l7-n-1` — Squares and square roots
2. `l7-n-2` — Prime factorisation and expanded notation
3. `l7-n-3` — Equivalent fractions and the number line
4. `l7-n-4` — Rounding and estimation
5. `l7-n-5` — Multiply and divide fractions and decimals
6. `l7-n-6` — 4 operations with positive rationals
7. `l7-n-7` — Percentages of quantities
8. `l7-n-8` — Addition and subtraction of integers
9. `l7-n-9` — Ratios
10. `l7-n-10` — Mathematical modelling with rationals and percentages

#### Algebra
11. `l7-a-1` — Variables and formulas
12. `l7-a-2` — Laws and algebraic expressions
13. `l7-a-3` — One-variable linear equations
14. `l7-a-4` — Graphs of relationships in authentic data
15. `l7-a-5` — Tables of values and the Cartesian plane
16. `l7-a-6` — Formulas with several variables

#### Measurement
17. `l7-m-1` — Areas of rectangles, triangles and parallelograms
18. `l7-m-2` — Volume of right prisms
19. `l7-m-3` — Circle circumference and prism formulas
20. `l7-m-4` — Parallel lines and angle relationships
21. `l7-m-5` — Triangle angle sum
22. `l7-m-6` — Modelling with ratios of lengths, areas and volumes

#### Space
23. `l7-sp-1` — 3D objects in 2D
24. `l7-sp-2` — Classifying polygons
25. `l7-sp-3` — Coordinate transformations
26. `l7-sp-4` — Sorting and classifying shapes

#### Statistics
27. `l7-st-1` — Measures of centre
28. `l7-st-2` — Data displays and distributions
29. `l7-st-3` — Statistical investigations

#### Probability
30. `l7-p-1` — Sample spaces and probability
31. `l7-p-2` — Repeated chance experiments

### Year 8 Mathematics

29 dot points. Like Year 7, every topic declares its strand via the first
coverage code.

#### Number
1. `l8-n-1` — Irrational numbers
2. `l8-n-2` — Exponent laws with positive integers
3. `l8-n-3` — Fractions, terminating and recurring decimals
4. `l8-n-4` — 4 operations with integers and rationals
5. `l8-n-5` — Percentages, including percentage error
6. `l8-n-6` — Modelling with rationals and percentages

#### Algebra
7. `l8-a-1` — Linear expressions
8. `l8-a-2` — Linear equations and inequalities
9. `l8-a-3` — Linear modelling in financial contexts
10. `l8-a-4` — Algorithms and testing procedures
11. `l8-a-5` — Linear functions and relations

#### Measurement
12. `l8-m-1` — Area and perimeter of composite shapes
13. `l8-m-2` — Volume and capacity of right prisms
14. `l8-m-3` — Circumference and area of a circle
15. `l8-m-4` — Time and time zones
16. `l8-m-5` — Rates
17. `l8-m-6` — Pythagoras' theorem
18. `l8-m-7` — Modelling with ratios and rates

#### Space
19. `l8-sp-1` — Congruence and similarity
20. `l8-sp-2` — Properties of quadrilaterals
21. `l8-sp-3` — 3D coordinate systems
22. `l8-sp-4` — Algorithms for congruency and similarity

#### Statistics
23. `l8-st-1` — Populations, samples and data collection
24. `l8-st-2` — Sampling techniques
25. `l8-st-3` — Comparing sample distributions
26. `l8-st-4` — Statistical investigations with samples

#### Probability
27. `l8-p-1` — Complementary events
28. `l8-p-2` — Outcome combinations for two events
29. `l8-p-3` — Chance experiments and simulations

### Year 9 Mathematics

24 dot points. Adds scientific notation, quadratic functions, and
similar-triangle trig — the bridge between Year 8 and Year 10.

#### Number
1. `l9-n-1` — Real numbers, rational and irrational

#### Algebra
2. `l9-a-1` — Exponent laws with variables
3. `l9-a-2` — Simplifying, expanding and factorising
4. `l9-a-3` — Linear graphs and linear equations
5. `l9-a-4` — Gradient, midpoint and distance
6. `l9-a-5` — Quadratic functions and equations
7. `l9-a-6` — Mathematical modelling of change
8. `l9-a-7` — Variation of parameters

#### Measurement
9. `l9-m-1` — Volume and surface area of prisms and cylinders
10. `l9-m-2` — Scientific notation
11. `l9-m-3` — Pythagoras and trigonometry
12. `l9-m-4` — Errors in measurements
13. `l9-m-5` — Modelling with proportion, rates and scale

#### Space
14. `l9-sp-1` — Trigonometric ratios in similar triangles
15. `l9-sp-2` — Enlargement transformation
16. `l9-sp-3` — Geometric algorithms

#### Statistics
17. `l9-st-1` — Survey reports and data collection
18. `l9-st-2` — Sampling methods
19. `l9-st-3` — Comparing data sets
20. `l9-st-4` — Choosing data displays
21. `l9-st-5` — Statistical investigations

#### Probability
22. `l9-p-1` — Two-step chance experiments
23. `l9-p-2` — Relative frequencies
24. `l9-p-3` — Repeated chance experiments and simulations

### Year 10 Mathematics (Victorian Curriculum F-10 V2.0)

30 dot points, fully authored (with parameters and AI intros). The bridge
into VCE Methods. Organised into the six curriculum strands:

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

### Year 10A Mathematics — extension into VCE

26 dot points. There is no achievement standard for Level 10A; the topics
are organised as an extension bridge into VCE Mathematical Methods. Adds
surds, logarithms, polynomials, factor / remainder theorems, standard
deviation, sine/cosine/area rules, and counting principles.

#### Number
1. `l10a-an-1` — Surds and fractional indices
2. `l10a-an-2` — Operations with fractional exponents and surds
3. `l10a-an-3` — Logarithms and logarithmic scales

#### Algebra
4. `l10a-aa-1` — Polynomials, factor and remainder theorems
5. `l10a-aa-2` — Algorithms and simulations
6. `l10a-aa-3` — Linear expressions with rational coefficients
7. `l10a-aa-4` — Exponentials and logarithms as inverses
8. `l10a-aa-5` — Parabolas, hyperbolas, circles and exponentials
9. `l10a-aa-6` — Polynomial features and sketching
10. `l10a-aa-7` — Factorising and solving quadratics
11. `l10a-aa-8` — Function notation in modelling
12. `l10a-aa-9` — Linear and non-linear simultaneous equations
13. `l10a-aa-10` — Functions and relations with digital tools

#### Measurement
14. `l10a-am-1` — Surface area and volume of pyramids, cones, spheres
15. `l10a-am-2` — Rates of change and limiting values

#### Space
16. `l10a-asp-1` — Circle theorems
17. `l10a-asp-2` — Sine, cosine and area rules
18. `l10a-asp-3` — Symmetry and periodicity of trig functions
19. `l10a-asp-4` — Simple trigonometric equations
20. `l10a-asp-5` — 3D right-angled triangle problems
21. `l10a-asp-6` — Algorithms for spatial problems

#### Statistics
22. `l10a-ast-1` — Mean, standard deviation and data sets
23. `l10a-ast-2` — Measures of spread
24. `l10a-ast-3` — Bivariate data and lines of best fit

#### Probability
25. `l10a-ap-1` — Counting principles and factorial notation
26. `l10a-ap-2` — Investigating reports of studies

### VCE Mathematical Methods — Unit 1

Functions, algebra, calculus & probability. Eleven topics covering the four
Areas of Study (FR, AL, CA, PR):

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

### VCE Mathematical Methods — Unit 2

Transcendental functions, calculus & probability. Eleven topics covering
the four Areas of Study:

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

---

See [`src/content/coverage.ts`](./src/content/coverage.ts) for the full
dot-point catalog (every `code` field is the original Victorian Curriculum
F-10 V2.0 code, e.g. `VC2M7N01`) and which topics cover each one.

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