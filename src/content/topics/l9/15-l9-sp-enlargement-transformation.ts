import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Space · l9-sp-2 (VC2M9SP02).
// Enlargement transformation.

export const l9SpEnlargementTransformation: Topic = {
  id: 'l9-sp-enlargement-transformation',
  unit: 9,
  order: 15,
  title: 'Enlargement transformation',
  blurb:
    'Apply the enlargement transformation to shapes and objects using dynamic geometry software, and identify what stays the same and what changes using the language of similarity, ratio and scale.',
  dotPoints: ['l9-sp-2'],

  lessons: [
    {
      id: 'enlargement-basics',
      heading: 'Enlargement with a scale factor',
      summary: 'Every point is moved along a ray from the centre of enlargement by a scale factor; the shape stays similar.',
      body: `An **enlargement** is a transformation that produces a similar shape, scaled by some factor $k$ about a **centre of enlargement** $C$.

### Recipe
1. Pick the **centre of enlargement** $C$ (a point).
2. Pick the **scale factor** $k$ (any non-zero real number).
3. For each point $P$ in the original, the new point $P'$ lies on the ray from $C$ through $P$, with $CP' = k \\cdot CP$.

### What stays the same, what changes
- **Same**: shape (angles), orientation (for $k > 0$), each point's ray from $C$.
- **Changes**: every length by the factor $k$; areas by $k^2$; volumes by $k^3$.
- **Sign of $k$**: $k > 0$ keeps the point on the same side of $C$; $k < 0$ puts it on the opposite side.`,
      examples: [
        {
          id: 'ex-scale-2',
          statement:
            'Triangle $ABC$ has vertices $A(1,1), B(3,1), C(2,3)$. Apply an enlargement centred at the origin with scale factor $2$. What are the new coordinates?',
          steps: [
            'Multiply each coordinate by $2$.',
            "$A' = (2, 2), B' = (6, 2), C' = (4, 6)$.",
          ],
        },
        {
          id: 'ex-scale-frac',
          statement:
            'A square of side $10$ cm is enlarged by scale factor $0.5$. What is the perimeter and area of the image?',
          steps: [
            'New side: $10 \\times 0.5 = 5$ cm. Perimeter: $4 \\times 5 = 20$ cm.',
            'New area: $5^2 = 25$ cm². (Original was $100$ cm² — quarter of it, i.e. $k^2 = 0.25$.)',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-enlarge-coords',
          difficulty: 'intro',
          instance: {
            prompt:
              'Point $P(2, 3)$ is enlarged about the origin with scale factor $4$. What are the new coordinates (as "x, y")?',
            answer: '8, 12',
            answerType: 'exact',
            hint: 'Multiply each coordinate by the scale factor.',
            solution: [
              "$(2 \\times 4, 3 \\times 4) = (8, 12)$.",
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-enlarge-area',
          difficulty: 'core',
          instance: {
            prompt:
              'A shape with area $20$ cm² is enlarged by scale factor $3$. What is the area of the image (in cm²)?',
            answer: '180',
            answerType: 'numeric',
            hint: 'Areas scale by $k^2$.',
            solution: [
              '$20 \\times 3^2 = 20 \\times 9 = 180$ cm².',
            ],
          },
        },
      ],
    },

    {
      id: 'similarity-aspects',
      heading: 'What stays the same and what changes',
      summary: 'Enlargements preserve angles, shape and orientation; lengths, areas and volumes scale by powers of $k$.',
      body: `An enlargement preserves the **shape** of an object — angles are unchanged, parallel lines stay parallel, a circle stays a circle. This is what makes the image **similar** to the original.

### Quantities that change
- Each **length** is multiplied by $|k|$.
- Each **area** is multiplied by $k^2$.
- Each **volume** is multiplied by $k^3$.

### Why area scales by $k^2$
A $k \\times k$ square of area $1$ becomes a $1 \\times 1$ square of area $k^2$ (count the little $k \\times k$ tiles).

### Why volume scales by $k^3$
A $k \\times k \\times k$ cube of volume $1$ is filled with $k^3$ unit cubes.`,
      examples: [
        {
          id: 'ex-perimeter',
          statement:
            'A triangle has perimeter $12$ cm. After an enlargement by scale factor $5$, what is its perimeter?',
          steps: [
            'Each side becomes $5$ times longer, so the perimeter is multiplied by $5$: $12 \\times 5 = 60$ cm.',
          ],
        },
        {
          id: 'ex-volume',
          statement:
            'A solid of volume $40$ cm³ is enlarged by scale factor $2$. What is the new volume?',
          steps: [
            'Volumes scale by $k^3 = 2^3 = 8$.',
            '$40 \\times 8 = 320$ cm³.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-perim',
          difficulty: 'intro',
          instance: {
            prompt:
              'A pentagon has perimeter $30$ cm. After an enlargement by scale factor $4$, what is its perimeter?',
            answer: '120',
            answerType: 'numeric',
            hint: 'Perimeter scales by $k$ (one-dimensional).',
            solution: [
              '$30 \\times 4 = 120$ cm.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-volume',
          difficulty: 'core',
          instance: {
            prompt:
              'A sphere has volume $500$ cm³. After enlargement by scale factor $2$, what is the new volume?',
            answer: '4000',
            answerType: 'numeric',
            hint: 'Volumes scale by $k^3$.',
            solution: [
              '$500 \\times 2^3 = 500 \\times 8 = 4000$ cm³.',
            ],
          },
        },
      ],
    },
  ],
}
