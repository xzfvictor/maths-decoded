import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A14.
// Solve simple exponential equations.

export const algebraExponentials: Topic = {
  id: 'm10-algebra-exponentials',
  unit: 10,
  order: 19,
  title: 'Solving simple exponential equations',
  blurb:
    'Match bases to read off exponents; otherwise, take logs to bring the unknown down.',
  dotPoints: ['m10-a-14'],

  lessons: [
    {
      id: 'match-or-logs',
      heading: 'Match the base, or take logs',
      summary: 'Same base → exponents equal. Otherwise → take logs on both sides.',
      body: `An **exponential equation** has the unknown in an exponent. Solve it by either matching bases (when possible) or using logarithms.

### Matching bases
If both sides can be written with the **same base**, set the exponents equal:
$$2^{x + 1} = 8 = 2^3 \\Rightarrow x + 1 = 3 \\Rightarrow x = 2.$$

### Using logs (otherwise)
Take the logarithm of both sides, then use the power law $\\log(b^k) = k\\log b$ to bring the unknown down:
$$\\log(2^x) = \\log(10) \\Rightarrow x\\log 2 = \\log 10 \\Rightarrow x = \\frac{\\log 10}{\\log 2}.$$

For practical work, the natural log $\\ln$ is convenient.`,
      examples: [
        {
          id: 'ex-match-base',
          statement: 'Solve $2^{x + 1} = 8$.',
          steps: [
            '$8 = 2^3$, so $2^{x + 1} = 2^3$.',
            'Set exponents equal: $x + 1 = 3 \\Rightarrow x = 2$.',
          ],
        },
        {
          id: 'ex-logs',
          statement:
            'Solve $3^x = 20$. Give $x$ in the form $\\dfrac{\\log 20}{\\log 3}$.',
          steps: [
            'Take logs: $x \\log 3 = \\log 20$.',
            '$x = \\dfrac{\\log 20}{\\log 3}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-match',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $2^x = 32$. State $x$.',
            answer: '5',
            answerType: 'numeric',
            hint: '$32 = 2^5$.',
            solution: [
              '$2^x = 2^5 \\Rightarrow x = 5$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-logs',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $2^x = 10$ in the form $\\dfrac{\\log 10}{\\log k}$. What is $k$?',
            answer: '2',
            answerType: 'numeric',
            hint: 'Take logs of both sides and solve for $x$.',
            solution: [
              '$x \\log 2 = \\log 10 \\Rightarrow x = \\dfrac{\\log 10}{\\log 2}$.',
              'So $k = 2$.',
            ],
          },
        },
      ],
    },
  ],
}