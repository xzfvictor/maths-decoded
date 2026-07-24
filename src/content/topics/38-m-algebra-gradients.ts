import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A10.
// Solve problems involving gradients of parallel and perpendicular lines.

export const algebraGradients: Topic = {
  id: 'm10-algebra-gradients',
  unit: 10,
  order: 16,
  title: 'Parallel & perpendicular gradients',
  blurb:
    'Use gradient rules to find equations of parallel and perpendicular lines.',
  dotPoints: ['m10-a-10'],

  lessons: [
    {
      id: 'parallel',
      heading: 'Parallel lines',
      summary: 'Same gradient, different y-intercept. Equation via point-slope form.',
      body: `Two lines in the plane are **parallel** when they have the **same gradient** and different $y$-intercepts:
$$m_1 = m_2.$$

### Equation of a parallel line
A line parallel to $y = mx + c$ and passing through $(x_0, y_0)$ is:
$$y - y_0 = m(x - x_0).$$

### Reading from a graph
Two non-intersecting lines on a graph are parallel. The gradient of each line is the same; only the $y$-intercept differs.`,
      examples: [
        {
          id: 'ex-parallel',
          statement:
            'Write the equation of a line parallel to $y = 2x + 5$ through $(1, 7)$.',
          steps: [
            'Parallel: same gradient $m = 2$.',
            'Point-slope: $y - 7 = 2(x - 1) \\Rightarrow y = 2x + 5$.',
          ],
        },
        {
          id: 'ex-parallel-2',
          statement:
            'Write the equation of a line parallel to $y = 3x - 1$ through $(0, 4)$.',
          steps: [
            'Same gradient $m = 3$.',
            '$y - 4 = 3(x - 0) \\Rightarrow y = 3x + 4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-parallel-check',
          difficulty: 'core',
          instance: {
            prompt:
              'Are the lines $y = 3x + 1$ and $y = 3x - 4$ parallel? Answer "yes" or "no".',
            answer: 'yes',
            answerType: 'exact',
            hint: 'Same gradient, different intercepts.',
            solution: [
              'Both have gradient $3$ but different $y$-intercepts → parallel.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-parallel-eq',
          difficulty: 'intro',
          instance: {
            prompt:
              'A line parallel to $y = -2x + 5$ passes through $(0, 7)$. What is its $y$-intercept?',
            answer: '7',
            answerType: 'numeric',
            hint: 'Same gradient $-2$, but it must pass through $(0, 7)$.',
            solution: [
              'The line has gradient $-2$ and at $x = 0$ gives $y = 7$. So $y$-intercept $= 7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'perpendicular',
      heading: 'Perpendicular lines',
      summary: 'Gradients multiply to -1; the perpendicular to m is -1/m.',
      body: `Two lines are **perpendicular** when the product of their gradients is $-1$:
$$m_1 \\cdot m_2 = -1.$$

So the gradient of any line perpendicular to one with gradient $m$ is $-\\tfrac{1}{m}$ (the **negative reciprocal**).

### Reading from a graph
Two perpendicular lines meet at a right angle. If you know one gradient, the other is forced.

### Quick check
- $m = 1$ → perpendicular gradient $-1$.
- $m = 2$ → perpendicular gradient $-\\tfrac{1}{2}$.
- $m = -\\tfrac{1}{3}$ → perpendicular gradient $3$.`,
      examples: [
        {
          id: 'ex-perp',
          statement:
            'A line has gradient $4$. What is the gradient of any line perpendicular to it?',
          steps: [
            'Perpendicular gradients multiply to $-1$: $4 \\cdot m = -1$.',
            '$m = -\\tfrac{1}{4}$.',
          ],
        },
        {
          id: 'ex-perp-eq',
          statement:
            'A line perpendicular to $y = \\tfrac{1}{2}x + 3$ passes through $(0, 5)$. Write its equation.',
          steps: [
            'Perpendicular gradient: $-2$.',
            '$y - 5 = -2(x - 0) \\Rightarrow y = -2x + 5$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-perp-gradient',
          difficulty: 'intro',
          instance: {
            prompt:
              'A line has gradient $5$. What is the gradient of any line perpendicular to it? (As a fraction in lowest terms.)',
            answer: '-1/5',
            answerType: 'numeric',
            hint: 'Product of gradients $= -1$.',
            solution: [
              '$m = -\\tfrac{1}{5}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-perp-grad-2',
          difficulty: 'core',
          instance: {
            prompt:
              'A line has gradient $-\\tfrac{1}{3}$. What is the gradient of any line perpendicular to it? (As an integer.)',
            answer: '3',
            answerType: 'numeric',
            hint: 'Product of gradients $= -1$.',
            solution: [
              '$-\\tfrac{1}{3} \\cdot m = -1 \\Rightarrow m = 3$.',
            ],
          },
        },
      ],
    },
  ],
}