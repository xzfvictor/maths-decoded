import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Number · l8-n-5 (VC2M8N05).
// Solve problems involving the use of percentages, including percentage
// increases and decreases and percentage error, with and without digital tools.

export const l8NPercentagesError: Topic = {
  id: 'l8-n-percentages-error',
  unit: 8,
  order: 5,
  title: 'Percentages, including percentage error',
  blurb:
    'Solve problems with percentage increases, decreases, and percentage error, with and without digital tools.',
  dotPoints: ['l8-n-5'],
  lessons: [
    {
      id: 'increase-decrease',
      heading: 'Percentage increase and decrease',
      summary:
        'Convert the percentage to a multiplier and apply it to the original value to grow or shrink it.',
      body: `A percentage change rescales the original amount by a fixed ratio. The cleanest way to handle it is to **convert the percentage to a multiplier** first.

### The two key multipliers
- **Increase by $p$%**: new value $=$ original $\\times \\left(1 + \\dfrac{p}{100}\\right)$.
- **Decrease by $p$%**: new value $=$ original $\\times \\left(1 - \\dfrac{p}{100}\\right)$.

So a $20$% increase uses the multiplier $1.20$, and a $15$% decrease uses $0.85$.

### Why the multiplier is $1 + p/100$
You keep $100$% of the original, then **add** $p$% more. So you end up with $100$% + $p$% = $(100 + p)$% of the original.

### Reversing the change
To go back from the new value to the original, **divide** by the multiplier:
- Original $= \\dfrac{\\text{new value}}{1 + p/100}$ for an increase.
- Original $= \\dfrac{\\text{new value}}{1 - p/100}$ for a decrease.

> [!warning] Watch out
> A $50$% increase followed by a $50$% decrease does **not** return to the original. $100 \\to 150 \\to 75$. The decrease multiplier is on the new (larger) amount.`,
      examples: [
        {
          id: 'ex-increase',
          statement: 'A \$80 jacket is increased by $25$%. What is the new price?',
          steps: [
            'Multiplier: $1 + \\dfrac{25}{100} = 1.25$.',
            'New price: $80 \\times 1.25 = 100$.',
            'Result: \$100.',
          ],
        },
        {
          id: 'ex-decrease',
          statement: 'A \$120 pair of shoes is discounted by $15$%. What is the sale price?',
          steps: [
            'Multiplier: $1 - \\dfrac{15}{100} = 0.85$.',
            'Sale price: $120 \\times 0.85 = 102$.',
            'Result: \$102.',
          ],
        },
        {
          id: 'ex-reverse',
          statement:
            'After a $10$% increase, a phone costs \$550. What was the original price?',
          steps: [
            'The multiplier was $1.10$.',
            'Original $= \\dfrac{550}{1.10} = 500$.',
            'Result: \$500.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-increase',
          difficulty: 'intro',
          instance: {
            prompt:
              'A \$50 shirt is increased by $20$%. What is the new price in dollars?',
            answer: '60',
            answerType: 'numeric',
            hint: 'Use the multiplier $1.20$.',
            solution: [
              '$50 \\times 1.20 = 60$.',
            ],
          },
        },
      ],
    },
    {
      id: 'percentage-error',
      heading: 'Percentage error',
      summary:
        'Compare how far an estimate or measurement is from the true value, as a percentage of the true value.',
      body: `Whenever you measure or estimate something, the answer is rarely **exactly** the true value. **Percentage error** is a way of saying "how big is the gap, relative to the truth?".

### The formula
$$\\text{Percentage error} = \\dfrac{|\\text{measured} - \\text{true}|}{\\text{true}} \\times 100\\%.$$

The numerator is the **absolute** error — how far off, ignoring sign. The denominator is the **true** value, not the measured one. The result is a percentage.

### Reading the result
- A small percentage error means the measurement is accurate.
- A large percentage error means the measurement is far from the truth.

> [!warning] Watch out
> The denominator must be the **true** value, not the measured value. Dividing by the measured value gives a different (and less useful) number.

### Why we care
Scientists report percentage error so others can judge how reliable an experiment is. Engineers use it to set tolerances. A $2$% error is excellent for most measurements; a $20$% error would be unacceptable.`,
      examples: [
        {
          id: 'ex-pct-error',
          statement:
            'A student measures a length of paper as $29.4$ cm. The true length is $30.0$ cm. What is the percentage error?',
          steps: [
            'Absolute error: $|29.4 - 30.0| = 0.6$.',
            'Divide by the true value: $\\dfrac{0.6}{30.0} = 0.02$.',
            'Convert to a percentage: $0.02 \\times 100 = 2$%.',
            'Result: $2$% error.',
          ],
        },
        {
          id: 'ex-larger-error',
          statement:
            'A speedometer reads $58$ km/h when the true speed is $50$ km/h. What is the percentage error?',
          steps: [
            'Absolute error: $|58 - 50| = 8$.',
            'Divide by the true value: $\\dfrac{8}{50} = 0.16$.',
            'Convert: $0.16 \\times 100 = 16$%.',
            'Result: $16$% error.',
          ],
        },
        {
          id: 'ex-choose-better',
          statement:
            'Two measurements of a $1$ m rod give $1.01$ m and $0.96$ m. Which has the smaller percentage error?',
          steps: [
            'First: $\\dfrac{|1.01 - 1.00|}{1.00} = 0.01$ → $1$% error.',
            'Second: $\\dfrac{|0.96 - 1.00|}{1.00} = 0.04$ → $4$% error.',
            'The first measurement ($1.01$ m) has the smaller percentage error.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pct-error',
          difficulty: 'intro',
          instance: {
            prompt:
              'A measured value is $9.6$ and the true value is $10.0$. What is the percentage error? (Give as a percentage to $1$ decimal place.)',
            answer: '4',
            answerType: 'numeric',
            hint: 'Use $\\dfrac{|9.6 - 10.0|}{10.0} \\times 100$.',
            solution: [
              '$\\dfrac{0.4}{10.0} \\times 100 = 4$% error.',
            ],
          },
        },
      ],
    },
  ],
}
