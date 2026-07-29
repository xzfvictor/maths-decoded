import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Number · l8-n-1 (VC2M8N01).
// Recognise irrational numbers as numbers that cannot develop from the
// division of integer values by natural numbers and terminating or recurring decimals.

export const l8NIrrationalNumbers: Topic = {
  id: 'l8-n-irrational-numbers',
  unit: 8,
  order: 1,
  title: 'Irrational numbers',
  blurb:
    'Recognise irrational numbers as values that cannot arise from dividing integers by natural numbers or from terminating/recurring decimals.',
  dotPoints: ['l8-n-1'],
  lessons: [
    {
      id: 'what-is-irrational',
      heading: 'What makes a number irrational?',
      summary:
        'A number is irrational when it cannot be written as a fraction of two integers — and therefore its decimal never terminates or repeats.',
      body: `A number is **rational** if it can be written as a fraction $\\dfrac{p}{q}$ where $p$ and $q$ are integers and $q \\ne 0$. Every rational number, when written as a decimal, is either **terminating** (e.g. $0.75$) or **recurring** (e.g. $0.333\\ldots = 0.\\overline{3}$).

An **irrational number** is a real number that is not rational. Its decimal goes on forever **without ever repeating**.

### Quick test
Ask: "Can I write this number as a fraction of two integers?"
- If **yes** → rational.
- If **no** → irrational.

### Common examples
- $\\sqrt{2} \\approx 1.41421356\\ldots$ — never repeats.
- $\\sqrt{5} \\approx 2.2360679\\ldots$ — never repeats.
- $\\pi \\approx 3.14159265\\ldots$ — never repeats.
- $\\sqrt{9} = 3$ — this is rational, because $3 = \\dfrac{3}{1}$.

### Why non-perfect-square roots are irrational
If a number $n$ is **not** a perfect square, then $\\sqrt{n}$ cannot be written as a fraction of two integers. The decimal goes on forever with no repeating block.

> [!warning] Watch out
> "A long decimal" is not the same as "an irrational decimal". A number like $0.101001000100001\\ldots$ (more zeros between the $1$s each time) never repeats, so it is irrational. The giveaway is whether the digits **ever settle into a repeating block**.

### How to spot a rational from its decimal
- **Terminates**: $0.5$, $0.125$, $0.375$ — clearly rational.
- **Recurs** (a block repeats): $0.\\overline{3}$, $0.1\\overline{6}$, $0.\\overline{142857}$ — rational.
- **Never settles and never repeats**: irrational.`,
      examples: [
        {
          id: 'ex-perfect-square',
          statement: 'Is $\\sqrt{25}$ rational or irrational? Explain.',
          steps: [
            '$25$ is a perfect square ($5 \\times 5 = 25$).',
            '$\\sqrt{25} = 5$, which is an integer — integers are rational.',
            'Conclusion: $\\sqrt{25}$ is rational.',
          ],
        },
        {
          id: 'ex-non-perfect-square',
          statement: 'Is $\\sqrt{7}$ rational or irrational?',
          steps: [
            '$7$ is **not** a perfect square — the closest squares are $4$ and $9$.',
            'There is no integer $n$ with $n^2 = 7$.',
            'So $\\sqrt{7}$ cannot be written as a fraction of two integers.',
            'Conclusion: $\\sqrt{7}$ is irrational.',
          ],
        },
        {
          id: 'ex-pi',
          statement:
            'Is the number $0.101001000100001\\ldots$ (more zeros between each $1$) rational or irrational?',
          steps: [
            'Look for a repeating block.',
            'The pattern of $1$s is $1, 10, 100, 1000, 10000, \\ldots$ — the gap keeps growing.',
            'No block ever repeats, so the decimal never settles.',
            'Conclusion: irrational.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-classify',
          difficulty: 'intro',
          instance: {
            prompt:
              'Is $\\sqrt{10}$ rational or irrational? Answer "rational" or "irrational".',
            answer: 'irrational',
            answerType: 'exact',
            hint: 'Is $10$ a perfect square?',
            solution: [
              '$10$ is not a perfect square ($3^2 = 9$ and $4^2 = 16$). So $\\sqrt{10}$ cannot be written as a fraction of two integers, and is irrational.',
            ],
          },
        },
      ],
    },
  ],
}
