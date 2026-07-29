import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Measurement · l7-m-1 (VC2M7M01).
// Establish the formulas for areas of rectangles, triangles and parallelograms
// and use these in problem-solving.

export const l7MAreasRectanglesTriangles: Topic = {
  id: 'l7-m-areas-rectangles-triangles',
  unit: 7,
  order: 17,
  title: 'Areas of rectangles, triangles and parallelograms',
  blurb:
    'Establish the area formulas for rectangles, triangles and parallelograms and use them in problem solving.',
  dotPoints: ['l7-m-1'],
  lessons: [
    {
      id: 'rectangles',
      heading: 'Area of a rectangle',
      summary:
        'Count unit squares to build the formula area = length × width, then apply it.',
      body: `The **area** of a shape is the amount of flat surface it covers, measured in square units (cm², m², km²...).

### Building the formula
Imagine a rectangle that is $4$ cm long and $3$ cm wide. You can tile it with $1$ cm × $1$ cm squares. There are $4$ squares along the length and $3$ along the width, so the number of squares is

$$4 \times 3 = 12.$$

In general, for a rectangle with length $l$ and width $w$:

$$A = l \times w.$$

> [!definition] Rectangle area
> The area of a rectangle is **length × width**. Both measurements must be in the **same unit**.

### Same unit, every time
If a rectangle is $2$ m by $50$ cm, first convert: $50$ cm $= 0.5$ m. Then $A = 2 \times 0.5 = 1$ m².

### Why we need the formula
Without it, counting squares for a large rectangle would take forever. With it, the answer is immediate.`,
      examples: [
        {
          id: 'ex-tile-rectangle',
          statement:
            'A garden bed is $6$ m long and $4$ m wide. What is its area?',
          steps: [
            'Identify length $= 6$ m, width $= 4$ m.',
            'Apply the formula: $A = 6 \times 4$.',
            'Result: $A = 24$ m².',
          ],
        },
        {
          id: 'ex-mixed-units',
          statement:
            'A photo is $15$ cm by $200$ mm. Find its area in cm².',
          steps: [
            'Convert: $200$ mm $= 20$ cm.',
            '$A = 15 \times 20 = 300$.',
            'Area: $300$ cm².',
          ],
        },
        {
          id: 'ex-missing-side',
          statement:
            'A rectangle has area $42$ cm² and width $6$ cm. Find its length.',
          steps: [
            'Substitute: $42 = 6 \times w$.',
            'Divide both sides by $6$: $w = 42 / 6 = 7$.',
            'Length: $7$ cm.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-rect-area',
          difficulty: 'intro',
          instance: {
            prompt:
              'A rectangular room is $5$ m long and $3$ m wide. What is its area (in m²)?',
            answer: '15',
            answerType: 'numeric',
            hint: 'Multiply length by width.',
            solution: [
              '$A = 5 \times 3 = 15$ m².',
            ],
          },
        },
      ],
    },
    {
      id: 'triangles-and-parallelograms',
      heading: 'Area of triangles and parallelograms',
      summary:
        'A triangle is half a rectangle; a parallelogram is built from two copies of the same triangle.',
      body: `The rectangle formula is the springboard for two more shapes.

### Area of a triangle
A triangle is exactly **half** of a rectangle (or a parallelogram). Take any triangle and rotate a copy of it $180°$ around the midpoint of one side — they fit together into a parallelogram with the same base and the same height.

$$A = \tfrac{1}{2} \times b \times h.$$

Here $b$ is the **base** and $h$ is the **perpendicular height** (the height measured at right angles to the base — not the slanted side length).

### Area of a parallelogram
Slide the triangular notch from one side to the other and a parallelogram becomes a rectangle with the same base and the same perpendicular height.

$$A = b \times h.$$

> [!warning] Perpendicular height only
> The $h$ in these formulas is the **perpendicular height**, the straight-line distance to the base at a right angle. Tilting the triangle sideways doesn't change the area.

### Quick check
- Right triangle with legs $4$ cm and $6$ cm: $A = \tfrac{1}{2} \times 4 \times 6 = 12$ cm².
- Parallelogram with base $8$ cm, perpendicular height $5$ cm: $A = 8 \times 5 = 40$ cm².`,
      examples: [
        {
          id: 'ex-triangle-area',
          statement:
            'A triangular flag has base $10$ cm and perpendicular height $7$ cm. What is its area?',
          steps: [
            'Use the triangle formula: $A = \tfrac{1}{2} \times b \times h$.',
            'Substitute: $A = \tfrac{1}{2} \times 10 \times 7$.',
            '$A = \tfrac{1}{2} \times 70 = 35$ cm².',
          ],
        },
        {
          id: 'ex-parallelogram-area',
          statement:
            'A parallelogram has base $12$ cm and perpendicular height $6$ cm. Find its area.',
          steps: [
            'Use $A = b \times h$.',
            'Substitute: $A = 12 \times 6$.',
            'Area: $72$ cm².',
          ],
        },
        {
          id: 'ex-triangle-missing-h',
          statement:
            'A triangle has area $30$ cm² and base $12$ cm. Find the perpendicular height.',
          steps: [
            'Substitute: $30 = \tfrac{1}{2} \times 12 \times h$.',
            'Simplify: $30 = 6h$.',
            'Divide: $h = 30 / 6 = 5$ cm.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-triangle-area',
          difficulty: 'intro',
          instance: {
            prompt:
              'A triangle has base $8$ cm and perpendicular height $5$ cm. What is its area (in cm²)?',
            answer: '20',
            answerType: 'numeric',
            hint: 'Multiply base and height, then halve.',
            solution: [
              '$A = \\tfrac{1}{2} \\times 8 \\times 5 = \\tfrac{1}{2} \\times 40 = 20$ cm².',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-parallelogram-area',
          difficulty: 'core',
          instance: {
            prompt:
              'A parallelogram has base $9$ cm and perpendicular height $4$ cm. What is its area (in cm²)?',
            answer: '36',
            answerType: 'numeric',
            hint: 'Multiply base by perpendicular height.',
            solution: [
              '$A = 9 \\times 4 = 36$ cm².',
            ],
          },
        },
      ],
    },
  ],
}
