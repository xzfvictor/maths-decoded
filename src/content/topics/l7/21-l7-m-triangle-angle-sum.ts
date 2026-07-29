import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Measurement · l7-m-5 (VC2M7M05).
// Demonstrate that the interior angle sum of a triangle in the plane is
// 180° and apply this to determine the interior angle sum of other shapes
// and the size of unknown angles.

export const l7MTriangleAngleSum: Topic = {
  id: 'l7-m-triangle-angle-sum',
  unit: 7,
  order: 21,
  title: 'Triangle angle sum',
  blurb:
    'Show that the interior angles of any triangle add to 180°, then use that fact to find unknown angles and the angle sum of other polygons.',
  dotPoints: ['l7-m-5'],
  lessons: [
    {
      id: 'sum-equals-180',
      heading: 'The angle sum of a triangle is 180°',
      summary:
        'Tear the corner angles off a triangle and they form a straight line — proof that they sum to 180°.',
      body: `Take any triangle. Mark its three interior angles $\\alpha, \\beta, \\gamma$ at the corners. Now rip the triangle along those three vertices and slide the three angles together so they meet at a single point with their points touching.

The three angles snap together into a **straight line**, which is an angle of $180°$. This works for every triangle — that is why the sum is the same for all of them.

$$\\alpha + \\beta + \\gamma = 180°.$$

### A more rigorous version
Draw a straight line through one vertex, parallel to the opposite side. The two new angles formed there are **alternate** to two of the triangle's interior angles (so they equal them), and the third interior angle sits between them. The three sit on a straight line, summing to $180°$.

### Consequences
- A triangle cannot have two right angles ($2 \\times 90° = 180°$ already used up).
- A triangle cannot have two obtuse angles.
- If two angles are equal, the third must be $180°$ minus that common value.

> [!warning] Degrees only
> This rule holds for angles in **degrees**, the unit we measure angles in for shape work in the plane.`,
      examples: [
        {
          id: 'ex-find-third',
          statement:
            'Two angles of a triangle are $55°$ and $70°$. Find the third.',
          steps: [
            'Use $\\alpha + \\beta + \\gamma = 180°$.',
            'Substitute: $55° + 70° + \\gamma = 180°$.',
            'Sum the known angles: $125° + \\gamma = 180°$.',
            'Subtract: $\\gamma = 55°$.',
          ],
        },
        {
          id: 'ex-isoceles',
          statement:
            'An isosceles triangle has two equal base angles of $65°$. Find the apex angle.',
          steps: [
            'Two base angles are $65°$ each.',
            'Sum of two: $130°$.',
            'Apex angle $= 180° - 130° = 50°$.',
          ],
        },
        {
          id: 'ex-right-triangle',
          statement:
            'A right triangle has angles $90°$ and $34°$. Find the third angle.',
          steps: [
            'Sum: $90° + 34° + \\gamma = 180°$.',
            '$124° + \\gamma = 180°$.',
            '$\\gamma = 56°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-third-angle',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two angles of a triangle are $60°$ and $75°$. What is the third angle (in degrees)?',
            answer: '45',
            answerType: 'numeric',
            hint: 'The three interior angles of a triangle add to $180°$.',
            solution: [
              '$180° - 60° - 75° = 45°$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-isoceles-third',
          difficulty: 'core',
          instance: {
            prompt:
              'An isosceles triangle has two equal angles of $72°$ each. What is the third angle (in degrees)?',
            answer: '36',
            answerType: 'numeric',
            hint: 'Subtract the two known angles from $180°$.',
            solution: [
              '$180° - 2 \\times 72° = 180° - 144° = 36°$.',
            ],
          },
        },
      ],
    },
    {
      id: 'angle-sums-other-shapes',
      heading: 'Angle sums of other polygons',
      summary:
        'Cut a polygon into triangles to get its angle sum: (n − 2) × 180°.',
      body: `The triangle rule becomes a tool for **every** polygon once you can chop the polygon into triangles.

### The recipe
1. Pick one vertex of the polygon.
2. Draw diagonals from that vertex to **every other** non-adjacent vertex.
3. Those diagonals split the polygon into triangles — exactly $(n - 2)$ triangles, where $n$ is the number of sides.

Each triangle contributes $180°$ of interior angle, so the **angle sum** of the whole polygon is

$$S = (n - 2) \\times 180°.$$

### A few examples
- Triangle $(n = 3)$: $(3 - 2) \\times 180° = 180°$. ✓
- Quadrilateral $(n = 4)$: $(4 - 2) \\times 180° = 360°$.
- Pentagon $(n = 5)$: $(5 - 2) \\times 180° = 540°$.
- Hexagon $(n = 6)$: $(6 - 2) \\times 180° = 720°$.

> [!warning] Convex polygons only
> The formula gives the **interior** angle sum. It works cleanly for **convex** polygons (every interior angle less than $180°$). For a concave polygon it still gives the right total, but one or more of the "interior" angles will be reflex (larger than $180°$).

### Regular polygons
A **regular** polygon has all sides equal and all angles equal. The interior angle is then

$$\\text{interior angle} = \\dfrac{(n - 2) \\times 180°}{n}.$$

For a regular hexagon: $720° / 6 = 120°$. For a regular octagon: $1080° / 8 = 135°$.`,
      examples: [
        {
          id: 'ex-quad-sum',
          statement:
            'Find the interior angle sum of a quadrilateral.',
          steps: [
            '$n = 4$ sides.',
            "$(n - 2) \\times 180° = 2 \\times 180° = 360°$.",
          ],
        },
        {
          id: 'ex-pentagon-angle',
          statement:
            'Three interior angles of a pentagon are $110°$, $120°$ and $130°$. If the other two are equal, find each of them.',
          steps: [
            'Pentagon sum: $(5 - 2) \\times 180° = 540°$.',
            'Sum of known angles: $110° + 120° + 130° = 360°$.',
            "Remaining sum: $540° - 360° = 180°$, split into two equal angles.",
            'Each unknown angle: $180° / 2 = 90°$.',
          ],
        },
        {
          id: 'ex-regular-pentagon',
          statement:
            'Find the size of each interior angle of a regular pentagon.',
          steps: [
            'Sum: $(5 - 2) \\times 180° = 540°$.',
            'A regular pentagon has $5$ equal angles.',
            'Each angle: $540° / 5 = 108°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-hexagon-sum',
          difficulty: 'core',
          instance: {
            prompt:
              'What is the interior angle sum of a hexagon (in degrees)?',
            answer: '720',
            answerType: 'numeric',
            hint: 'Use $(n - 2) \\times 180°$ with $n = 6$.',
            solution: [
              "$(6 - 2) \\times 180° = 4 \\times 180° = 720°$.",
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-regular-octagon',
          difficulty: 'core',
          instance: {
            prompt:
              'Find the size of each interior angle of a regular octagon (in degrees).',
            answer: '135',
            answerType: 'numeric',
            hint: 'Sum is $(8 - 2) \\times 180° = 1080°$. Divide by $8$.',
            solution: [
              "$(8 - 2) \\times 180° = 1080°$, each angle is $1080° / 8 = 135°$.",
            ],
          },
        },
      ],
    },
  ],
}
