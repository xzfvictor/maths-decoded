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
      id: 'parallel-and-perp',
      heading: 'Parallel and perpendicular lines',
      summary: 'Equal gradients for parallel; gradients multiply to -1 for perpendicular.',
      body: `Two lines in the plane are related by their gradients. Knowing one line lets you write down any line that's parallel or perpendicular to it.

### Parallel lines
Two lines are **parallel** when they have the **same gradient** and different $y$-intercepts:
$$m_1 = m_2.$$

So a line parallel to $y = mx + c$ and through $(x_0, y_0)$ is:
$$y - y_0 = m(x - x_0).$$

### Perpendicular lines
Two lines are **perpendicular** when the product of their gradients is $-1$:
$$m_1 \\cdot m_2 = -1.$$

So the gradient of any line perpendicular to one with gradient $m$ is $-\\tfrac{1}{m}$ (the **negative reciprocal**).

### Worked example
A line has gradient $m = 3$.
- Parallel line: also has gradient $3$.
- Perpendicular line: gradient $= -\\tfrac{1}{3}$.`,
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
          id: 'ex-perp',
          statement:
            'A line has gradient $4$. What is the gradient of any line perpendicular to it?',
          steps: [
            'Perpendicular gradients multiply to $-1$: $4 \\cdot m = -1$.',
            '$m = -\\tfrac{1}{4}$.',
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
      ],
    },
  ],
}