import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Algebra · l7-a-6 (VC2M7A06).
// Manipulate formulas involving several variables using digital tools, and
// describe the effect of systematic variation in the values of the variables.

export const l7AFormulasSeveralVariables: Topic = {
  id: 'l7-a-formulas-several-variables',
  unit: 7,
  order: 16,
  title: 'Formulas with several variables',
  blurb:
    'Manipulate formulas with multiple variables using digital tools and describe the effect of systematic variation in the values.',
  dotPoints: ['l7-a-6'],
  lessons: [
    {
      id: 'multi-variable-formulas',
      heading: 'Working with formulas that have several variables',
      summary:
        'Substitute, rearrange and explore how changing one variable changes the result, keeping the others fixed.',
      body: `Many formulas from real life involve **more than one variable**. The **area of a rectangle** $A = lw$ uses length $l$ and width $w$. The **perimeter of a triangle** $P = a + b + c$ uses three sides.

### Substituting into a multi-variable formula
With $A = lw$:

- $l = 5, w = 3 \\Rightarrow A = 5 \\times 3 = 15$.
- $l = 12, w = 4 \\Rightarrow A = 12 \\times 4 = 48$.

Only the values change — the formula stays the same.

### Rearranging (transposing)
You can rearrange a formula to make a different variable the subject. The algebra is the same as solving an equation: do the same thing to both sides.

- $A = lw$ → divide by $w$: $l = A / w$.
- $P = 2l + 2w$ → subtract $2w$: $P - 2w = 2l$ → divide by $2$: $l = (P - 2w) / 2$.

> [!definition] Subject of a formula
> The **subject** is the variable that stands alone on one side of the equation — the one the formula is "solving for".

### Systematic variation
"S**ystematic variation**" means changing one variable in a regular pattern (often by the same step each time) while keeping the others fixed. A spreadsheet makes this easy.

- Hold $w = 4$ and let $l$ grow: $1, 2, 3, 4, 5$ → $A$ grows by $4$ each row.
- Hold $l = 5$ and let $w$ grow: $1, 2, 3, 4, 5$ → $A$ grows by $5$ each row.

**Doubling** one variable doubles the area; doubling both quadruples it.

### Describing the effect
- "As $l$ increases by $1$ (with $w$ fixed), $A$ increases by $w$."
- "If $l$ is doubled (with $w$ fixed), $A$ is also doubled."`,
      examples: [
        {
          id: 'ex-substitute-multi',
          statement:
            'The area of a triangle is $A = \\dfrac{1}{2} b h$. Find $A$ when $b = 10$ cm and $h = 6$ cm.',
          steps: [
            'Substitute: $A = \\dfrac{1}{2} \\times 10 \\times 6$.',
            'Multiply: $10 \\times 6 = 60$.',
            'Halve: $A = 30$ cm$^2$.',
          ],
        },
        {
          id: 'ex-rearrange',
          statement:
            'Rearrange $v = u + at$ to make $a$ the subject.',
          steps: [
            'Subtract $u$ from both sides: $v - u = at$.',
            'Divide both sides by $t$: $a = (v - u) / t$.',
            'Check: substitute back: $u + ((v - u) / t) \\times t = u + v - u = v$ ✓.',
          ],
        },
        {
          id: 'ex-systematic-doubling',
          statement:
            'A rectangle has area $A = lw$. With $w = 4$, the length is doubled from $l = 3$ to $l = 6$. How does the area change?',
          steps: [
            'Original: $A = 3 \\times 4 = 12$.',
            'New: $A = 6 \\times 4 = 24$.',
            'Ratio: $24 / 12 = 2$. The area doubled.',
            'Doubling one variable (with the other fixed) doubles the area.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-substitute-area',
          difficulty: 'intro',
          instance: {
            prompt:
              'The area of a rectangle is $A = l \\times w$. Find $A$ when $l = 9$ cm and $w = 7$ cm.',
            answer: '63',
            answerType: 'numeric',
            hint: 'Multiply $9$ by $7$.',
            solution: [
              '$A = 9 \\times 7 = 63$ cm$^2$.',
            ],
          },
        },
      ],
    },
  ],
}
