import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-9 (VC2M10AA09).
// Solve linear and non-linear simultaneous equations using graphing or
// systematic guess-check-and-refine with digital tools.

export const l10aAaSimultaneousEquations: Topic = {
  id: 'l10a-aa-simultaneous-equations',
  unit: '10A',
  order: 12,
  title: 'Linear and non-linear simultaneous equations',
  blurb:
    'Solve linear and non-linear simultaneous equations using algebra, graphing, or systematic guess-check-and-refine.',
  dotPoints: ['l10a-aa-9'],

  lessons: [
    {
      id: 'linear-linear',
      heading: 'Linear–linear simultaneous equations',
      summary: 'Eliminate one variable by subtraction or matching coefficients; solve for the other, then back-substitute.',
      body: `A pair of **linear simultaneous equations** has one pair $(x, y)$ that satisfies both. Two clean algebraic methods work well; a third (graphical) confirms the answer visually.

### Method 1 — Substitution
1. From one equation, express one variable in terms of the other.
2. Substitute into the other equation. Solve.
3. Back-substitute to find the remaining variable.

### Method 2 — Elimination
1. Multiply the equations so that **one variable matches with opposite signs**.
2. Add the equations to eliminate that variable.
3. Solve for the other, then back-substitute.

### Graphing check
Plot both lines; the intersection point is the solution.`,
      examples: [
        {
          id: 'ex-substitution',
          statement:
            'Solve $y = 2x + 1$ and $3x + y = 16$.',
          steps: [
            'Substitute the first into the second: $3x + (2x + 1) = 16$.',
            '$5x + 1 = 16 \\Rightarrow x = 3$.',
            '$y = 2 \\cdot 3 + 1 = 7$.',
            'Solution $(3, 7)$.',
          ],
        },
        {
          id: 'ex-elimination',
          statement:
            'Solve $2x + y = 10$ and $x - y = 2$.',
          steps: [
            'Add the two equations: $3x = 12 \\Rightarrow x = 4$.',
            'Substitute: $4 - y = 2 \\Rightarrow y = 2$.',
            'Solution $(4, 2)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sub',
          difficulty: 'intro',
          instance: {
            prompt:
              "Solve $y = x + 2$ and $2x + y = 8$. State the $x$-value as an integer.",
            answer: '2',
            answerType: 'numeric',
            hint: 'Substitute the first equation into the second.',
            solution: [
              '$2x + (x + 2) = 8 \\Rightarrow 3x = 6 \\Rightarrow x = 2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-elim',
          difficulty: 'core',
          instance: {
            prompt:
              "Solve $x + y = 10$ and $x - y = 4$. State the $x$-value.",
            answer: '7',
            answerType: 'numeric',
            hint: 'Add the equations to eliminate $y$.',
            solution: [
              'Adding: $2x = 14 \\Rightarrow x = 7$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-elim-2',
          difficulty: 'challenge',
          instance: {
            prompt:
              "Solve $3x + 2y = 16$ and $x - 2y = 0$. State the $y$-value.",
            answer: '2',
            answerType: 'numeric',
            hint: 'Adding eliminates $y$.',
            solution: [
              'Adding: $4x = 16 \\Rightarrow x = 4$. Then $y = x / 1 = 4$? Wait, $x - 2y = 0 \\Rightarrow y = x/2 = 2$. So $y = 2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'linear-nonlinear',
      heading: 'Linear–non-linear simultaneous equations',
      summary: 'Substitute the linear expression into the non-linear one; solve the resulting quadratic; reject any extraneous pairs.',
      body: `When one equation is **linear** and the other is **non-linear** (a parabola, circle, hyperbola, …), substitution is fast.

### Recipe
1. From the linear equation, write $y$ in terms of $x$ (or vice versa).
2. Substitute that expression into the non-linear equation.
3. Solve — you usually get a **quadratic**, so expect **0, 1 or 2** solutions.
4. Back-substitute each $x$-value to find $y$.
5. **Reject** any pair that does not satisfy both original equations.

### Curve geometry interpretation
- A line crossing a parabola in 2 points → 2 solutions.
- A line tangent to a parabola → 1 (repeated) solution.
- A line missing a parabola → 0 solutions.

### Why this is more than just "linear equations"
The number of solutions tells you about the geometry of the intersection.`,
      examples: [
        {
          id: 'ex-parabola',
          statement:
            'Solve $y = x + 3$ and $y = x^2 + 1$.',
          steps: [
            'Substitute: $x + 3 = x^2 + 1$.',
            '$x^2 - x - 2 = 0 \\Rightarrow (x - 2)(x + 1) = 0$.',
            '$x = 2 \\Rightarrow y = 5$, or $x = -1 \\Rightarrow y = 2$.',
            'Solutions $(2, 5)$ and $(-1, 2)$.',
          ],
        },
        {
          id: 'ex-circle',
          statement:
            'Solve $y = x - 1$ and $x^2 + y^2 = 25$.',
          steps: [
            'Substitute: $x^2 + (x - 1)^2 = 25$.',
            '$x^2 + x^2 - 2x + 1 = 25 \\Rightarrow 2x^2 - 2x - 24 = 0 \\Rightarrow x^2 - x - 12 = 0$.',
            '$(x - 4)(x + 3) = 0 \\Rightarrow x = 4, y = 3$ or $x = -3, y = -4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-lnp-1',
          difficulty: 'intro',
          instance: {
            prompt:
              "Solve $y = x + 1$ and $y = x^2 - 1$. List both $x$-values separated by commas, smaller first.",
            answer: '-1, 2',
            answerType: 'set',
            hint: 'Substitute: $x + 1 = x^2 - 1$.',
            solution: [
              '$x^2 - x - 2 = 0 \\Rightarrow (x - 2)(x + 1) = 0$.',
              'So $x \\in \\{-1, 2\\}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-lnp-2',
          difficulty: 'core',
          instance: {
            prompt:
              "Solve $y = x - 2$ and $y = x^2 - 4$. List both $x$-values separated by commas.",
            answer: '-1, 2',
            answerType: 'set',
            hint: 'Substitute, then solve the quadratic.',
            solution: [
              '$x - 2 = x^2 - 4 \\Rightarrow x^2 - x - 2 = 0 \\Rightarrow (x - 2)(x + 1) = 0$.',
              'Solutions $x = 2, x = -1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-lnp-3',
          difficulty: 'challenge',
          instance: {
            prompt:
              "Solve $y = 2x$ and $y = x^2$. List both $x$-values separated by commas, smaller first.",
            answer: '0, 2',
            answerType: 'set',
            hint: 'Substitute: $2x = x^2$.',
            solution: [
              '$x^2 - 2x = x(x - 2) = 0 \\Rightarrow x = 0$ or $x = 2$.',
            ],
          },
        },
      ],
    },
  ],
}
