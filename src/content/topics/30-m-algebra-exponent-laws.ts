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
      id: 'laws-and-application',
      heading: 'The three fundamental exponent laws',
      summary: 'Same base → add/subtract exponents; same exponent → multiply; power of a power → multiply.',
      body: `For any real numbers $a, b$ and any integers $m, n$ (with $a, b > 0$ when the exponent is negative or zero with a zero base):

### The three laws
1. **Product**: $a^m \\cdot a^n = a^{m + n}$.
2. **Quotient**: $\\dfrac{a^m}{a^n} = a^{m - n}$.
3. **Power**: $(a^m)^n = a^{mn}$.

### With algebra
Apply the same rules, but include variables and coefficients.

### Negative and zero indices
- $a^0 = 1$ for $a \\neq 0$.
- $a^{-n} = \\dfrac{1}{a^n}$ for $a \\neq 0$.

### Examples
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
  ],
}