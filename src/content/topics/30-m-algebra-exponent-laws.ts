import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A02.
// Simplify algebraic products and quotients using exponent laws.

export const algebraExponentLaws: Topic = {
  id: 'm10-algebra-exponent-laws',
  unit: 10,
  order: 8,
  title: 'Exponent laws with algebra',
  blurb:
    'Apply product, quotient and power laws to simplify expressions with positive and negative integer indices.',
  dotPoints: ['m10-a-2'],

  lessons: [
    {
      id: 'three-laws',
      heading: 'The three fundamental exponent laws',
      summary: 'Same base → add/subtract exponents; same exponent → multiply; power of a power → multiply.',
      body: `For any real numbers $a, b$ and any integers $m, n$ (with $a, b > 0$ when the exponent is negative):

### The three laws
1. **Product**: $a^m \\cdot a^n = a^{m + n}$.
2. **Quotient**: $\\dfrac{a^m}{a^n} = a^{m - n}$.
3. **Power**: $(a^m)^n = a^{mn}$.

### With algebra
Apply the same rules, but include variables and coefficients.
- $x^3 \\cdot x^5 = x^{8}$.
- $\\dfrac{x^{10}}{x^{4}} = x^{6}$.
- $(x^2)^5 = x^{10}$.
- $2x^3 \\cdot 3x^4 = 6x^{7}$ — combine coefficients like numbers.`,
      examples: [
        {
          id: 'ex-quotient',
          statement: 'Simplify $\\dfrac{x^{10}}{x^4}$.',
          steps: [
            'Same base $x$; subtract exponents.',
            '$10 - 4 = 6$.',
            'Result: $x^6$.',
          ],
        },
        {
          id: 'ex-mixed',
          statement:
            'Simplify $\\dfrac{3x^2 \\cdot 4x^5}{2x^3}$.',
          steps: [
            'Numerator: $3 \\cdot 4 = 12$; exponents $2 + 5 = 7$, so $12x^7$.',
            'Denominator: $2x^3$.',
            'Divide: $\\dfrac{12}{2} = 6$, $x^{7 - 3} = x^4$.',
            'Result: $6x^4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-product-powers',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $x^3 \\cdot x^5$. Type as x^k.',
            answer: 'x^8',
            answerType: 'polynomial',
            hint: 'Same base — add the exponents.',
            solution: [
              '$x^3 \\cdot x^5 = x^{3 + 5} = x^8$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-power-of-power',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $(x^2)^5$. Type as x^k.',
            answer: 'x^10',
            answerType: 'polynomial',
            hint: 'Power of a power: multiply the exponents.',
            solution: [
              '$(x^2)^5 = x^{2 \\cdot 5} = x^{10}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'negative-zero-indices',
      heading: 'Negative and zero indices',
      summary: 'Anything to the power 0 is 1; a negative index flips the term upside down.',
      body: `Two more rules complete the picture for integer exponents.

### Zero index
$$a^0 = 1 \\quad \\text{for } a \\ne 0.$$

So $5^0 = 1$, $(-3)^0 = 1$, $(x + 1)^0 = 1$.

### Negative index
$$a^{-n} = \\dfrac{1}{a^n} \\quad \\text{for } a \\ne 0.$$

So $3^{-2} = \\dfrac{1}{3^2} = \\dfrac{1}{9}$, and $x^{-3} = \\dfrac{1}{x^3}$.

### Why these work
The quotient law with $m = 0$: $\\dfrac{a^n}{a^n} = a^{n-n} = a^0$. But $\\dfrac{a^n}{a^n} = 1$, so $a^0 = 1$.
The quotient law with a smaller top exponent: $\\dfrac{a^1}{a^{n+1}} = a^{1 - (n+1)} = a^{-n}$. And $\\dfrac{a}{a^{n+1}} = \\dfrac{1}{a^n}$, so $a^{-n} = \\dfrac{1}{a^n}$.`,
      examples: [
        {
          id: 'ex-negative',
          statement: 'Simplify $x^5 \\cdot x^{-2}$.',
          steps: [
            'Apply product law: $x^{5 + (-2)} = x^3$.',
            'Result: $x^3$.',
          ],
        },
        {
          id: 'ex-zero',
          statement: 'Simplify $\\dfrac{x^3}{x^3}$.',
          steps: [
            'Quotient law: $x^{3 - 3} = x^0 = 1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-zero',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is $7^0$?',
            answer: '1',
            answerType: 'numeric',
            hint: 'Anything (except $0$) to the power $0$ is $1$.',
            solution: [
              '$7^0 = 1$ by the zero index rule.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-negative',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $x^{-3} \\cdot x^8$. Type as x^k.',
            answer: 'x^5',
            answerType: 'polynomial',
            hint: 'Add the exponents: $-3 + 8$.',
            solution: [
              '$x^{-3} \\cdot x^8 = x^{-3 + 8} = x^5$.',
            ],
          },
        },
      ],
    },

    {
      id: 'combined-applications',
      heading: 'Combined applications',
      summary: 'Mix the four rules and coefficients in one simplification.',
      body: `Real simplifications mix all the rules — coefficients combine like numbers, while exponents follow the three laws plus zero/negative rules.

### Workflow
1. Combine **coefficients** separately: multiply/divide the numbers.
2. Combine **exponents** by counting how each variable's exponent moves:
   - Product: add.
   - Quotient: subtract.
   - Power: multiply.
   - Zero index: drops out.
3. Negative indices: rewrite as reciprocals at the end if a clean form is needed.`,
      examples: [
        {
          id: 'ex-combined',
          statement: 'Simplify $\\dfrac{(2x^3)^2}{4x^4}$.',
          steps: [
            'Numerator: $4 x^{6}$.',
            'Denominator: $4 x^4$.',
            'Divide: $\\dfrac{4}{4} = 1$, $x^{6 - 4} = x^2$.',
            'Result: $x^2$.',
          ],
        },
        {
          id: 'ex-coeff-mix',
          statement: 'Simplify $\\dfrac{15 x^7 y^2}{3 x^2 y^5}$.',
          steps: [
            'Coefficients: $15 / 3 = 5$.',
            '$x$: $x^{7 - 2} = x^5$.',
            '$y$: $y^{2 - 5} = y^{-3}$.',
            'Result: $5 x^5 y^{-3} = \\dfrac{5 x^5}{y^3}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-combined',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $\\dfrac{(3x^2)^3}{9x^4}$. Type as a simplified expression.',
            answer: '3x^2',
            answerType: 'polynomial',
            hint: '$(3x^2)^3 = 27 x^6$. Then divide by $9 x^4$.',
            solution: [
              '$27 x^6 / (9 x^4) = 3 x^{6 - 4} = 3 x^2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-coeff',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $4 x^3 \\cdot 2 x^5$. Type as a simplified expression.',
            answer: '8x^8',
            answerType: 'polynomial',
            hint: 'Multiply the coefficients and add the exponents.',
            solution: [
              '$4 \\cdot 2 = 8$, $x^{3 + 5} = x^8$, so $8 x^8$.',
            ],
          },
        },
      ],
    },
  ],
}