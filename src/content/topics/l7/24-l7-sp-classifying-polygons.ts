import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Space · l7-sp-2 (VC2M7SP02).
// Classify triangles, quadrilaterals and other polygons by their side and
// angle properties and identify relationships between them.

export const l7SpClassifyingPolygons: Topic = {
  id: 'l7-sp-classifying-polygons',
  unit: 7,
  order: 24,
  title: 'Classifying polygons',
  blurb:
    'Classify triangles, quadrilaterals and other polygons by their side and angle properties and identify relationships between them.',
  dotPoints: ['l7-sp-2'],
  lessons: [
    {
      id: 'triangles-by-sides',
      heading: 'Classifying triangles',
      summary:
        'Sort triangles by side length (equilateral, isosceles, scalene) and by angle (acute, right, obtuse).',
      body: `A **triangle** has three sides and three interior angles. Triangles can be sorted into families by either property.

### By sides

- **Equilateral**: all three sides equal. All three angles equal $60°$.
- **Isosceles**: at least two sides equal. The two angles opposite the equal sides are also equal (the **base angles**).
- **Scalene**: all three sides different in length. All three angles different.

### By angles

- **Acute triangle**: every interior angle is less than $90°$.
- **Right triangle**: one interior angle is exactly $90°$.
- **Obtuse triangle**: one interior angle is greater than $90°$ (so the other two must be acute, since the angles sum to $180°$).

### Combining the two

The two classifications can be applied together. For example, a right-angled isosceles triangle has a $90°$ angle and two equal legs — the two remaining angles are each $45°$.

> [!definition] Key fact
> The three interior angles of any triangle add to $180°$.`,
      examples: [
        {
          id: 'ex-classify-tri',
          statement:
            'A triangle has sides of length $5$ cm, $5$ cm and $8$ cm. What type is it by sides?',
          steps: [
            'Two sides are equal ($5$ cm and $5$ cm).',
            'So it is an **isosceles** triangle.',
          ],
        },
        {
          id: 'ex-angle-sum',
          statement:
            'Two angles of a triangle are $50°$ and $70°$. Find the third angle.',
          steps: [
            'The three angles sum to $180°$.',
            'Third angle $= 180° - 50° - 70° = 60°$.',
          ],
        },
        {
          id: 'ex-combined',
          statement:
            'A triangle has angles $30°$, $60°$ and $90°$. What type of triangle is it by angle?',
          steps: [
            'One angle is $90°$, so it is a **right** triangle.',
            'All three sides are different lengths, so it is also scalene.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-isosceles-base-angle',
          difficulty: 'intro',
          instance: {
            prompt:
              'An isosceles triangle has an apex angle of $40°$. What is each base angle? Answer as a number.',
            answer: '70',
            answerType: 'numeric',
            hint: 'The base angles are equal and the three angles sum to $180°$.',
            solution: [
              '$180° - 40° = 140°$. Split equally between the two base angles: $140° \\div 2 = 70°$ each.',
            ],
          },
        },
      ],
    },

    {
      id: 'quadrilaterals-and-polygons',
      heading: 'Quadrilaterals and other polygons',
      summary:
        'Identify squares, rectangles, rhombuses, parallelograms, trapeziums and kites, and sort polygons by number of sides.',
      body: `A **quadrilateral** is any closed shape with four straight sides. Different quadrilaterals share some properties and not others.

### Families of quadrilateral

- **Parallelogram**: opposite sides are parallel **and** equal; opposite angles are equal.
- **Rectangle**: a parallelogram with four right angles.
- **Rhombus**: a parallelogram with four equal sides.
- **Square**: a parallelogram that is both a rectangle and a rhombus — all sides equal and all angles right.
- **Trapezium** (or trapezoid): exactly **one** pair of parallel sides.
- **Kite**: two pairs of adjacent equal sides.

### Inclusion chain

Some families sit inside others. Every square is a rectangle, every rectangle is a parallelogram, but not every parallelogram is a rectangle.

### Polygons with more sides

Polygons are named by their number of sides. The interior angles sum to $(n - 2) \\times 180°$ for an $n$-sided polygon.

- Pentagon: $5$ sides — angle sum $540°$.
- Hexagon: $6$ sides — angle sum $720°$.
- Octagon: $8$ sides — angle sum $1080°$.

> [!warning] Don't confuse "looks like" with "is"
> A shape that looks square-ish but has angles of $89°$ and $91°$ isn't a square. Always check the property — side lengths and angles — before naming the shape.`,
      examples: [
        {
          id: 'ex-rect-vs-rhomb',
          statement:
            'A shape has four equal sides but its angles are $70°$, $110°$, $70°$ and $110°$. What is it?',
          steps: [
            'Four equal sides → it could be a square or a rhombus.',
            'But the angles are not all $90°$, so it is not a square.',
            'A rhombus has equal sides with non-right opposite angles. Answer: **rhombus**.',
          ],
        },
        {
          id: 'ex-angle-sum-hexagon',
          statement:
            'Find the sum of the interior angles of a hexagon.',
          steps: [
            'A hexagon has $n = 6$ sides.',
            'Sum $= (n - 2) \\times 180° = 4 \\times 180° = 720°$.',
          ],
        },
        {
          id: 'ex-is-square-rect',
          statement:
            'True or false: every square is a rectangle.',
          steps: [
            'A rectangle has four right angles and opposite sides equal.',
            'A square also has four right angles and four equal sides (which are also opposite).',
            'So a square meets the rectangle rule. **True**.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pentagon-angle-sum',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the sum of the interior angles of a pentagon? Answer as a number of degrees.',
            answer: '540',
            answerType: 'numeric',
            hint: 'Use $(n - 2) \\times 180°$ for an $n$-sided polygon.',
            solution: [
              '$n = 5$, so the sum is $(5 - 2) \\times 180° = 3 \\times 180° = 540°$.',
            ],
          },
        },
      ],
    },
  ],
}
