import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Algebra · l7-a-3 (VC2M7A03).
// Solve one-variable linear equations of increasing complexity with natural
// number solutions; verify equation solutions by substitution.

export const l7ALinearEquations: Topic = {
  id: 'l7-a-linear-equations',
  unit: 7,
  order: 13,
  title: 'One-variable linear equations',
  blurb:
    'Solve one-variable linear equations of increasing complexity with natural number solutions, and verify by substitution.',
  dotPoints: ['l7-a-3'],
  lessons: [
    {
      id: 'solving-linear-equations',
      heading: 'Solving one-variable linear equations',
      summary:
        'Use inverse operations to isolate the variable, then substitute back to check the solution.',
      body: `A **linear equation** in one variable is an equation like $3x + 5 = 20$ — the variable has no exponent and is not inside a fraction. To **solve** it means to find the value of the variable that makes the equation true.

### Balance principle
An equation is like a balanced set of scales. Whatever you do to one side, you must do to the other.

- Add the same number to both sides.
- Subtract the same number from both sides.
- Multiply or divide both sides by the same (non-zero) number.

### Two-step recipe
1. **Undo addition or subtraction first** to move the constant off the variable term.
2. **Undo multiplication or division** to isolate the variable.
3. **Substitute** the answer back into the original equation to check.

> [!definition] Verification
> Always replace the variable with your answer in the **original** equation. If both sides match, your solution is correct.

### Worked through
$3x + 5 = 20$

- Subtract $5$ from both sides: $3x = 15$.
- Divide both sides by $3$: $x = 5$.
- Check: $3 \\times 5 + 5 = 15 + 5 = 20$ ✓.

### More complex shapes
Some equations have $x$ on both sides or a bracket. Tackle the **brackets first**, then move variable terms to one side and constants to the other.

- $5x - 7 = 3x + 9$ → subtract $3x$: $2x - 7 = 9$ → add $7$: $2x = 16$ → $x = 8$.`,
      examples: [
        {
          id: 'ex-two-step',
          statement: 'Solve $2x + 9 = 21$.',
          steps: [
            'Subtract $9$ from both sides: $2x = 12$.',
            'Divide both sides by $2$: $x = 6$.',
            'Check: $2 \\times 6 + 9 = 12 + 9 = 21$ ✓.',
          ],
        },
        {
          id: 'ex-brackets',
          statement: 'Solve $4(x - 3) = 20$.',
          steps: [
            'Either expand: $4x - 12 = 20$ → $4x = 32$ → $x = 8$.',
            'Or divide both sides by $4$ first: $x - 3 = 5$ → $x = 8$.',
            'Check: $4 \\times (8 - 3) = 4 \\times 5 = 20$ ✓.',
          ],
        },
        {
          id: 'ex-both-sides',
          statement: 'Solve $5x - 4 = 3x + 12$.',
          steps: [
            'Subtract $3x$ from both sides: $2x - 4 = 12$.',
            'Add $4$ to both sides: $2x = 16$.',
            'Divide by $2$: $x = 8$.',
            'Check: $5 \\times 8 - 4 = 36$, $3 \\times 8 + 12 = 36$ ✓.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-two-step',
          difficulty: 'intro',
          instance: {
            prompt: 'Solve $3x + 4 = 19$. State the value of $x$.',
            answer: '5',
            answerType: 'numeric',
            hint: 'Subtract $4$ first, then divide by $3$.',
            solution: [
              '$3x = 15$, so $x = 5$. Check: $3 \\times 5 + 4 = 19$ ✓.',
            ],
          },
        },
      ],
    },
  ],
}
