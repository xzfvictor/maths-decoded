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
      id: 'substitute',
      heading: 'Substituting into formulas',
      summary: 'Plug the known values in; apply order of operations to evaluate.',
      body: `A **formula** is a rule that relates variables. **Substitution** is the act of plugging the given values into a formula and computing.

### Order of operations
Brackets first, then powers, then multiplication/division, then addition/subtraction. A calculator follows the same order.

### Watch units
A formula can mix units (e.g. speed in km/h, distance in km). Convert before substituting if the units don't match.`,
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
          id: 'ex-substitute-2',
          statement:
            'The kinetic energy of an object is $E = \\tfrac{1}{2} m v^2$. Find $E$ when $m = 4$ kg and $v = 3$ m/s.',
          steps: [
            '$E = \\tfrac{1}{2} \\cdot 4 \\cdot 3^2 = \\tfrac{1}{2} \\cdot 4 \\cdot 9 = 18$ J.',
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
          id: 'c-substitute-kinetic',
          difficulty: 'core',
          instance: {
            prompt:
              'For $E = \\tfrac{1}{2} m v^2$ with $m = 2$ kg and $v = 5$ m/s, find $E$ (in J).',
            answer: '25',
            answerType: 'numeric',
            hint: '$E = \\tfrac{1}{2} \\cdot 2 \\cdot 25$.',
            solution: [
              '$E = \\tfrac{1}{2} \\cdot 50 = 25$ J.',
            ],
          },
        },
      ],
    },

    {
      id: 'rearrange',
      heading: 'Rearranging formulas',
      summary: 'Apply inverse operations to make the chosen variable the subject.',
      body: `**Rearranging** a formula isolates a chosen variable on its own. Use the same inverse-operations approach as solving an equation.

### Recipe
- Move an **added** term by subtracting it from both sides.
- Move a **multiplied** factor by dividing both sides.
- Move a **power** by taking the matching root (or appropriate index).

### Always check
Substitute back: the rearranged formula should give the same value as the original for any test point.`,
      examples: [
        {
          id: 'ex-rearrange',
          statement:
            'Rearrange $V = \\pi r^2 h$ to make $h$ the subject.',
          steps: [
            'Divide both sides by $\\pi r^2$ (the factor on $h$).',
            '$h = \\dfrac{V}{\\pi r^2}$.',
          ],
        },
        {
          id: 'ex-rearrange-2',
          statement:
            'Rearrange $y = 3x + 5$ to make $x$ the subject.',
          steps: [
            'Subtract $5$: $y - 5 = 3x$.',
            'Divide by $3$: $x = \\dfrac{y - 5}{3}$.',
          ],
        },
      ],
      exercises: [
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
        {
          kind: 'curated',
          id: 'c-rearrange-3',
          difficulty: 'intro',
          instance: {
            prompt:
              'Rearrange $P = 2(L + W)$ to make $W$ the subject. State the formula (as "W = ...").',
            answer: 'W = P/2 - L',
            answerType: 'exact',
            hint: 'Divide both sides by $2$ first, then subtract $L$.',
            solution: [
              '$\\dfrac{P}{2} = L + W$, so $W = \\dfrac{P}{2} - L$.',
            ],
          },
        },
      ],
    },
  ],
}