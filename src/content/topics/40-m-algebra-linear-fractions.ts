import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A12.
// Solve linear equations involving simple algebraic fractions.

export const algebraLinearFractions: Topic = {
  id: 'm10-algebra-linear-fractions',
  unit: 10,
  order: 18,
  title: 'Linear equations with algebraic fractions',
  blurb:
    'Clear denominators by multiplying through by the LCD, then solve as a regular linear equation.',
  dotPoints: ['m10-a-12'],

  lessons: [
    {
      id: 'clear-numerical',
      heading: 'Clearing numerical denominators',
      summary: 'Multiply every term by the LCD; the fractions collapse; solve.',
      body: `When an equation has **numerical** fractions, the cleanest approach is to **clear denominators**: multiply every term by the LCD.

### Recipe
1. Identify the LCD — the smallest number divisible by every denominator.
2. Multiply each term on **both** sides by the LCD.
3. Cancel denominators; the equation is now fraction-free.
4. Solve as a linear equation.
5. **Check** by substituting back.

### Worked numerical example
$\\dfrac{x}{3} + \\dfrac{x}{4} = 7 \\Rightarrow$ multiply by $12$: $4x + 3x = 84 \\Rightarrow 7x = 84 \\Rightarrow x = 12$.`,
      examples: [
        {
          id: 'ex-clear-1',
          statement:
            'Solve $\\dfrac{x}{2} + \\dfrac{x}{3} = 10$.',
          steps: [
            'LCD $= 6$. Multiply through: $3x + 2x = 60$.',
            '$5x = 60 \\Rightarrow x = 12$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-clear-simple',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $\\dfrac{x}{2} + 3 = 7$. State $x$.',
            answer: '8',
            answerType: 'numeric',
            hint: 'Multiply through by $2$ to clear the denominator.',
            solution: [
              '$x + 6 = 14 \\Rightarrow x = 8$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-clear',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $\\dfrac{x}{2} + \\dfrac{x}{3} = 5$. State $x$.',
            answer: '6',
            answerType: 'numeric',
            hint: 'LCD $= 6$.',
            solution: [
              '$3x + 2x = 30 \\Rightarrow 5x = 30 \\Rightarrow x = 6$.',
            ],
          },
        },
      ],
    },

    {
      id: 'algebraic-denominators',
      heading: 'Algebraic denominators & extraneous roots',
      summary: 'Multiplying by something that could be zero can introduce extraneous solutions — always check.',
      body: `Sometimes the denominator contains a variable. The strategy is the same — clear the denominator by multiplying through — but you must **check** that the answer doesn't make any denominator zero.

### Recipe
1. Identify the LCD, including any algebraic factors.
2. Multiply through.
3. Solve.
4. **Substitute back** to ensure no denominator is $0$. If it is, that value is **extraneous** and must be discarded.

### Worked example
$\\dfrac{2}{x - 1} = 5 \\Rightarrow$ multiply by $x - 1$: $2 = 5(x - 1) \\Rightarrow 2 = 5x - 5 \\Rightarrow x = \\tfrac{7}{5}$. The answer $x = \\tfrac{7}{5}$ doesn't make $x - 1 = 0$, so it's valid.`,
      examples: [
        {
          id: 'ex-clear-2',
          statement:
            'Solve $\\dfrac{2x + 1}{3} - \\dfrac{x}{4} = 5$.',
          steps: [
            'LCD $= 12$. Multiply through: $4(2x + 1) - 3x = 60$.',
            '$8x + 4 - 3x = 60 \\Rightarrow 5x = 56 \\Rightarrow x = \\tfrac{56}{5} = 11.2$.',
          ],
        },
        {
          id: 'ex-extraneous',
          statement:
            'Solve $\\dfrac{1}{x - 2} = \\dfrac{1}{3}$. What value(s) of $x$ are valid?',
          steps: [
            'Multiply by $x - 2$: $1 = \\tfrac{1}{3}(x - 2)$.',
            '$x - 2 = 3 \\Rightarrow x = 5$.',
            'Check: $\\tfrac{1}{5 - 2} = \\tfrac{1}{3}$ ✓. So $x = 5$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-algebraic',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $\\dfrac{3}{x} = \\tfrac{1}{2}$. State $x$.',
            answer: '6',
            answerType: 'numeric',
            hint: 'Multiply both sides by $x$: $3 = \\tfrac{1}{2} x$.',
            solution: [
              '$x = 6$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-mixed',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $\\dfrac{x}{2} + \\dfrac{x}{5} = 7$. State $x$.',
            answer: '10',
            answerType: 'numeric',
            hint: 'LCD $= 10$.',
            solution: [
              '$5x + 2x = 70 \\Rightarrow 7x = 70 \\Rightarrow x = 10$.',
            ],
          },
        },
      ],
    },
  ],
}