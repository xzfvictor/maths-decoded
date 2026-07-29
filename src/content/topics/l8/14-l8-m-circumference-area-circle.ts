import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Measurement · l8-m-3 (VC2M8M03).
// Solve problems involving the circumference and area of a circle using
// formulas and appropriate units.

export const l8MCircumferenceAreaCircle: Topic = {
  id: 'l8-m-circumference-area-circle',
  unit: 8,
  order: 14,
  title: 'Circumference and area of a circle',
  blurb:
    'Solve problems involving the circumference and area of a circle using formulas and appropriate units.',
  dotPoints: ['l8-m-3'],

  lessons: [
    {
      id: 'circle-formulas',
      heading: 'Circumference and area',
      summary: 'Use C = 2πr and A = πr²; convert between radius and diameter.',
      body: `A circle has two key measurements:
- **Radius** $r$ — distance from the centre to the edge.
- **Diameter** $d$ — distance across the circle through the centre. The diameter is twice the radius: $d = 2r$.

The **circumference** $C$ is the distance around the outside of the circle.

### The two formulas
$$C = 2 \\pi r = \\pi d$$
$$A = \\pi r^2$$

> [!warning] Watch out
> The area uses $r^2$, not $r$. If the question gives the **diameter**, halve it before squaring. Squaring the diameter gives an answer that is $4$ times too big.

### Approximating $\pi$
Use $\\pi \\approx 3.14159\\ldots$ for calculations. Many problems ask for an answer rounded to a whole number or to one or two decimal places — keep $\\pi$ in the calculator's full precision until the very end.

### Choosing units
- Circumference is a length: cm, m, km.
- Area is two-dimensional: cm², m², km².`,
      examples: [
        {
          id: 'ex-circumference',
          statement:
            'A circular pond has radius $5$ m. Find its circumference (round to two decimal places).',
          steps: [
            '$C = 2 \\pi r = 2 \\times \\pi \\times 5 = 10 \\pi$ m.',
            '$10 \\pi \\approx 31.42$ m.',
          ],
        },
        {
          id: 'ex-area-diameter',
          statement:
            'A circular plate has diameter $14$ cm. Find its area (round to two decimal places).',
          steps: [
            'Radius $= 14 / 2 = 7$ cm.',
            '$A = \\pi r^2 = \\pi \\times 7^2 = 49\\pi$ cm².',
            '$49 \\pi \\approx 153.94$ cm².',
          ],
        },
        {
          id: 'ex-half-circle',
          statement:
            'A semicircle has radius $6$ cm. Find its perimeter (the curved half plus the diameter).',
          steps: [
            'Curved half: $\\dfrac{1}{2} \\times 2 \\pi r = \\pi r = 6\\pi$ cm.',
            'Diameter: $2r = 12$ cm.',
            'Total perimeter: $6\\pi + 12 \\approx 18.85 + 12 = 30.85$ cm.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-circumference',
          difficulty: 'intro',
          instance: {
            prompt:
              'A circle has radius $4$ m. Find its circumference as an exact multiple of $\\pi$ (just write the number in front of $\\pi$, e.g. "12").',
            answer: '8',
            answerType: 'numeric',
            hint: '$C = 2 \\pi r$.',
            solution: [
              '$C = 2 \\times \\pi \\times 4 = 8\\pi$ m.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-area',
          difficulty: 'core',
          instance: {
            prompt:
              'A circle has radius $3$ cm. Find its area as an exact multiple of $\\pi$ (just write the number in front of $\\pi$).',
            answer: '9',
            answerType: 'numeric',
            hint: '$A = \\pi r^2$.',
            solution: [
              '$A = \\pi \\times 3^2 = 9\\pi$ cm².',
            ],
          },
        },
      ],
    },
  ],
}