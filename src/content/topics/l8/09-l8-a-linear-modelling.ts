import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Algebra · l8-a-3 (VC2M8A03).
// Use mathematical modelling to solve applied problems involving linear
// relations, including financial contexts involving profit and loss.

export const l8ALinearModelling: Topic = {
  id: 'l8-a-linear-modelling',
  unit: 8,
  order: 9,
  title: 'Linear modelling in financial contexts',
  blurb:
    'Use mathematical modelling to solve applied problems involving linear relations, including financial contexts involving profit and loss.',
  dotPoints: ['l8-a-3'],
  lessons: [
    {
      id: 'building-the-model',
      heading: 'Building a linear model from words',
      summary:
        'Define a variable, translate the situation into an equation in the form y = mx + c, and use the model to predict.',
      body: `A **linear model** is an equation of the form $y = mx + c$ that approximates a real situation. The model is built by **translating words into algebra**.

### The modelling steps
1. **Define** the variable. "Let $n$ be the number of items, $C$ be the total cost, ..."
2. **Identify** the constant term (the part that doesn't depend on the variable) and the variable rate.
3. **Write** the equation: $C = (\\text{rate}) \\times n + (\\text{fixed part})$.
4. **Use** the model: substitute a value to predict, or solve the equation to find an unknown.
5. **Check** that the answer makes sense in the original context.

### Common shape
Most flat-fee-plus-rate problems look like:
$$\\text{Total} = \\text{fixed cost} + (\\text{rate} \\times \\text{quantity}).$$

### Why a digital tool helps
A spreadsheet or graphing app lets you **try different values** of the variable and see the result instantly — useful for "what if?" questions.

> [!definition] Profit and loss
> A business makes a **profit** when revenue is greater than cost, and a **loss** when cost is greater than revenue. The break-even point is where revenue equals cost.`,
      examples: [
        {
          id: 'ex-mobile-plan',
          statement:
            'A mobile plan charges \$25 per month plus \$0.10 per text message. Build a linear model for the monthly bill.',
          steps: [
            'Let $n$ be the number of texts and $B$ be the bill.',
            'Fixed cost: \$25. Variable cost: \$0.10 per text.',
            'Model: $B = 25 + 0.10n$.',
            'If $n = 80$, the bill is $25 + 0.10(80) = 25 + 8 = 33$ dollars.',
          ],
        },
        {
          id: 'ex-taxi',
          statement:
            'A taxi charges a \$3 flag-fall plus \$2.20 per km. Write a model for the fare $F$ for a trip of $k$ km.',
          steps: [
            'Fixed cost: \$3. Variable cost: \$2.20 per km.',
            'Model: $F = 3 + 2.20k$.',
            'For $k = 10$, $F = 3 + 22 = 25$ dollars.',
          ],
        },
        {
          id: 'ex-break-even',
          statement:
            'A bakery sells each cake for \$15. The cost to make $n$ cakes in a day is $C = 8n + 40$. How many cakes must be sold to break even?',
          steps: [
            'Revenue: $R = 15n$.',
            'Break-even when $R = C$: $15n = 8n + 40$.',
            'Solve: $7n = 40$, so $n = \\dfrac{40}{7} \\approx 5.71$.',
            'They need to sell $6$ cakes to cover costs.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-mobile-plan',
          difficulty: 'intro',
          instance: {
            prompt:
              'A plan costs \$20 per month plus \$0.15 per text message. Using $B = 20 + 0.15n$, find the bill for $n = 60$ messages. State the bill in dollars.',
            answer: '29',
            answerType: 'numeric',
            hint: 'Substitute $n = 60$ into $B = 20 + 0.15n$.',
            solution: [
              '$B = 20 + 0.15 \\times 60 = 20 + 9 = 29$.',
            ],
          },
        },
      ],
    },
    {
      id: 'profit-loss-models',
      heading: 'Profit and loss with linear models',
      summary:
        'Set up separate linear models for revenue and cost; find the break-even point where they meet.',
      body: `Two linear models usually describe a business:
- **Revenue** $R$: how much money comes in. Often $R = p \\times n$, where $p$ is the price per item and $n$ is the number sold.
- **Cost** $C$: how much money goes out. Often $C = v \\times n + f$, where $v$ is the variable cost per item and $f$ is the fixed cost.

### Profit
$$\\text{Profit} = R - C.$$

If $R > C$, the business is in the black (profit). If $R < C$, it is in the red (loss).

### Break-even
The break-even point is where $R = C$. Set the two equations equal and solve for $n$:
$$pn = vn + f \\Rightarrow (p - v)n = f \\Rightarrow n = \\dfrac{f}{p - v}.$$

Below break-even: loss. Above break-even: profit.

> [!warning] Watch out
> The break-even $n$ is the smallest **whole** number of items that covers the cost. If the algebra gives $5.71$, the break-even is $6$ items, not $5$.

### Graphical view
Plot $R$ and $C$ against $n$ on the same axes. The two lines cross at break-even. For $n$ values to the **left** of the cross, $C > R$ (loss); to the **right**, $R > C$ (profit).`,
      examples: [
        {
          id: 'ex-profit',
          statement:
            'A store buys mugs for \$6 and sells them for \$10. Fixed costs are \$80 per day. Build the profit model and find the break-even point.',
          steps: [
            'Revenue: $R = 10n$.',
            'Cost: $C = 6n + 80$.',
            'Profit: $P = R - C = 4n - 80$.',
            'Break-even: $P = 0 \\Rightarrow 4n = 80 \\Rightarrow n = 20$ mugs.',
          ],
        },
        {
          id: 'ex-prediction',
          statement:
            'Using the model from the previous example, what is the profit on $n = 50$ mugs?',
          steps: [
            'Profit: $P = 4(50) - 80 = 200 - 80 = 120$.',
            'Result: \$120 profit.',
          ],
        },
        {
          id: 'ex-loss',
          statement:
            'A market stall sells lemonade. Each cup brings in \$3 and costs \$1 to make. The stall pays \$50 rent per session. How many cups cover the rent?',
          steps: [
            'Revenue: $R = 3n$. Cost: $C = 1 \\cdot n + 50 = n + 50$.',
            'Break-even: $3n = n + 50 \\Rightarrow 2n = 50 \\Rightarrow n = 25$.',
            'Selling $25$ cups exactly covers the rent; the 26th cup is pure profit.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-break-even',
          difficulty: 'intro',
          instance: {
            prompt:
              'A baker sells cookies for \$2 each. Each cookie costs \$0.50 to make, and the daily oven rental is \$30. How many cookies must be sold to break even?',
            answer: '20',
            answerType: 'numeric',
            hint: 'Set $2n = 0.5n + 30$ and solve.',
            solution: [
              '$2n = 0.5n + 30 \\Rightarrow 1.5n = 30 \\Rightarrow n = 20$.',
            ],
          },
        },
      ],
    },
  ],
}
