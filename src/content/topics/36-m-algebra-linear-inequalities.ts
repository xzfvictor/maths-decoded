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
      id: 'solve',
      heading: 'Solving linear inequalities',
      summary: 'Solve like an equation, but flip the inequality if you divide by a negative.',
      body: `An **inequality** compares two expressions with $<$, $>$, $\\le$, $\\ge$. To solve, isolate the variable using inverse operations — almost the same as solving an equation, with one **critical rule**.

### The rule
If you multiply or divide both sides by a **negative** number, the inequality **flips**.

- $3x < 12$ → divide by $3$: $x < 4$.
- $-3x < 12$ → divide by $-3$ (and flip): $x > -4$.

### Multiplying by negatives
Same rule: $-2x > 6 \\Rightarrow x < -3$.`,
      examples: [
        {
          id: 'ex-positive-coeff',
          statement: 'Solve $4x - 5 < 11$.',
          steps: [
            'Add $5$: $4x < 16$.',
            'Divide by $4$ (positive, no flip): $x < 5$.',
          ],
        },
        {
          id: 'ex-negative-coeff',
          statement: 'Solve $-2x + 6 \\ge 10$.',
          steps: [
            'Subtract $6$: $-2x \\ge 4$.',
            'Divide by $-2$ (negative, **flip**): $x \\le -2$.',
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

    {
      id: 'graph',
      heading: 'Graphing on a number line',
      summary: 'Open or closed circle at the boundary; a ray extending in the solution direction.',
      body: `Once you've solved, draw the **solution set** on a number line.

### Open vs. closed circle
- $\\le$ or $\\ge$ → **closed** circle at the endpoint (the endpoint is included).
- $<$ or $>$ → **open** circle at the endpoint (the endpoint is NOT included).

### Direction of the ray
- $x < 5$ → open circle at $5$, ray extending to the **left**.
- $x \\ge -2$ → closed circle at $-2$, ray extending to the **right**.

### Why a ray?
The inequality defines an infinite set of $x$-values — every value past the boundary satisfies it.`,
      examples: [
        {
          id: 'ex-graph-1',
          statement: 'Describe the graph of $x \\le 3$.',
          steps: [
            'Closed circle at $x = 3$ (endpoint included).',
            'Ray extending to the left (every value less than $3$ is allowed).',
          ],
        },
        {
          id: 'ex-graph-2',
          statement: 'Describe the graph of $-2 < x \\le 4$.',
          steps: [
            'Open circle at $-2$, closed circle at $4$.',
            'Shade the segment between them — the **interval** $(-2, 4]$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-graph-direction',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $x > -1$, which way does the ray extend on a number line? Answer "left" or "right".',
            answer: 'right',
            answerType: 'exact',
            hint: 'Numbers greater than $-1$ lie to the right on a number line.',
            solution: [
              '$x > -1$ includes $-0.5, 0, 5, 100, \\dots$ — all to the right of $-1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-graph-open',
          difficulty: 'core',
          instance: {
            prompt:
              'For $x \\le 6$, is the circle at $6$ open or closed? Answer "open" or "closed".',
            answer: 'closed',
            answerType: 'exact',
            hint: '$\\le$ means the endpoint is included.',
            solution: [
              '$\\le$ includes the endpoint — draw a closed circle at $6$.',
            ],
          },
        },
      ],
    },
  ],
}