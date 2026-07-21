# CLAUDE.md

Guidance for working in this repository.

## What this is

A static web app that helps a student study **all** of VCE Mathematical Methods
Units 1 & 2, covering every VCAA study-design dot point. A student navigates to a
topic, works through short lessons (theory + worked examples), and does exercises
with worked solutions. No backend; progress is stored in the browser.

**Status:** Unit 1 is fully authored (11 topics). Unit 2 is not yet authored — its
dot points exist in `coverage.ts` but no topics claim them yet (so `check:coverage`
reports them as unmapped; this is expected until Unit 2 is written).

## Stack

Vite 5 + React 18 + TypeScript (strict) + Tailwind CSS 3 (`darkMode: 'class'`) +
KaTeX 0.16 for maths. Routing is `react-router-dom` 6 with **HashRouter** and Vite
`base: './'`, so the built app runs from any static host or the filesystem.

## Commands

```
npm run dev              # local dev server
npm run build            # tsc -b && vite build (must pass before committing)
npm run check:coverage   # assert every VCAA dot point is claimed by >=1 topic
npm run check:exercises  # instantiate every param exercise over 300 seeds and validate
```

Always run all three before considering content work done. `check:coverage` will
"fail" on unmapped Unit 2 dot points until Unit 2 is authored — that's expected;
what matters is that no **Unit 1** dot point regresses to unmapped.

## Content model (`src/content/types.ts`)

Content is authored as plain data, not JSX, so the whole site is static and the
checkers can reason about it.

```
Topic → lessons: Lesson[]
Lesson → examples: WorkedExample[] + exercises: Exercise[]
Exercise = CuratedExercise (fixed) | ParamExercise (build(seed) => ExerciseInstance)
```

- A **Lesson** is one short study session. Keep its theory, examples, and exercises
  self-contained.
- `body` and all solution/example strings are lightweight markdown + TeX. Supported
  markdown (see `src/components/Prose.tsx`): `$...$` / `$$...$$`, `**bold**`,
  `*italic*`, `` `code` ``, `###` headings, `-`/`*` and `1.` lists, `>` blockquotes,
  and `| pipe | tables |`. Don't use markdown Prose doesn't support — it renders literally.

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

`src/content/coverage.ts` lists all 43 VCAA dot points (19 Unit 1, 24 Unit 2) with
stable ids like `u1-al-6`. Each `Topic` declares the dot-point ids it covers in its
`dotPoints` array. `scripts/check-coverage.ts` asserts every id is claimed by at
least one topic. This is what makes "covers all study requirements" verifiable
rather than a promise.

## Registering a new topic

1. Create `src/content/topics/NN-slug.ts` exporting a `Topic` (order `NN` within its
   unit, `dotPoints` from `coverage.ts`).
2. Import and add it to the `TOPICS` array in `src/content/topics/index.ts` — that
   array is the single source of truth for the sidebar, routing, and both checkers.
3. Run `npm run build`, `npm run check:coverage`, `npm run check:exercises`.

## Progress storage (`src/lib/storage.ts`)

localStorage key `vce-mm-progress-v1`, tracking completed lessons and per-exercise
attempt/correct counts. Updates fire a same-tab `vce-progress` event so the UI
refreshes (`src/lib/useProgress.ts`). A legacy `sections` key is read for migration.

## Next up

Author the 11 Unit 2 topics (circular functions, exponentials & logarithms, the
derivative and differentiation, anti-differentiation, and the Unit 2 probability
strand) so the remaining `u2-*` dot points are all claimed.
