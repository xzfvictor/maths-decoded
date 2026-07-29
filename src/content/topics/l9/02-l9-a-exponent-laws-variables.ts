import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Algebra · l9-a-1 (VC2M9A01).
// Exponent laws with variables.

export const l9AExponentLawsVariables: Topic = {
  id: 'l9-a-exponent-laws-variables',
  unit: 9,
  order: 2,
  title: 'Exponent laws with variables',
  blurb:
    'Apply the exponent laws to numerical expressions with integer exponents and the zero exponent, and extend them to variables.',
  dotPoints: ['l9-a-1'],

  lessons: [
    {
      id: 'three-laws',
      heading: 'The three fundamental laws',
      summary:
        'Same base → add or subtract exponents; same exponent → multiply; power of a power → multiply.',
      body: `For any real number $a \\ne 0$ and integers $m, n$, three rules govern exponents.

### The laws
1. **Product**: $a^m \\cdot a^n = a^{m+n}$.
2. **Quotient**: $\\dfrac{a^m}{a^n} = a^{m - n}$.
3. **Power**: $(a^m)^n = a^{mn}$.

### Extending to variables
Variables obey the same rules. The only difference: you may also need to combine the **coefficients**.
- $x^3 \\cdot x^5 = x^{3+5} = x^8$ (same base, add exponents).
- $\\dfrac{x^{10}}{x^4} = x^{10 - 4} = x^6$.
- $(x^2)^5 = x^{2 \\cdot 5} = x^{10}$.
- $2x^3 \\cdot 3x^4 = (2 \\cdot 3) x^{3+4} = 6x^7$.

### Mixing variables
When two variables appear, treat each one independently.
- $x^2 y^3 \\cdot x^4 y = x^{2+4} y^{3+1} = x^6 y^4$.
- $(x^2 y)^3 = x^{2 \\cdot 3} y^{3} = x^6 y^3$.`,
      examples: [
        {
          id: 'ex-product',
          statement:
            'Simplify $x^3 \\cdot x^5$.',
          steps: [
            'Same base $x$; add exponents.',
            '$3 + 5 = 8$.',
            'Result: $x^8$.',
          ],
        },
        {
          id: 'ex-quotient',
          statement:
            'Simplify $\\dfrac{x^{10}}{x^4}$.',
          steps: [
            'Same base $x$; subtract exponents.',
            '$10 - 4 = 6$.',
            'Result: $x^6$.',
          ],
        },
        {
          id: 'ex-power',
          statement:
            'Simplify $(2x^3)^4$.',
          steps: [
            'Power law: $2^4 \\cdot (x^3)^4$.',
            '$2^4 = 16$ and $(x^3)^4 = x^{12}$.',
            'Result: $16 x^{12}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-product',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $x^4 \\cdot x^3$. Type as x^k.',
            answer: 'x^7',
            answerType: 'polynomial',
            hint: 'Same base — add the exponents.',
            solution: [
              '$x^4 \\cdot x^3 = x^{4+3} = x^7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'zero-and-negative',
      heading: 'Zero and negative exponents',
      summary:
        'Anything to the power 0 is 1; a negative index flips the term upside down.',
      body: `Two more rules complete the picture.

### Zero exponent
$$a^0 = 1 \\quad \\text{for } a \\ne 0.$$
So $5^0 = 1$, $(-3)^0 = 1$, $(x + 1)^0 = 1$. The base just has to be non-zero.

### Negative exponent
$$a^{-n} = \\dfrac{1}{a^n} \\quad \\text{for } a \\ne 0.$$
So $3^{-2} = \\dfrac{1}{3^2} = \\dfrac{1}{9}$, and $x^{-3} = \\dfrac{1}{x^3}$.

### Why these work
The quotient law with $m = n$: $\\dfrac{a^n}{a^n} = a^{n-n} = a^0$. But $\\dfrac{a^n}{a^n} = 1$, so $a^0 = 1$.
For negatives: $\\dfrac{a^1}{a^{n+1}} = a^{1-(n+1)} = a^{-n}$. And $\\dfrac{a}{a^{n+1}} = \\dfrac{1}{a^n}$, so the two forms match.`,
      examples: [
        {
          id: 'ex-zero',
          statement:
            'What is $7^0$?',
          steps: [
            'Any non-zero number to the power $0$ is $1$.',
            '$7^0 = 1$.',
          ],
        },
        {
          id: 'ex-negative-mix',
          statement:
            'Simplify $x^5 \\cdot x^{-2}$.',
          steps: [
            'Add exponents: $x^{5 + (-2)} = x^3$.',
            'Result: $x^3$.',
          ],
        },
        {
          id: 'ex-negative-quotient',
          statement:
            'Simplify $\\dfrac{x^3}{x^7}$.',
          steps: [
            'Subtract exponents: $x^{3 - 7} = x^{-4}$.',
            'Rewrite as a positive power: $\\dfrac{1}{x^4}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-zero-var',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is $(x^2 + 1)^0$? (Assume $x^2 + 1 \\ne 0$.)',
            answer: '1',
            answerType: 'numeric',
            hint: 'Anything non-zero to the power 0 is 1.',
            solution: [
              '$(x^2 + 1)^0 = 1$ by the zero exponent rule.',
            ],
          },
        },
      ],
    },
  ],
}