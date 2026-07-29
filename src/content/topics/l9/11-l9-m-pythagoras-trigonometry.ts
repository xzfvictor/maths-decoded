import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Measurement · l9-m-3 (VC2M9M03).
// Pythagoras and trigonometry.

export const l9MPythagorasTrigonometry: Topic = {
  id: 'l9-m-pythagoras-trigonometry',
  unit: 9,
  order: 11,
  title: 'Pythagoras and trigonometry',
  blurb:
    'Solve spatial problems by applying angle properties, scale, similarity, ratio, Pythagoras\' theorem, and trigonometry in right-angled triangles.',
  dotPoints: ['l9-m-3'],

  lessons: [
    {
      id: 'pythagoras',
      heading: 'Pythagoras\' theorem in spatial problems',
      summary: 'In a right triangle the square on the hypotenuse equals the sum of the squares on the other two sides.',
      body: `Pythagoras' theorem links the three sides of a **right-angled triangle**. Label the side opposite the right angle the **hypotenuse** $c$, and the other two sides $a$ and $b$:
$$a^2 + b^2 = c^2.$$

### Using it
- Given any two sides, you can find the third.
- Take the square root to recover a length: $c = \\sqrt{a^2 + b^2}$ (or $a = \\sqrt{c^2 - b^2}$).

### Spatial contexts
Pythagoras shows up whenever a right angle is hiding — diagonals across rectangles, slants on ramps, gaps between points on a grid.`,
      examples: [
        {
          id: 'ex-diagonal',
          statement:
            'A rectangular field is $80$ m by $150$ m. How long is the diagonal path across it (nearest metre)?',
          steps: [
            '$d^2 = 80^2 + 150^2 = 6400 + 22\\,500 = 28\\,900$.',
            '$d = \\sqrt{28\\,900} = 170$ m.',
          ],
        },
        {
          id: 'ex-ramp',
          statement:
            'A ramp $5$ m long reaches a platform $1.2$ m above the ground. How far from the platform is the base of the ramp?',
          steps: [
            'Right triangle: hypotenuse $5$, vertical $1.2$, horizontal $h$.',
            '$h^2 = 5^2 - 1.2^2 = 25 - 1.44 = 23.56$.',
            '$h = \\sqrt{23.56} \\approx 4.85$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pythag-3-4-5',
          difficulty: 'intro',
          instance: {
            prompt:
              'A right triangle has legs $6$ m and $8$ m. What is the hypotenuse? (As a number.)',
            answer: '10',
            answerType: 'numeric',
            hint: '$c = \\sqrt{6^2 + 8^2}$.',
            solution: [
              '$c = \\sqrt{36 + 64} = \\sqrt{100} = 10$ m.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-pythag-unk-leg',
          difficulty: 'core',
          instance: {
            prompt:
              'A right triangle has hypotenuse $13$ and one leg $5$. What is the other leg?',
            answer: '12',
            answerType: 'numeric',
            hint: '$b^2 = 13^2 - 5^2$.',
            solution: [
              '$b^2 = 169 - 25 = 144$, so $b = 12$.',
            ],
          },
        },
      ],
    },

    {
      id: 'trig-ratios',
      heading: 'Trigonometric ratios in right-angled triangles',
      summary: 'sin, cos, tan pair the sides of a right triangle with an acute angle; pick the one that matches the sides you have.',
      body: `For a right-angled triangle, label the sides relative to a chosen acute angle $\\theta$:
- **Hypotenuse** — the side opposite the right angle (longest).
- **Opposite** — the side opposite the angle $\\theta$.
- **Adjacent** — the side next to $\\theta$ (not the hypotenuse).

### The three ratios
$$\\sin\\theta = \\frac{\\text{opposite}}{\\text{hypotenuse}}, \\quad \\cos\\theta = \\frac{\\text{adjacent}}{\\text{hypotenuse}}, \\quad \\tan\\theta = \\frac{\\text{opposite}}{\\text{adjacent}}.$$

### Solving a problem
1. Mark the right angle and the angle you know.
2. Decide which two sides are involved (the **given** side and the **unknown** side).
3. Pick the ratio that has both. Use a calculator to evaluate.`,
      examples: [
        {
          id: 'ex-trig-side',
          statement:
            'In a right triangle, the angle is $30°$, the hypotenuse is $10$ m. How long is the side opposite the angle (nearest metre)?',
          steps: [
            '$\\sin 30° = \\dfrac{\\text{opposite}}{10}$.',
            '$\\text{opposite} = 10 \\times \\sin 30° = 10 \\times 0.5 = 5$ m.',
          ],
        },
        {
          id: 'ex-trig-angle',
          statement:
            'A right triangle has opposite $7$ m and adjacent $9$ m. Find the angle (nearest degree).',
          steps: [
            '$\\tan\\theta = \\dfrac{7}{9}$.',
            '$\\theta = \\tan^{-1}(7/9) \\approx 37.87°$, about $38°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-trig-side',
          difficulty: 'core',
          instance: {
            prompt:
              'A right triangle has angle $60°$ and hypotenuse $20$ cm. How long is the side opposite the angle (nearest cm)?',
            answer: '17',
            answerType: 'numeric',
            hint: '$\\sin 60° \\approx 0.866$.',
            solution: [
              '$\\text{opposite} = 20 \\times \\sin 60° \\approx 20 \\times 0.866 = 17.32$, about $17$ cm.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-trig-choose',
          difficulty: 'intro',
          instance: {
            prompt:
              'You know the opposite side and want to find the adjacent side. Which ratio do you start with? (Answer "sin", "cos", or "tan".)',
            answer: 'tan',
            answerType: 'exact',
            hint: 'Opposite and adjacent together form the tangent.',
            solution: [
              '$\\tan\\theta = \\dfrac{\\text{opposite}}{\\text{adjacent}}$, so the answer is tan.',
            ],
          },
        },
      ],
    },
  ],
}
