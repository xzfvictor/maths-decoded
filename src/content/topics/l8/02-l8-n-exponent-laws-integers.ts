import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Number · l8-n-2 (VC2M8N02).
// Establish and apply the exponent laws with positive integer exponents and the
// zero exponent, using exponent notation with numbers.

export const l8NExponentLawsIntegers: Topic = {
  id: 'l8-n-exponent-laws-integers',
  unit: 8,
  order: 2,
  title: 'Exponent laws with positive integers',
  blurb:
    'Establish and apply the exponent laws with positive integer exponents and the zero exponent, using exponent notation with numbers.',
  dotPoints: ['l8-n-2'],
  lessons: [
    {
      id: 'three-laws',
      heading: 'Product, quotient and power laws',
      summary:
        'Same base → add exponents (product) or subtract exponents (quotient); power of a power → multiply exponents.',
      body: `Exponents are shorthand for repeated multiplication. $3^4$ means $3 \\times 3 \\times 3 \\times 3$. With the same base, there are three laws that let you combine powers.

### The three laws
1. **Product**: $a^m \\times a^n = a^{m + n}$.
2. **Quotient**: $\\dfrac{a^m}{a^n} = a^{m - n}$.
3. **Power**: $(a^m)^n = a^{m \\times n}$.

### Why the product law works
Count the factors. $a^3 \\times a^4 = (a \\times a \\times a) \\times (a \\times a \\times a \\times a) = a^7$. The total number of factors is the sum of the original counts.

### Worked shapes
- $2^3 \\times 2^4 = 2^{3 + 4} = 2^7 = 128$.
- $\\dfrac{5^6}{5^2} = 5^{6 - 2} = 5^4 = 625$.
- $(3^2)^4 = 3^{2 \\times 4} = 3^8 = 6561$.

> [!warning] Watch out
> The base must be the **same** for the product and quotient laws. $2^3 \\times 3^2$ cannot be combined — keep as is or just compute ($= 72$).`,
      examples: [
        {
          id: 'ex-product',
          statement: 'Simplify $4^3 \\times 4^5$.',
          steps: [
            'Same base $4$; product law: add exponents.',
            '$3 + 5 = 8$.',
            'Result: $4^8$.',
          ],
        },
        {
          id: 'ex-quotient',
          statement: 'Simplify $\\dfrac{7^9}{7^4}$.',
          steps: [
            'Same base $7$; quotient law: subtract exponents.',
            '$9 - 4 = 5$.',
            'Result: $7^5$.',
          ],
        },
        {
          id: 'ex-power',
          statement: 'Simplify $(2^3)^4$.',
          steps: [
            'Power of a power: multiply exponents.',
            '$3 \\times 4 = 12$.',
            'Result: $2^{12}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-power-of-power',
          difficulty: 'intro',
          instance: {
            prompt: 'Simplify $(5^2)^3$. State the answer as $5^k$ — give $k$.',
            answer: '6',
            answerType: 'numeric',
            hint: 'Power of a power: multiply the exponents.',
            solution: [
              '$(5^2)^3 = 5^{2 \\times 3} = 5^6$, so $k = 6$.',
            ],
          },
        },
      ],
    },
    {
      id: 'zero-exponent',
      heading: 'The zero exponent and the zero base',
      summary:
        'Anything (except 0) to the power 0 is 1; 0 raised to a positive power is 0. 0^0 is undefined.',
      body: `The quotient law leads to one more useful rule: the **zero exponent**.

### The rule
$$a^0 = 1 \\quad \\text{for any } a \\ne 0.$$

### Why
Take $\\dfrac{a^n}{a^n}$. It equals $1$ (a number divided by itself). But the quotient law gives $a^{n - n} = a^0$. So $a^0 = 1$.

- $7^0 = 1$.
- $(-3)^0 = 1$.
- $100^0 = 1$.

> [!warning] Watch out
> $0^0$ is **not** defined here. The rule $a^0 = 1$ only applies for $a \\ne 0$.

### The zero base
On the other hand, multiplying $0$ by itself any positive number of times still gives $0$:
$$0^3 = 0 \\times 0 \\times 0 = 0.$$

So $0^5 = 0$ and $0^{100} = 0$, but $0^0$ is undefined.`,
      examples: [
        {
          id: 'ex-zero-exponent',
          statement: 'Evaluate $12^0$.',
          steps: [
            'Base $12$ is not zero, so $12^0 = 1$.',
          ],
        },
        {
          id: 'ex-mixed',
          statement: 'Evaluate $5^3 \\times 5^0$.',
          steps: [
            'Product law: $5^{3 + 0} = 5^3$.',
            'Or simply note $5^0 = 1$, so $5^3 \\times 1 = 125$.',
            'Result: $5^3 = 125$.',
          ],
        },
        {
          id: 'ex-zero-base',
          statement: 'Evaluate $0^4$.',
          steps: [
            'Multiply $0$ by itself four times: $0 \\times 0 \\times 0 \\times 0 = 0$.',
            'Result: $0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-zero-eval',
          difficulty: 'intro',
          instance: {
            prompt: 'Evaluate $(-7)^0$.',
            answer: '1',
            answerType: 'numeric',
            hint: 'Any non-zero number to the power 0 is 1.',
            solution: [
              '$(-7)^0 = 1$ by the zero-exponent rule (the base is $-7$, not $0$).',
            ],
          },
        },
      ],
    },
  ],
}
