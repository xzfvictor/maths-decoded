import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Measurement · l8-m-7 (VC2M8M07).
// Use mathematical modelling to solve practical problems involving ratios
// and rates, including distance-time problems for travel at a constant
// speed and financial contexts.

export const l8MModellingRatiosRates: Topic = {
  id: 'l8-m-modelling-ratios-rates',
  unit: 8,
  order: 18,
  title: 'Modelling with ratios and rates',
  blurb:
    'Use mathematical modelling to solve practical problems involving ratios and rates, including distance-time problems for travel at a constant speed and financial contexts.',
  dotPoints: ['l8-m-7'],

  lessons: [
    {
      id: 'distance-time',
      heading: 'Distance, time and constant speed',
      summary: 'Triangle of speed: distance = speed × time. Rearrange to solve for any one of the three.',
      body: `When something moves at a **constant speed**, three quantities are linked by one formula:
$$\\text{distance} = \\text{speed} \\times \\text{time}.$$
This is the **distance-rate-time triangle** — cover the unknown quantity and the formula for it is what is left.

### Setting up a model
1. Identify the **known** quantities and the **unknown**.
2. Pick the form that isolates the unknown:
   - Unknown distance: $d = s \\times t$.
   - Unknown speed: $s = d / t$.
   - Unknown time: $t = d / s$.
3. Convert units so they match (km with km/h with hours; m with m/s with seconds).
4. Compute and check the answer is sensible — a car does not travel $1000$ km in $5$ minutes.

### Modelling in action
To model a journey in writing:
- "Let $d$ km be the distance."
- "The car travels at $80$ km/h for $t$ hours, so $d = 80t$."
- Solve for the missing variable.`,
      examples: [
        {
          id: 'ex-find-time',
          statement:
            'A cyclist rides at $15$ km/h for $2.5$ hours. How far do they travel?',
          steps: [
            '$d = s \\times t = 15 \\times 2.5 = 37.5$ km.',
          ],
        },
        {
          id: 'ex-find-speed',
          statement:
            'A train travels $210$ km in $2$ hours $30$ min. What is its average speed?',
          steps: [
            'Convert time: $2$ h $30$ min $= 2.5$ h.',
            '$s = d / t = 210 / 2.5 = 84$ km/h.',
          ],
        },
        {
          id: 'ex-meeting',
          statement:
            'Two cyclists start at the same point and ride in opposite directions, one at $18$ km/h and the other at $12$ km/h. After how long are they $45$ km apart?',
          steps: [
            'They separate at a combined speed of $18 + 12 = 30$ km/h.',
            '$t = d / s = 45 / 30 = 1.5$ hours.',
            'Answer: $1$ hour $30$ minutes.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-distance',
          difficulty: 'intro',
          instance: {
            prompt:
              'A car drives at $60$ km/h for $3$ hours. How far does it travel in km?',
            answer: '180',
            answerType: 'numeric',
            hint: '$d = s \\times t$.',
            solution: [
              '$d = 60 \\times 3 = 180$ km.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-time',
          difficulty: 'core',
          instance: {
            prompt:
              'A truck must travel $260$ km at $65$ km/h. How many hours does the trip take? (Round to one decimal place.)',
            answer: '4',
            answerType: 'numeric',
            hint: '$t = d / s$.',
            solution: [
              '$t = 260 / 65 = 4$ hours exactly.',
            ],
          },
        },
      ],
    },

    {
      id: 'financial-modelling',
      heading: 'Financial contexts with ratios and rates',
      summary: 'Apply unit rates to best-buy, wages and fuel-cost problems.',
      body: `Ratios and rates show up everywhere money is involved — comparing prices, working out wages, and budgeting fuel.

### Best buy
To compare two products, find the **unit rate** (cost per single unit — per kg, per L, per 100 g) and pick the cheaper one.

### Wages
Wages are a rate: $\$/\\text{hour}$. Total pay is:
$$\\text{pay} = \\text{rate per hour} \\times \\text{hours worked}.$$
Overtime is often paid at $1.5$ or $2$ times the normal rate.

### Fuel cost
Fuel cost is a rate too — dollars per litre. Total fuel cost for a trip:
$$\\text{cost} = \\text{fuel price per L} \\times \\text{litres used}.$$

### Modelling a budget
A common financial model is to **scale** by the same ratio:
- "$5$ days of food costs $\$120$. How much does $7$ days cost?"
- Model: cost $\\propto$ days $\\Rightarrow$ cost $= 24 \\times \\text{days}$.
- For $7$ days: $24 \\times 7 = \$168$.`,
      examples: [
        {
          id: 'ex-wages',
          statement:
            'A casual worker earns $\$28$/hour during the week and $\$42$/hour on Saturday. They work $15$ weekday hours and $6$ Saturday hours. What is their total pay?',
          steps: [
            'Weekday: $15 \\times 28 = \$420$.',
            'Saturday: $6 \\times 42 = \$252$.',
            'Total: $420 + 252 = \$672$.',
          ],
        },
        {
          id: 'ex-fuel',
          statement:
            'A car uses $8.5$ L of fuel per $100$ km. Fuel costs $\$1.85$/L. What is the fuel cost for a $350$ km trip?',
          steps: [
            'Litres used: $350 \\times 8.5 / 100 = 29.75$ L.',
            'Cost: $29.75 \\times 1.85 = \$55.04$ (approx).',
          ],
        },
        {
          id: 'ex-budget',
          statement:
            'A family of $4$ spends $\$680$ per week on groceries. If the family grows to $6$ (assuming the same per-person amount), how much will groceries cost per week?',
          steps: [
            'Per-person spend: $\$680 / 4 = \$170$.',
            'For $6$ people: $6 \\times 170 = \$1020$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-unit-cost',
          difficulty: 'intro',
          instance: {
            prompt:
              'A $1.5$ kg bag of rice costs $\$6.30$. What is the cost per kilogram?',
            answer: '4.2',
            answerType: 'numeric',
            hint: 'Divide the cost by the mass.',
            solution: [
              'Unit cost $= 6.30 / 1.5 = \$4.20$/kg.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-fuel',
          difficulty: 'core',
          instance: {
            prompt:
              'A van uses $10$ L of fuel per $100$ km. Petrol costs $\$1.95$/L. How much does a $250$ km trip cost in fuel? (Round to the nearest dollar.)',
            answer: '49',
            answerType: 'numeric',
            hint: 'Find the litres used, then multiply by the price per litre.',
            solution: [
              'Litres: $250 \\times 10 / 100 = 25$ L.',
              'Cost: $25 \\times 1.95 = \$48.75 \\approx \$49$.',
            ],
          },
        },
      ],
    },
  ],
}