import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Measurement · l7-m-2 (VC2M7M02).
// Solve problems involving the volume of right prisms including rectangular
// and triangular prisms, using established formulas and appropriate units.

export const l7MVolumePrisms: Topic = {
  id: 'l7-m-volume-prisms',
  unit: 7,
  order: 18,
  title: 'Volume of right prisms',
  blurb:
    'Solve problems involving the volume of right prisms, including rectangular and triangular prisms, using formulas and appropriate units.',
  dotPoints: ['l7-m-2'],
  lessons: [
    {
      id: 'volume-meaning',
      heading: 'What volume means',
      summary:
        'Volume counts the cubes that fit inside a 3D solid — measured in cubic units.',
      body: `If **area** is how much flat surface a shape covers, **volume** is how much space a 3D object occupies. It is measured in **cubic units**: cm³, m³, etc.

### Counting cubes
Imagine a small cube that is $1$ cm on every side. Stack these unit cubes inside a solid and count them — that count is the volume.

- A cube that is $3$ cm on each side holds $3 \times 3 \times 3 = 27$ unit cubes. So $V = 3^3 = 27$ cm³.
- A $4 \times 2 \times 5$ cm box holds $4 \times 2 \times 5 = 40$ unit cubes. So $V = 40$ cm³.

### The general rectangle-box rule
A **rectangular prism** (a box) with length $l$, width $w$ and height $h$ has volume

$$V = l \times w \times h.$$

> [!warning] Same unit on every side
> All three measurements must be in the **same unit** before you multiply. Convert first if needed.

### Capacity vs volume
A container's **volume** is the amount of 3D space inside it, while its **capacity** is how much liquid it can hold (often in litres or millilitres). For a closed box, these are the same number in different units.`,
      examples: [
        {
          id: 'ex-box-volume',
          statement:
            'A shoebox is $30$ cm long, $15$ cm wide and $12$ cm tall. Find its volume.',
          steps: [
            'Same unit on every side (cm).',
            '$V = 30 \\times 15 \\times 12$.',
            '$30 \\times 15 = 450$; $450 \\times 12 = 5400$.',
            'Volume: $5400$ cm³.',
          ],
        },
        {
          id: 'ex-cube-volume',
          statement:
            'A cube has side $6$ cm. Find its volume.',
          steps: [
            'A cube is a rectangular prism with $l = w = h = 6$.',
            '$V = 6 \\times 6 \\times 6 = 216$.',
            'Volume: $216$ cm³.',
          ],
        },
        {
          id: 'ex-mixed-units',
          statement:
            'A tank is $2$ m long, $50$ cm wide and $40$ cm deep. Find its volume in cm³.',
          steps: [
            'Convert: $2$ m $= 200$ cm.',
            '$V = 200 \\times 50 \\times 40$.',
            '$200 \\times 50 = 10000$; $10000 \\times 40 = 400000$.',
            'Volume: $400\\,000$ cm³.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-box-volume',
          difficulty: 'intro',
          instance: {
            prompt:
              'A box is $10$ cm long, $4$ cm wide and $5$ cm tall. What is its volume (in cm³)?',
            answer: '200',
            answerType: 'numeric',
            hint: 'Multiply length, width and height together.',
            solution: [
              '$V = 10 \\times 4 \\times 5 = 200$ cm³.',
            ],
          },
        },
      ],
    },
    {
      id: 'right-prism-formula',
      heading: 'Volume of any right prism',
      summary:
        'Area of cross-section × perpendicular height — the same formula for every right prism.',
      body: `A **right prism** is a 3D solid whose cross-section stays the same shape all the way along, and whose sides are **perpendicular** to that cross-section. A box of cereal is a right prism; a Toblerone is a right triangular prism.

### The general formula
Stack cross-sections from one end to the other. Each cross-section has the same area, say $A$, and there are $h$ layers of them (the prism's perpendicular height):

$$V = A \\times h.$$

So the recipe is:
1. Find the area $A$ of the **cross-section** (the face that's the same shape all the way along).
2. Multiply by the prism's **perpendicular height** $h$.

### Worked shapes
- Rectangular prism: $A = l \\times w$, so $V = l \\times w \\times h$.
- Triangular prism: $A = \\tfrac{1}{2} \\times b \\times h_{\\text{tri}}$, so $V = \\tfrac{1}{2} \\times b \\times h_{\\text{tri}} \\times h_{\\text{prism}}$.

### Why the same formula works
For a box, the cross-section is a rectangle with area $l \\times w$, and there are $h$ layers of those. For a triangular prism, the cross-section is a triangle, and there are again $h$ layers. The "area of one cross-section × number of layers" pattern is the same.

> [!warning] Perpendicular height only
> $h$ in the prism formula is the **perpendicular distance** between the two end faces, not the slant length.`,
      examples: [
        {
          id: 'ex-triangular-prism',
          statement:
            'A triangular prism has a triangular cross-section with base $6$ cm and perpendicular height $4$ cm. The prism is $20$ cm long. Find its volume.',
          steps: [
            'Triangle area: $A = \\tfrac{1}{2} \\times 6 \\times 4 = 12$ cm².',
            'Prism volume: $V = A \\times h = 12 \\times 20$.',
            'Volume: $240$ cm³.',
          ],
        },
        {
          id: 'ex-rectangular-prism',
          statement:
            'A swimming pool is a rectangular prism with length $25$ m, width $10$ m and depth $2$ m. Find the volume of water it holds (in m³).',
          steps: [
            'Cross-section: $25 \\times 10 = 250$ m².',
            'Prism volume: $V = 250 \\times 2$.',
            'Volume: $500$ m³.',
          ],
        },
        {
          id: 'ex-missing-h',
          statement:
            'A triangular prism has cross-sectional area $18$ cm² and volume $162$ cm³. Find its length.',
          steps: [
            'Use $V = A \\times h$.',
            'Substitute: $162 = 18 \\times h$.',
            'Divide: $h = 162 / 18 = 9$ cm.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-tri-prism-volume',
          difficulty: 'intro',
          instance: {
            prompt:
              'A triangular prism has a cross-section with base $8$ cm and perpendicular height $3$ cm. The prism is $15$ cm long. What is its volume (in cm³)?',
            answer: '180',
            answerType: 'numeric',
            hint: 'Triangle area is half base × height, then multiply by the prism length.',
            solution: [
              '$A = \\tfrac{1}{2} \\times 8 \\times 3 = 12$ cm².',
              '$V = 12 \\times 15 = 180$ cm³.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-prism-missing-h',
          difficulty: 'core',
          instance: {
            prompt:
              'A prism has cross-sectional area $25$ cm² and volume $350$ cm³. What is its perpendicular height (in cm)?',
            answer: '14',
            answerType: 'numeric',
            hint: 'Divide the volume by the cross-sectional area.',
            solution: [
              '$h = V / A = 350 / 25 = 14$ cm.',
            ],
          },
        },
      ],
    },
  ],
}
