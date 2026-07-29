import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Measurement · l7-m-6 (VC2M7M06).
// Use mathematical modelling to solve practical problems involving ratios
// of lengths, areas and volumes.

export const l7MModellingRatios: Topic = {
  id: 'l7-m-modelling-ratios',
  unit: 7,
  order: 22,
  title: 'Modelling with ratios of lengths, areas and volumes',
  blurb:
    'Use mathematical modelling to solve practical problems involving ratios of lengths, areas and volumes in real-world contexts.',
  dotPoints: ['l7-m-6'],
  lessons: [
    {
      id: 'ratio-of-lengths',
      heading: 'Ratios of lengths',
      summary:
        'A linear scale factor between two shapes makes each length change by that factor.',
      body: `When two shapes are mathematical **similar**, every length on the smaller one is multiplied by the same number (the **scale factor**) to get the corresponding length on the larger one.

### The rule for lengths
If the scale factor is $k$, then for every length $L$ on one shape:

$$L_{\\text{large}} = k \\times L_{\\text{small}}.$$

This is a **direct ratio**: $L_{\\text{large}} : L_{\\text{small}} = k : 1$.

### Where this shows up
- Map scales: $1 : 50\\,000$ means every $1$ cm on the map is $50\\,000$ cm (or $500$ m) in real life.
- Scale models: a model plane at scale $1 : 48$ is $48$ times smaller than the real plane in every dimension.
- Enlargements on a photocopier: $140\%$ means every length is multiplied by $1.4$.

### Quick checks
- A $12$ cm pencil at scale $1 : 3$ becomes a $36$ cm pencil model.
- A $50$ m real fence at scale $1 : 200$ becomes a $25$ cm line on a plan.

> [!definition] Direct ratio
> $a : b = c : d$ means $\\dfrac{a}{b} = \\dfrac{c}{d}$. With length scale factor $k$, every length ratio stays $k$ to $1$.`,
      examples: [
        {
          id: 'ex-map',
          statement:
            'A map has scale $1 : 25\\,000$. Two towns are $6$ cm apart on the map. How far apart are they in real life, in metres?',
          steps: [
            'Scale factor $25\\,000$.',
            'Real distance: $6 \\times 25\\,000 = 150\\,000$ cm.',
            'Convert: $150\\,000$ cm $= 1500$ m.',
          ],
        },
        {
          id: 'ex-model-plane',
          statement:
            'A model plane is built at scale $1 : 48$. Its wingspan is $36$ cm. What is the real wingspan (in metres)?',
          steps: [
            "Real length $= 48 \\times 36 = 1728$ cm.",
            'Convert: $1728$ cm $= 17.28$ m.',
          ],
        },
        {
          id: 'ex-enlargement',
          statement:
            'A photocopier is set to $140\\%$. A line $5$ cm long is copied. What is the length of the copy (in cm)?',
          steps: [
            "$140\\%$ means scale factor $1.4$.",
            'New length $= 1.4 \\times 5 = 7$ cm.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-scale-map',
          difficulty: 'intro',
          instance: {
            prompt:
              'A map has scale $1 : 50\\,000$. Two points are $4$ cm apart on the map. How far apart are they in real life (in metres)?',
            answer: '2000',
            answerType: 'numeric',
            hint: 'Real length = $4 \\times 50\\,000$ cm, then convert to metres.',
            solution: [
              '$4 \\times 50\\,000 = 200\\,000$ cm $= 2000$ m.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-enlargement',
          difficulty: 'core',
          instance: {
            prompt:
              'A rectangle is enlarged by a scale factor of $3$. A side of original length $7$ cm becomes how long (in cm)?',
            answer: '21',
            answerType: 'numeric',
            hint: 'Multiply the original length by the scale factor.',
            solution: [
              '$3 \\times 7 = 21$ cm.',
            ],
          },
        },
      ],
    },
    {
      id: 'ratio-areas-volumes',
      heading: 'Ratios of areas and volumes',
      summary:
        'Areas scale with the square of the linear factor; volumes scale with the cube.',
      body: `Same shape, two sizes. Once you know the linear scale factor $k$, you can read off the **area ratio** and the **volume ratio** without measuring each face again.

### Areas scale with $k^2$
If you double every length (so $k = 2$), the new shape fits $2 \\times 2 = 4$ of the old shape inside it. So

$$\\dfrac{\\text{area of large}}{\\text{area of small}} = k^2 : 1.$$

- A square of side $3$ cm has area $9$ cm². A square of side $6$ cm ($k = 2$) has area $36$ cm². Note $36 / 9 = 4 = 2^2$.
- A triangle of base $4$, height $3$ has area $6$. The version with base $8$, height $6$ has area $24$. Ratio $24 / 6 = 4 = 2^2$.

### Volumes scale with $k^3$
Double every length ($k = 2$) and the new shape has $2 \\times 2 \\times 2 = 8$ times the volume:

$$\\dfrac{\\text{volume of large}}{\\text{volume of small}} = k^3 : 1.$$

- A $2$ cm cube has volume $8$ cm³. A $4$ cm cube has volume $64$ cm³. Ratio $64 / 8 = 8 = 2^3$.

> [!warning] Don't mix up $k^2$ and $k^3$
> A bigger area means bigger **lengths squared**, not bigger lengths cubed. Check: a $3$ m × $4$ m rug has area $12$ m²; a rug with each side $2$ times longer has area $48$ m² = $4 \\times 12$, exactly $2^2$ times — not $2^3$.

### Modelling recipe
1. Identify the linear scale factor $k$ between the two shapes.
2. Multiply the length ratio by $k$ for length questions.
3. Multiply the area ratio by $k^2$ for area questions.
4. Multiply the volume ratio by $k^3$ for volume questions.`,
      examples: [
        {
          id: 'ex-area-from-scale',
          statement:
            'A small rectangle has area $20$ cm². A similar rectangle is scaled by a linear factor $k = 3$. What is the new area?',
          steps: [
            'Area scales by $k^2$.',
            'New area $= 3^2 \\times 20 = 9 \\times 20 = 180$ cm².',
          ],
        },
        {
          id: 'ex-volume-from-scale',
          statement:
            'A small box has volume $500$ cm³. A similar box is built with linear scale factor $k = 2$. What is the new volume?',
          steps: [
            'Volume scales by $k^3$.',
            'New volume $= 2^3 \\times 500 = 8 \\times 500 = 4000$ cm³.',
          ],
        },
        {
          id: 'ex-actual-from-scale',
          statement:
            'A scale model of a tank is at $1 : 10$. The model holds $0.4$ L of water (modelling the real tank at full). How much does the real tank hold, in litres?',
          steps: [
            "Linear scale factor $k = 10$.",
            'Volume scale factor $k^3 = 1000$.',
            'Real volume $= 1000 \\times 0.4 = 400$ L.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-area-scale',
          difficulty: 'core',
          instance: {
            prompt:
              'A small shape has area $12$ cm². A similar shape is enlarged by linear scale factor $k = 4$. What is its new area (in cm²)?',
            answer: '192',
            answerType: 'numeric',
            hint: 'Areas scale by $k^2$.',
            solution: [
              '$4^2 \\times 12 = 16 \\times 12 = 192$ cm².',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-volume-scale',
          difficulty: 'core',
          instance: {
            prompt:
              'A small cube has volume $5$ cm³. A similar cube is built with linear scale factor $k = 3$. What is the new volume (in cm³)?',
            answer: '135',
            answerType: 'numeric',
            hint: 'Volumes scale by $k^3$.',
            solution: [
              '$3^3 \\times 5 = 27 \\times 5 = 135$ cm³.',
            ],
          },
        },
      ],
    },
  ],
}
