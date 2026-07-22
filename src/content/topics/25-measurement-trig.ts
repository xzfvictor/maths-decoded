import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Measurement · VC2M10M03.
// Solve practical problems by applying Pythagoras' theorem and trigonometry
// to right-angled triangles, including problems involving direction and
// angles of elevation and depression.

export const measurementTrig: Topic = {
  id: 'm10-measurement-trig',
  unit: 10,
  order: 3,
  title: 'Pythagoras & right-angled trigonometry',
  blurb:
    'Apply $a^2 + b^2 = c^2$ and the sine/cosine/tangent ratios to real-world bearing, elevation and depression problems.',
  dotPoints: ['m10-m-3'],

  lessons: [
    {
      id: 'pythagoras-and-trig',
      heading: 'Pythagoras and the sine / cosine / tangent ratios',
      summary: 'The three essential formulas for any right triangle problem.',
      body: `For a right-angled triangle with the right angle opposite the **hypotenuse** $c$, and the other two sides labelled $a, b$ (with angle $\\theta$ between $a$ and $c$):

### Pythagoras' theorem
$$a^2 + b^2 = c^2.$$
Given any two sides, you can find the third.

### Trigonometric ratios
Choose the ratio that pairs the **given** side with the **asked** side:

| You know | You want | Use |
|---|---|---|
| Adjacent | Opposite | $\\tan\\theta = \\dfrac{\\text{opposite}}{\\text{adjacent}}$ |
| Hypotenuse | Opposite | $\\sin\\theta = \\dfrac{\\text{opposite}}{\\text{hypotenuse}}$ |
| Hypotenuse | Adjacent | $\\cos\\theta = \\dfrac{\\text{adjacent}}{\\text{hypotenuse}}$ |

### Bearings, elevation, depression
- A **bearing** is measured clockwise from North, written as three digits (e.g. $075°$).
- **Angle of elevation** is measured *up* from the horizontal.
- **Angle of depression** is measured *down* from the horizontal (from the observer's eye line).

The angle of depression from $A$ to $B$ equals the angle of elevation from $B$ to $A$ (alternate angles with the horizontal).`,
      examples: [
        {
          id: 'ex-pythagoras',
          statement:
            'A ladder of length $4$ m leans against a wall. Its base is $1.5$ m from the wall. How high up the wall does the ladder reach?',
          steps: [
            'Right triangle: hypotenuse $4$, base $1.5$, height $h$.',
            'Pythagoras: $1.5^2 + h^2 = 4^2 \\Rightarrow 2.25 + h^2 = 16$.',
            '$h^2 = 13.75 \\Rightarrow h = \\sqrt{13.75} \\approx 3.71$ m.',
          ],
        },
        {
          id: 'ex-elevation',
          statement:
            'From a point $30$ m from the base of a tower, the angle of elevation to the top is $40°$. How tall is the tower?',
          steps: [
            'Right triangle: adjacent $= 30$ m, angle $= 40°$, opposite $= h$.',
            'Use $\\tan$: $\\tan 40° = \\dfrac{h}{30}$.',
            '$h = 30 \\tan 40° \\approx 30 \\times 0.839 \\approx 25.2$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pythagoras-3-4',
          difficulty: 'intro',
          instance: {
            prompt:
              'A right triangle has legs $3$ m and $4$ m. What is the hypotenuse? (Answer as a number.)',
            answer: '5',
            answerType: 'numeric',
            hint: 'Pythagoras: $c = \\sqrt{3^2 + 4^2}$.',
            solution: [
              '$c = \\sqrt{9 + 16} = \\sqrt{25} = 5$ m.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-trig-sin',
          difficulty: 'core',
          instance: {
            prompt:
              'In a right triangle, the hypotenuse is $10$ and the angle $\\theta$ opposite a side of length $6$ is unknown. Use $\\sin\\theta = \\dfrac{6}{10}$ to find $\\sin\\theta$ as a decimal.',
            answer: '0.6',
            answerType: 'numeric',
            hint: 'Compute the ratio.',
            solution: [
              '$\\sin\\theta = 6 / 10 = 0.6$.',
            ],
          },
        },
      ],
    },
  ],
}