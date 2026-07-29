import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Algebra · l7-a-5 (VC2M7A05).
// Generate tables of values from visually changing patterns or the rule of a
// function; describe and plot these relationships on the Cartesian plane.

export const l7ATablesCartesian: Topic = {
  id: 'l7-a-tables-cartesian',
  unit: 7,
  order: 15,
  title: 'Tables of values and the Cartesian plane',
  blurb:
    'Generate tables of values from a rule or pattern, and plot those points on the Cartesian plane to describe the relationship.',
  dotPoints: ['l7-a-5'],
  lessons: [
    {
      id: 'tables-of-values',
      heading: 'Building tables of values from a rule',
      summary:
        'Pick x-values, run each one through the rule, and record the result to build an ordered table.',
      body: `A **table of values** is a list of inputs and the matching outputs from a rule. It is the bridge between a formula (or pattern) and a graph.

### Recipe
1. **Choose input values** for the variable. Pick small whole numbers first: $0, 1, 2, 3, \\dots$ — easy to work with.
2. **Apply the rule** to each input. Substitute it into the formula in place of the variable.
3. **Record** the output in the second column.
4. **Look for a pattern** — does each step add the same amount? Multiply by the same number?

### From a visual pattern
A "staircase" pattern where each new term adds $3$ bricks gives the rule $b = 3n$, where $n$ is the step number and $b$ is the number of bricks.

> [!definition] Function
> A **function** is a rule that takes one input and gives exactly one output. The rule may be a formula, a pattern, or a description.

### Two-column layout
| $n$ (input) | Rule $b = 3n$ | $b$ (output) |
| --- | --- | --- |
| $0$ | $3 \\times 0$ | $0$ |
| $1$ | $3 \\times 1$ | $3$ |
| $2$ | $3 \\times 2$ | $6$ |
| $3$ | $3 \\times 3$ | $9$ |

Each row is one **ordered pair** like $(1, 3)$ — input first, output second.`,
      examples: [
        {
          id: 'ex-rule-table',
          statement:
            'Build a table of values for the rule $y = 2x + 1$ using $x = 0, 1, 2, 3$.',
          steps: [
            '$x = 0$: $y = 2(0) + 1 = 1$.',
            '$x = 1$: $y = 2(1) + 1 = 3$.',
            '$x = 2$: $y = 2(2) + 1 = 5$.',
            '$x = 3$: $y = 2(3) + 1 = 7$.',
            'Table: $(0, 1), (1, 3), (2, 5), (3, 7)$.',
          ],
        },
        {
          id: 'ex-pattern-table',
          statement:
            'A pattern of squares: row $n$ has $n^2$ dots. Build a table for rows $1$ to $4$.',
          steps: [
            'Row $1$: $1^2 = 1$ dot.',
            'Row $2$: $2^2 = 4$ dots.',
            'Row $3$: $3^2 = 9$ dots.',
            'Row $4$: $4^2 = 16$ dots.',
            'Table: $(1, 1), (2, 4), (3, 9), (4, 16)$.',
          ],
        },
        {
          id: 'ex-read-rule',
          statement:
            'A table reads $(1, 5), (2, 7), (3, 9), (4, 11)$. Find the rule.',
          steps: [
            'Inputs go up by $1$ each time.',
            'Outputs go up by $2$ each time.',
            'When $x = 1$, $y = 5$ — the rule is $y = 2x + 3$.',
            'Check $x = 4$: $2(4) + 3 = 11$ ✓.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-table-rule',
          difficulty: 'intro',
          instance: {
            prompt:
              'For the rule $y = 3x - 2$, find $y$ when $x = 4$.',
            answer: '10',
            answerType: 'numeric',
            hint: 'Substitute $x = 4$ into the rule.',
            solution: [
              '$y = 3 \\times 4 - 2 = 12 - 2 = 10$.',
            ],
          },
        },
      ],
    },

    {
      id: 'cartesian-plane',
      heading: 'Plotting on the Cartesian plane',
      summary:
        'Read ordered pairs as (x, y), plot them on the two-number-line grid, and connect them to see the rule.',
      body: `The **Cartesian plane** is the grid formed by two number lines crossing at right angles. Every point on the grid can be named by an **ordered pair** $(x, y)$.

### Anatomy
- The **horizontal axis** is the $x$-axis. Positive values are to the right of the centre, negative to the left.
- The **vertical axis** is the $y$-axis. Positive values are above the centre, negative below.
- The point where they meet is the **origin**, written $(0, 0)$.
- The plane is split into four **quadrants** by the two axes.

### Plotting a point
To plot $(3, 4)$:

1. Start at the origin $(0, 0)$.
2. Move $3$ units to the **right** along the $x$-axis.
3. Move $4$ units **up** parallel to the $y$-axis.
4. Mark the point.

> [!warning] Order matters
> $(3, 4)$ and $(4, 3)$ are **different** points. Always travel along $x$ first, then $y$.

### From table to graph
Take each row of the table as an ordered pair, plot the points, and **join them** (with a ruler for a straight line, or freehand for a curve) to see the shape of the rule.`,
      examples: [
        {
          id: 'ex-plot-points',
          statement:
            'Plot the points $(0, 1), (1, 3), (2, 5), (3, 7)$ from the rule $y = 2x + 1$ on the Cartesian plane.',
          steps: [
            'Mark the origin $(0, 0)$.',
            '$(0, 1)$: $0$ right, $1$ up.',
            '$(1, 3)$: $1$ right, $3$ up.',
            '$(2, 5)$: $2$ right, $5$ up.',
            '$(3, 7)$: $3$ right, $7$ up.',
            'Join the four points — they form a straight line sloping upward.',
          ],
        },
        {
          id: 'ex-read-point',
          statement:
            'A point on a graph sits $5$ units right of the origin and $2$ units down. Write it as an ordered pair.',
          steps: [
            'Right is positive on the $x$-axis, so $x = 5$.',
            'Down is negative on the $y$-axis, so $y = -2$.',
            'The point is $(5, -2)$.',
          ],
        },
        {
          id: 'ex-quadrants',
          statement:
            'In which quadrant does the point $(-2, 3)$ lie?',
          steps: [
            '$x = -2$: to the left of the origin.',
            '$y = 3$: above the origin.',
            'Left and up = **Quadrant II** (top-left).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-quadrant',
          difficulty: 'intro',
          instance: {
            prompt:
              'The point $(4, -3)$ lies in which quadrant? Answer with a Roman numeral: I, II, III or IV.',
            answer: 'IV',
            answerType: 'exact',
            hint: 'Right is positive on the $x$-axis; down is negative on the $y$-axis.',
            solution: [
              'Right ($+$) and down ($-$) is the bottom-right quadrant, which is **Quadrant IV**.',
            ],
          },
        },
      ],
    },
  ],
}
