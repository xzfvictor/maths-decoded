import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Space · l10a-asp-1 (VC2M10ASP01).
// Circle theorems.

export const l10aAspCircleTheorems: Topic = {
  id: 'l10a-asp-circle-theorems',
  unit: '10A',
  order: 16,
  title: 'Circle theorems',
  blurb:
    'Prove and apply relationships between angles and the various lines associated with circles — radii, diameters, chords and tangents.',
  dotPoints: ['l10a-asp-1'],

  lessons: [
    {
      id: 'angles-in-a-circle',
      heading: 'Angles at the centre & circumference',
      summary: 'The angle at the centre is twice the angle at the circumference, on the same arc.',
      body: `A circle hides many useful angle relationships. The first one ties the centre and the circumference together.

### Theorem 1: Angle at the centre
The angle subtended by an arc at the **centre** of a circle is **twice** the angle subtended by the same arc at any point on the remaining **circumference** (on the major arc).

$$\\angle \\text{at centre} = 2 \\times \\angle \\text{at circumference}$$

### Theorem 2: Angles in the same segment
Angles subtended by the same chord (or arc) at the circumference, standing on the **same side** of the chord, are **equal**.

### Theorem 3: Angle in a semicircle
The angle subtended by a **diameter** at the circumference is a **right angle** (this is a special case of Theorem 1).

### Proving them
The proofs use isosceles triangles made from two radii. Drawing the triangle and labelling equal base angles is the standard start.`,
      examples: [
        {
          id: 'ex-centre-twice',
          statement:
            'In a circle, the angle at the centre subtended by arc $AB$ is $120°$. What is the angle at the circumference standing on the same arc?',
          steps: [
            'Apply Theorem 1: $\\angle \\text{centre} = 2 \\times \\angle \\text{circumference}$.',
            '$120° = 2 \\times \\angle \\text{circumference}$.',
            '$\\angle \\text{circumference} = 60°$.',
          ],
        },
        {
          id: 'ex-semicircle',
          statement:
            '$AB$ is a diameter of a circle. $C$ is a point on the circle (not $A$ or $B$). What is $\\angle ACB$?',
          steps: [
            'Apply Theorem 3: the angle in a semicircle is a right angle.',
            '$\\angle ACB = 90°$.',
          ],
        },
        {
          id: 'ex-same-segment',
          statement:
            'Points $C$ and $D$ lie on the same side of chord $AB$ on a circle. $\\angle ACB = 35°$. What is $\\angle ADB$?',
          steps: [
            'Apply Theorem 2: same segment $\\Rightarrow$ equal angles.',
            '$\\angle ADB = 35°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-centre-vs-circum',
          difficulty: 'intro',
          instance: {
            prompt:
              'The angle at the centre is $80°$. What is the angle at the circumference subtending the same arc?',
            answer: '40',
            answerType: 'numeric',
            hint: 'Centre angle is twice the circumference angle.',
            solution: [
              '$\\angle \\text{centre} = 2 \\times \\angle \\text{circumference}$.',
              '$80° = 2 \\times \\angle \\text{circumference} \\Rightarrow \\angle = 40°$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-diameter-right',
          difficulty: 'core',
          instance: {
            prompt:
              'A triangle is inscribed in a circle so that one of its sides is a diameter of the circle. What is the angle opposite the diameter? Answer as a number.',
            answer: '90',
            answerType: 'numeric',
            hint: 'The angle in a semicircle is a right angle.',
            solution: [
              'By Thales\' theorem (angle in a semicircle), the angle opposite the diameter is $90°$.',
            ],
          },
        },
      ],
    },

    {
      id: 'chords-tangents',
      heading: 'Chords, tangents & cyclic quadrilaterals',
      summary: 'Equal chords cut equal arcs; tangent meets radius at 90°; opposite angles of cyclic quadrilaterals sum to 180°.',
      body: `Beyond the centre–circumference angle, a few more theorems help with most circle problems.

### Theorem 4: Tangent–radius
A tangent to a circle is **perpendicular** to the radius drawn to the point of tangency. (So the tangent meets the radius at $90°$.)

### Theorem 5: Tangent–chord angle (alternate segment)
The angle between a tangent and a chord through the point of tangency equals the angle in the **alternate segment**.

### Theorem 6: Equal chords
In the same circle (or equal circles), equal chords subtend equal angles at the centre and equal arcs.

### Theorem 7: Cyclic quadrilateral
A quadrilateral whose four vertices all lie on a circle is called **cyclic**. Its **opposite angles sum to $180°$**.

$$\\angle A + \\angle C = 180°, \\quad \\angle B + \\angle D = 180°.$$

### Putting it together
Many "find the angle" problems chain two of these: e.g. tangent–radius gives a right angle, then cyclic-quadrilateral sums give the rest.`,
      examples: [
        {
          id: 'ex-tangent-radius',
          statement:
            'A tangent touches a circle at $T$. A radius $OT$ is drawn to the point of tangency. What is the angle between the tangent and $OT$?',
          steps: [
            'By Theorem 4, the tangent meets the radius at right angles.',
            'The angle is $90°$.',
          ],
        },
        {
          id: 'ex-cyclic-quad',
          statement:
            '$ABCD$ is a cyclic quadrilateral with $\\angle A = 110°$. What is $\\angle C$?',
          steps: [
            'Apply Theorem 7: opposite angles of a cyclic quadrilateral sum to $180°$.',
            '$\\angle C = 180° - 110° = 70°$.',
          ],
        },
        {
          id: 'ex-tangent-chord',
          statement:
            'A tangent at $A$ and chord $AB$ form a $40°$ angle. $C$ lies on the circle on the *opposite* side of $AB$ from the tangent. What is $\\angle ACB$?',
          steps: [
            'Apply Theorem 5 (alternate segment): tangent–chord angle $=$ angle in the alternate segment.',
            '$\\angle ACB = 40°$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-tangent-radius',
          difficulty: 'intro',
          instance: {
            prompt:
              'A tangent meets a radius at the point of tangency. What is the angle between them? Answer as a number.',
            answer: '90',
            answerType: 'numeric',
            hint: 'The tangent is perpendicular to the radius.',
            solution: [
              'A tangent is perpendicular to the radius at the point of tangency, so the angle is $90°$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cyclic-opposite',
          difficulty: 'core',
          instance: {
            prompt:
              '$ABCD$ is cyclic. $\\angle B = 65°$. Find $\\angle D$.',
            answer: '115',
            answerType: 'numeric',
            hint: 'Opposite angles of a cyclic quadrilateral sum to $180°$.',
            solution: [
              '$\\angle B + \\angle D = 180° \\Rightarrow \\angle D = 180° - 65° = 115°$.',
            ],
          },
        },
      ],
    },
  ],
}