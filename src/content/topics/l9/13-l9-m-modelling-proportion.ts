import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Measurement · l9-m-5 (VC2M9M05).
// Mathematical modelling with proportion, rates and scale.

export const l9MModellingProportion: Topic = {
  id: 'l9-m-modelling-proportion',
  unit: 9,
  order: 13,
  title: 'Modelling with proportion, rates and scale',
  blurb:
    'Use mathematical modelling to solve practical problems involving direct proportion, rates, ratio and scale, including financial contexts.',
  dotPoints: ['l9-m-5'],

  lessons: [
    {
      id: 'proportion-rates',
      heading: 'Direct proportion & rates',
      summary: 'Find the unit rate; multiply to scale up, divide to scale down.',
      body: `Two quantities are in **direct proportion** when doubling one doubles the other. The relationship can always be written
$$y = kx,$$
where $k$ is the constant of proportionality (also called the **unit rate**).

### The recipe
1. From one known pair, compute $k = y/x$.
2. Use $y = kx$ to answer any other $x$ (or rearrange to get $x$ from $y$).

### Rates
A **rate** is a comparison of two quantities with different units, e.g. km/h, $/kg, L/100 km. Rates are the unit values $k$ in the proportion formula.`,
      examples: [
        {
          id: 'ex-rate',
          statement:
            'A car uses $6$ L of petrol to travel $80$ km. How far can it travel on $15$ L (assume direct proportion)?',
          steps: [
            'Rate: $80 / 6 \\approx 13.33$ km per litre.',
            'On $15$ L: $15 \\times 13.33 \\approx 200$ km.',
          ],
        },
        {
          id: 'ex-constant',
          statement:
            'A machine stamps $240$ parts in $4$ hours at a constant rate. How many parts in $7$ hours?',
          steps: [
            'Rate: $240 / 4 = 60$ parts per hour.',
            'In $7$ hours: $60 \\times 7 = 420$ parts.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-rate',
          difficulty: 'intro',
          instance: {
            prompt:
              'A car uses $5$ L of fuel to travel $60$ km. How many litres for $240$ km (direct proportion)?',
            answer: '20',
            answerType: 'numeric',
            hint: 'Rate $= 60/5 = 12$ km/L.',
            solution: [
              '$240 / 12 = 20$ L.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-wage',
          difficulty: 'core',
          instance: {
            prompt:
              'A worker earns $\\$180$ for $6$ hours. At the same rate, how much for $11$ hours? (As an integer.)',
            answer: '330',
            answerType: 'numeric',
            hint: 'Rate: $180/6 = 30$ per hour.',
            solution: [
              '$11 \\times 30 = \\$330$.',
            ],
          },
        },
      ],
    },

    {
      id: 'ratio-scale-finance',
      heading: 'Ratio, scale & financial contexts',
      summary: 'A ratio compares two quantities; a scale turns a drawing into reality; both feed financial maths.',
      body: `A **ratio** $a : b$ compares two quantities of the same kind. To split a total in ratio $a : b$, share it as $\\tfrac{a}{a+b}$ and $\\tfrac{b}{a+b}$.

### Scale drawings
A **scale** of $1 : n$ means $1$ unit on the drawing represents $n$ units in real life. **Lengths** scale by the factor $n$; **areas** by $n^2$; **volumes** by $n^3$.

### Financial modelling
Direct proportion powers simple financial maths:
- Best-buy comparison: price $\\div$ weight or price $\\div$ volume gives a unit rate.
- Wages, fuel use, electricity bills all reduce to a unit rate times the quantity used.`,
      examples: [
        {
          id: 'ex-ratio',
          statement:
            'Split $\\$150$ between Anu and Bao in the ratio $2 : 3$.',
          steps: [
            'Total parts: $2 + 3 = 5$. Each part: $150 / 5 = \\$30$.',
            'Anu: $2 \\times 30 = \\$60$. Bao: $3 \\times 30 = \\$90$.',
          ],
        },
        {
          id: 'ex-scale',
          statement:
            'A plan uses scale $1 : 50$. A room is drawn $8.4$ cm long. How long is it in real life (in metres)?',
          steps: [
            'Real length: $8.4 \\times 50 = 420$ cm.',
            'In metres: $420 / 100 = 4.20$ m.',
          ],
        },
        {
          id: 'ex-best-buy',
          statement:
            'Brand A: $1.2$ kg for $\\$5$. Brand B: $2$ kg for $\\$8$. Which is cheaper per kg?',
          steps: [
            'A: $5/1.2 \\approx \\$4.17$/kg.',
            'B: $8/2 = \\$4$/kg.',
            'Brand B is cheaper per kg.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-best-buy',
          difficulty: 'core',
          instance: {
            prompt:
              'Brand X: $500$ g for $\\$3$. Brand Y: $1.2$ kg for $\\$7$. What is the price per kg of the cheaper brand (rounded to nearest cent)?',
            answer: '5.83',
            answerType: 'numeric',
            hint: 'X: $3/0.5 = 6$ per kg. Y: $7/1.2 \\approx 5.83$ per kg.',
            solution: [
              'X: $6$/kg. Y: $7/1.2 = 5.833...$ rounds to $5.83$/kg.',
              'Brand Y is the cheaper per kg.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-split',
          difficulty: 'intro',
          instance: {
            prompt:
              'Split $\\$90$ in the ratio $2 : 1$. How much does the larger share get?',
            answer: '60',
            answerType: 'numeric',
            hint: 'Total parts $= 3$.',
            solution: [
              '$2/(2+1) = 2/3$ of $90 = \\$60$.',
            ],
          },
        },
      ],
    },
  ],
}
