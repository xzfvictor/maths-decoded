import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-10 (VC2M10AA10).
// Experiment with functions and relations using digital tools, making
// and testing conjectures and generalising emerging patterns.

export const l10aAaFunctionsRelations: Topic = {
  id: 'l10a-aa-functions-relations',
  unit: '10A',
  order: 13,
  title: 'Functions and relations with digital tools',
  blurb:
    'Experiment with functions and relations using digital tools, making and testing conjectures and generalising emerging patterns.',
  dotPoints: ['l10a-aa-10'],

  lessons: [
    {
      id: 'investigate-variation',
      heading: 'Investigating parameter variation',
      summary: 'Vary one parameter at a time and observe how the graph changes; form a conjecture, then test it.',
      body: `Digital tools (Desmos, GeoGebra, calculators) let you change a parameter in real time and see the effect on the graph. This makes **patterns visible** — patterns that are very hard to spot from a static picture.

### Investigation workflow
1. **Pick a family**: e.g. $y = ax^2$.
2. **Hold all parameters fixed** except one — vary it.
3. **Observe** the change in shape, position, or both.
4. **Form a conjecture**: "As $a$ increases, the parabola gets…".
5. **Test** the conjecture with several different values.
6. **Generalise**: state a rule about the parameter's effect.

### Example conjecture
For $y = a(x - h)^2 + k$:
- Increasing $a$ makes the parabola **narrower**.
- Changing $h$ moves it **horizontally**.
- Changing $k$ moves it **vertically**.

### What you're really doing
You are turning a **rule** into a **graphical description**, and using many graphs to spot a rule that any single example wouldn't show.`,
      examples: [
        {
          id: 'ex-stretch',
          statement:
            'Using Desmos, vary $a$ in $y = a x^2$ from $1$ to $3$. What changes?',
          steps: [
            '$a = 1$: $y = x^2$ — standard parabola.',
            '$a = 3$: at the same $x$, $y$ is $3$ times as large — narrower "U".',
            'Conjecture: increasing $a$ **shrinks** the parabola horizontally and stretches it vertically.',
          ],
        },
        {
          id: 'ex-shift',
          statement:
            'In $y = x^2 + k$, vary $k$ from $-2$ to $2$. What changes?',
          steps: [
            '$k$ moves the whole graph up (positive) or down (negative).',
            'Vertex $(0, k)$ slides along the $y$-axis.',
            'The shape is unchanged.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-effect',
          difficulty: 'intro',
          instance: {
            prompt:
              'In $y = a \\cdot 2^x$, does increasing $a$ move the graph up, down, or change its shape? Answer "moves up", "moves down", or "changes shape".',
            answer: 'moves up',
            answerType: 'exact',
            hint: '$a$ multiplies every output.',
            solution: [
              'Multiplying every $y$ by $a > 1$ makes the curve move up uniformly; the shape is preserved.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-stretch',
          difficulty: 'core',
          instance: {
            prompt:
              'In $y = k/x$, does increasing $|k|$ make the curve move away from the axes or closer to them? Answer "away" or "closer".',
            answer: 'away',
            answerType: 'exact',
            hint: 'A larger $k$ means a larger $y$ at each $x$.',
            solution: [
              'Larger $|k|$ pushes the curve outward, increasing the distance from each axis.',
            ],
          },
        },
      ],
    },

    {
      id: 'testing-conjectures',
      heading: 'Testing and refining conjectures',
      summary: 'Make a claim, then test with three different inputs — if all match, the conjecture holds; if not, refine it.',
      body: `A conjecture is only as strong as the **evidence** supporting it. A good test:
- Picks **several different** inputs (not just one or two).
- Covers **edge cases** (e.g. large $x$, $x = 0$, negative $x$).
- Compares the predicted value to the actual value exactly.

### Refinement loop
1. State the conjecture clearly.
2. Test multiple inputs.
3. If all match → **keep** the conjecture.
4. If something disagrees → **adjust** the conjecture (e.g. "always" → "only for $x > 0$").

### Common digital-tool workflows
- Build a table of values via spreadsheet.
- Use **sliders** to vary parameters; record the resulting intercept / vertex.
- Plot multiple functions at once and look for intersections.

### From conjecture to proof
For VCE Mathematical Methods you will formalise these patterns; for now, a conjecture supported by tested evidence is the goal.`,
      examples: [
        {
          id: 'ex-test',
          statement:
            'Conjecture: "In $y = 2^x + c$, doubling $x$ quadruples $y$ minus $c$." Test with $c = 1$, $x = 2, 3, 4$.',
          steps: [
            'At $x = 2$: $y = 5$.',
            'At $x = 4$ (double $x$): $y = 17$.',
            '$17 - 1 = 16$. Is $16 = 4 \\cdot (5 - 1) = 16$? Yes ✓.',
            'Try $x = 3, 6$: $y(3) = 9, y(6) = 65$. $65 - 1 = 64$. Is $64 = 4 \\cdot 8 = 32$? No.',
            'Conjecture fails — refine.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-true',
          difficulty: 'intro',
          instance: {
            prompt:
              'Is the following conjecture true or false? Conjecture: "In $y = 3x$, doubling $x$ doubles $y$." Answer "true" or "false".',
            answer: 'true',
            answerType: 'exact',
            hint: 'If $x$ becomes $2x$, does $y$ become $2 \\cdot (3x) = 6x$?',
            solution: [
              'Yes. $y(2x) = 3(2x) = 6x = 2 \\cdot 3x = 2y(x)$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-false',
          difficulty: 'core',
          instance: {
            prompt:
              'Is the following conjecture true or false? Conjecture: "In $y = x^2 + 1$, doubling $x$ quadruples $y$." Answer "true" or "false".',
            answer: 'false',
            answerType: 'exact',
            hint: 'Check with $x = 1$ and $x = 2$.',
            solution: [
              '$y(1) = 2$, $y(2) = 5$. $5 \\ne 4 \\cdot 2 = 8$. So the conjecture is false.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-refine',
          difficulty: 'challenge',
          instance: {
            prompt:
              'A conjecture says: "$y = x^2$ passes through $(0,0), (1,1), (2,4), (3,9)$". State the $y$-value at $x = 4$ as an integer.',
            answer: '16',
            answerType: 'numeric',
            hint: 'Extend the pattern.',
            solution: [
              'Following the pattern $0, 1, 4, 9, \\ldots$ (perfect squares), $x = 4$ gives $y = 16$.',
            ],
          },
        },
      ],
    },
  ],
}
