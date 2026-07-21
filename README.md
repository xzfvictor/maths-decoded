# VCE Maths Methods

A study web app for **VCE Mathematical Methods Units 1 & 2**. Navigate to a topic,
work through short lessons of theory and worked examples, then practise with
exercises that give full worked solutions. Every question is mapped to the official
VCAA study-design content, so the app covers the whole course — not just a sample.

- **Learn in small sessions.** Each topic is split into lessons that fit a single
  sitting, each with its own theory, worked examples, and exercises.
- **Practise with feedback.** Exercises check your answer, offer a hint, and reveal a
  step-by-step solution. Many are randomised, so you get a fresh question each time.
- **Track your progress.** Completed lessons and exercise scores are saved locally in
  your browser — no account, no server.
- **Complete coverage, guaranteed.** A build-time check asserts that every VCAA
  study-design dot point is covered by a topic.

> **Status:** Both units are fully authored. **22 topics, 80 lessons, 140
> exercises**, covering every study-design dot point. The
> `check:coverage` script asserts that 43/43 dot points are claimed and
> stays green.

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
| `npm run check:coverage` | Verify every VCAA dot point is claimed by a topic. |
| `npm run check:exercises` | Validate every randomised exercise across 300 seeds. |

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

See [`src/content/coverage.ts`](./src/content/coverage.ts) for the full dot-point
catalog and which topics cover each one.

## How content is organised

Lessons and exercises are authored as plain data (not markup), which keeps the site
static and lets the app verify its own coverage and correctness.

```
Topic  →  Lessons  →  Worked examples  +  Exercises
```

- **Topics** live in `src/content/topics/` and are registered in
  `src/content/topics/index.ts`.
- **Coverage** is defined in `src/content/coverage.ts`: every VCAA study-design dot
  point has a stable id, and each topic declares which ids it covers.
- **Exercises** are either hand-written or randomised. Randomised exercises are pure
  functions of a seed, so a given question always has the same answer and solution —
  which is what `check:exercises` verifies.

Contributor guidance and authoring conventions are in [`CLAUDE.md`](./CLAUDE.md).

## Building for deployment

```bash
npm run build     # outputs a static site to dist/
```

The `dist/` folder can be served by any static host (GitHub Pages, Netlify, Vercel,
or a plain file server). Because routing uses hash URLs and asset paths are relative,
no special server configuration is needed.

## Disclaimer

This is an independent study resource and is not affiliated with or endorsed by the
VCAA. Study-design content points are referenced for the purpose of curriculum
alignment.
