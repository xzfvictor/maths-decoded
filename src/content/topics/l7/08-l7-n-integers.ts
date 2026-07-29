import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-8 (VC2M7N08).
// Addition and subtraction of integers.

export const l7NIntegers: Topic = {
  id: 'l7-n-integers',
  unit: 7,
  order: 8,
  title: 'Addition and subtraction of integers',
  blurb:
    'Compare, order, and solve problems involving adding and subtracting positive and negative integers.',
  dotPoints: ['l7-n-8'],
  lessons: [
    {
      id: 'integers-add-subtract',
      heading: 'Comparing, ordering, and operating on integers',
      summary: 'Use the number line and opposite signs to add and subtract any pair of integers.',
      body: `**Integers** are the whole numbers and their negatives: $\\ldots, -3, -2, -1, 0, 1, 2, 3, \\ldots$. The **magnitude** of an integer is its distance from zero; the **sign** tells you which side.

### Comparing and ordering
On a number line, the number further to the right is **greater**. So:
- $-7 < -3 < 0 < 4$.
- A bigger magnitude does not mean a bigger number: $-100 < -1$ because $-100$ is further left.

### Adding integers
A **number line** is the most reliable picture.
- $+3$ means move $3$ to the **right**.
- $-3$ means move $3$ to the **left**.

**Sign rules** (an alternative to the number line):
- Same signs: add the magnitudes, keep the sign. $(-4) + (-6) = -10$.
- Different signs: subtract the smaller magnitude from the larger, keep the sign of the larger-magnitude number. $(-7) + 4 = -3$.

### Subtracting integers
Subtracting is the same as **adding the opposite**:
$$a - b = a + (-b).$$
So $5 - (-2) = 5 + 2 = 7$ and $3 - 8 = 3 + (-8) = -5$.

> [!definition] Magnitude vs sign
> Magnitude is *how far* from zero; sign is *which side* of zero. Both matter when comparing.

> [!warning] Watch out
> Subtracting a negative **adds**: "five take away minus two" is the same as "five add two".`,
      examples: [
        {
          id: 'ex-compare',
          statement: 'Order $-5, 3, -1, 0, -7$ from smallest to largest.',
          steps: [
            'Picture them on a number line: negative numbers to the left of $0$, positive to the right.',
            'Smallest is the most negative: $-7$.',
            'Then $-5, -1, 0, 3$.',
            'Result: $-7 < -5 < -1 < 0 < 3$.',
          ],
        },
        {
          id: 'ex-add-mixed',
          statement: 'Find $-8 + 5$.',
          steps: [
            'Different signs: subtract magnitudes: $|{-8}| - |5| = 8 - 5 = 3$.',
            'Larger-magnitude number is $-8$ (negative), so the answer is negative.',
            'Result: $-8 + 5 = -3$.',
          ],
        },
        {
          id: 'ex-subtract-negative',
          statement: 'Find $4 - (-6)$.',
          steps: [
            'Subtracting a negative: change to adding the opposite.',
            '$4 - (-6) = 4 + 6 = 10$.',
            'Result: $10$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-subtract-negative',
          difficulty: 'intro',
          instance: {
            prompt: 'Find $2 - (-5)$.',
            answer: '7',
            answerType: 'numeric',
            hint: 'Subtracting a negative is the same as adding.',
            solution: [
              '$2 - (-5) = 2 + 5 = 7$.',
            ],
          },
        },
      ],
    },
  ],
}
