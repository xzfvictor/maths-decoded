import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-4 (VC2M7N04).
// Rounding and estimation to check reasonableness.

export const l7NRoundingEstimation: Topic = {
  id: 'l7-n-rounding-estimation',
  unit: 7,
  order: 4,
  title: 'Rounding and estimation',
  blurb:
    'Round to a given accuracy and use estimates to sanity-check whether an answer is in the right ballpark.',
  dotPoints: ['l7-n-4'],
  lessons: [
    {
      id: 'rounding-and-estimation',
      heading: 'Rounding decimals and estimating answers',
      summary: 'Round to the accuracy the question asks for, then use a rough estimate to check the answer.',
      body: `Rounding shortens a number without losing the big picture. The right **accuracy** depends on what the answer is used for — money to the nearest cent, paint quantities to the nearest whole litre, a renovation budget to the nearest hundred dollars.

### How to round
1. Find the digit just to the right of the rounding place.
2. If that digit is $5$ or more, **round up** (the rounding-place digit increases by $1$).
3. If that digit is less than $5$, **round down** (the rounding-place digit stays).
4. Drop every digit to the right of the rounding place.

> [!definition] "5 or more, raise the score"
> A common way to remember: any digit $5, 6, 7, 8, 9$ rounds the place up; $0, 1, 2, 3, 4$ round it down.

### Choosing the right accuracy
- **Money**: round to the nearest cent ($2$ decimal places).
- **Paint, fencing, anything sold by the whole unit**: round **up** so you do not run short.
- **House renovation estimate**: nearest $\$100$ is precise enough.
- **Scientific measurements**: match the precision of the least-precise input.

### Estimation as a reasonableness check
Round every number to **one** significant figure, then do the calculation mentally. Compare the estimate to the actual answer — if the actual answer is wildly different, redo the work.

> [!warning] Watch out
> Estimation is for **checking**, not for **answering**. A question asking for a specific accuracy expects a specific answer.`,
      examples: [
        {
          id: 'ex-round-2dp',
          statement: 'Round $3.4762$ to $2$ decimal places.',
          steps: [
            'The $2$nd-decimal-place digit is $7$. Look at the next digit: $6$.',
            '$6 \\ge 5$, so round the $7$ up to $8$.',
            'Result: $3.48$.',
          ],
        },
        {
          id: 'ex-round-up-paint',
          statement:
            'A wall needs exactly $3.21$ litres of paint. How many whole litres should you buy?',
          steps: [
            'Paint is sold by the whole litre, and buying less than you need is the worse mistake.',
            'Round **up**: $3.21$ rounds up to $4$ litres.',
            'Result: buy $4$ litres.',
          ],
        },
        {
          id: 'ex-estimate',
          statement:
            'A bill comes to $\\$47.80$ and you want to leave a $15\\%$ tip. Estimate the total to the nearest dollar.',
          steps: [
            'Round each input: $\\$47.80 \\approx \\$50$, $15\\% \\approx \\frac{1}{5}$ (one-fifth).',
            'Tip estimate: $15\\% \\times \\$50 \\approx \\frac{1}{5} \\times \\$50 = \\$10$.',
            'Total estimate: $\\$50 + \\$10 = \\$60$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-round-1dp',
          difficulty: 'intro',
          instance: {
            prompt: 'Round $14.347$ to $1$ decimal place.',
            answer: '14.3',
            answerType: 'numeric',
            hint: 'Look at the second decimal place.',
            solution: [
              'The first-decimal-place digit is $3$. The next digit is $4$, which is less than $5$, so round down.',
              'Result: $14.3$.',
            ],
          },
        },
      ],
    },
  ],
}
