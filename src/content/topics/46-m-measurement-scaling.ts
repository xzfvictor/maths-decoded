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
      id: 'proportion',
      heading: 'Direct and inverse proportion',
      summary: 'Find k from one pair; use it for any other. For inverse, xy is constant.',
      body: `### Direct proportion
Two quantities $y$ and $x$ are in **direct proportion** when $y = kx$ for some constant $k$:
$$k = \\frac{y}{x}.$$
Find $k$ from **one** known pair, then use $y = kx$ for any other.

### Inverse proportion
$y$ and $x$ are in **inverse proportion** when $y = \\dfrac{k}{x}$ — the product $xy$ is constant.

### Reading the context
"More X, more Y" usually means direct. "More X, less Y" usually means inverse.`,
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
          id: 'ex-inverse-prop',
          statement:
            'It takes $4$ workers $6$ days to build a wall. How long for $8$ workers (inverse proportion)?',
          steps: [
            'Workers $\\cdot$ days $= 4 \\cdot 6 = 24$ (constant).',
            '$8 \\cdot d = 24 \\Rightarrow d = 3$ days.',
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
          id: 'c-inverse',
          difficulty: 'core',
          instance: {
            prompt:
              'It takes $3$ workers $10$ days to do a job. How many days for $6$ workers (inverse proportion)?',
            answer: '5',
            answerType: 'numeric',
            hint: 'Workers $\\cdot$ days $= 3 \\cdot 10 = 30$.',
            solution: [
              '$6 \\cdot d = 30 \\Rightarrow d = 5$ days.',
            ],
          },
        },
      ],
    },

    {
      id: 'scale',
      heading: 'Scale drawings',
      summary: 'Convert between drawing and real using the scale factor.',
      body: `A **scale** of $1 : n$ means every $1$ unit on the drawing represents $n$ units in real life.

### Converting
- **Real length** = drawing length $\\times$ scale factor.
- **Drawing length** = real length $\\div$ scale factor.

### Units
If the scale is in cm, both sides must be in cm first, then convert at the end.

### Areas and volumes
A scale factor of $k$ for **lengths** gives $k^2$ for **areas** and $k^3$ for **volumes**.`,
      examples: [
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
        {
          kind: 'curated',
          id: 'c-scale-2',
          difficulty: 'intro',
          instance: {
            prompt:
              'A plan uses scale $1 : 50$. A door is drawn $3.2$ cm wide. How wide is the door in real life (in metres)?',
            answer: '1.6',
            answerType: 'numeric',
            hint: 'Real length $= 3.2 \\times 50$ cm.',
            solution: [
              '$3.2 \\times 50 = 160$ cm $= 1.60$ m.',
            ],
          },
        },
      ],
    },

    {
      id: 'errors',
      heading: 'Measurement errors',
      summary: 'Errors add in sums/differences; relative errors add in products/quotients.',
      body: `Every measurement has some uncertainty. That uncertainty **propagates** through calculations.

### Sum / difference
Absolute errors add:
$$(a \\pm \\Delta a) + (b \\pm \\Delta b) = (a + b) \\pm (\\Delta a + \\Delta b).$$

### Product / quotient
**Relative** errors add:
$$\\frac{\\Delta(ab)}{ab} \\approx \\frac{\\Delta a}{a} + \\frac{\\Delta b}{b}.$$

### Rule of thumb
Report a result to the precision of the **least precise** measurement.`,
      examples: [
        {
          id: 'ex-sum',
          statement:
            'A board is $120 \\pm 1$ cm long, another is $85 \\pm 1$ cm long. Total length and its uncertainty?',
          steps: [
            'Total $= 120 + 85 = 205$ cm.',
            'Uncertainty $= 1 + 1 = 2$ cm.',
            'Result: $205 \\pm 2$ cm.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-error',
          difficulty: 'intro',
          instance: {
            prompt:
              'You measure $A = 10 \\pm 0.5$ and $B = 20 \\pm 0.5$. What is the uncertainty in $A + B$?',
            answer: '1',
            answerType: 'numeric',
            hint: 'Errors add in a sum.',
            solution: [
              '$0.5 + 0.5 = 1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-precision',
          difficulty: 'core',
          instance: {
            prompt:
              'You add $3.2$ m and $4.567$ m. To how many decimal places should you report the sum?',
            answer: '1',
            answerType: 'numeric',
            hint: 'Report to the precision of the least precise measurement.',
            solution: [
              '$3.2$ m is precise only to the tenths. So the sum is reported to $1$ decimal place: $7.8$ m.',
            ],
          },
        },
      ],
    },
  ],
}