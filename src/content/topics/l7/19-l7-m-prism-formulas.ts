import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Measurement · l7-m-3 (VC2M7M03).
// Compare the circumference of circles in relation to their radius and
// diameter, and establish measurement formulas for the circumference
// of a circle.

export const l7MPrismFormulas: Topic = {
  id: 'l7-m-prism-formulas',
  unit: 7,
  order: 19,
  title: 'Circle circumference and prism formulas',
  blurb:
    'Establish the connection between the radius, diameter and circumference of a circle, and practice the prism volume formula by deriving it from area and height.',
  dotPoints: ['l7-m-3'],
  lessons: [
    {
      id: 'circumference-formula',
      heading: 'Comparing circumferences',
      summary:
        'Bigger circles have bigger circumferences — at a fixed ratio. The number is pi.',
      body: `Walk around a circle's edge once. That distance is the **circumference**. It is the circle's "perimeter".

### A pattern appears
Roll a circle along a straight line and mark where it goes after one full spin. For every circle, no matter the size, that marked length is about **a bit more than three times** the diameter.

- Diameter $10$ cm → circumference about $31.4$ cm.
- Diameter $1$ m → circumference about $3.14$ m.
- Diameter $100$ m → circumference about $314$ m.

Every time, circumference ÷ diameter ≈ $3.14159...$, a number we call $\\pi$ ("pi").

### The formula
$$C = \\pi \\times d,$$
where $d$ is the diameter. Because $d = 2r$, the same formula written with the radius $r$ is

$$C = 2 \\pi r.$$

### Why $\\pi$ is the same for every circle
All circles are **similar** — every circle is just a scaled-up version of every other circle. So the ratio of circumference to diameter is a universal constant.

> [!warning] Use the value carefully
> For exact answers, leave $\\pi$ in the answer (e.g. $C = 6\\pi$ cm). For numerical answers, use $\\pi \\approx 3.14$ or the calculator value $3.14159...$ and round sensibly.`,
      examples: [
        {
          id: 'ex-from-diameter',
          statement:
            'A circle has diameter $14$ cm. Find its circumference, leaving $\\pi$ in your answer.',
          steps: [
            'Use $C = \\pi \\times d$.',
            'Substitute: $C = 14\\pi$.',
            'Numerical (using $\\pi \\approx 3.14$): $C \\approx 43.96$ cm.',
          ],
        },
        {
          id: 'ex-from-radius',
          statement:
            'A circular pond has radius $5$ m. What is its circumference (to the nearest metre)?',
          steps: [
            'Use $C = 2 \\pi r$.',
            'Substitute: $C = 2 \\pi \\times 5 = 10\\pi$.',
            'Approximate: $C \\approx 10 \\times 3.14 = 31.4$ m, so about $31$ m.',
          ],
        },
        {
          id: 'ex-finding-diameter',
          statement:
            'A wheel travels $44$ m in one full turn. Estimate its diameter in metres.',
          steps: [
            'Each full turn covers one circumference.',
            'So $C \\approx 44$ m. Rearranging $C = \\pi d$: $d = C / \\pi$.',
            '$d \\approx 44 / 3.14 \\approx 14$ m.',
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
              'A circle has diameter $10$ cm. What is its circumference (to the nearest cm)?',
            answer: '31',
            answerType: 'numeric',
            hint: '$C = \\pi d$. Use $\\pi \\approx 3.14$.',
            solution: [
              '$C = \\pi \\times 10 \\approx 31.4$ cm, so $\\approx 31$ cm.',
            ],
          },
        },
      ],
    },
    {
      id: 'connecting-area-and-prism',
      heading: 'From face area to prism volume',
      summary:
        'Volume = area of cross-section × height: one formula that covers rectangular and triangular prisms.',
      body: `The rectangle-area and triangle-area formulas of the dot point before lead straight to the volume-of-a-prism formula.

### The derivation in pictures
Cut a right prism into thin layers, each one a copy of the cross-section, until you have $h$ layers.

- Each layer has area $A$ (the area of the cross-section: $l \\times w$ for a rectangle, $\\tfrac{1}{2} b h_{\\text{tri}}$ for a triangle).
- There are $h$ layers.

So the prism's volume is

$$V = A \\times h.$$

### Same formula, two faces
- **Rectangular prism**: $V = (l \\times w) \\times h = lwh$.
- **Triangular prism**: $V = \\big(\\tfrac{1}{2} b h_{\\text{tri}}\\big) \\times h_{\\text{prism}}$.

> [!definition] Universal prism volume
> Pick a cross-section shape, compute its area, multiply by the prism's perpendicular height. Works for every right prism.

### Why two different $h$'s show up
For a triangular prism, the triangle has its own perpendicular height $h_{\\text{tri}}$ (used in $\\tfrac{1}{2} b h$), while the whole prism has its own perpendicular height $h_{\\text{prism}}$ (used in $V = A h$). They are *different* numbers unless the triangle happens to be the prism's cross-section in the special way that makes them equal.`,
      examples: [
        {
          id: 'ex-rect-prism-derive',
          statement:
            'A rectangular prism is $8$ cm long, $3$ cm wide and $4$ cm tall. Use $V = A \\times h$ to find its volume.',
          steps: [
            'Cross-section (a rectangle): $A = 8 \\times 3 = 24$ cm².',
            'Prism height: $h = 4$ cm.',
            '$V = 24 \\times 4 = 96$ cm³.',
          ],
        },
        {
          id: 'ex-tri-prism-derive',
          statement:
            'A triangular prism has triangular cross-section with base $5$ cm and perpendicular height $4$ cm. The prism is $12$ cm long. Find the volume.',
          steps: [
            'Triangle area: $A = \\tfrac{1}{2} \\times 5 \\times 4 = 10$ cm².',
            "Prism height $h_{\\text{prism}} = 12$ cm.",
            "$V = 10 \\times 12 = 120$ cm³.",
          ],
        },
        {
          id: 'ex-cylinder-preview',
          statement:
            'A cylinder has radius $3$ cm and height $10$ cm. Its cross-section is a circle with area $\\pi r^2 = \\pi \\times 3^2 = 9\\pi$ cm². Find its volume, leaving $\\pi$ in your answer.',
          steps: [
            "Cross-section area: $A = 9\\pi$ cm².",
            'Prism-style formula $V = A \\times h$ works for a cylinder too.',
            '$V = 9\\pi \\times 10 = 90\\pi$ cm³.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-prism-derive',
          difficulty: 'core',
          instance: {
            prompt:
              'A triangular prism has triangular cross-section with base $6$ cm and perpendicular height $4$ cm. The prism is $10$ cm long. What is its volume (in cm³)?',
            answer: '120',
            answerType: 'numeric',
            hint: 'Triangle area is half base × height, then multiply by the prism length.',
            solution: [
              '$A = \\tfrac{1}{2} \\times 6 \\times 4 = 12$ cm².',
              "$V = 12 \\times 10 = 120$ cm³.",
            ],
          },
        },
      ],
    },
  ],
}
