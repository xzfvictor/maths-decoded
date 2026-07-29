import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Space · l8-sp-3 (VC2M8SP03).
// Describe in different ways the position and location of three-dimensional
// objects in 3 dimensions, including using a 3D Cartesian coordinate system
// with the use of dynamic geometry software or other digital tools.

export const l8Sp3dCoordinates: Topic = {
  id: 'l8-sp-3d-coordinates',
  unit: 8,
  order: 21,
  title: '3D coordinate systems',
  blurb:
    'Locate and describe the position of three-dimensional objects using a 3D Cartesian coordinate system, with the help of dynamic geometry software.',
  dotPoints: ['l8-sp-3'],

  lessons: [
    {
      id: 'three-dimensional-cartesian',
      heading: 'The 3D Cartesian coordinate system',
      summary:
        'Three perpendicular axes — $x$, $y$, $z$ — locate a point in space as an ordered triple $(x, y, z)$.',
      body: `A 2D Cartesian plane uses **two** perpendicular axes ($x$ and $y$) to describe a point as an ordered pair $(x, y)$. To describe a point in space we need a **third** axis.

### The three axes
- The **$x$-axis** runs left-right (east-west).
- The **$y$-axis** runs forward-backward (north-south).
- The **$z$-axis** runs up-down.
- All three axes are perpendicular to each other and meet at the **origin** $O(0, 0, 0)$.

The three axes split space into **eight octants** (just as the two axes split the plane into four quadrants). We usually work in the **first octant**, where $x \\ge 0$, $y \\ge 0$ and $z \\ge 0$.

### Points in 3D
A point is written as an **ordered triple** $(x, y, z)$:
- $x$ — how far along the $x$-axis.
- $y$ — how far along the $y$-axis.
- $z$ — how far up (or down) along the $z$-axis.

The order matters — $(2, 3, 4)$ and $(3, 2, 4)$ are different points.

### Comparing 2D and 3D
- In 2D, an ordered pair gives the column then the row.
- In 3D, an ordered triple gives the **$x$-coordinate first**, then the **$y$-coordinate**, then the **$z$-coordinate**.
- A 2D point $(x, y)$ becomes the 3D point $(x, y, 0)$ — it lies in the floor plane.

> [!warning] Watch out
> Conventions differ: some software uses $(x, y, z)$ with $z$ up; games and maps often use $(x, y, z)$ with $y$ up. Always check the axis labels on the diagram before reading coordinates.

### Real-world 3D coordinates
- **Latitude, longitude, altitude** locate an aircraft or drone in the air.
- **Floor, row, seat** locate a person in a stadium or theatre.
- **Floor, zone, bay** locate a car in a multistorey car park.
- **3D printing software** describes every vertex of a model with a triple so the printer knows where to extrude.`,
      examples: [
        {
          id: 'ex-read-triple',
          statement:
            'A point $P$ is $4$ units along the $x$-axis, $2$ units along the $y$-axis, and $5$ units up the $z$-axis. Write $P$ as an ordered triple.',
          steps: [
            '$x$-coordinate first: $4$.',
            '$y$-coordinate next: $2$.',
            '$z$-coordinate last: $5$.',
            'So $P = (4, 2, 5)$.',
          ],
        },
        {
          id: 'ex-octant',
          statement:
            'A point has coordinates $(3, -2, 5)$. Which octant is it in?',
          steps: [
            'Signs: $x = 3 > 0$, $y = -2 < 0$, $z = 5 > 0$.',
            'Two positive coordinates and one negative — it lies in the octant with signs $(+, -, +)$.',
          ],
        },
        {
          id: 'ex-missing-coordinate',
          statement:
            'A box has corners at $(0,0,0)$, $(6,0,0)$, $(0,4,0)$ and $(0,0,3)$. What is the coordinate of the corner diagonally opposite the origin?',
          steps: [
            'The box runs $0 \\to 6$ in $x$, $0 \\to 4$ in $y$, $0 \\to 3$ in $z$.',
            'The opposite corner takes the **largest** $x$, $y$ and $z$ values.',
            'So it is at $(6, 4, 3)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-first-octant',
          difficulty: 'intro',
          instance: {
            prompt:
              'A point has all three coordinates positive. Which octant is it in? (One word: first, second, third, etc.)',
            answer: 'first',
            answerType: 'exact',
            hint: 'When $x > 0$, $y > 0$ and $z > 0$, the point sits in the octant nearest the +$x$, +$y$, +$z$ corner.',
            solution: [
              'All three coordinates positive places the point in the **first** octant.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-missing-z',
          difficulty: 'core',
          instance: {
            prompt:
              'A point lies in the $xy$-plane (so $z = 0$) at $(5, -2, z)$. What is the value of $z$?',
            answer: '0',
            answerType: 'numeric',
            hint: 'Any point in the $xy$-plane has $z = 0$.',
            solution: [
              'Points in the $xy$-plane lie at height $z = 0$, so $z = 0$.',
            ],
          },
        },
      ],
    },
  ],
}