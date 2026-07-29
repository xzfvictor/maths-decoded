import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Space · l9-sp-3 (VC2M9SP03).
// Geometric algorithms.

export const l9SpGeometricAlgorithms: Topic = {
  id: 'l9-sp-geometric-algorithms',
  unit: 9,
  order: 16,
  title: 'Geometric algorithms',
  blurb:
    'Design, test and refine algorithms based on geometric constructions and theorems, and discuss and evaluate refinements.',
  dotPoints: ['l9-sp-3'],

  lessons: [
    {
      id: 'construction-algorithms',
      heading: 'Algorithms for geometric constructions',
      summary: 'A construction algorithm is a finite list of steps (using compass and straightedge) that produces a specific shape.',
      body: `A **construction algorithm** is a sequence of geometric steps — using only a compass and straightedge — that produces a target shape, point or line.

### Common building blocks
- Construct a **perpendicular bisector** of a segment (gives the midpoint and a line at right angles).
- Construct a **perpendicular from a point to a line** (drops a right angle).
- Construct an **angle bisector** (splits an angle into two equal halves).
- **Copy an angle** at a new vertex.
- **Bisect a segment** (locate the midpoint).

### Recipe style
1. State the **inputs** (given points, segments, angles).
2. List the **steps** in order — each step references a building block or a previous step's output.
3. State the **outputs** (the constructed object).`,
      examples: [
        {
          id: 'ex-perp-bisect',
          statement:
            'Describe an algorithm to construct the perpendicular bisector of a segment $AB$.',
          steps: [
            'Place the compass at $A$ with radius $> \\tfrac{AB}{2}$; draw an arc above and below the segment.',
            'Same radius from $B$; draw arcs that cross the first pair.',
            'Join the two crossing points with a straightedge. This line is the perpendicular bisector of $AB$.',
          ],
        },
        {
          id: 'ex-angle-copy',
          statement:
            'Outline an algorithm to copy angle $\\angle XYZ$ to a new ray starting at a chosen point $P$.',
          steps: [
            'From $Y$ draw an arc cutting the two arms of $\\angle XYZ$ at $A$ (on $YX$) and $B$ (on $YZ$).',
            'From $P$ draw a ray; from $P$ mark the same radius arc, crossing the new ray at $A\'$.',
            'Set compass to length $AB$; from $A\'$ mark that length on the arc to get $B\'$.',
            'Draw ray $PB\'$. The angle at $P$ is a copy of $\\angle XYZ$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-alg-step',
          difficulty: 'intro',
          instance: {
            prompt:
              'When describing a construction algorithm, you should first state: the inputs, the steps, or the colour scheme?',
            answer: 'inputs',
            answerType: 'exact',
            hint: 'Every algorithm starts with what you are given.',
            solution: [
              'State the **inputs** first — what points, segments or angles you are given.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-bisect',
          difficulty: 'core',
          instance: {
            prompt:
              'Constructing the perpendicular bisector of segment $AB$ — what compass radius must you use? (Answer: any radius greater than what fraction of $AB$?)',
            answer: '1/2',
            answerType: 'exact',
            hint: 'Each arc must reach past the midpoint of $AB$.',
            solution: [
              'Any radius greater than $\\tfrac{1}{2} AB$ (i.e. strictly more than half the length).',
            ],
          },
        },
      ],
    },

    {
      id: 'test-refine',
      heading: 'Testing, refining, evaluating',
      summary: 'Run the algorithm on examples; check the output; revise if it fails. Each test should expose a new case.',
      body: `An algorithm isn't finished when it's written — it's finished when it **works for every case** it's supposed to handle.

### Testing loop
1. **Run** the algorithm on a representative example.
2. **Check** that the output matches the goal (e.g. perpendicular, midpoint, equal angles).
3. If it fails, **revise** the steps (often one step was underspecified).
4. Try **edge cases**: very small angles, a point on the line, equal sides, very long segments, etc.

### Common refinements
- Replace "draw a circle" with "draw a circle of radius $r$" if the size matters.
- Add a check before continuing: "if $X$ and $Y$ coincide, the construction is degenerate".
- Combine steps when they always occur together.

### Evaluating
Ask: does the algorithm always terminate? Does it use only the allowed tools? Is the output unique?`,
      examples: [
        {
          id: 'ex-test-angle',
          statement:
            'You wrote an algorithm to bisect an angle. On the test case $\\angle ABC = 60°$, the two resulting angles measure $28°$ and $32°$. What is wrong?',
          steps: [
            'A bisector should split the angle into two **equal** parts (so $30°$ each).',
            'Likely the compass radius was changed between the two arc-drawing steps — the algorithm needs to specify "same radius".',
          ],
        },
        {
          id: 'ex-edge-case',
          statement:
            'Your perpendicular-from-point-to-line construction fails when the point is already on the line. What refinement handles it?',
          steps: [
            'Add a check: if the point is on the line, the perpendicular passes through the point at right angles — construct it directly with a single compass step from the point.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-refine',
          difficulty: 'core',
          instance: {
            prompt:
              'Your algorithm produces an output, but a check shows it is wrong. What is the first thing to do? Answer "rewrite from scratch", "change one step", or "ignore it".',
            answer: 'change one step',
            answerType: 'exact',
            hint: 'Refine, don\'t restart.',
            solution: [
              '**Change one step** — narrow down which step is wrong rather than rewriting from scratch.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-edge',
          difficulty: 'intro',
          instance: {
            prompt:
              'When testing an algorithm, is it useful to try inputs that are "extreme" (e.g. very small or very large)? Answer "yes" or "no".',
            answer: 'yes',
            answerType: 'exact',
            hint: 'Edge cases often reveal bugs.',
            solution: [
              '**Yes** — edge cases are where broken algorithms usually show their bugs.',
            ],
          },
        },
      ],
    },
  ],
}
