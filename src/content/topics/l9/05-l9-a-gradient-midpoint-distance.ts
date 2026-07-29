import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Algebra · l9-a-4 (VC2M9A04).
// Gradient, midpoint and distance.

export const l9AGradientMidpointDistance: Topic = {
  id: 'l9-a-gradient-midpoint-distance',
  unit: 9,
  order: 5,
  title: 'Gradient, midpoint and distance',
  blurb:
    'Find the gradient of a line segment, the midpoint of the line interval, and the distance between 2 distinct points on the Cartesian plane.',
  dotPoints: ['l9-a-4'],

  lessons: [
    {
      id: 'gradient',
      heading: 'Gradient of a line segment',
      summary:
        'Rise over run: vertical change divided by horizontal change between two points.',
      body: `The **gradient** (slope) of a line segment tells you how steep it is — how much $y$ changes per unit of $x$.

### Formula
For two points $(x_1, y_1)$ and $(x_2, y_2)$ with $x_1 \\ne x_2$:
$$m = \\dfrac{y_2 - y_1}{x_2 - x_1}.$$

This is **rise over run**: vertical change on top, horizontal change on the bottom.

### Sign of the gradient
- $m > 0$: line goes **up** to the right.
- $m < 0$: line goes **down** to the right.
- $m = 0$: horizontal line (no vertical change).
- Vertical line ($x_1 = x_2$): gradient is **undefined** (you'd divide by zero).

### Why this works
The gradient is the same regardless of which two points on the line you pick. Try it: pick any two points on $y = 2x + 1$, compute the gradient — you always get $2$.`,
      examples: [
        {
          id: 'ex-gradient-2pts',
          statement:
            'Find the gradient of the line through $(1, 3)$ and $(5, 11)$.',
          steps: [
            '$m = \\dfrac{11 - 3}{5 - 1} = \\dfrac{8}{4} = 2$.',
            'Gradient $= 2$.',
          ],
        },
        {
          id: 'ex-gradient-neg',
          statement:
            'Find the gradient of the line through $(2, 7)$ and $(6, -1)$.',
          steps: [
            '$m = \\dfrac{-1 - 7}{6 - 2} = \\dfrac{-8}{4} = -2$.',
            'Gradient $= -2$ (line goes down to the right).',
          ],
        },
        {
          id: 'ex-horizontal',
          statement:
            'What is the gradient of the line through $(3, 4)$ and $(8, 4)$?',
          steps: [
            '$m = \\dfrac{4 - 4}{8 - 3} = \\dfrac{0}{5} = 0$.',
            'Horizontal line: gradient is $0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-gradient',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the gradient of the line through $(2, 1)$ and $(6, 9)$.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Gradient $= \\dfrac{y_2 - y_1}{x_2 - x_1}$.',
            solution: [
              '$m = \\dfrac{9 - 1}{6 - 2} = \\dfrac{8}{4} = 2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'midpoint',
      heading: 'Midpoint of a line interval',
      summary:
        'Average the $x$-coordinates and average the $y$-coordinates.',
      body: `The **midpoint** of the segment joining $(x_1, y_1)$ and $(x_2, y_2)$ is exactly halfway between them.

### Formula
$$M = \\left( \\dfrac{x_1 + x_2}{2}, \\ \\dfrac{y_1 + y_2}{2} \\right).$$

Just average the $x$'s and average the $y$'s. The midpoint is equidistant from both endpoints.

### When it helps
- Finding the centre of a circle through two points.
- Locating a point on a number line that's halfway between two markers.
- Geometry proofs that need a centre of symmetry.`,
      examples: [
        {
          id: 'ex-mid',
          statement:
            'Find the midpoint of $(2, 3)$ and $(8, 7)$.',
          steps: [
            '$M_x = \\dfrac{2 + 8}{2} = 5$.',
            '$M_y = \\dfrac{3 + 7}{2} = 5$.',
            'Midpoint: $(5, 5)$.',
          ],
        },
        {
          id: 'ex-mid-neg',
          statement:
            'Find the midpoint of $(-4, 2)$ and $(6, -8)$.',
          steps: [
            '$M_x = \\dfrac{-4 + 6}{2} = 1$.',
            '$M_y = \\dfrac{2 + (-8)}{2} = -3$.',
            'Midpoint: $(1, -3)$.',
          ],
        },
        {
          id: 'ex-endpoints',
          statement:
            'One endpoint is $(3, 5)$ and the midpoint is $(7, 4)$. Find the other endpoint.',
          steps: [
            'If $M = (7, 4) = \\left(\\tfrac{3 + x_2}{2}, \\tfrac{5 + y_2}{2}\\right)$.',
            '$\\tfrac{3 + x_2}{2} = 7 \\Rightarrow x_2 = 11$.',
            '$\\tfrac{5 + y_2}{2} = 4 \\Rightarrow y_2 = 3$.',
            'Other endpoint: $(11, 3)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-midpoint',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the midpoint of $(4, 6)$ and $(10, 2)$. State the $x$-coordinate of the midpoint.',
            answer: '7',
            answerType: 'numeric',
            hint: 'Midpoint $x = \\dfrac{x_1 + x_2}{2}$.',
            solution: [
              '$M_x = \\dfrac{4 + 10}{2} = 7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'distance',
      heading: 'Distance between two points',
      summary:
        'Apply Pythagoras: distance² = horizontal² + vertical².',
      body: `The **distance** between two points comes straight from Pythagoras' theorem.

### Distance formula
For two points $(x_1, y_1)$ and $(x_2, y_2)$:
$$d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.$$

This is the length of the hypotenuse of a right triangle whose legs are the horizontal change $|x_2 - x_1|$ and the vertical change $|y_2 - y_1|$.

### Always positive
The squares under the square root make every term non-negative, so $d \\ge 0$ — distance is never negative.

### Special cases
- Horizontal line: $y_1 = y_2$, so $d = |x_2 - x_1|$.
- Vertical line: $x_1 = x_2$, so $d = |y_2 - y_1|$.`,
      examples: [
        {
          id: 'ex-distance',
          statement:
            'Find the distance between $(1, 2)$ and $(4, 6)$.',
          steps: [
            'Horizontal change: $4 - 1 = 3$.',
            'Vertical change: $6 - 2 = 4$.',
            '$d = \\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$.',
          ],
        },
        {
          id: 'ex-distance-irrational',
          statement:
            'Find the distance between $(0, 0)$ and $(2, 3)$.',
          steps: [
            '$d = \\sqrt{(2 - 0)^2 + (3 - 0)^2} = \\sqrt{4 + 9} = \\sqrt{13}$.',
            '$\\sqrt{13}$ is irrational (since $13$ is not a perfect square).',
          ],
        },
        {
          id: 'ex-distance-horizontal',
          statement:
            'Find the distance between $(2, 5)$ and $(9, 5)$.',
          steps: [
            '$y$-coordinates match — horizontal line.',
            '$d = |9 - 2| = 7$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-distance',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the distance between $(0, 0)$ and $(3, 4)$.',
            answer: '5',
            answerType: 'numeric',
            hint: '$d = \\sqrt{3^2 + 4^2}$.',
            solution: [
              '$d = \\sqrt{9 + 16} = \\sqrt{25} = 5$.',
            ],
          },
        },
      ],
    },
  ],
}