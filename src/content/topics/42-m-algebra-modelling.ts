import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A15.
// Use mathematical modelling to solve applied problems involving inverse
// proportion, growth and decay, including in financial contexts to
// establish the compound interest formula; formulate problems, choose
// to apply linear, quadratic or exponential models; interpret solutions
// in terms of the situation; evaluate and modify models as necessary.

export const algebraModelling: Topic = {
  id: 'm10-algebra-modelling',
  unit: 10,
  order: 20,
  title: 'Modelling with linear, quadratic & exponential functions',
  blurb:
    'Pick the model that fits the data — linear for constant change, quadratic for constant second-difference, exponential for constant ratio.',
  dotPoints: ['m10-a-15'],

  lessons: [
    {
      id: 'choose-the-model',
      heading: 'Choosing the right model',
      summary: 'Look at how consecutive values change to pick linear, quadratic or exponential.',
      body: `Mathematical modelling picks the right function family for the data.

### How to pick
- **Constant first differences** → **linear** $y = mx + b$.
- **Constant second differences** → **quadratic** $y = ax^2 + bx + c$.
- **Constant ratio** between consecutive values → **exponential** $y = a \\cdot b^x$.

### Compound interest
After $n$ periods at rate $r$ per period,
$$A_n = A_0 \\bigl(1 + r\\bigr)^n.$$
E.g. $\\$1000$ at $5\\%$ per year, compounded: $A_n = 1000 \\cdot 1.05^n$.

### Inverse proportion
$y = \\dfrac{k}{x}$ — the product $xy$ is constant. Examples: travel time vs speed, brightness vs distance from a light source.

### Growth and decay
Exponential with $b > 1$ is growth; $0 < b < 1$ is decay. Half-life $t_{1/2}$: the time until the amount halves — satisfy $(1/2)^1 = (1/2)$ from the equation.`,
      examples: [
        {
          id: 'ex-pick-model',
          statement:
            'A sequence goes $\\{2, 6, 18, 54, \\dots\\}$. Linear, quadratic, or exponential?',
          steps: [
            'Ratios: $6/2 = 3$, $18/6 = 3$, $54/18 = 3$.',
            'Constant ratio $3$ → **exponential** with rule $y = 2 \\cdot 3^n$ (starting $n=0$).',
          ],
        },
        {
          id: 'ex-compound',
          statement:
            "You invest $\\$1000$ at $5\\%$ per year, compounded annually. What is the balance after $3$ years? (Nearest dollar.)",
          steps: [
            '$A_3 = 1000 \\cdot 1.05^3 = 1000 \\cdot 1.157625 = \\$1157.63$.',
            'Rounded: $\\$1158$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pick',
          difficulty: 'intro',
          instance: {
            prompt:
              'A sequence goes $\\{5, 8, 11, 14, \\dots\\}$. Linear, quadratic, or exponential? Answer "linear", "quadratic", or "exponential".',
            answer: 'linear',
            answerType: 'exact',
            hint: 'Look at the differences between consecutive terms.',
            solution: [
              'Differences are $3, 3, 3$ — constant first differences.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-compound',
          difficulty: 'core',
          instance: {
            prompt:
              'You invest $\\$500$ at $4\\%$ per year, compounded annually. What is the balance after $2$ years? (Nearest dollar.)',
            answer: '541',
            answerType: 'numeric',
            hint: '$A_2 = 500 \\cdot 1.04^2$.',
            solution: [
              '$500 \\cdot 1.0816 = 540.80$, which rounds to $\\$541$.',
            ],
          },
        },
      ],
    },
  ],
}