import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Algebra · l9-a-6 (VC2M9A06).
// Mathematical modelling of change.

export const l9AModellingChange: Topic = {
  id: 'l9-a-modelling-change',
  unit: 9,
  order: 7,
  title: 'Mathematical modelling of change',
  blurb:
    'Use mathematical modelling to solve applied problems involving change — including financial contexts with simple interest — choosing linear, quadratic, or other simple functions.',
  dotPoints: ['l9-a-6'],

  lessons: [
    {
      id: 'linear-modelling',
      heading: 'Linear modelling',
      summary:
        'Use $y = mx + b$ when the change per step is constant — perfect for simple interest and flat rates.',
      body: `When something changes by a **fixed amount** each step, a **linear model** fits:
$$y = mx + b.$$

- $m$ = change per unit step (the rate).
- $b$ = starting value (when $x = 0$).

### Recognise linear situations
- Phone plans with a flat monthly fee plus a per-minute charge.
- A taxi flag-fall plus per-kilometre rate.
- **Simple interest**: principal grows by the same dollar amount each year.
- Distance at constant speed.

### Simple interest
$$A = P(1 + rt)$$
- $A$ = final amount.
- $P$ = principal (initial deposit).
- $r$ = interest rate (per period, as a decimal).
- $t$ = number of periods.

This is linear in $t$ because each year adds the same amount $Pr$.`,
      examples: [
        {
          id: 'ex-simple-interest',
          statement:
            'You deposit $\\$1000$ at $5\\%$ per year simple interest. What is the balance after $4$ years?',
          steps: [
            '$A = 1000(1 + 0.05 \\cdot 4) = 1000(1 + 0.2) = 1000 \\cdot 1.2$.',
            '$A = \\$1200$.',
          ],
        },
        {
          id: 'ex-flat-rate',
          statement:
            'A plumber charges a $\\$60$ call-out fee plus $\\$40$ per hour. Write a formula for the cost $C$ (in dollars) for $h$ hours of work.',
          steps: [
            'Start: $\\$60$ (flat).',
            'Per hour: $\\$40 \\cdot h$.',
            '$C = 40h + 60$.',
          ],
        },
        {
          id: 'ex-distance',
          statement:
            'A cyclist rides at $15$ km/h for $t$ hours. Write the distance $d$ (km) as a linear function of $t$.',
          steps: [
            'Constant rate: $15$ km/h.',
            'Distance: $d = 15 t$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-simple-interest',
          difficulty: 'intro',
          instance: {
            prompt:
              'You deposit $\\$500$ at $4\\%$ per year simple interest. What is the balance after $3$ years (in dollars)?',
            answer: '560',
            answerType: 'numeric',
            hint: '$A = P(1 + rt) = 500(1 + 0.04 \\cdot 3)$.',
            solution: [
              '$A = 500(1 + 0.12) = 500 \\cdot 1.12 = \\$560$.',
            ],
          },
        },
      ],
    },

    {
      id: 'quadratic-and-other-modelling',
      heading: 'Quadratic and other models',
      summary:
        'When the second difference is constant, the model is quadratic; pick the model that fits the shape of the data.',
      body: `Linear models handle constant-rate change. When the **rate of change itself changes**, you need a different shape.

### Quadratic model
$$y = ax^2 + bx + c.$$
A quantity that grows quadratically has **constant second differences**. Examples:
- Area of a square with side $x$: $A = x^2$.
- Free-fall distance: $d = \\tfrac{1}{2} g t^2$ (ignoring air resistance).
- Revenue when price is tuned: $R = (price)(quantity sold)$, and quantity drops linearly with price → quadratic in price.

### Recognise it
For a sequence $a_0, a_1, a_2, \\ldots$:
- Constant first differences → linear.
- Constant second differences → quadratic.

### Choosing between models
Ask: **what is constant?**
- A constant amount added each step → linear.
- A constant multiplier each step → exponential.
- A constant *change in change* → quadratic.
- Real-world data often lies between two simple models — use digital tools to fit a curve and check the match.`,
      examples: [
        {
          id: 'ex-quad-area',
          statement:
            'A square has side length $s$ cm. Write its area $A$ as a quadratic function of $s$.',
          steps: [
            '$A = s^2$.',
            'This is quadratic — doubling $s$ quadruples the area.',
          ],
        },
        {
          id: 'ex-quad-revenue',
          statement:
            'A product sells for $\\$10$ per item. For every $\\$1$ you raise the price, you sell $5$ fewer items. If you start with $100$ items sold at $\\$10$, write revenue as a quadratic in $x$ (the price increase).',
          steps: [
            'New price: $10 + x$. Items sold: $100 - 5x$.',
            'Revenue: $R = (10 + x)(100 - 5x)$.',
            'Expand: $R = 1000 - 50x + 100x - 5x^2 = -5x^2 + 50x + 1000$.',
          ],
        },
        {
          id: 'ex-second-diff',
          statement:
            'A sequence goes $\\{0, 3, 12, 27, 48, \\dots\\}$. Which type of model fits?',
          steps: [
            'First differences: $3, 9, 15, 21$ (linear growth).',
            'Second differences: $6, 6, 6$ — constant.',
            'Constant second differences → **quadratic** model: $y = 3n^2$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pick-model',
          difficulty: 'intro',
          instance: {
            prompt:
              'A sequence goes $\\{2, 5, 8, 11, \\dots\\}$. Linear, quadratic, or exponential? Answer "linear", "quadratic", or "exponential".',
            answer: 'linear',
            answerType: 'exact',
            hint: 'Look at the differences between consecutive terms.',
            solution: [
              'First differences: $3, 3, 3$ — constant first differences → linear.',
            ],
          },
        },
      ],
    },
  ],
}