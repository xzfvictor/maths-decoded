import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Space · l8-sp-2 (VC2M8SP02).
// Establish properties of quadrilaterals using congruent triangles and
// angle properties, and solve related problems explaining reasoning.

export const l8SpQuadrilateralProperties: Topic = {
  id: 'l8-sp-quadrilateral-properties',
  unit: 8,
  order: 20,
  title: 'Properties of quadrilaterals',
  blurb:
    'Establish properties of squares, rectangles, parallelograms, rhombuses, trapeziums and kites using congruent triangles and angle properties.',
  dotPoints: ['l8-sp-2'],

  lessons: [
    {
      id: 'quadrilateral-families',
      heading: 'Families of quadrilaterals',
      summary:
        'Recognise the side, angle, diagonal and symmetry properties that distinguish the special quadrilaterals.',
      body: `A **quadrilateral** is a closed 2D shape with exactly four straight sides. The interior angles of any quadrilateral sum to $360°$ (a full turn) because every quadrilateral can be split into two triangles.

### Building up the family
Each special quadrilateral adds one or two extra constraints on top of the basic "four straight sides" rule.

- **Parallelogram** — both pairs of opposite sides are parallel.
- **Rectangle** — a parallelogram with four right angles.
- **Rhombus** — a parallelogram with all four sides equal.
- **Square** — a rectangle with all four sides equal (so it is both a rectangle and a rhombus).
- **Trapezium** — exactly **one** pair of opposite sides is parallel (the *parallel* sides are the *bases*).
- **Kite** — two pairs of adjacent sides equal in length.

### Side and angle properties
- In a **parallelogram**, opposite sides are equal and opposite angles are equal.
- In a **rectangle**, all four interior angles are $90°$ and the diagonals are equal.
- In a **rhombus**, all four sides are equal and the diagonals **bisect each other at right angles**.
- In a **kite**, one diagonal is the perpendicular bisector of the other.

### Diagonal and symmetry clues
- Rectangle: diagonals equal and bisect each other.
- Rhombus: diagonals perpendicular and bisect each other.
- Square: both of the above hold.
- Kite: one diagonal is an axis of symmetry (the one joining the two *unequal* vertices).
- Isosceles trapezium: one axis of symmetry perpendicular to the parallel sides.

### Why these matter in the real world
Linkages, scissor lifts, folding umbrellas, car jacks, cherry pickers and toolboxes all rely on the way opposite sides and angles of a parallelogram stay equal as the shape opens and closes.`,
      examples: [
        {
          id: 'ex-angles-sum',
          statement:
            'Three interior angles of a quadrilateral are $90°$, $85°$ and $100°$. What is the fourth?',
          steps: [
            'Interior angles of a quadrilateral sum to $360°$.',
            'Fourth angle $= 360° - (90° + 85° + 100°) = 360° - 275° = 85°$.',
          ],
        },
        {
          id: 'ex-classify',
          statement:
            'A quadrilateral has both pairs of opposite sides parallel, all four sides equal, but its angles are not $90°$. What is it?',
          steps: [
            'Both pairs of opposite sides parallel — it is a parallelogram.',
            'All four sides equal — it is a rhombus.',
            'Angles not $90°$ — so it is **not** a rectangle or a square.',
            'The shape is a **rhombus**.',
          ],
        },
        {
          id: 'ex-diagonal-rhombus',
          statement:
            'A rhombus has diagonals of length $6$ and $8$. The diagonals bisect each other at right angles. What is the side length?',
          steps: [
            'Each diagonal is cut in half: $3$ and $4$.',
            'The two halves and the side form a right-angled triangle with legs $3$ and $4$.',
            'Side $= \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-fourth-angle',
          difficulty: 'intro',
          instance: {
            prompt:
              'Three interior angles of a quadrilateral are $70°$, $110°$ and $90°$. What is the fourth angle (in degrees)?',
            answer: '90',
            answerType: 'numeric',
            hint: 'The interior angles of a quadrilateral sum to $360°$.',
            solution: [
              'Fourth angle $= 360° - (70° + 110° + 90°) = 360° - 270° = 90°$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-name-kite',
          difficulty: 'core',
          instance: {
            prompt:
              'A quadrilateral has two pairs of adjacent sides equal, but no parallel sides. What is it? (one word)',
            answer: 'kite',
            answerType: 'exact',
            hint: 'It is the only quadrilateral defined by two pairs of *adjacent* equal sides.',
            solution: [
              'Two pairs of adjacent sides equal — that is the definition of a **kite**.',
            ],
          },
        },
      ],
    },
  ],
}