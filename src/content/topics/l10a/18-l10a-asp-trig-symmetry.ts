import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Space · l10a-asp-3 (VC2M10ASP03).
// Symmetry and periodicity of trigonometric functions.

export const l10aAspTrigSymmetry: Topic = {
  id: 'l10a-asp-trig-symmetry',
  unit: '10A',
  order: 18,
  title: 'Symmetry and periodicity of trig functions',
  blurb:
    'Establish the symmetrical properties of trigonometric functions, investigate angles of any magnitude, and identify points on the unit circle via arc lengths in radians.',
  dotPoints: ['l10a-asp-3'],

  lessons: [
    {
      id: 'unit-circle-radians',
      heading: 'Unit circle & radians',
      summary: 'Wrap a number line around the circle: angle in radians = arc length on a unit circle.',
      body: `A **radian** is a way of measuring angle by *arc length* on a unit circle (radius $1$).

### Definition
For an angle $\\theta$ at the centre of a unit circle, the arc length from the positive $x$-axis to the second arm is exactly $\\theta$ radians.

### Key conversions
- One full turn $= 2\\pi$ radians $= 360°$.
- $\\pi$ radians $= 180°$.
- 1 radian $\\approx 57.3°$.

### Reading coordinates
On the unit circle, the point reached by rotating $\\theta$ radians anticlockwise from $(1, 0)$ is $(\\cos \\theta, \\sin \\theta)$.

### Quadrant signs
| Quadrant | $\\sin$ | $\\cos$ |
|---|---|---|
| I   | $+$ | $+$ |
| II  | $+$ | $-$ |
| III | $-$ | $-$ |
| IV  | $-$ | $+$ |

These signs come from the coordinates of $(\\cos \\theta, \\sin \\theta)$ in each quadrant.`,
      examples: [
        {
          id: 'ex-radian-conversion',
          statement:
            'Convert $45°$ to radians. (Answer as a multiple of $\\pi$ using "pi".)',
          steps: [
            '$\\pi$ rad $= 180°$, so divide by $180$.',
            '$45° = \\dfrac{45}{180} \\pi = \\dfrac{1}{4} \\pi$ rad.',
          ],
        },
        {
          id: 'ex-coords-on-circle',
          statement:
            'What are the coordinates on the unit circle at $\\theta = \\pi$?',
          steps: [
            'Anticlockwise half turn from $(1, 0)$.',
            'Lands at $(-1, 0)$.',
            'Check: $\\cos \\pi = -1$, $\\sin \\pi = 0$.',
          ],
        },
        {
          id: 'ex-quadrant-sign',
          statement:
            '$\\theta$ is in quadrant III. Is $\\sin \\theta$ positive or negative?',
          steps: [
            'In Q3 both $\\sin$ and $\\cos$ are negative.',
            '$\\sin \\theta$ is **negative**.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-radian-conv',
          difficulty: 'intro',
          instance: {
            prompt:
              'Convert $60°$ to radians. (Answer as a fraction of pi, e.g. "pi/3".)',
            answer: 'pi/3',
            answerType: 'exact',
            hint: 'Divide the degree measure by $180$.',
            solution: [
              '$60° = \\dfrac{60}{180} \\pi = \\dfrac{1}{3} \\pi$ rad.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-coords-pi-over-2',
          difficulty: 'core',
          instance: {
            prompt:
              'What is $\\cos\\left(\\dfrac{\\pi}{2}\\right)$? Answer as a number.',
            answer: '0',
            answerType: 'numeric',
            hint: 'At $\\pi/2$ the point on the unit circle is $(0, 1)$.',
            solution: [
              'At $\\theta = \\pi/2$ the unit circle reaches $(0, 1)$, so $\\cos(\\pi/2) = 0$.',
            ],
          },
        },
      ],
    },

    {
      id: 'symmetry-periodicity',
      heading: 'Symmetry & periodicity',
      summary: 'Identities like $\\sin(\\pi - x) = \\sin x$, and the period $2\\pi$ for sine and cosine.',
      body: `Trigonometric functions are predictable because they have **symmetry** and **periodicity**.

### Periodicity
$$\\sin(\\theta + 2\\pi) = \\sin \\theta, \\quad \\cos(\\theta + 2\\pi) = \\cos \\theta$$
So sine and cosine repeat every $2\\pi$ radians (every $360°$).

### Even and odd
- $\\cos$ is **even**: $\\cos(-\\theta) = \\cos \\theta$ (symmetric about the $y$-axis).
- $\\sin$ is **odd**: $\\sin(-\\theta) = -\\sin \\theta$ (symmetric about the origin).

### Supplementary / complementary identities
$$\\sin(\\pi - \\theta) = \\sin \\theta \\quad \\text{(Q1 = Q2)}$$
$$\\cos(\\pi - \\theta) = -\\cos \\theta \\quad \\text{(Q1 vs Q2 sign flip)}$$
$$\\sin(\\pi + \\theta) = -\\sin \\theta, \\quad \\cos(\\pi + \\theta) = -\\cos \\theta$$

### Why these matter
They let you **reduce** any angle to one in $[0, \\pi/2]$ and read off its value. The unit circle is the picture: the $(x, y)$ coordinates are $(\\cos, \\sin)$ for any angle.`,
      examples: [
        {
          id: 'ex-even-odd',
          statement:
            'Use $\\sin(-x) = -\\sin x$ to find $\\sin(-\\dfrac{\\pi}{6})$.',
          steps: [
            '$\\sin(-\\tfrac{\\pi}{6}) = -\\sin(\\tfrac{\\pi}{6}) = -\\tfrac{1}{2}$.',
          ],
        },
        {
          id: 'ex-supplementary',
          statement:
            'Find $\\sin\\left(\\dfrac{2\\pi}{3}\\right)$.',
          steps: [
            '$\\dfrac{2\\pi}{3} = \\pi - \\tfrac{\\pi}{3}$.',
            '$\\sin(\\pi - x) = \\sin x$, so $\\sin\\left(\\dfrac{2\\pi}{3}\\right) = \\sin\\left(\\tfrac{\\pi}{3}\\right) = \\dfrac{\\sqrt{3}}{2}$.',
          ],
        },
        {
          id: 'ex-period',
          statement:
            'Find $\\cos\\left(\\dfrac{9\\pi}{4}\\right)$.',
          steps: [
            '$\\dfrac{9\\pi}{4} = 2\\pi + \\dfrac{\\pi}{4}$.',
            '$\\cos(2\\pi + x) = \\cos x$.',
            '$\\cos\\left(\\dfrac{9\\pi}{4}\\right) = \\cos\\left(\\dfrac{\\pi}{4}\\right) = \\dfrac{\\sqrt{2}}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-even',
          difficulty: 'intro',
          instance: {
            prompt:
              'Use the even property of cosine to find $\\cos\\left(-\\dfrac{\\pi}{4}\\right)$. Answer as a decimal (2 dp).',
            answer: '0.71',
            answerType: 'numeric',
            hint: '$\\cos(-x) = \\cos x$.',
            solution: [
              '$\\cos(-\\tfrac{\\pi}{4}) = \\cos(\\tfrac{\\pi}{4}) = \\tfrac{\\sqrt{2}}{2} \\approx 0.71$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-supplementary-sin',
          difficulty: 'core',
          instance: {
            prompt:
              'Find $\\sin\\left(\\dfrac{3\\pi}{4}\\right)$. Answer as a decimal (2 dp).',
            answer: '0.71',
            answerType: 'numeric',
            hint: '$\\tfrac{3\\pi}{4} = \\pi - \\tfrac{\\pi}{4}$.',
            solution: [
              '$\\sin(\\tfrac{3\\pi}{4}) = \\sin(\\pi - \\tfrac{\\pi}{4}) = \\sin(\\tfrac{\\pi}{4}) = \\tfrac{\\sqrt{2}}{2} \\approx 0.71$.',
            ],
          },
        },
      ],
    },
  ],
}