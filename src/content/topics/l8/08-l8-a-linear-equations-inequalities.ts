import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Algebra · l8-a-2 (VC2M8A02).
// Graph linear relations on the Cartesian plane using digital tools where
// appropriate; solve linear equations and one-variable inequalities using
// graphical and algebraic techniques; verify solutions by substitution.

export const l8ALinearEquationsInequalities: Topic = {
  id: 'l8-a-linear-equations-inequalities',
  unit: 8,
  order: 8,
  title: 'Linear equations and inequalities',
  blurb:
    'Graph linear relations on the Cartesian plane, and solve linear equations and one-variable inequalities using graphical and algebraic techniques.',
  dotPoints: ['l8-a-2'],
  lessons: [
    {
      id: 'graphing-linear-relations',
      heading: 'Graphing linear relations',
      summary:
        'A table of values gives you a handful of points; connect them with a straight line that extends in both directions.',
      body: `A **linear relation** is an equation whose graph is a straight line. The simplest form to graph is $y = mx + c$, where $m$ is the gradient and $c$ is the $y$-intercept.

### How to graph
1. Make a **table of values**: pick at least $3$ values of $x$ and compute the matching $y$.
2. **Plot** the points $(x, y)$ on the Cartesian plane.
3. **Join** them with a straight line that extends past the outermost points.

### Reading from a graph
- The point where the line crosses the **$y$-axis** is the $y$-intercept $c$.
- The **gradient** $m$ is "rise over run": how much $y$ changes when $x$ increases by $1$.

### Using a digital tool
A digital tool (e.g. a spreadsheet or graphing app) lets you plug in many $x$-values quickly and gives an accurate graph.

> [!warning] Watch out
> The line continues **in both directions** — the table only shows a window. Pick $x$-values that spread out (e.g. $-2, 0, 2$) so you can see the line's overall direction.`,
      examples: [
        {
          id: 'ex-table',
          statement:
            'Build a table of values for $y = 2x - 1$ for $x = 0, 1, 2, 3$.',
          steps: [
            '$x = 0$: $y = 2(0) - 1 = -1$.',
            '$x = 1$: $y = 2(1) - 1 = 1$.',
            '$x = 2$: $y = 2(2) - 1 = 3$.',
            '$x = 3$: $y = 2(3) - 1 = 5$.',
            'Points: $(0, -1), (1, 1), (2, 3), (3, 5)$.',
          ],
        },
        {
          id: 'ex-graph-features',
          statement: 'For $y = -3x + 6$, find the $y$-intercept and the gradient.',
          steps: [
            'The $y$-intercept is the constant: $c = 6$, so the line passes through $(0, 6)$.',
            'The gradient is the coefficient of $x$: $m = -3$, so the line falls $3$ units for every $1$ unit right.',
          ],
        },
        {
          id: 'ex-from-two-points',
          statement:
            'A line passes through $(0, 4)$ and $(2, 10)$. Find its equation in the form $y = mx + c$.',
          steps: [
            '$c$ is the $y$-intercept, so $c = 4$.',
            'Gradient: $m = \\dfrac{10 - 4}{2 - 0} = \\dfrac{6}{2} = 3$.',
            'Equation: $y = 3x + 4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-y-intercept',
          difficulty: 'intro',
          instance: {
            prompt: 'For $y = 3x + 5$, what is the $y$-intercept?',
            answer: '5',
            answerType: 'numeric',
            hint: 'The $y$-intercept is the value of $y$ when $x = 0$.',
            solution: [
              'When $x = 0$, $y = 5$. So the $y$-intercept is $5$.',
            ],
          },
        },
      ],
    },
    {
      id: 'solving-equations',
      heading: 'Solving linear equations algebraically',
      summary:
        'Use inverse operations to isolate the variable, then substitute back to verify.',
      body: `Solving a linear equation means finding the value of the variable that makes the equation true. The technique is to apply **inverse operations** to both sides — the same way you did in Year 7, with extra practice at more complex shapes.

### Two-step recipe
1. **Undo addition or subtraction** to move the constant off the variable term.
2. **Undo multiplication or division** to isolate the variable.
3. **Substitute** the answer back into the original equation to verify.

### Variables on both sides
Subtract the smaller variable term from both sides first to get the variable on one side. Then handle the constant as usual.

### Brackets
Expand any brackets first using the distributive law, then continue as above.

> [!definition] Substitution check
> Replace the variable with your answer in the **original** equation. If both sides are equal, the solution is correct.`,
      examples: [
        {
          id: 'ex-two-step',
          statement: 'Solve $3x + 5 = 17$.',
          steps: [
            'Subtract $5$ from both sides: $3x = 12$.',
            'Divide by $3$: $x = 4$.',
            'Check: $3(4) + 5 = 12 + 5 = 17$ ✓.',
          ],
        },
        {
          id: 'ex-both-sides',
          statement: 'Solve $5x - 4 = 2x + 11$.',
          steps: [
            'Subtract $2x$ from both sides: $3x - 4 = 11$.',
            'Add $4$: $3x = 15$.',
            'Divide by $3$: $x = 5$.',
            'Check: $5(5) - 4 = 21$ and $2(5) + 11 = 21$ ✓.',
          ],
        },
        {
          id: 'ex-brackets',
          statement: 'Solve $4(x - 3) = 8$.',
          steps: [
            'Option 1 — divide first: $x - 3 = 2$, so $x = 5$.',
            'Option 2 — expand: $4x - 12 = 8$, then $4x = 20$, then $x = 5$.',
            'Check: $4(5 - 3) = 4(2) = 8$ ✓.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-solve-both-sides',
          difficulty: 'intro',
          instance: {
            prompt: 'Solve $4x + 3 = 2x + 11$.',
            answer: '4',
            answerType: 'numeric',
            hint: 'Subtract $2x$ from both sides first.',
            solution: [
              '$2x + 3 = 11 \\Rightarrow 2x = 8 \\Rightarrow x = 4$.',
            ],
          },
        },
      ],
    },
    {
      id: 'solving-inequalities',
      heading: 'Solving one-variable inequalities',
      summary:
        'Solve like an equation, but flip the sign whenever you divide or multiply by a negative.',
      body: `An **inequality** compares two expressions with $<$, $>$, $\\le$ or $\\ge$. The solution is a **set of values**, not a single number.

### The single critical rule
If you multiply or divide both sides by a **negative** number, the inequality **flips**.

- $3x < 12 \\Rightarrow x < 4$ (no flip — dividing by a positive).
- $-3x < 12 \\Rightarrow x > -4$ (flip — dividing by a negative).

### Otherwise, the rules are the same
- Adding or subtracting (any number) keeps the inequality direction.
- Multiplying or dividing by a positive number keeps the direction.
- Multiplying or dividing by a negative number flips it.

> [!warning] Watch out
> A common slip: dividing by $-2$ and forgetting to flip. The sign of the comparison must change every time you cross a negative multiplier.`,
      examples: [
        {
          id: 'ex-positive-coeff',
          statement: 'Solve $2x + 3 < 11$.',
          steps: [
            'Subtract $3$: $2x < 8$.',
            'Divide by $2$ (positive, no flip): $x < 4$.',
          ],
        },
        {
          id: 'ex-negative-coeff',
          statement: 'Solve $-2x + 3 \\le 9$.',
          steps: [
            'Subtract $3$: $-2x \\le 6$.',
            'Divide by $-2$ (negative, **flip**): $x \\ge -3$.',
          ],
        },
        {
          id: 'ex-with-brackets',
          statement: 'Solve $3(x - 1) > 9$.',
          steps: [
            'Divide by $3$ (positive): $x - 1 > 3$.',
            'Add $1$: $x > 4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-inequality',
          difficulty: 'intro',
          instance: {
            prompt: 'Solve $-3x + 6 \\le 15$. State the largest integer $x$ satisfying this.',
            answer: '-3',
            answerType: 'numeric',
            hint: '$-3x \\le 9 \\Rightarrow x \\ge -3$.',
            solution: [
              '$-3x \\le 9 \\Rightarrow x \\ge -3$. The largest integer satisfying is $-3$.',
            ],
          },
        },
      ],
    },
  ],
}
