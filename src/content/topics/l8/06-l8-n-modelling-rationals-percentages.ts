import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Number · l8-n-6 (VC2M8N06).
// Use mathematical modelling to solve practical problems involving rational
// numbers and percentages, including financial contexts involving profit and loss.

export const l8NModellingRationalsPercentages: Topic = {
  id: 'l8-n-modelling-rationals-percentages',
  unit: 8,
  order: 6,
  title: 'Modelling with rationals and percentages',
  blurb:
    'Use mathematical modelling to solve practical problems involving rational numbers and percentages, including financial contexts involving profit and loss.',
  dotPoints: ['l8-n-6'],
  lessons: [
    {
      id: 'profit-loss',
      heading: 'Profit and loss as percentages',
      summary:
        'Profit and loss are always measured against the cost price; turn the difference into a percentage of the cost.',
      body: `**Profit** is the amount you earn above what you paid. **Loss** is the amount you fall short. The size of the profit or loss only makes sense when compared to the **cost price**.

### The two basic formulas
$$\\text{Profit \%} = \\dfrac{\\text{selling price} - \\text{cost price}}{\\text{cost price}} \\times 100\%.$$
$$\\text{Loss \%} = \\dfrac{\\text{cost price} - \\text{selling price}}{\\text{cost price}} \\times 100\%.$$

If the result is positive, it's a profit; if negative (or you use the loss formula), it's a loss.

### Modelling steps
1. Read the problem and pick out the **cost price** and **selling price**.
2. Subtract to find the absolute profit (or loss).
3. Divide by the cost price and multiply by $100$ to express it as a percentage.

> [!warning] Watch out
> Always divide by the **cost price**, not the selling price. The cost price is the "investment" you're measuring the return on.

### Why we use percentages
A $50 profit on a $50 item is a $100$% return. A $50$ profit on a $5000$ item is only a $1$% return. The percentage makes the two comparable.`,
      examples: [
        {
          id: 'ex-profit',
          statement:
            'A shop buys a hat for \$24 and sells it for \$30. What is the profit as a percentage of the cost price?',
          steps: [
            'Profit $= 30 - 24 = 6$.',
            'Divide by cost: $\\dfrac{6}{24} = 0.25$.',
            'Convert: $0.25 \\times 100 = 25$% profit.',
          ],
        },
        {
          id: 'ex-loss',
          statement:
            'A bike is bought for \$400 and sold for \$340. What is the loss as a percentage of the cost price?',
          steps: [
            'Loss $= 400 - 340 = 60$.',
            'Divide by cost: $\\dfrac{60}{400} = 0.15$.',
            'Convert: $0.15 \\times 100 = 15$% loss.',
          ],
        },
        {
          id: 'ex-selling-from-pct',
          statement:
            'A trader wants a $20$% profit on an item that cost \$50. What price should they sell it for?',
          steps: [
            'Profit needed: $20$% of $50 = 10$.',
            'Selling price: $50 + 10 = 60$.',
            'Or use the multiplier: $50 \\times 1.20 = 60$.',
            'Result: \$60.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-profit',
          difficulty: 'intro',
          instance: {
            prompt:
              'A shop buys a book for \$12 and sells it for \$15. What is the profit as a percentage of the cost price? (Give to the nearest whole percent.)',
            answer: '25',
            answerType: 'numeric',
            hint: 'Profit $= 15 - 12 = 3$. Divide by the cost and convert to a percentage.',
            solution: [
              '$\\dfrac{3}{12} \\times 100 = 25$%.',
            ],
          },
        },
      ],
    },
    {
      id: 'financial-contexts',
      heading: 'Modelling with rationals in financial contexts',
      summary:
        'Set up a calculation from the words; use a single multiplier for percentage changes and a single fraction for rates.',
      body: `A **mathematical model** turns a real situation into numbers and operations. The work is in setting it up correctly: identify the **given** values, decide **what to find**, and pick the right operation.

### Common financial patterns
- **Discount then tax**: apply the discount first to find the sale price, then apply the tax on the reduced amount.
- **Wage**: $\\text{earnings} = \\text{hourly rate} \\times \\text{hours worked}$.
- **Fuel cost**: $\\text{cost} = \\text{price per litre} \\times \\text{litres used}$.
- **Best buy**: divide price by quantity to get a unit rate, then compare.

### Why the order matters
$\$100$ with a $10$% discount is $\$90$. Add $10$% tax on top, and you pay $\$99$, not back to $\$100$. Discounts and taxes use the **new** amount as the base.

> [!definition] Unit rate
> A **unit rate** is the cost or amount per **one** unit (one hour, one litre, one kilogram). Comparing unit rates is the fastest way to find the best buy.`,
      examples: [
        {
          id: 'ex-discount-tax',
          statement:
            'A \$200 item is discounted by $25$%, then a $10$% GST is added. What is the final price?',
          steps: [
            'Discount: $200 \\times 0.75 = 150$.',
            'Add $10$% tax: $150 \\times 1.10 = 165$.',
            'Result: \$165.',
          ],
        },
        {
          id: 'ex-wage',
          statement:
            'Mia earns \\$18.50 per hour and works $12$ hours. How much does she earn?',
          steps: [
            '$\\text{earnings} = 18.50 \\times 12$.',
            'Compute: $18 \\times 12 = 216$, $0.5 \\times 12 = 6$, so $216 + 6 = 222$.',
            'Result: \$222.',
          ],
        },
        {
          id: 'ex-best-buy',
          statement:
            'Brand A: $500$ g for \\$4.50. Brand B: $750$ g for \\$6.00. Which is the better buy per gram?',
          steps: [
            'Unit rate A: $4.50 \\div 500 = 0.009$ dollars per gram.',
            'Unit rate B: $6.00 \\div 750 = 0.008$ dollars per gram.',
            'Brand B is cheaper per gram.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-discount-then-tax',
          difficulty: 'intro',
          instance: {
            prompt:
              'A \$100 item is first discounted by $20$%, then a $10$% GST is added. What is the final price in dollars?',
            answer: '88',
            answerType: 'numeric',
            hint: 'Apply the discount first to get \$80, then multiply by $1.10$.',
            solution: [
              '$100 \\times 0.80 = 80$, then $80 \\times 1.10 = 88$.',
            ],
          },
        },
      ],
    },
  ],
}
