import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Number · l9-n-1 (VC2M9N01).
// Real numbers, rational and irrational.

export const l9NRealNumbers: Topic = {
  id: 'l9-n-real-numbers',
  unit: 9,
  order: 1,
  title: 'Real numbers, rational and irrational',
  blurb:
    'Recognise that the real number system includes both rational and irrational numbers, and solve problems involving real numbers with and without digital tools.',
  dotPoints: ['l9-n-1'],

  lessons: [
    {
      id: 'rational-irrational',
      heading: 'Rational vs irrational numbers',
      summary:
        'A rational number can be written as a fraction of two integers; an irrational one cannot.',
      body: `The **real number system** contains every number you can place on the number line. It splits into two big families: **rational** and **irrational**.

### Rational numbers
A number is **rational** if it can be written as a fraction $\\dfrac{a}{b}$ where $a$ and $b$ are integers (and $b \\ne 0$). This includes:
- Every integer (e.g. $5 = \\dfrac{5}{1}$).
- Terminating decimals (e.g. $0.75 = \\dfrac{3}{4}$).
- Recurring decimals (e.g. $0.\\overline{3} = \\dfrac{1}{3}$).

### Irrational numbers
A number is **irrational** if it **cannot** be written as a fraction of two integers. Its decimal goes on forever without repeating. Famous examples:
- $\\sqrt{2} \\approx 1.41421356\\ldots$
- $\\pi \\approx 3.14159265\\ldots$
- $\\sqrt{3}$, $\\sqrt{5}$, $\\sqrt[3]{2}$, the golden ratio $\\varphi = \\dfrac{1+\\sqrt{5}}{2}$.

### Quick test
- Square roots of **non-perfect** squares are irrational: $\\sqrt{2}$, $\\sqrt{3}$, $\\sqrt{5}$, $\\sqrt{7}$, $\\sqrt{8}$.
- Square roots of **perfect** squares are rational: $\\sqrt{4} = 2$, $\\sqrt{9} = 3$, $\\sqrt{16} = 4$.`,
      examples: [
        {
          id: 'ex-identify',
          statement:
            'Is $\\sqrt{5}$ rational or irrational?',
          steps: [
            '$5$ is not a perfect square ($2^2 = 4$, $3^2 = 9$).',
            'So $\\sqrt{5}$ is **irrational**.',
          ],
        },
        {
          id: 'ex-convert',
          statement:
            'Write $0.\\overline{6}$ as a fraction.',
          steps: [
            'Let $x = 0.\\overline{6}$. Then $10x = 6.\\overline{6}$.',
            'Subtract: $10x - x = 6$, so $9x = 6$.',
            'Result: $x = \\dfrac{6}{9} = \\dfrac{2}{3}$.',
          ],
        },
        {
          id: 'ex-classify',
          statement:
            'Is $3.14159$ rational or irrational?',
          steps: [
            'The decimal terminates — it is finite.',
            'Any terminating decimal can be written as a fraction: $3.14159 = \\dfrac{314159}{100000}$.',
            'So it is **rational**.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-classify-sqrt',
          difficulty: 'intro',
          instance: {
            prompt:
              'Is $\\sqrt{7}$ rational or irrational? Answer "rational" or "irrational".',
            answer: 'irrational',
            answerType: 'exact',
            hint: '$7$ is not a perfect square.',
            solution: [
              '$7$ is not a perfect square ($2^2 = 4$, $3^2 = 9$).',
              'So $\\sqrt{7}$ is irrational.',
            ],
          },
        },
      ],
    },

    {
      id: 'real-number-operations',
      heading: 'Operating with real numbers',
      summary:
        'Real numbers are closed under +, −, ×, ÷ (except ÷0); use known irrationals to find more.',
      body: `You can add, subtract, multiply and divide real numbers (when the divisor is not zero) and stay inside the real numbers. That makes the real numbers a **closed** system.

### Sums and products
- Rational + Rational = Rational (e.g. $\\tfrac{1}{2} + \\tfrac{1}{3} = \\tfrac{5}{6}$).
- Rational × Rational = Rational (e.g. $\\tfrac{2}{3} \\cdot \\tfrac{3}{4} = \\tfrac{1}{2}$).
- Irrational + Irrational can be **either**: $(\\sqrt{2}) + (-\\sqrt{2}) = 0$ (rational), but $\\sqrt{2} + \\sqrt{3}$ is irrational.
- Rational + Irrational = Irrational (a non-zero rational cannot cancel an irrational tail).

### Estimating
When a digital tool gives you $1.41421356237$, you can spot $\\sqrt{2}$ in there. Knowing the common irrationals helps you check answers and recognise patterns.

### Pythagoras gives irrationals
For any right triangle with legs $a$ and $b$, the hypotenuse $c = \\sqrt{a^2 + b^2}$ is irrational whenever $a^2 + b^2$ is not a perfect square. The $(1, 1, \\sqrt{2})$ and $(1, 2, \\sqrt{5})$ triangles are the canonical examples.`,
      examples: [
        {
          id: 'ex-approx',
          statement:
            'Between which two consecutive integers does $\\sqrt{20}$ lie?',
          steps: [
            '$4^2 = 16$, $5^2 = 25$.',
            'So $16 < 20 < 25$, meaning $4 < \\sqrt{20} < 5$.',
          ],
        },
        {
          id: 'ex-pythag',
          statement:
            'A right triangle has legs $1$ and $2$. What is the length of the hypotenuse (exact form)?',
          steps: [
            '$c = \\sqrt{1^2 + 2^2} = \\sqrt{1 + 4} = \\sqrt{5}$.',
            'Since $5$ is not a perfect square, $\\sqrt{5}$ is irrational.',
          ],
        },
        {
          id: 'ex-compare',
          statement:
            'Is $\\pi + 3$ rational or irrational?',
          steps: [
            '$\\pi$ is irrational.',
            'Adding a non-zero rational ($3$) to an irrational keeps it irrational.',
            'So $\\pi + 3$ is **irrational**.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-between',
          difficulty: 'intro',
          instance: {
            prompt:
              'Between which two consecutive integers does $\\sqrt{50}$ lie? State the smaller integer.',
            answer: '7',
            answerType: 'numeric',
            hint: '$7^2 = 49$, $8^2 = 64$.',
            solution: [
              '$7^2 = 49 < 50 < 64 = 8^2$.',
              'So $7 < \\sqrt{50} < 8$. The smaller integer is $7$.',
            ],
          },
        },
      ],
    },
  ],
}