import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-7 (VC2M7N07).
// Percentages of quantities.

export const l7NPercentages: Topic = {
  id: 'l7-n-percentages',
  unit: 7,
  order: 7,
  title: 'Percentages of quantities',
  blurb:
    'Calculate a percentage of a quantity and express one quantity as a percentage of another, with and without digital tools.',
  dotPoints: ['l7-n-7'],
  lessons: [
    {
      id: 'percentages-of-quantities',
      heading: 'Finding a percentage of a quantity',
      summary: 'Convert the percentage to a decimal or fraction, then multiply by the quantity.',
      body: `A **percentage** is a fraction with denominator $100$. The symbol % literally means "out of 100", so $45\\% = \\dfrac{45}{100} = 0.45$.

### Finding a percentage of a quantity
Three steps:
1. Convert the percentage to a **decimal** (divide by $100$) or a **fraction** (write over $100$).
2. **Multiply** by the quantity.
3. Round sensibly (to cents for money, to whole units for things you count).

**Mental shortcut**: $10\\%$ of any number is the number divided by $10$. Then build other percentages from $10\\%$:
- $1\\% = 10\\% \\div 10$
- $5\\% = 10\\% \\div 2$
- $20\\% = 10\\% \\times 2$
- $25\\% = $ divide by $4$
- $50\\% = $ divide by $2$

### Expressing one quantity as a percentage of another
Set up a fraction and multiply by $100$:
$$\\text{percentage} = \\frac{\\text{part}}{\\text{whole}} \\times 100\\%.$$
The "whole" is the quantity the part is being compared **to**.

> [!warning] Watch out
> The **whole** changes with the question. "$20$ as a percentage of $50$" gives $40\\%$; but "$50$ as a percentage of $20$" gives $250\\%$. Always identify the whole first.`,
      examples: [
        {
          id: 'ex-percent-of',
          statement: 'Find $15\\%$ of $\\$240$.',
          steps: [
            'Convert: $15\\% = 0.15$.',
            'Multiply: $0.15 \\times 240 = 36$.',
            'Result: $\\$36$.',
          ],
        },
        {
          id: 'ex-mental',
          statement: 'Find $20\\%$ of $\\$85$ using a mental strategy.',
          steps: [
            '$20\\% = \\dfrac{1}{5}$, so divide by $5$.',
            '$85 \\div 5 = 17$.',
            'Result: $\\$17$.',
          ],
        },
        {
          id: 'ex-as-percent',
          statement:
            'A class has $18$ students, and $12$ of them walk to school. What percentage walk to school?',
          steps: [
            'Whole = total students $= 18$. Part = walkers $= 12$.',
            'Set up the fraction: $\\dfrac{12}{18} = \\dfrac{2}{3}$.',
            'Convert to a percentage: $\\dfrac{2}{3} \\times 100\\% = 66.\\overline{6}\\% \\approx 66.7\\%$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-percent-of-60',
          difficulty: 'intro',
          instance: {
            prompt: 'Find $25\\%$ of $60$.',
            answer: '15',
            answerType: 'numeric',
            hint: '$25\\%$ is a quarter.',
            solution: [
              '$25\\% = \\dfrac{1}{4}$, so $60 \\div 4 = 15$.',
            ],
          },
        },
      ],
    },
  ],
}
