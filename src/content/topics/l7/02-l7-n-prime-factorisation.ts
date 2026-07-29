import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-2 (VC2M7N02).
// Expanded notation using powers of 10 and prime factorisation.

export const l7NPrimeFactorisation: Topic = {
  id: 'l7-n-prime-factorisation',
  unit: 7,
  order: 2,
  title: 'Prime factorisation and expanded notation',
  blurb:
    'Write natural numbers in expanded form and as products of prime powers, and use those factorisations to find HCF and LCM.',
  dotPoints: ['l7-n-2'],
  lessons: [
    {
      id: 'expanded-and-prime',
      heading: 'Expanded notation and prime factorisation',
      summary: 'Write any whole number as a sum of powers of 10, and as a product of prime powers.',
      body: `Every whole number can be written in two useful expanded forms: one based on **place value** (powers of 10), and one based on **primes** (its prime factorisation).

### Expanded notation using powers of 10
The place value of every digit is a power of 10:
- $10^0 = 1$ (ones), $10^1 = 10$ (tens), $10^2 = 100$ (hundreds), $10^3 = 1000$ (thousands), $\\ldots$

So $3527 = 3 \\times 10^3 + 5 \\times 10^2 + 2 \\times 10^1 + 7 \\times 10^0$.

### Primes and prime factorisation
A **prime number** has exactly two factors: $1$ and itself. The first few primes are $2, 3, 5, 7, 11, 13, 17, 19, 23, \\ldots$

**Prime factorisation** rewrites a number as a product of prime numbers. Every number greater than $1$ has a unique prime factorisation (this is called the **Fundamental Theorem of Arithmetic**).

### How to find the prime factorisation
1. Start with the smallest prime, $2$. Keep dividing while the number is even.
2. Try $3$, then $5$, then $7$, $\\ldots$ — stop when the quotient is $1$.
3. The primes you divided by, written with exponents, are the factorisation.

### Using prime factorisation
- **HCF (highest common factor)**: take the *lowest* power of every prime that appears in **both** numbers.
- **LCM (lowest common multiple)**: take the *highest* power of every prime that appears in **either** number.`,
      examples: [
        {
          id: 'ex-expanded',
          statement: 'Write $4052$ in expanded form using powers of $10$.',
          steps: [
            'Each digit sits in its own place: $4$ thousands, $0$ hundreds, $5$ tens, $2$ ones.',
            'So $4052 = 4 \\times 10^3 + 0 \\times 10^2 + 5 \\times 10^1 + 2 \\times 10^0$.',
            'The $0 \\times 10^2$ term is just $0$ and is usually left out.',
          ],
        },
        {
          id: 'ex-prime-factor',
          statement: 'Find the prime factorisation of $180$.',
          steps: [
            'Divide by $2$: $180 = 2 \\times 90$. Divide by $2$ again: $90 = 2 \\times 45$.',
            '$45$ is odd, so try $3$: $45 = 3 \\times 15 = 3 \\times 3 \\times 5$.',
            'Put it together: $180 = 2 \\times 2 \\times 3 \\times 3 \\times 5$.',
            'Using exponents: $180 = 2^2 \\times 3^2 \\times 5$.',
          ],
        },
        {
          id: 'ex-hcf-lcm',
          statement:
            'Find the HCF and LCM of $12$ and $18$.',
          steps: [
            'Prime factorisations: $12 = 2^2 \\times 3$, $18 = 2 \\times 3^2$.',
            'HCF — lowest power of each shared prime: $2^1 \\times 3^1 = 6$.',
            'LCM — highest power of every prime that appears: $2^2 \\times 3^2 = 36$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-prime-factor-72',
          difficulty: 'intro',
          instance: {
            prompt: 'Find the prime factorisation of $72$. Enter in the form "2^a * 3^b * 5^c ...".',
            answer: '2^3*3^2',
            answerType: 'polynomial',
            hint: 'Keep dividing by $2$, then by $3$.',
            solution: [
              '$72 = 2 \\times 36 = 2 \\times 2 \\times 18 = 2^3 \\times 9 = 2^3 \\times 3^2$.',
            ],
          },
        },
      ],
    },
  ],
}
