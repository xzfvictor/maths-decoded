import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-3 (VC2M10AA03).
// Simplify combinations of linear expressions with rational coefficients
// and the solution of related equations.

export const l10aAaLinearRational: Topic = {
  id: 'l10a-aa-linear-rational',
  unit: '10A',
  order: 6,
  title: 'Linear expressions with rational coefficients',
  blurb:
    'Simplify combinations of linear expressions with rational coefficients and solve equations with fractions in them.',
  dotPoints: ['l10a-aa-3'],

  lessons: [
    {
      id: 'expanding-rational',
      heading: 'Expanding brackets with rational coefficients',
      summary: 'Distribute negative signs and fractions carefully; every term must receive the multiplier.',
      body: `Linear expressions with rational (fraction) coefficients are still expanded with the distributive law — you just have to be more careful with signs and small numerators.

### Worked-out types
- **Fractional coefficient**: $\\tfrac{1}{2}(4x - 6) = 2x - 3$.
- **Distributing a negative**: $-(3x - 5) = -3x + 5$.
- **A combined example**: $-\\tfrac{2}{3}(9x + 12) = -6x - 8$.

### Pitfalls
- Forgetting to distribute to **every** term inside the bracket.
- Forgetting that minus signs flip signs.
- Letting units slip — $\\tfrac{1}{2} \\cdot 12 = 6$, not $5$.`,
      examples: [
        {
          id: 'ex-half',
          statement: 'Expand $\\tfrac{1}{4}(8x - 12)$.',
          steps: [
            'Multiply every term by $\\tfrac{1}{4}$.',
            '$\\tfrac{1}{4} \\cdot 8x = 2x$ and $\\tfrac{1}{4} \\cdot (-12) = -3$.',
            'Result: $2x - 3$.',
          ],
        },
        {
          id: 'ex-neg',
          statement: 'Expand $-\\tfrac{3}{5}(10x + 15)$.',
          steps: [
            'Distribute $-\\tfrac{3}{5}$.',
            '$-\\tfrac{3}{5} \\cdot 10x = -6x$ and $-\\tfrac{3}{5} \\cdot 15 = -9$.',
            'Result: $-6x - 9$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-expand-half',
          difficulty: 'intro',
          instance: {
            prompt:
              'Expand $\\tfrac{1}{3}(6x - 9)$.',
            answer: '2x-3',
            answerType: 'polynomial',
            hint: 'Multiply each term by $\\tfrac{1}{3}$.',
            solution: [
              '$\\tfrac{1}{3} \\cdot 6x = 2x$ and $\\tfrac{1}{3} \\cdot (-9) = -3$. So $2x - 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-expand-neg',
          difficulty: 'core',
          instance: {
            prompt:
              'Expand $-2(3x - 5)$.',
            answer: '-6x+10',
            answerType: 'polynomial',
            hint: 'Distribute the minus sign to every term.',
            solution: [
              '$-2 \\cdot 3x = -6x$ and $-2 \\cdot (-5) = 10$. So $-6x + 10$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-expand-3',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Expand $-\\tfrac{2}{7}(14x + 21)$.',
            answer: '-4x-6',
            answerType: 'polynomial',
            hint: 'Both terms get the factor $-\\tfrac{2}{7}$.',
            solution: [
              '$-\\tfrac{2}{7} \\cdot 14x = -4x$ and $-\\tfrac{2}{7} \\cdot 21 = -6$. So $-4x - 6$.',
            ],
          },
        },
      ],
    },

    {
      id: 'simplifying-rational',
      heading: 'Simplifying rational linear expressions',
      summary: 'Combine like terms after expanding, or collect like terms before expanding — either path yields the same simplified form.',
      body: `Many simplification tasks come as **products of binomials with rational coefficients** that must be expanded and collected.

### Recipe
1. **Distribute**: expand each bracket fully.
2. **Collect like terms**: group the $x$ terms and constants.
3. **Simplify the coefficients**: any fraction arithmetic (e.g. $\\tfrac{1}{2} + \\tfrac{1}{4} = \\tfrac{3}{4}$).

### Equivalently: factor first
Sometimes expanding just to recollect is wasteful. Look for a common factor **before** distributing.`,
      examples: [
        {
          id: 'ex-collect',
          statement:
            'Simplify $\\tfrac{1}{2}(x + 4) + \\tfrac{1}{3}(x - 6)$.',
          steps: [
            'Expand: $\\tfrac{1}{2}x + 2 + \\tfrac{1}{3}x - 2$.',
            'Collect $x$: $\\tfrac{1}{2}x + \\tfrac{1}{3}x = \\tfrac{3}{6}x + \\tfrac{2}{6}x = \\tfrac{5}{6}x$.',
            'Constants: $2 - 2 = 0$.',
            'Result: $\\tfrac{5}{6}x$.',
          ],
        },
        {
          id: 'ex-factor-first',
          statement:
            'Simplify $\\tfrac{3}{4}(2x + 6) - \\tfrac{1}{2}(x + 4)$.',
          steps: [
            'Expand: $\\tfrac{3}{2}x + \\tfrac{9}{2} - \\tfrac{1}{2}x - 2$.',
            '$\\tfrac{3}{2}x - \\tfrac{1}{2}x = x$.',
            '$\\tfrac{9}{2} - 2 = \\tfrac{9}{2} - \\tfrac{4}{2} = \\tfrac{5}{2}$.',
            'Result: $x + \\tfrac{5}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-simplify',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $\\tfrac{1}{3}(3x + 6) + \\tfrac{1}{2}(4x - 8)$. Type the polynomial.',
            answer: '3x-2',
            answerType: 'polynomial',
            hint: 'Expand each bracket first.',
            solution: [
              '$x + 2 + 2x - 4 = 3x - 2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-simplify-2',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Simplify $-\\tfrac{1}{4}(8x + 12) + \\tfrac{1}{2}(6x - 10)$. Type the polynomial.',
            answer: 'x-8',
            answerType: 'polynomial',
            hint: 'Distribute carefully and watch the signs.',
            solution: [
              '$-2x - 3 + 3x - 5 = x - 8$.',
            ],
          },
        },
      ],
    },

    {
      id: 'solving-rational',
      heading: 'Equations with rational coefficients',
      summary: 'Multiply through by the common denominator to clear fractions; then solve the resulting linear equation.',
      body: `Many linear equations have rational coefficients. The cleanest path is to **clear the fractions** first, then solve.

### Method 1 — Multiply by the LCD
1. Find the lowest common denominator of all fractions in the equation.
2. Multiply **every term** on both sides by the LCD.
3. Solve the resulting whole-number equation.

### Method 2 — Keep fractions, use inverse operations
Equivalent but more error-prone for beginners. Method $1$ is recommended.

### Why multiplying through works
Multiplication is reversible and preserves equality: if $A = B$ then $kA = kB$ for any non-zero $k$. So multiplying every term by the LCD is a legitimate step.`,
      examples: [
        {
          id: 'ex-lcd',
          statement: 'Solve $\\tfrac{x}{3} + 2 = 5$.',
          steps: [
            'LCD is $3$. Multiply through: $3 \\cdot \\tfrac{x}{3} + 3 \\cdot 2 = 3 \\cdot 5$.',
            '$x + 6 = 15$.',
            '$x = 9$.',
          ],
        },
        {
          id: 'ex-lcd-2',
          statement: 'Solve $\\tfrac{1}{2}(x - 3) = \\tfrac{2}{3}(x + 4)$.',
          steps: [
            'LCD is $6$. Multiply through: $3(x - 3) = 4(x + 4)$.',
            '$3x - 9 = 4x + 16$.',
            '$-x = 25 \\Rightarrow x = -25$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-solve-half',
          difficulty: 'intro',
          instance: {
            prompt:
              'Solve $\\tfrac{x}{2} = 7$.',
            answer: '14',
            answerType: 'numeric',
            hint: 'Multiply both sides by $2$.',
            solution: [
              '$x = 7 \\cdot 2 = 14$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-solve-bracket',
          difficulty: 'core',
          instance: {
            prompt:
              'Solve $\\tfrac{1}{4}(x + 8) = 5$.',
            answer: '12',
            answerType: 'numeric',
            hint: 'LCD is $4$.',
            solution: [
              '$\\tfrac{1}{4}(x + 8) = 5 \\Rightarrow x + 8 = 20 \\Rightarrow x = 12$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-solve-neg',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Solve $-\\tfrac{2}{5}(x - 3) = 4$.',
            answer: '-7',
            answerType: 'numeric',
            hint: 'Multiply through by $5$ first.',
            solution: [
              '$-2(x - 3) = 20 \\Rightarrow -2x + 6 = 20 \\Rightarrow -2x = 14 \\Rightarrow x = -7$.',
            ],
          },
        },
      ],
    },
  ],
}
