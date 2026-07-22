import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A08.
// Solve linear inequalities and graph their solutions on a number line.

export const algebraInequalities: Topic = {
  id: 'm10-algebra-linear-inequalities',
  unit: 10,
  order: 14,
  title: 'Linear inequalities on a number line',
  blurb:
    'Solve linear inequalities the same way as equations, then draw the solution set on a number line with the right open / closed circle.',
  dotPoints: ['m10-a-8'],

  lessons: [
    {
      id: 'solve-and-graph',
      heading: 'Solving & graphing linear inequalities',
      summary: 'Solve like an equation, but flip the inequality if you divide by a negative.',
      body: `An **inequality** compares two expressions with $<$, $>$, $\\le$, $\\ge$. To solve, isolate the variable using inverse operations — almost the same as solving an equation, with one **critical rule**.

### The rule
If you multiply or divide both sides by a **negative** number, the inequality **flips**.

- $3x < 12$ → divide by $3$: $x < 4$.
- $-3x < 12$ → divide by $-3$ (and flip): $x > -4$.

### Graphing the solution set
On a number line:
- $\\le$ or $\\ge$ → **closed** circle at the endpoint (the endpoint is included).
- $<$ or $>$ → **open** circle at the endpoint (the endpoint is NOT included).
- The solution set is a **half-line**: a ray extending from the endpoint to the right (or left).`,
      examples: [
        {
          id: 'ex-positive-coeff',
          statement: 'Solve $4x - 5 < 11$ and graph on a number line.',
          steps: [
            'Add $5$: $4x < 16$.',
            'Divide by $4$ (positive, no flip): $x < 5$.',
            'Open circle at $5$, ray extending to the left.',
          ],
        },
        {
          id: 'ex-negative-coeff',
          statement: 'Solve $-2x + 6 \\ge 10$.',
          steps: [
            'Subtract $6$: $-2x \\ge 4$.',
            'Divide by $-2$ (negative, **flip**): $x \\le -2$.',
            'Closed circle at $-2$, ray to the left.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-solve-positive',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $3x - 4 < 8$. State the smallest integer $x$ satisfying this. (Use integer values.)',
            answer: '3',
            answerType: 'numeric',
            hint: 'Solve $3x < 12$, so $x < 4$.',
            solution: [
              '$x < 4$. Smallest integer satisfying is $x = 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-solve-flip',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $-5x + 10 \\le 30$. State the largest integer $x$ satisfying this.',
            answer: '-4',
            answerType: 'numeric',
            hint: '$-5x \\le 20 \\Rightarrow x \\ge -4$.',
            solution: [
              '$-5x \\le 20 \\Rightarrow x \\ge -4$. Largest integer is $-4$.',
            ],
          },
        },
      ],
    },
  ],
}