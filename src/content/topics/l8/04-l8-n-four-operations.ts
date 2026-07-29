import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Number · l8-n-4 (VC2M8N04).
// Use the 4 operations with integers and with rational numbers, choosing and
// using efficient mental and written strategies, and digital tools where
// appropriate, and making estimates for these computations.

export const l8NFourOperations: Topic = {
  id: 'l8-n-four-operations',
  unit: 8,
  order: 4,
  title: '4 operations with integers and rationals',
  blurb:
    'Apply the 4 operations with integers and rational numbers, choosing efficient mental and written strategies, and making estimates for these computations.',
  dotPoints: ['l8-n-4'],
  lessons: [
    {
      id: 'with-integers',
      heading: 'Efficient strategies with integers',
      summary:
        'Use sign rules, factors and place value to add, subtract, multiply and divide integers quickly and accurately.',
      body: `Working efficiently with integers means picking the **best strategy** for the numbers in front of you — not always reaching for a calculator or a long written method.

### Mental strategies
- **Compensation**: $99 \\times 7 = 100 \\times 7 - 1 \\times 7 = 700 - 7 = 693$.
- **Halving and doubling**: $15 \\times 16 = 30 \\times 8 = 240$.
- **Factor it out**: $24 \\times 15 = 12 \\times 2 \\times 15 = 12 \\times 30 = 360$.

### Sign rules
- **Multiplying / dividing** two with the **same** sign → positive.
- **Multiplying / dividing** two with **different** signs → negative.
- **Adding / subtracting**: think of subtraction as adding the opposite.

### Estimate first
Round each number to $1$ significant figure, then do the rough calculation. If the rough answer is very different from the calculator answer, you've made a slip.

> [!warning] Watch out
> A common slip is forgetting to keep a negative sign when subtracting: $5 - 12 = -7$, not $7$.`,
      examples: [
        {
          id: 'ex-mental-multiply',
          statement: 'Compute $25 \\times 32$ in your head.',
          steps: [
            'Rewrite $32 = 4 \\times 8$ so $25 \\times 4 = 100$ first.',
            '$25 \\times 4 = 100$.',
            'Then $100 \\times 8 = 800$.',
            'Result: $800$.',
          ],
        },
        {
          id: 'ex-signs',
          statement: 'Compute $-18 \\times (-3)$.',
          steps: [
            'Same sign (both negative) → positive result.',
            '$18 \\times 3 = 54$.',
            'Result: $54$.',
          ],
        },
        {
          id: 'ex-estimate',
          statement:
            'Estimate $52 \\times 71$ to one significant figure first, then compute the exact value.',
          steps: [
            'Round: $50 \\times 70 = 3500$. (Estimate: about $3500$.)',
            'Exact: $52 \\times 71 = 52 \\times 70 + 52 = 3640 + 52 = 3692$.',
            'Estimate is close to exact — the answer is sensible.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-mental',
          difficulty: 'intro',
          instance: {
            prompt: 'Compute $25 \\times 48$ in your head.',
            answer: '1200',
            answerType: 'numeric',
            hint: 'Try $25 \\times 4 \\times 12$ — start with the easy $25 \\times 4 = 100$.',
            solution: [
              '$25 \\times 4 = 100$, then $100 \\times 12 = 1200$.',
            ],
          },
        },
      ],
    },
    {
      id: 'with-rationals',
      heading: 'Efficient strategies with rationals',
      summary:
        'Convert to a common form, then apply the matching integer strategy; estimates catch mistakes quickly.',
      body: `A **rational number** is anything that can be written as $\\dfrac{p}{q}$ for integers $p, q$ with $q \\ne 0$. This includes fractions, terminating decimals and recurring decimals. The trick with rationals is to **convert to one form** first, then apply the integer strategy.

### Two key moves
- **Convert a fraction to a decimal** when the denominator is a power of $10$: $\\dfrac{3}{4} = 0.75$, $\\dfrac{7}{20} = 0.35$.
- **Convert a decimal to a fraction** when you need an exact answer: $0.6 = \\dfrac{3}{5}$.

### Order of operations with rationals
PEMDAS still applies — brackets first, then powers, then multiplication/division (left to right), then addition/subtraction (left to right).

### Why estimate
Estimating catches careless slips. $0.51 \\times 9.7$ is roughly $0.5 \\times 10 = 5$. If your answer comes out as $50$ or $0.5$, you've gone wrong.

> [!definition] Significant figure
> A **significant figure** is a digit that contributes to the precision of a number. In $52$ both digits are significant; in $0.071$ only the $7$ and $1$ are significant.`,
      examples: [
        {
          id: 'ex-rational-mix',
          statement: 'Compute $\\dfrac{3}{4} + 0.5$.',
          steps: [
            'Convert $\\dfrac{3}{4} = 0.75$.',
            'Then $0.75 + 0.5 = 1.25$.',
          ],
        },
        {
          id: 'ex-rational-product',
          statement: 'Compute $\\dfrac{2}{5} \\times 35$.',
          steps: [
            '$\\dfrac{2}{5} \\times 35 = \\dfrac{2 \\times 35}{5} = \\dfrac{70}{5} = 14$.',
            'Or think of $\\dfrac{35}{5} = 7$ first, then $7 \\times 2 = 14$.',
          ],
        },
        {
          id: 'ex-estimate',
          statement:
            'Estimate $4.9 \\times 21$ to one significant figure per number.',
          steps: [
            'Round: $5 \\times 20 = 100$.',
            'Estimate: about $100$.',
            'Exact: $4.9 \\times 21 = 102.9$ — close to the estimate, so the answer is sensible.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-rational-mix',
          difficulty: 'intro',
          instance: {
            prompt: 'Compute $\\dfrac{1}{4} + 0.5$.',
            answer: '0.75',
            answerType: 'numeric',
            hint: 'Convert $\\dfrac{1}{4}$ to a decimal first.',
            solution: [
              '$\\dfrac{1}{4} = 0.25$, then $0.25 + 0.5 = 0.75$.',
            ],
          },
        },
      ],
    },
  ],
}
