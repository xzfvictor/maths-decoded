import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Space · l10a-asp-5 (VC2M10ASP05).
// 3D right-angled triangle problems.

export const l10aAsp3dRightAngled: Topic = {
  id: 'l10a-asp-3d-right-angled',
  unit: '10A',
  order: 20,
  title: '3D right-angled triangle problems',
  blurb:
    "Apply Pythagoras' theorem and trigonometry to solve three-dimensional problems in right-angled triangles.",
  dotPoints: ['l10a-asp-5'],

  lessons: [
    {
      id: 'decompose-3d',
      heading: 'Decomposing 3D into 2D',
      summary: 'Slice a 3D problem into two right triangles — one for the base, one for the vertical.',
      body: `Most 3D problems hide two right triangles. The trick is to **decompose** the solid into a horizontal "footprint" right triangle and a vertical right triangle that uses the footprint's hypotenuse as a leg.

### The pattern
1. Identify a right triangle in the **base plane** — find a length there.
2. Treat that length as a side of a **second right triangle** in a vertical plane.
3. Solve the second triangle with Pythagoras or the trig ratios.

### When to use which
- Find a **straight-line distance** through space: two Pythagoras steps.
- Find an **angle of elevation** to a point above the ground: trig in the vertical triangle.
- Find a **diagonal of a rectangular prism** of sides $a, b, c$: use the "space diagonal" formula $d = \\sqrt{a^2 + b^2 + c^2}$.`,
      examples: [
        {
          id: 'ex-rectangular-prism',
          statement:
            'A rectangular box has dimensions $3$ m $\\times 4$ m $\\times 12$ m. Find the length of the space diagonal (corner-to-opposite-corner).',
          steps: [
            'Base diagonal $d = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5$ m.',
            'Space diagonal $= \\sqrt{5^2 + 12^2} = \\sqrt{169} = 13$ m.',
          ],
        },
        {
          id: 'ex-angle-of-elevation',
          statement:
            'From a point on the ground $30$ m from the foot of a vertical tower, the angle of elevation to the top is $40°$. A bird sits on the top. How high is the bird (round to 1 dp)?',
          steps: [
            'Right triangle in vertical plane: opposite = height $h$, adjacent = $30$ m, angle = $40°$.',
            '$\\tan 40° = h / 30 \\Rightarrow h = 30 \\tan 40° \\approx 25.2$ m.',
          ],
        },
        {
          id: 'ex-roof',
          statement:
            'A house roof ridge is $8$ m long. The roof slopes down to eaves $3$ m away horizontally, dropping $1.5$ m. Find the angle the roof slope makes with the horizontal (round to 1 dp).',
          steps: [
            'Right triangle: horizontal run $= 3$ m, vertical drop $= 1.5$ m.',
            '$\\tan \\theta = 1.5 / 3 = 0.5 \\Rightarrow \\theta = \\arctan 0.5 \\approx 26.6°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-space-diagonal',
          difficulty: 'intro',
          instance: {
            prompt:
              'A rectangular box has sides $6$ cm, $8$ cm, $10$ cm. What is the length of the space diagonal (corner-to-opposite-corner)? (Round to 1 dp.)',
            answer: '14.14',
            answerType: 'numeric',
            hint: 'Two Pythagoras steps: base diagonal, then the vertical.',
            solution: [
              'Base diagonal: $\\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10$ cm.',
              'Space diagonal: $\\sqrt{10^2 + 10^2} = \\sqrt{200} \\approx 14.14$ cm.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-roof-pitch',
          difficulty: 'core',
          instance: {
            prompt:
              'A roof slopes $4$ m horizontally and rises $3$ m vertically. What angle does it make with the horizontal (round to nearest degree)?',
            answer: '37',
            answerType: 'numeric',
            hint: '$\\tan \\theta = \\dfrac{\\text{rise}}{\\text{run}}$.',
            solution: [
              '$\\tan \\theta = 3/4 = 0.75 \\Rightarrow \\theta = \\arctan(0.75) \\approx 36.87°$.',
              'Round to $37°$.',
            ],
          },
        },
      ],
    },

    {
      id: 'angle-between-lines',
      heading: 'Angles between lines & planes in 3D',
      summary: 'Drop a perpendicular to translate a 3D angle into a 2D one.',
      body: `The angle between two lines in 3D — or between a line and a plane — is the **acute** angle between them. The standard move is to drop a perpendicular so the problem becomes 2D.

### Angle between two lines
Translate one line (without rotating) until it meets the other. The angle at the meeting point is the angle between them.

### Angle between a line and a plane
Drop a perpendicular from any point on the line onto the plane. The angle between the line and its projection is the angle between the line and the plane.

### Why this matters
Surveying, roof pitch, ramp gradients, and any 3D navigation problem reduce to one of these. The Pythagoras-trig toolkit applies once you've isolated the right triangle.`,
      examples: [
        {
          id: 'ex-line-plane',
          statement:
            'A ramp rises $1.5$ m over a horizontal run of $6$ m. What angle does the ramp make with the ground (round to 1 dp)?',
          steps: [
            'Right triangle: rise $1.5$, run $6$.',
            '$\\tan \\theta = 1.5 / 6 = 0.25 \\Rightarrow \\theta = \\arctan 0.25 \\approx 14.0°$.',
          ],
        },
        {
          id: 'ex-cube-diagonal',
          statement:
            'A cube has side $1$. What is the angle between a space diagonal and a face diagonal (round to 1 dp)?',
          steps: [
            'Place the cube with one vertex at the origin. Space diagonal goes to $(1, 1, 1)$.',
            'Face diagonal in the $xy$-plane goes from $(0,0,0)$ to $(1, 1, 0)$.',
            'Length of space diagonal $= \\sqrt{3}$, length of face diagonal $= \\sqrt{2}$.',
            'Dot product: $\\vec{u} \\cdot \\vec{v} = 1 \\cdot 1 + 1 \\cdot 1 + 1 \\cdot 0 = 2$.',
            '$\\cos \\theta = \\dfrac{2}{\\sqrt{3} \\cdot \\sqrt{2}} = \\dfrac{2}{\\sqrt{6}}$.',
            '$\\theta = \\arccos(2/\\sqrt{6}) \\approx 35.3°$.',
          ],
        },
        {
          id: 'ex-diagonal-plane',
          statement:
            'A ladder $5$ m long leans against a vertical wall. Its base is $3$ m from the wall. Find the angle it makes with the wall (round to nearest degree).',
          steps: [
            'Triangle: hypotenuse $5$, base $3$, height $h = 4$.',
            'Angle to wall is the complement: $\\sin \\theta = 3/5$ gives the angle to the ground $= 53.13°$.',
            'Angle with wall $= 90° - 53° = 37°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-ramp-angle',
          difficulty: 'intro',
          instance: {
            prompt:
              'A ramp rises $2$ m over a horizontal run of $10$ m. What angle does the ramp make with the ground (round to nearest degree)?',
            answer: '11',
            answerType: 'numeric',
            hint: '$\\tan \\theta = \\text{rise} / \\text{run}$.',
            solution: [
              '$\\tan \\theta = 2/10 = 0.2 \\Rightarrow \\theta = \\arctan(0.2) \\approx 11.31°$.',
              'Round to $11°$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-ladder',
          difficulty: 'core',
          instance: {
            prompt:
              'A $10$ m ladder leans against a wall, base $6$ m from the wall. Find the angle the ladder makes with the wall (round to nearest degree).',
            answer: '53',
            answerType: 'numeric',
            hint: 'Find the angle with the ground first; the angle with the wall is the complement.',
            solution: [
              'Triangle: hypotenuse $10$, base $6$, so $\\sin \\theta = 6/10 = 0.6 \\Rightarrow \\theta = \\arcsin(0.6) \\approx 36.87°$.',
              'Angle with wall $= 90° - 37° = 53°$.',
            ],
          },
        },
      ],
    },
  ],
}