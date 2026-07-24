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
      id: 'matching-bases',
      heading: 'Matching bases',
      summary: 'Same base on both sides → set the exponents equal.',
      body: `An **exponential equation** has the unknown in an exponent. The cleanest way to solve is to make both sides share the **same base**.

### Recipe
1. Rewrite both sides with the same base.
2. Set the exponents equal.
3. Solve the resulting linear equation.

### When matching works
If both sides are powers of small integers (2, 3, 5, 10) — express them and match.

$$2^{x + 1} = 8 = 2^3 \\Rightarrow x + 1 = 3 \\Rightarrow x = 2.$$`,
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
          id: 'ex-match-base-2',
          statement: 'Solve $3^{2x} = 81$.',
          steps: [
            '$81 = 3^4$, so $3^{2x} = 3^4$.',
            'Set exponents equal: $2x = 4 \\Rightarrow x = 2$.',
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
          id: 'c-match-3',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $5^{x - 1} = 125$. State $x$.',
            answer: '4',
            answerType: 'numeric',
            hint: '$125 = 5^3$.',
            solution: [
              '$5^{x - 1} = 5^3 \\Rightarrow x - 1 = 3 \\Rightarrow x = 4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'using-logs',
      heading: 'Using logarithms',
      summary: 'Take logs on both sides and apply the power law to bring the unknown down.',
      body: `When the bases don't match — e.g. $3^x = 20$ — **take the logarithm of both sides**.

### Steps
1. Take $\\log$ (or $\\ln$) on both sides.
2. Use the power law: $\\log(b^k) = k \\log b$.
3. Solve for the unknown.

$$\\log(2^x) = \\log(10) \\Rightarrow x\\log 2 = \\log 10 \\Rightarrow x = \\frac{\\log 10}{\\log 2}.$$

### Practical tip
The natural log $\\ln$ works the same way; using $\\ln$ keeps the algebra simple if the right side is an $e$-power.`,
      examples: [
        {
          id: 'ex-logs',
          statement:
            'Solve $3^x = 20$. Give $x$ in the form $\\dfrac{\\log 20}{\\log 3}$.',
          steps: [
            'Take logs: $x \\log 3 = \\log 20$.',
            '$x = \\dfrac{\\log 20}{\\log 3}$.',
          ],
        },
        {
          id: 'ex-logs-2',
          statement:
            'Solve $2^x = 50$. Give $x$ in the form $\\dfrac{\\log k}{\\log 2}$. What is $k$?',
          steps: [
            'Take logs: $x \\log 2 = \\log 50$.',
            '$x = \\dfrac{\\log 50}{\\log 2}$.',
            'So $k = 50$.',
          ],
        },
      ],
      exercises: [
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
        {
          kind: 'curated',
          id: 'c-logs-2',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $4^x = 100$ in the form $\\dfrac{\\log 100}{\\log k}$. What is $k$?',
            answer: '4',
            answerType: 'numeric',
            hint: 'Take logs of both sides.',
            solution: [
              '$x \\log 4 = \\log 100 \\Rightarrow x = \\dfrac{\\log 100}{\\log 4}$.',
              'So $k = 4$.',
            ],
          },
        },
      ],
    },
  ],
}