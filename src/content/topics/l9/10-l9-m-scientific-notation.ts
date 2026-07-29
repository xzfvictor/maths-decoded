import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Measurement · l9-m-2 (VC2M9M02).
// Scientific notation.

export const l9MScientificNotation: Topic = {
  id: 'l9-m-scientific-notation',
  unit: 9,
  order: 10,
  title: 'Scientific notation',
  blurb:
    'Solve problems involving very small and very large measurements, timescales, and intervals expressed in scientific notation.',
  dotPoints: ['l9-m-2'],

  lessons: [
    {
      id: 'writing-scientific-notation',
      heading: 'Writing numbers in scientific notation',
      summary: 'Move the decimal so exactly one non-zero digit sits to its left; count the steps as the exponent.',
      body: `A number is in **scientific notation** when it is written as
$$a \\times 10^n$$
where $1 \\le a < 10$ and $n$ is an integer.

### Writing a number in scientific notation
1. Place the decimal so **one non-zero digit** sits immediately to its left.
2. Count how many places you shifted the decimal. That count is the exponent $n$.
3. Shift **right** (small number → big exponent) or **left** (big number → negative exponent).

### Examples of conversion
- $4500 = 4.5 \\times 10^3$ (decimal moved $3$ places left → $+3$).
- $0.0032 = 3.2 \\times 10^{-3}$ (decimal moved $3$ places right → $-3$).`,
      examples: [
        {
          id: 'ex-large',
          statement:
            'Write the speed of light, $300\\,000\\,000$ m/s, in scientific notation.',
          steps: [
            'Move the decimal so one non-zero digit is in front: $3.00000000$.',
            'The decimal moved $8$ places to the left, so the exponent is $8$.',
            '$300\\,000\\,000 = 3 \\times 10^8$ m/s.',
          ],
        },
        {
          id: 'ex-small',
          statement:
            'The diameter of a hydrogen atom is about $0.000\\,000\\,000\\,1$ m. Write in scientific notation.',
          steps: [
            'Move the decimal so one non-zero digit is in front: $1.0$.',
            'The decimal moved $10$ places to the right, so the exponent is $-10$.',
            '$0.000\\,000\\,000\\,1 = 1 \\times 10^{-10}$ m.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-large',
          difficulty: 'intro',
          instance: {
            prompt:
              'Write $6\\,500\\,000$ in scientific notation. (Type as "6.5 x 10^8".)',
            answer: '6.5 x 10^6',
            answerType: 'exact',
            hint: 'Move the decimal $6$ places left.',
            solution: [
              '$6\\,500\\,000 = 6.5 \\times 10^6$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-small',
          difficulty: 'core',
          instance: {
            prompt:
              'Write $0.000\\,045$ in scientific notation. (Type as "4.5 x 10^-5".)',
            answer: '4.5 x 10^-5',
            answerType: 'exact',
            hint: 'Move the decimal $5$ places right.',
            solution: [
              '$0.000\\,045 = 4.5 \\times 10^{-5}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'comparing-scientific',
      heading: 'Comparing & ordering numbers in scientific notation',
      summary: 'Compare the exponents first; if they match, compare the coefficients.',
      body: `Scientific notation makes it easy to compare huge or tiny numbers.

### Comparing two numbers
1. Compare the **exponents** of $10$. The **larger exponent** wins for positive numbers; the **smaller (more negative) exponent** is smaller in value.
2. If the exponents match, compare the **coefficients** $a$ directly.

### Ordering from smallest to largest
Sort by the exponent (most negative first), then by coefficient.`,
      examples: [
        {
          id: 'ex-compare',
          statement:
            'Which is larger, $4.2 \\times 10^6$ or $8.7 \\times 10^5$?',
          steps: [
            'Exponents: $6$ vs $5$. $4.2 \\times 10^6$ has the larger exponent, so it is larger.',
          ],
        },
        {
          id: 'ex-order',
          statement:
            'Order from smallest to largest: $3.1 \\times 10^{-4}$, $5.0 \\times 10^{-6}$, $2.4 \\times 10^{-4}$.',
          steps: [
            'Smallest exponent first: $5.0 \\times 10^{-6}$ (exponent $-6$).',
            'Then compare the two $-4$ ones: $2.4 \\times 10^{-4} < 3.1 \\times 10^{-4}$.',
            'Order: $5.0 \\times 10^{-6}$, $2.4 \\times 10^{-4}$, $3.1 \\times 10^{-4}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-order',
          difficulty: 'core',
          instance: {
            prompt:
              'Which is larger, $2.3 \\times 10^8$ or $7.1 \\times 10^7$?',
            answer: '2.3 x 10^8',
            answerType: 'exact',
            hint: 'Compare exponents first.',
            solution: [
              '$2.3 \\times 10^8$ has the bigger exponent ($8 > 7$), so it is larger.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-same-exponent',
          difficulty: 'intro',
          instance: {
            prompt:
              'Which is larger, $5.4 \\times 10^{-3}$ or $5.4 \\times 10^{-5}$?',
            answer: '5.4 x 10^-3',
            answerType: 'exact',
            hint: 'Same coefficient — compare exponents.',
            solution: [
              '$-3$ is greater than $-5$, so $5.4 \\times 10^{-3}$ is larger.',
            ],
          },
        },
      ],
    },
  ],
}
