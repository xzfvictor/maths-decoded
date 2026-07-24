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
      id: 'choose-model',
      heading: 'Choosing the right model',
      summary: 'Look at how consecutive values change to pick linear, quadratic or exponential.',
      body: `Mathematical modelling picks the right function family for the data.

### How to pick
- **Constant first differences** → **linear** $y = mx + b$.
- **Constant second differences** → **quadratic** $y = ax^2 + bx + c$.
- **Constant ratio** between consecutive values → **exponential** $y = a \\cdot b^x$.

### Quick test
For a sequence $a_0, a_1, a_2, \\ldots$:
- Look at $a_{i+1} - a_i$. If constant → linear.
- Look at the differences of those differences. If constant → quadratic.
- Look at $a_{i+1} / a_i$. If constant → exponential.`,
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
          id: 'ex-pick-linear',
          statement:
            'A sequence goes $\\{5, 8, 11, 14, \\dots\\}$. Which model fits?',
          steps: [
            'Differences: $3, 3, 3$ — constant first differences.',
            '**Linear**: $y = 3n + 5$ (starting at $n=0$).',
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
          id: 'c-pick-exp',
          difficulty: 'core',
          instance: {
            prompt:
              'A sequence goes $\\{4, 12, 36, 108, \\dots\\}$. Linear, quadratic, or exponential? Answer "linear", "quadratic", or "exponential".',
            answer: 'exponential',
            answerType: 'exact',
            hint: 'Look at the ratios between consecutive terms.',
            solution: [
              'Ratios are $3, 3, 3$ — constant ratio → exponential.',
            ],
          },
        },
      ],
    },

    {
      id: 'compound-interest',
      heading: 'Compound interest & growth/decay',
      summary: 'A_n = A_0 (1 + r)^n; b>1 grows, 0<b<1 decays.',
      body: `### Compound interest
After $n$ periods at rate $r$ per period,
$$A_n = A_0 \\bigl(1 + r\\bigr)^n.$$
E.g. $\\$1000$ at $5\\%$ per year, compounded: $A_n = 1000 \\cdot 1.05^n$.

### Growth and decay
- $b > 1$ in $y = a \\cdot b^x$ → **growth**.
- $0 < b < 1$ in $y = a \\cdot b^x$ → **decay**.

### Half-life
The time until the amount halves. For decay $b = \\tfrac{1}{2}$, $t_{1/2} = 1$ period.`,
      examples: [
        {
          id: 'ex-compound',
          statement:
            "You invest $\\$1000$ at $5\\%$ per year, compounded annually. What is the balance after $3$ years? (Nearest dollar.)",
          steps: [
            '$A_3 = 1000 \\cdot 1.05^3 = 1000 \\cdot 1.157625 = \\$1157.63$.',
            'Rounded: $\\$1158$.',
          ],
        },
        {
          id: 'ex-decay',
          statement:
            "A substance decays so each year $80\\%$ of the previous year's mass remains. After $4$ years, what fraction remains?",
          steps: [
            '$0.8^4 = 0.4096$.',
            'So about $41\\%$ remains.',
          ],
        },
      ],
      exercises: [
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
        {
          kind: 'curated',
          id: 'c-decay',
          difficulty: 'intro',
          instance: {
            prompt:
              'A quantity halves each day. Starting from $64$, what is the amount after $4$ days?',
            answer: '4',
            answerType: 'numeric',
            hint: 'Each day multiply by $\\tfrac{1}{2}$.',
            solution: [
              '$64 \\cdot (\\tfrac{1}{2})^4 = 64 / 16 = 4$.',
            ],
          },
        },
      ],
    },

    {
      id: 'inverse-proportion',
      heading: 'Inverse proportion',
      summary: 'y = k/x — the product xy is constant.',
      body: `Two quantities are in **inverse proportion** when one grows as the other shrinks, so their product stays constant:
$$y = \\frac{k}{x} \\quad \\text{or} \\quad xy = k.$$

### Examples
- Travel time vs speed for a fixed distance: $t \\cdot v = d$.
- Brightness vs distance from a light source (in simple settings).
- Workers vs days to finish a job (workers $\\cdot$ days = constant).`,
      examples: [
        {
          id: 'ex-inverse',
          statement:
            'It takes $4$ workers $6$ days to build a wall. How long would $3$ workers take (inverse proportion)?',
          steps: [
            'Workers $\\cdot$ days $= 4 \\cdot 6 = 24$ (constant).',
            '$3 \\cdot d = 24 \\Rightarrow d = 8$ days.',
          ],
        },
        {
          id: 'ex-inverse-2',
          statement:
            'At $60$ km/h, a trip takes $2$ hours. How long at $40$ km/h (same distance)?',
          steps: [
            'Speed $\\cdot$ time $= 60 \\cdot 2 = 120$ km (the distance).',
            'New time: $120 / 40 = 3$ hours.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-inverse',
          difficulty: 'core',
          instance: {
            prompt:
              'It takes $6$ workers $5$ days to do a job. How many days for $10$ workers (inverse proportion)?',
            answer: '3',
            answerType: 'numeric',
            hint: 'Workers $\\cdot$ days $= 6 \\cdot 5 = 30$.',
            solution: [
              '$10 \\cdot d = 30 \\Rightarrow d = 3$ days.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-inverse-2',
          difficulty: 'intro',
          instance: {
            prompt:
              'At $30$ km/h, a trip takes $4$ hours. At $60$ km/h (same distance), how long does it take?',
            answer: '2',
            answerType: 'numeric',
            hint: 'Distance $= 30 \\cdot 4 = 120$ km.',
            solution: [
              '$120 / 60 = 2$ hours.',
            ],
          },
        },
      ],
    },
  ],
}