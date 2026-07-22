import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A03.
// Apply the 4 operations to simple algebraic fractions with numerical or
// single variable denominators.

export const algebraFractions: Topic = {
  id: 'm10-algebra-fractions',
  unit: 10,
  order: 9,
  title: 'Adding and subtracting algebraic fractions',
  blurb:
    'Combine fractions with a common denominator (literal or numerical); use the exponent laws to simplify products and quotients of algebraic fractions.',
  dotPoints: ['m10-a-3'],

  lessons: [
    {
      id: 'common-denominator',
      heading: 'Adding and subtracting fractions',
      summary: 'Same denominator → add numerators; different denominators → find the LCD first.',
      body: `Algebraic fractions follow the **same rules** as numerical fractions.

### Adding and subtracting
- **Same denominator**: $\\dfrac{a}{c} + \\dfrac{b}{c} = \\dfrac{a + b}{c}$.
- **Different denominators**: find the **lowest common denominator (LCD)** first, then rewrite each fraction with that denominator.

### LCD trick
- Numerical: $\\dfrac{1}{4} + \\dfrac{1}{6}$: LCD $= 12$, so $\\dfrac{3}{12} + \\dfrac{2}{12} = \\dfrac{5}{12}$.
- Algebraic: $\\dfrac{x}{3} + \\dfrac{2}{5}$: LCD $= 15$, so $\\dfrac{5x}{15} + \\dfrac{6}{15} = \\dfrac{5x + 6}{15}$.

### Multiplying and dividing
- Multiply: multiply numerators, multiply denominators. Simplify before multiplying if you can.
- Divide: $\\dfrac{a}{b} \\div \\dfrac{c}{d} = \\dfrac{a}{b} \\cdot \\dfrac{d}{c}$ (multiply by the reciprocal).`,
      examples: [
        {
          id: 'ex-add-fractions',
          statement:
            'Simplify $\\dfrac{x}{3} + \\dfrac{2}{5}$.',
          steps: [
            'LCD $= 15$.',
            '$\\dfrac{x}{3} = \\dfrac{5x}{15}$, $\\dfrac{2}{5} = \\dfrac{6}{15}$.',
            'Sum: $\\dfrac{5x + 6}{15}$.',
          ],
        },
        {
          id: 'ex-divide-fractions',
          statement:
            'Simplify $\\dfrac{x^2}{6} \\div \\dfrac{x}{3}$.',
          steps: [
            'Multiply by reciprocal: $\\dfrac{x^2}{6} \\cdot \\dfrac{3}{x}$.',
            'Cancel $x$: $\\dfrac{x \\cdot 3}{6} = \\dfrac{x}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-add',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $\\dfrac{x}{2} + \\dfrac{x}{3}$. (Type as a single fraction like 5x/6.)',
            answer: '5x/6',
            answerType: 'exact',
            hint: 'LCD $= 6$.',
            solution: [
              '$\\dfrac{x}{2} = \\dfrac{3x}{6}$, $\\dfrac{x}{3} = \\dfrac{2x}{6}$. Sum: $\\dfrac{5x}{6}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-divide',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $\\dfrac{2x}{5} \\div \\dfrac{x}{3}$. (As a fraction.)',
            answer: '6/5',
            answerType: 'exact',
            hint: 'Multiply by reciprocal: $\\dfrac{2x}{5} \\cdot \\dfrac{3}{x}$.',
            solution: [
              'Cancel $x$: $\\dfrac{2 \\cdot 3}{5} = \\dfrac{6}{5}$.',
            ],
          },
        },
      ],
    },
  ],
}