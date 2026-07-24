import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Measurement · VC2M10M01.
// Solve problems involving the surface area and volume of composite
// objects using appropriate units.

export const measurementAreaVolume: Topic = {
  id: 'm10-measurement-area-volume',
  unit: 10,
  order: 22,
  title: 'Surface area & volume of composite solids',
  blurb:
    'Break a composite solid into familiar shapes (prisms, cylinders), compute each part, then add or subtract.',
  dotPoints: ['m10-m-1'],

  lessons: [
    {
      id: 'volume',
      heading: 'Volume of composite solids',
      summary: 'Split the solid; compute the volume of each piece; add.',
      body: `A **composite solid** is two or more standard solids joined together. To find its **volume**, split it into familiar shapes, compute each, and add.

$$V_{\\text{total}} = V_1 + V_2 + \\dots$$

### Key formulas
- Right rectangular prism: $V = lwh$.
- Right circular cylinder: $V = \\pi r^2 h$.
- Cube: $V = s^3$.

### Subtracting
If the composite is a solid with a chunk removed, subtract: $V_{\\text{net}} = V_{\\text{whole}} - V_{\\text{cut}}$.`,
      examples: [
        {
          id: 'ex-cylinder-prism',
          statement:
            'A cylinder of radius $3$ cm and height $10$ cm sits on top of a $10 \\times 10 \\times 5$ cm rectangular prism. Find the total volume.',
          steps: [
            "Prism volume: $10 \\times 10 \\times 5 = 500$ cm³.",
            "Cylinder volume: $\\pi \\cdot 3^2 \\cdot 10 = 90\\pi \\approx 282.74$ cm³.",
            "Total: $500 + 90\\pi \\approx 783$ cm³.",
          ],
        },
        {
          id: 'ex-cube-minus',
          statement:
            'A cube of side $6$ cm has a $2 \\times 2 \\times 6$ cm slot removed. Find the remaining volume.',
          steps: [
            'Cube volume: $6^3 = 216$ cm³.',
            'Slot volume: $2 \\cdot 2 \\cdot 6 = 24$ cm³.',
            'Remaining: $216 - 24 = 192$ cm³.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-volume-cube',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the volume of a cube with side $5$ cm?',
            answer: '125',
            answerType: 'numeric',
            hint: '$V = s^3$.',
            solution: [
              '$V = 5^3 = 125$ cm³.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-volume-cylinder',
          difficulty: 'core',
          instance: {
            prompt:
              'A cylinder has radius $2$ m and height $5$ m. Find its volume (give as an integer; round).',
            answer: '63',
            answerType: 'numeric',
            hint: '$V = \\pi r^2 h$.',
            solution: [
              '$V = \\pi \\cdot 2^2 \\cdot 5 = 20\\pi \\approx 62.83$ m³.',
              'Rounded to nearest integer: $63$ m³.',
            ],
          },
        },
      ],
    },

    {
      id: 'surface-area',
      heading: 'Surface area of composite solids',
      summary: 'Count the exposed faces; subtract the parts hidden at the join.',
      body: `For **surface area**, count the visible faces — and remember to **subtract** the parts hidden at the join.

$$SA_{\\text{total}} = \\sum \\text{exposed face areas}.$$

### Key formulas
- Right rectangular prism: $SA = 2(lw + lh + wh)$.
- Right circular cylinder: $SA = 2\\pi r^2 + 2\\pi r h$ (two circles + lateral).
- Cube: $SA = 6 s^2$.

### Common mistake
Don't just add the surface areas of the parts — the **join faces** disappear from the exterior.`,
      examples: [
        {
          id: 'ex-surface',
          statement:
            'Find the surface area of a $4 \\times 4 \\times 4$ cm cube.',
          steps: [
            'Six identical faces, each $4 \\times 4 = 16$ cm².',
            "Total $SA = 6 \\cdot 16 = 96$ cm².",
          ],
        },
        {
          id: 'ex-cylinder-surface',
          statement:
            'A cylinder has radius $2$ cm and height $5$ cm. Find its surface area (round to nearest integer).',
          steps: [
            'Two circles: $2 \\cdot \\pi \\cdot 2^2 = 8\\pi$.',
            'Lateral: $2\\pi \\cdot 2 \\cdot 5 = 20\\pi$.',
            'Total: $28\\pi \\approx 87.96$, so $\\approx 88$ cm².',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-cube-sa',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the surface area of a cube with side $3$ cm.',
            answer: '54',
            answerType: 'numeric',
            hint: 'Six faces, each $3 \\times 3 = 9$ cm².',
            solution: [
              '$SA = 6 \\cdot 9 = 54$ cm².',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cylinder-sa',
          difficulty: 'core',
          instance: {
            prompt:
              'A cylinder has radius $1$ m and height $3$ m. Find its surface area (round to nearest integer).',
            answer: '25',
            answerType: 'numeric',
            hint: '$SA = 2\\pi r^2 + 2\\pi r h = 2\\pi(1 + 3) = 8\\pi$.',
            solution: [
              '$SA = 8\\pi \\approx 25.13$, so $\\approx 25$ m².',
            ],
          },
        },
      ],
    },
  ],
}