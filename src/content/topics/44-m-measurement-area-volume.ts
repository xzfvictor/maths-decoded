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
      id: 'composite-solids',
      heading: 'Surface area & volume of composite solids',
      summary: 'Split the solid; compute the area or volume of each piece; combine.',
      body: `A **composite solid** is two or more standard solids joined together. To find its **volume**, split it into familiar shapes, compute each, and add. For **surface area**, count the visible faces — and remember to **subtract** the parts hidden at the join.

### Key formulas to remember
- Right rectangular prism: $V = lwh$, $SA = 2(lw + lh + wh)$.
- Right circular cylinder: $V = \\pi r^2 h$, $SA = 2\\pi r^2 + 2\\pi r h$ (two circles + lateral).

### Volume of composite solids
$$V_{\\text{total}} = V_1 + V_2 + \\dots$$

### Surface area of composite solids
Compute the **exposed** area of each face separately:
$$SA_{\\text{total}} = \\sum \\text{exposed face areas}.$$
Faces touching the join are **not** part of the exterior.`,
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
          id: 'ex-surface',
          statement:
            'Find the surface area of a $4 \\times 4 \\times 4$ cm cube.',
          steps: [
            'Six identical faces, each $4 \\times 4 = 16$ cm².',
            "Total $SA = 6 \\cdot 16 = 96$ cm².",
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
  ],
}