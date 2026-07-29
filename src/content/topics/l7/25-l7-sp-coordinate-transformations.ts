import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Space · l7-sp-3 (VC2M7SP03).
// Describe translations, reflections in an axis, and rotations about the
// origin in the Cartesian plane.

export const l7SpCoordinateTransformations: Topic = {
  id: 'l7-sp-coordinate-transformations',
  unit: 7,
  order: 25,
  title: 'Coordinate transformations',
  blurb:
    'Describe translations, reflections in an axis, and rotations about the origin in the Cartesian plane.',
  dotPoints: ['l7-sp-3'],
  lessons: [
    {
      id: 'translations',
      heading: 'Translations',
      summary:
        'Slide every point of a shape by the same horizontal and vertical shift — the size and orientation do not change.',
      body: `A **translation** slides a shape to a new position without rotating or resizing it. Every point moves by the same horizontal and vertical amount.

### How to translate

To translate a point $(x, y)$ by $a$ units right and $b$ units up:
$$(x, y) \\to (x + a, \\ y + b).$$

- $a > 0$ moves right; $a < 0$ moves left.
- $b > 0$ moves up; $b < 0$ moves down.

### Apply it to a whole shape

Translate **every vertex** by the same $(a, b)$ — connecting the new vertices gives the translated shape. The original and the translation are **congruent** (same size, same orientation).

> [!definition] Translation rule
> $(x, y) \\to (x + a, \\ y + b)$ where $a$ is the horizontal shift and $b$ is the vertical shift.`,
      examples: [
        {
          id: 'ex-translate-point',
          statement:
            'Translate the point $(3, 5)$ by $4$ units left and $2$ units down.',
          steps: [
            '$a = -4$ (left) and $b = -2$ (down).',
            'New point: $(3 + (-4), \\ 5 + (-2)) = (-1, 3)$.',
          ],
        },
        {
          id: 'ex-translate-triangle',
          statement:
            'A triangle has vertices $(1, 1)$, $(4, 1)$ and $(1, 5)$. Translate it by $3$ right and $2$ up. List the new vertices.',
          steps: [
            'Add $3$ to every $x$-coordinate and $2$ to every $y$-coordinate.',
            '$(1, 1) \\to (4, 3)$.',
            '$(4, 1) \\to (7, 3)$.',
            '$(1, 5) \\to (4, 7)$.',
          ],
        },
        {
          id: 'ex-translate-negative',
          statement:
            'Translate the point $(-2, 4)$ by $5$ units right and $1$ unit up.',
          steps: [
            'Apply $(x, y) \\to (x + 5, y + 1)$.',
            '$(-2 + 5, 4 + 1) = (3, 5)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-translate-point',
          difficulty: 'intro',
          instance: {
            prompt:
              'Translate the point $(2, 7)$ by $5$ units right and $3$ units down. Give the new point as "x,y".',
            answer: '7,4',
            answerType: 'exact',
            hint: 'Add $5$ to the $x$-coordinate and $-3$ to the $y$-coordinate.',
            solution: [
              '$(2 + 5, \\ 7 + (-3)) = (7, 4)$.',
            ],
          },
        },
      ],
    },

    {
      id: 'reflections-and-rotations',
      heading: 'Reflections in an axis and rotations about the origin',
      summary:
        'Flip a shape across the $x$- or $y$-axis (reflections), or rotate it about the origin by $90°$ or $180°$.',
      body: `Translations slide a shape. **Reflections** flip it across a line, and **rotations** turn it around a fixed point.

### Reflections in the axes

**Reflection in the $x$-axis** — flip up/down across the horizontal axis. The $x$-coordinate stays the same; the $y$-coordinate changes sign.
$$(x, y) \\to (x, -y).$$

**Reflection in the $y$-axis** — flip left/right across the vertical axis. The $y$-coordinate stays the same; the $x$-coordinate changes sign.
$$(x, y) \\to (-x, y).$$

### Rotations about the origin

Rotating about the origin (the point $(0, 0)$) by:
- $90°$ **clockwise**: $(x, y) \\to (y, -x)$.
- $90°$ **counter-clockwise** (or anti-clockwise): $(x, y) \\to (-y, x)$.
- $180°$ (either direction): $(x, y) \\to (-x, -y)$.

### Comparing the three

- **Translation**: orientation stays the same — text reads the same way.
- **Reflection**: orientation reverses — text becomes mirror-image.
- **Rotation**: orientation rotates by the turn angle — text reads a different way depending on the angle.

> [!warning] Watch the order
> For a $90°$ rotation, the rule depends on **direction**. Clockwise and counter-clockwise give different results.`,
      examples: [
        {
          id: 'ex-reflect-x',
          statement:
            'Reflect the point $(3, -2)$ in the $x$-axis.',
          steps: [
            'Reflection in the $x$-axis: $(x, y) \\to (x, -y)$.',
            '$(3, -2) \\to (3, 2)$.',
          ],
        },
        {
          id: 'ex-reflect-y',
          statement:
            'Reflect the point $(-5, 4)$ in the $y$-axis.',
          steps: [
            'Reflection in the $y$-axis: $(x, y) \\to (-x, y)$.',
            '$(-5, 4) \\to (5, 4)$.',
          ],
        },
        {
          id: 'ex-rotate-180',
          statement:
            'Rotate the point $(3, -1)$ by $180°$ about the origin.',
          steps: [
            'A $180°$ rotation sends $(x, y) \\to (-x, -y)$.',
            '$(3, -1) \\to (-3, 1)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-reflect-x-axis',
          difficulty: 'intro',
          instance: {
            prompt:
              'Reflect the point $(-2, 6)$ in the $x$-axis. Give the new point as "x,y".',
            answer: '-2,-6',
            answerType: 'exact',
            hint: 'Reflection in the $x$-axis: $(x, y) \\to (x, -y)$.',
            solution: [
              '$(-2, 6) \\to (-2, -6)$.',
            ],
          },
        },
      ],
    },
  ],
}
