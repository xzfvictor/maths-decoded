import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-6 (VC2M7N06).
// The 4 operations with positive rational numbers.

export const l7NFourOperationsRationals: Topic = {
  id: 'l7-n-four-operations-rationals',
  unit: 7,
  order: 6,
  title: '4 operations with positive rationals',
  blurb:
    'Use addition, subtraction, multiplication and division with fractions and decimals in problem solving.',
  dotPoints: ['l7-n-6'],
  lessons: [
    {
      id: 'four-operations-positive-rationals',
      heading: 'The 4 operations with positive rationals',
      summary: 'Use common denominators to add/subtract and inverse operations to multiply/divide.',
      body: `**Rational numbers** are numbers that can be written as a fraction $\\dfrac{a}{b}$ with $a, b$ integers and $b \\ne 0$. That includes all fractions, all decimals (terminating and repeating) and all whole numbers.

### Adding and subtracting fractions
You need a **common denominator** — multiply top and bottom of each fraction to reach the LCM of the denominators, then add or subtract the numerators.
$$\\frac{1}{4} + \\frac{2}{3} = \\frac{3}{12} + \\frac{8}{12} = \\frac{11}{12}.$$

### Adding and subtracting decimals
Line up the **decimal points** and add or subtract column by column, carrying as needed.
$2.4 + 0.76 = 3.16$.

### Multiplying and dividing
Use the rules from the previous lesson:
- Fractions × fractions: $\\dfrac{a}{b} \\times \\dfrac{c}{d} = \\dfrac{ac}{bd}$ (cancel first if you can).
- Fractions ÷ fractions: keep, change, flip.
- Decimals: count decimal places (×) or shift both (÷).

### Choosing an efficient strategy
- **Mental**: compatible numbers, halving, doubling, partitioning ($2.5 \\times 8 = 20$ via $2.5 \\times 2 \\times 4$).
- **Written**: common denominators, column addition, place-value.
- **Digital**: a calculator for long or awkward calculations.
- **Estimation**: one-significant-figure check, every time.

> [!warning] Watch out
> When you add or subtract fractions, **never** add the denominators. $\\dfrac{1}{2} + \\dfrac{1}{3}$ is not $\\dfrac{2}{5}$.`,
      examples: [
        {
          id: 'ex-add-fractions',
          statement: 'Find $\\dfrac{5}{6} + \\dfrac{3}{4}$.',
          steps: [
            'LCM of $6$ and $4$ is $12$.',
            'Convert: $\\dfrac{5}{6} = \\dfrac{10}{12}$, $\\dfrac{3}{4} = \\dfrac{9}{12}$.',
            'Add numerators: $\\dfrac{10 + 9}{12} = \\dfrac{19}{12} = 1\\dfrac{7}{12}$.',
          ],
        },
        {
          id: 'ex-subtract-decimals',
          statement: 'Find $12.5 - 4.78$.',
          steps: [
            'Line up decimal points: $12.50 - 4.78$.',
            'Subtract column by column, borrowing: $0 - 8$ borrows from $5$, $\\ldots$',
            'Result: $7.72$.',
          ],
        },
        {
          id: 'ex-mixed-strategy',
          statement:
            'A recipe needs $\\dfrac{3}{4}$ cup of flour, $\\dfrac{1}{2}$ cup of sugar and $0.25$ cup of cocoa. How much dry ingredient in total?',
          steps: [
            'Convert all to a common unit (cups).',
            '$\\dfrac{3}{4} + \\dfrac{1}{2} + \\dfrac{1}{4}$ (since $0.25 = \\dfrac{1}{4}$).',
            'Common denominator $4$: $\\dfrac{3}{4} + \\dfrac{2}{4} + \\dfrac{1}{4} = \\dfrac{6}{4} = 1\\dfrac{1}{2}$.',
            'Result: $1\\dfrac{1}{2}$ cups.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-add-fractions',
          difficulty: 'intro',
          instance: {
            prompt: 'Find $\\dfrac{1}{2} + \\dfrac{1}{3}$. Type as a/b.',
            answer: '5/6',
            answerType: 'numeric',
            hint: 'Common denominator is $6$.',
            solution: [
              '$\\dfrac{1}{2} = \\dfrac{3}{6}$, $\\dfrac{1}{3} = \\dfrac{2}{6}$, so the sum is $\\dfrac{5}{6}$.',
            ],
          },
        },
      ],
    },
  ],
}
