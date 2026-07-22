import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Measurement · VC2M10M04.
// Use mathematical modelling to solve practical problems involving direct
// and inverse proportion and scaling of objects; formulate problems and
// interpret solutions in terms of the situation, including the impact of
// measurement errors on the accuracy of results.

export const measurementScaling: Topic = {
  id: 'm10-measurement-scaling',
  unit: 10,
  order: 24,
  title: 'Direct & inverse proportion, scaling, errors',
  blurb:
    'Set up $y = kx$ or $y = k/x$ from context; convert between scale drawings and real measurements; track how measurement errors propagate.',
  dotPoints: ['m10-m-4'],

  lessons: [
    {
      id: 'proportion-scale-error',
      heading: 'Direct proportion, scaling and error',
      summary: 'Find $k$ from one pair; use it for any other. Error propagates linearly in sums/products.',
      body: `### Direct proportion
Two quantities $y$ and $x$ are in **direct proportion** when $y = kx$ for some constant $k$:
$$k = \\frac{y}{x}.$$
Find $k$ from **one** known pair, then use $y = kx$ for any other.

### Inverse proportion
$y$ and $x$ are in **inverse proportion** when $y = \\dfrac{k}{x}$ — the product $xy$ is constant.

### Scaling
A scale of $1 : 50$ means every $1$ cm on the drawing is $50$ cm in real life. To convert:
- Real length = drawing length $\\times$ scale factor.
- Drawing length = real length $\\div$ scale factor.

### Measurement errors
Errors propagate:
- **Sum / difference**: errors add.
- **Product / quotient**: relative errors add.
Always report a result to the precision of the **least precise** measurement.`,
      examples: [
        {
          id: 'ex-direct-prop',
          statement:
            'A recipe for $4$ people uses $200$ g of flour. How much flour is needed for $7$ people (direct proportion)?',
          steps: [
            '$k = 200/4 = 50$ g per person.',
            '$7$ people: $7 \\times 50 = 350$ g.',
          ],
        },
        {
          id: 'ex-scale',
          statement:
            'A plan uses scale $1 : 100$. A wall is drawn as $5.3$ cm. How long is the wall in real life (in metres)?',
          steps: [
            'Real length $= 5.3 \\times 100 = 530$ cm $= 5.30$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-direct',
          difficulty: 'intro',
          instance: {
            prompt:
              'A car uses $8$ L of fuel to travel $100$ km. How many litres for $250$ km (direct proportion)?',
            answer: '20',
            answerType: 'numeric',
            hint: '$k = 8/100$ L/km.',
            solution: [
              '$k = 0.08$ L/km. $250 \\times 0.08 = 20$ L.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-scale',
          difficulty: 'core',
          instance: {
            prompt:
              'A plan uses scale $1 : 200$. A fence is drawn $7.4$ cm long. How long is the fence in real life (in metres)?',
            answer: '14.8',
            answerType: 'numeric',
            hint: 'Real length $= 7.4 \\times 200$ cm.',
            solution: [
              '$7.4 \\times 200 = 1480$ cm $= 14.8$ m.',
            ],
          },
        },
      ],
    },
  ],
}