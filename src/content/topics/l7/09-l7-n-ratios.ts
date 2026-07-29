import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-9 (VC2M7N09).
// Ratios.

export const l7NRatios: Topic = {
  id: 'l7-n-ratios',
  unit: 7,
  order: 9,
  title: 'Ratios',
  blurb:
    'Recognise, represent and solve problems involving ratios — including part–part and part–whole relations.',
  dotPoints: ['l7-n-9'],
  lessons: [
    {
      id: 'ratios-part-whole',
      heading: 'Recognising and solving problems with ratios',
      summary: 'A ratio compares two or more quantities; use the unit value to share or scale.',
      body: `A **ratio** compares two or more quantities, showing how much of each there is relative to the others. A ratio of $1:4$ means "for every $1$ of the first, there are $4$ of the second".

### Two kinds of ratio
- **Part-to-part**: compares one part with another. If a recipe uses $2$ cups of flour and $1$ cup of sugar, the part-to-part ratio is $2:1$.
- **Part-to-whole**: compares one part with the **sum** of all parts. In the same recipe, flour is $2$ parts out of $3$ total, so the part-to-whole ratio is $2:3$.

### Representing ratios
Ratios can be written several equivalent ways:
- $2:3$
- $2$ to $3$
- $\\dfrac{2}{3}$ (only if the ratio has two parts)

### Simplifying ratios
Divide every number in the ratio by their HCF. The ratio $6:9$ simplifies to $2:3$ because HCF $= 3$.

### Solving ratio problems
The **unit value** is what one "part" is worth. To find it, divide the total by the number of parts.

Example: sharing $\$45$ in the ratio $2:3$ has $5$ parts in total. Unit value $= 45 \\div 5 = 9$. First share $= 2 \\times 9 = \\$18$, second share $= 3 \\times 9 = \\$27$.

> [!warning] Watch out
> Order matters in a ratio. $1:2$ is **not** the same as $2:1$ — the first number always refers to the first quantity mentioned.`,
      examples: [
        {
          id: 'ex-simplify',
          statement: 'Simplify the ratio $18:24$.',
          steps: [
            'Find the HCF of $18$ and $24$. $18 = 2 \\times 3^2$, $24 = 2^3 \\times 3$, so HCF $= 2 \\times 3 = 6$.',
            'Divide each by $6$: $18 \\div 6 = 3$, $24 \\div 6 = 4$.',
            'Result: $3:4$.',
          ],
        },
        {
          id: 'ex-divide-ratio',
          statement:
            'A length of ribbon is $90\\text{ cm}$ long and is cut into two pieces in the ratio $2:7$. How long is the longer piece?',
          steps: [
            'Total number of parts: $2 + 7 = 9$.',
            'Unit value: $90 \\div 9 = 10\\text{ cm}$ per part.',
            'Longer piece: $7 \\times 10 = 70\\text{ cm}$.',
          ],
        },
        {
          id: 'ex-scale-up',
          statement:
            'A recipe for $4$ people needs $300\\text{ g}$ of rice. How much rice is needed for $10$ people?',
          steps: [
            'Set up the ratio of people to rice: $4:300$.',
            'Unit value: $300 \\div 4 = 75\\text{ g}$ per person.',
            'For $10$ people: $10 \\times 75 = 750\\text{ g}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-simplify-ratio',
          difficulty: 'intro',
          instance: {
            prompt: 'Simplify the ratio $15:25$. Enter as "a:b".',
            answer: '3:5',
            answerType: 'exact',
            hint: 'Divide both by the HCF.',
            solution: [
              'HCF of $15$ and $25$ is $5$, so $15:25 = 3:5$.',
            ],
          },
        },
      ],
    },
  ],
}
