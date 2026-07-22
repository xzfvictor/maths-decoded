import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A05.
// Substitute values into formulas to determine an unknown and rearrange
// formulas to solve for a particular term.

export const algebraFormulas: Topic = {
  id: 'm10-algebra-formulas',
  unit: 10,
  order: 11,
  title: 'Substituting into and rearranging formulas',
  blurb:
    'Plug values into a formula to find an unknown; rearrange a formula to make a chosen variable the subject.',
  dotPoints: ['m10-a-5'],

  lessons: [
    {
      id: 'substitute-rearrange',
      heading: 'Substitute, then rearrange',
      summary: 'Two skills: substitute to evaluate; rearrange to solve for a chosen variable.',
      body: `A **formula** is a rule that relates variables. Two skills to master:

### 1. Substitution
Plug the given values into the formula and compute. Order of operations matters — brackets first, then powers, then multiplication/division, then addition/subtraction.

### 2. Rearrangement
Solve for a chosen variable by inverse operations, working from outside in.

- Move an **added** term by subtracting it from both sides.
- Move a **multiplied** factor by dividing both sides.
- Move a **power** by taking the matching root (or appropriate index).

Check your work by **substituting back**: the rearranged formula should give the same value as the original.`,
      examples: [
        {
          id: 'ex-substitute',
          statement:
            'The area of a trapezium is $A = \\dfrac{1}{2}(a + b)h$. Find $A$ when $a = 6, b = 4, h = 5$.',
          steps: [
            '$A = \\tfrac{1}{2}(6 + 4) \\cdot 5 = \\tfrac{1}{2} \\cdot 10 \\cdot 5 = 25$.',
          ],
        },
        {
          id: 'ex-rearrange',
          statement:
            'Rearrange $V = \\pi r^2 h$ to make $h$ the subject.',
          steps: [
            'Divide both sides by $\\pi r^2$ (the factor on $h$).',
            '$h = \\dfrac{V}{\\pi r^2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-substitute-2',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $A = \\dfrac{1}{2}(a + b)h$ with $a = 8$, $b = 2$, $h = 6$, find $A$.',
            answer: '30',
            answerType: 'numeric',
            hint: '$A = \\tfrac12(8 + 2) \\cdot 6 = \\tfrac12 \\cdot 10 \\cdot 6$.',
            solution: [
              '$A = \\tfrac12 \\cdot 60 = 30$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-rearrange-check',
          difficulty: 'core',
          instance: {
            prompt:
              'Rearrange $C = 2\\pi r$ to make $r$ the subject. State the formula (as "r = ...").',
            answer: 'r = C/(2pi)',
            answerType: 'exact',
            hint: 'Divide both sides by $2\\pi$.',
            solution: [
              '$r = \\dfrac{C}{2\\pi}$.',
            ],
          },
        },
      ],
    },
  ],
}