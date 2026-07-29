import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Measurement · l9-m-1 (VC2M9M01).
// Volume and surface area of prisms and cylinders.

export const l9MPrismsCylinders: Topic = {
  id: 'l9-m-prisms-cylinders',
  unit: 9,
  order: 9,
  title: 'Volume and surface area of prisms and cylinders',
  blurb:
    'Solve problems involving the volume and surface area of right prisms, cylinders, and composite objects using appropriate units.',
  dotPoints: ['l9-m-1'],

  lessons: [
    {
      id: 'prism-cylinder-volume',
      heading: 'Volume of prisms & cylinders',
      summary: 'Area of cross-section times the length/height — works for any right prism or cylinder.',
      body: `A **right prism** is a solid whose cross-section stays the same along its length. A **right cylinder** is the same idea with a circular cross-section.

### The volume formula
For any right prism or right cylinder:
$$V = A_{\\text{cross-section}} \\times h,$$
where $A_{\\text{cross-section}}$ is the area of the shape cut perpendicular to the length, and $h$ is the length/height.

### Common cases
- Right rectangular prism: $V = l \\times w \\times h$.
- Right triangular prism: $V = \\tfrac{1}{2} b h_\\text{tri} \\times L$ (half the rectangle, times the length).
- Right circular cylinder: $V = \\pi r^2 h$.

### Choosing units
Volume is in **cubic** units. If lengths are in centimetres, volume is in cm³; if in metres, m³. Stay consistent.`,
      examples: [
        {
          id: 'ex-rect-prism',
          statement:
            'A rectangular tank is $40$ cm long, $25$ cm wide and $30$ cm tall. Find its volume in litres.',
          steps: [
            '$V = 40 \\times 25 \\times 30 = 30\\,000$ cm³.',
            '$1$ litre $= 1000$ cm³, so $V = 30$ L.',
          ],
        },
        {
          id: 'ex-cylinder',
          statement:
            'A cylindrical pipe has radius $5$ cm and length $2$ m. Find its volume in cm³ (round to nearest integer).',
          steps: [
            'Convert $2$ m $= 200$ cm.',
            '$V = \\pi \\times 5^2 \\times 200 = \\pi \\times 5000 \\approx 15\\,708$ cm³.',
          ],
        },
        {
          id: 'ex-triangular-prism',
          statement:
            'A triangular prism has a right-triangle cross-section with legs $6$ cm and $8$ cm, and length $50$ cm. Find its volume.',
          steps: [
            'Triangle area: $\\tfrac{1}{2} \\times 6 \\times 8 = 24$ cm².',
            'Prism volume: $24 \\times 50 = 1200$ cm³.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-rect-prism-vol',
          difficulty: 'intro',
          instance: {
            prompt:
              'A box is $20$ cm long, $10$ cm wide and $5$ cm tall. What is its volume? (Answer in cm³ as an integer.)',
            answer: '1000',
            answerType: 'numeric',
            hint: '$V = l \\times w \\times h$.',
            solution: [
              '$V = 20 \\times 10 \\times 5 = 1000$ cm³.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cylinder-vol',
          difficulty: 'core',
          instance: {
            prompt:
              'A cylinder has radius $3$ cm and height $10$ cm. Find its volume (round to nearest integer).',
            answer: '283',
            answerType: 'numeric',
            hint: '$V = \\pi r^2 h = \\pi \\times 9 \\times 10 = 90\\pi$.',
            solution: [
              '$V = 90\\pi \\approx 282.74$, rounds to $283$ cm³.',
            ],
          },
        },
      ],
    },

    {
      id: 'surface-area',
      heading: 'Surface area of prisms & cylinders',
      summary: 'Sum the area of every face; for cylinders, count two circles plus the curved side.',
      body: `**Surface area** is the total area of every face (or curved surface) on the outside of the solid.

### Right rectangular prism
$SA = 2(lw + lh + wh)$ — three pairs of identical faces.

### Right circular cylinder
$SA = 2\\pi r^2 + 2\\pi r h$ — two end-circles plus the curved lateral (unrolls to a rectangle $2\\pi r$ by $h$).

### Right triangular prism
Sum the two triangular ends and the three rectangles around the sides.

### Reading the units
Surface area is in **square** units (cm², m², ...). Make sure the formula uses the same length unit throughout.`,
      examples: [
        {
          id: 'ex-cylinder-sa',
          statement:
            'A cylinder has radius $4$ cm and height $12$ cm. Find its surface area (round to nearest integer).',
          steps: [
            'Two circles: $2 \\times \\pi \\times 4^2 = 32\\pi$.',
            'Curved side: $2\\pi \\times 4 \\times 12 = 96\\pi$.',
            'Total: $128\\pi \\approx 402.1$ cm², so about $402$ cm².',
          ],
        },
        {
          id: 'ex-prism-sa',
          statement:
            'A $5 \\times 4 \\times 3$ cm rectangular box. Find its surface area.',
          steps: [
            'Face pairs: $5 \\times 4 = 20$ (×2), $5 \\times 3 = 15$ (×2), $4 \\times 3 = 12$ (×2).',
            'Total: $2(20 + 15 + 12) = 2 \\times 47 = 94$ cm².',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cylinder-sa',
          difficulty: 'core',
          instance: {
            prompt:
              'A cylinder has radius $2$ m and height $6$ m. Find its surface area (round to nearest integer).',
            answer: '101',
            answerType: 'numeric',
            hint: '$SA = 2\\pi r^2 + 2\\pi r h = 2\\pi(4) + 2\\pi(12) = 8\\pi + 24\\pi = 32\\pi$.',
            solution: [
              '$SA = 32\\pi \\approx 100.53$, rounds to $101$ m².',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cube-sa',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the surface area of a cube with side $4$ cm.',
            answer: '96',
            answerType: 'numeric',
            hint: 'Six faces, each $4 \\times 4$.',
            solution: [
              'Six faces: $6 \\times 16 = 96$ cm².',
            ],
          },
        },
      ],
    },
  ],
}
