import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Measurement · l8-m-1 (VC2M8M01).
// Solve problems involving the area and perimeter of irregular and
// composite shapes using appropriate units.

export const l8MCompositeShapes: Topic = {
  id: 'l8-m-composite-shapes',
  unit: 8,
  order: 12,
  title: 'Area and perimeter of composite shapes',
  blurb:
    'Solve problems involving the area and perimeter of irregular and composite shapes using appropriate units.',
  dotPoints: ['l8-m-1'],

  lessons: [
    {
      id: 'breaking-into-pieces',
      heading: 'Breaking composite shapes into pieces',
      summary: 'Split a composite shape into rectangles (and other familiar shapes); add areas and lengths.',
      body: `A **composite shape** is made by joining two or more simple shapes — usually rectangles, but sometimes triangles or parts of circles. To find its **area** or **perimeter**, split the shape into pieces, work out each piece, and combine.

### Two strategies for area
1. **Add pieces** — split the shape into familiar shapes and add their areas.
2. **Subtract the gap** — start with a big rectangle and subtract the empty part.

Both give the same answer; pick whichever has fewer (and simpler) pieces.

### Strategy for perimeter
Walk around the outside and add the lengths of every edge — **including any edge that lives between two pieces inside the shape**. If the shape is rectangular overall, opposite sides are equal, so you only need to know two adjacent side lengths.

### Choosing units
Pick the unit that makes the numbers sensible:
- A garden bed: square metres (m²).
- A sheet of paper: square centimetres (cm²).
- A farm: hectares (ha), where $1\\text{ ha} = 10{,}000\\text{ m}^2$.`,
      examples: [
        {
          id: 'ex-L-shape-add',
          statement:
            'An L-shaped room has a $6$ m by $4$ m rectangle with a $3$ m by $2$ m rectangle cut from one corner (re-entrant corner — the L sticks out, the corner is the inside of the L). Find its area.',
          steps: [
            'The L is a $6 \\times 4$ rectangle with a $3 \\times 2$ rectangle missing.',
            'Full rectangle area: $6 \\times 4 = 24$ m².',
            'Missing area: $3 \\times 2 = 6$ m².',
            'Area of the L: $24 - 6 = 18$ m².',
          ],
        },
        {
          id: 'ex-add-pieces',
          statement:
            'A shape is a $5$ m by $3$ m rectangle with a $2$ m by $2$ m square attached on top. Find the area and the perimeter.',
          steps: [
            'Two pieces: rectangle $5 \\times 3 = 15$ m² and square $2 \\times 2 = 4$ m².',
            'Total area: $15 + 4 = 19$ m².',
            'Perimeter: walk around the outside — $3 + 5 + 2 + 2 + 2 + 3 = 17$ m.',
          ],
        },
        {
          id: 'ex-trapezoid-split',
          statement:
            'A trapezium has parallel sides of $8$ cm and $5$ cm, and is $4$ cm tall. Find its area.',
          steps: [
            'Split the trapezium into a $5 \\times 4$ rectangle plus a right triangle with base $3$ cm and height $4$ cm.',
            'Rectangle: $5 \\times 4 = 20$ cm².',
            'Triangle: $\\dfrac{1}{2} \\times 3 \\times 4 = 6$ cm².',
            'Total area: $20 + 6 = 26$ cm².',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-L-area',
          difficulty: 'intro',
          instance: {
            prompt:
              'An L-shape is a $7$ m by $5$ m rectangle with a $3$ m by $2$ m rectangle removed from one corner. What is its area in m²?',
            answer: '29',
            answerType: 'numeric',
            hint: 'Full rectangle minus the cut-out.',
            solution: [
              'Full rectangle: $7 \\times 5 = 35$ m².',
              'Cut-out: $3 \\times 2 = 6$ m².',
              'L-shape: $35 - 6 = 29$ m².',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-perimeter',
          difficulty: 'core',
          instance: {
            prompt:
              'A rectangle is $12$ m long and $5$ m wide. What is its perimeter in metres?',
            answer: '34',
            answerType: 'numeric',
            hint: 'Perimeter $= 2 \\times (\\text{length} + \\text{width})$.',
            solution: [
              '$P = 2 \\times (12 + 5) = 2 \\times 17 = 34$ m.',
            ],
          },
        },
      ],
    },
  ],
}