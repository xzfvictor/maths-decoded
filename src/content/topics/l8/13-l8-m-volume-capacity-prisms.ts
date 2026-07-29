import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Measurement · l8-m-2 (VC2M8M02).
// Solve problems involving the volume and capacity of right prisms using
// appropriate units.

export const l8MVolumeCapacityPrisms: Topic = {
  id: 'l8-m-volume-capacity-prisms',
  unit: 8,
  order: 13,
  title: 'Volume and capacity of right prisms',
  blurb:
    'Solve problems involving the volume and capacity of right prisms using appropriate units.',
  dotPoints: ['l8-m-2'],

  lessons: [
    {
      id: 'right-prisms',
      heading: 'Volume of right prisms',
      summary: 'Volume = area of cross-section × length; pick the right cross-section for the prism.',
      body: `A **right prism** is a solid whose cross-section is the same shape all the way along its length. Imagine pushing the same flat shape along a straight line — that is a right prism.

### The volume formula
For any right prism:
$$V = A \\times l,$$
where $A$ is the area of the cross-section and $l$ is the length (the distance the cross-section travels).

### Common cross-sections
- **Rectangular prism**: $A = w \\times h$, so $V = w \\times h \\times l$.
- **Triangular prism**: $A = \\dfrac{1}{2} b h$, so $V = \\dfrac{1}{2} b h \\times l$.
- **Trapezoidal prism**: $A = \\dfrac{1}{2}(a + b) h$, so $V = \\dfrac{1}{2}(a + b) h \\times l$.

### Capacity vs volume
- **Volume** is how much 3D space the solid takes up — measured in cubic units (cm³, m³).
- **Capacity** is how much a container can hold — measured in litres (L) or millilitres (mL).
- The link: $1\\text{ mL} = 1\\text{ cm}^3$, and $1\\text{ L} = 1000\\text{ cm}^3$. So a $500$ cm³ container holds $500$ mL $= 0.5$ L.`,
      examples: [
        {
          id: 'ex-triangular-prism',
          statement:
            'A triangular prism has a right-triangular cross-section with base $6$ cm and height $4$ cm. The prism is $10$ cm long. Find its volume.',
          steps: [
            'Cross-section area: $A = \\dfrac{1}{2} \\times 6 \\times 4 = 12$ cm².',
            'Volume: $V = A \\times l = 12 \\times 10 = 120$ cm³.',
          ],
        },
        {
          id: 'ex-trapezoidal-prism',
          statement:
            'A trough has a trapezoidal cross-section with parallel sides $20$ cm and $30$ cm and height $15$ cm. It is $80$ cm long. Find its capacity in litres.',
          steps: [
            'Cross-section area: $A = \\dfrac{1}{2}(20 + 30) \\times 15 = 25 \\times 15 = 375$ cm².',
            'Volume: $V = 375 \\times 80 = 30{,}000$ cm³.',
            'Capacity: $30{,}000$ cm³ $= 30{,}000$ mL $= 30$ L.',
          ],
        },
        {
          id: 'ex-rectangular-capacity',
          statement:
            'A fish tank is $40$ cm long, $25$ cm wide and $30$ cm tall. Find its capacity in litres.',
          steps: [
            'Volume: $V = 40 \\times 25 \\times 30 = 30{,}000$ cm³.',
            'Capacity: $30{,}000$ mL $= 30$ L.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-volume-rect-prism',
          difficulty: 'intro',
          instance: {
            prompt:
              'A rectangular prism is $8$ cm long, $5$ cm wide and $3$ cm tall. What is its volume in cm³?',
            answer: '120',
            answerType: 'numeric',
            hint: '$V = l \\times w \\times h$.',
            solution: [
              '$V = 8 \\times 5 \\times 3 = 120$ cm³.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-capacity',
          difficulty: 'core',
          instance: {
            prompt:
              'A cube-shaped box has sides of $10$ cm. What is its capacity in millilitres?',
            answer: '1000',
            answerType: 'numeric',
            hint: '$V = 10^3$ cm³ and $1$ cm³ $= 1$ mL.',
            solution: [
              '$V = 10^3 = 1000$ cm³ $= 1000$ mL.',
            ],
          },
        },
      ],
    },
  ],
}