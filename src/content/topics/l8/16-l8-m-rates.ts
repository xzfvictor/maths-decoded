import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Measurement · l8-m-5 (VC2M8M05).
// Recognise and use rates to solve problems involving the comparison of 2
// related quantities of different units of measure.

export const l8MRates: Topic = {
  id: 'l8-m-rates',
  unit: 8,
  order: 16,
  title: 'Rates',
  blurb:
    'Recognise and use rates to solve problems involving the comparison of 2 related quantities of different units of measure.',
  dotPoints: ['l8-m-5'],

  lessons: [
    {
      id: 'rates-and-units',
      heading: 'Rates and unit rates',
      summary: 'A rate compares two quantities of different units; the unit rate is what one of them equals per single unit of the other.',
      body: `A **rate** compares two quantities that have **different units** — like dollars per kilogram, kilometres per hour, or words per minute. Unlike a ratio, a rate must keep its units attached.

### Writing rates
Write a rate as a fraction with the units in place:
$$\\text{rate} = \\dfrac{\\text{quantity A}}{\\text{quantity B}}.$$
Examples: $\$3.50/\\text{kg}$, $60\\text{ km/h}$, $5\\text{ L}/\\text{m}^2$.

### Unit rates
A **unit rate** answers the question: "How much of A per **one** of B?" Find it by dividing both sides by the second quantity.
- $360$ km in $4$ hours $\\Rightarrow 90$ km per hour.
- $\$15$ for $5$ kg $\\Rightarrow \$3$ per kg.

### Solving rate problems
Three equivalent forms:
$$A = r \\times B, \\quad B = A / r, \\quad r = A / B.$$
Choose the one that puts the unknown on its own.`,
      examples: [
        {
          id: 'ex-unit-rate',
          statement:
            'A car travels $240$ km in $3$ hours. What is its speed in km/h?',
          steps: [
            'Speed $= \\dfrac{\\text{distance}}{\\text{time}} = \\dfrac{240}{3} = 80$ km/h.',
          ],
        },
        {
          id: 'ex-best-buy',
          statement:
            'A $2$ L bottle of juice costs $\$5.40$. A $1.5$ L bottle of the same juice costs $\$4.20$. Which is the better buy?',
          steps: [
            'Bottle A: $\$5.40 / 2\\text{ L} = \$2.70$/L.',
            'Bottle B: $\$4.20 / 1.5\\text{ L} = \$2.80$/L.',
            'Bottle A is cheaper per litre, so it is the better buy.',
          ],
        },
        {
          id: 'ex-distance',
          statement:
            'A cyclist rides at $18$ km/h for $2.5$ hours. How far do they travel?',
          steps: [
            'Distance $= \\text{speed} \\times \\text{time}$.',
            '$\\text{Distance} = 18 \\times 2.5 = 45$ km.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-unit-rate',
          difficulty: 'intro',
          instance: {
            prompt:
              'A machine produces $480$ items in $6$ hours. How many items per hour (the unit rate)?',
            answer: '80',
            answerType: 'numeric',
            hint: 'Divide by $6$.',
            solution: [
              'Unit rate $= 480 / 6 = 80$ items per hour.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-best-buy',
          difficulty: 'core',
          instance: {
            prompt:
              'Box A holds $500$ g for $\$3.50$. Box B holds $750$ g for $\$4.50$. What is the price per kilogram of Box B? (Answer in dollars, rounded to two decimal places.)',
            answer: '6',
            answerType: 'numeric',
            hint: 'Divide the price by the mass, then scale to kg.',
            solution: [
              'Box B: $\$4.50 / 750\\text{ g} = \$0.006$ per g $= \$6.00$/kg.',
            ],
          },
        },
      ],
    },
  ],
}