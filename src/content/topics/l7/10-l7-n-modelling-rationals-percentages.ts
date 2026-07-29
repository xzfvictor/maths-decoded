import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-10 (VC2M7N10).
// Mathematical modelling with rationals and percentages.

export const l7NModellingRationalsPercentages: Topic = {
  id: 'l7-n-modelling-rationals-percentages',
  unit: 7,
  order: 10,
  title: 'Mathematical modelling with rationals and percentages',
  blurb:
    'Apply rational numbers and percentages in practical and financial contexts, and justify the choice of representation.',
  dotPoints: ['l7-n-10'],
  lessons: [
    {
      id: 'modelling-best-buys',
      heading: 'Best buys and everyday financial contexts',
      summary: 'Compare unit prices, work out percentage profit or loss, and check that the model fits.',
      body: `**Mathematical modelling** turns a real situation into a calculation, then interprets the result back in the original context. A good model is one whose answer is **useful** and whose assumptions are **stated**.

### The modelling cycle
1. **Formulate**: identify the quantities, the relationships, and the question.
2. **Choose a representation**: fraction, decimal, percentage, or ratio — whichever makes the calculation cleanest.
3. **Compute**: do the arithmetic with a sensible strategy.
4. **Interpret**: translate the answer back to the original situation.
5. **Evaluate**: does the answer make sense? If not, change the model.

### Best buys
A **best buy** is the package that costs the **least per unit**. To compare:
- **Same quantity, different prices**: the cheapest is the best buy.
- **Different quantities, different prices**: compute the **unit price** for each and compare.

Unit price is **total price ÷ number of units** (e.g. dollars per kilogram, cents per gram, dollars per litre).

### Profit and loss
- **Profit** = selling price $-$ cost price.
- **Profit percentage** = $\\dfrac{\\text{profit}}{\\text{cost price}} \\times 100\\%$.
- **Loss** is negative profit. A loss percentage uses the same formula; the answer is negative.

> [!warning] Watch out
> The "best buy" is the **cheapest per unit**, not always the cheapest pack. A $1.5\\text{ L}$ bottle for $\\$4$ is cheaper per litre than a $1\\text{ L}$ bottle for $\\$3$ ($\\$2.67/\\text{L}$ vs $\\$3.00/\\text{L}$).`,
      examples: [
        {
          id: 'ex-best-buy',
          statement:
            'A $500\\text{ g}$ block of cheese costs $\\$8$, and a $750\\text{ g}$ block costs $\\$11.50$. Which is the best buy?',
          steps: [
            'Unit price of $500\\text{ g}$: $8 \\div 500 = \\$0.016$ per gram $= \\$16$ per kilogram.',
            'Unit price of $750\\text{ g}$: $11.50 \\div 750 = \\$0.01533...$ per gram $= \\$15.33$ per kilogram.',
            'The $750\\text{ g}$ block is the best buy.',
          ],
        },
        {
          id: 'ex-profit',
          statement:
            'A school buys $80$ sausage sandwiches for $\\$120$ and sells them all for $\\$3$ each. What is the percentage profit?',
          steps: [
            'Revenue: $80 \\times 3 = \\$240$.',
            'Profit: $240 - 120 = \\$120$.',
            'Profit percentage: $\\dfrac{120}{120} \\times 100\\% = 100\\%$.',
            'Result: a $100\\%$ profit (the event doubled the money).',
          ],
        },
        {
          id: 'ex-evaluate',
          statement:
            'A sausage sizzle sells $60$ sausages and the percentage profit is $40\\%$. The class concludes "we made a profit of $40$ sausages worth". What is wrong with that conclusion?',
          steps: [
            'Profit is a **money** concept, not a unit-of-sausage concept.',
            'A $40\\%$ profit means the money earned is $40\\%$ more than the money spent — not that $40$ of the $60$ sausages were profit.',
            'To find the money profit, multiply the cost by $0.40$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-unit-price',
          difficulty: 'intro',
          instance: {
            prompt:
              'A $2\\text{ L}$ bottle of juice costs $\\$5.40$. What is the price per litre?',
            answer: '2.70',
            answerType: 'numeric',
            hint: 'Divide the cost by the litres.',
            solution: [
              '$\\$5.40 \\div 2 = \\$2.70$ per litre.',
            ],
          },
        },
      ],
    },
    {
      id: 'modelling-proportion-context',
      heading: 'Modelling with proportion in context',
      summary: 'Choose fractions, decimals or percentages to suit the context, then report findings clearly.',
      body: `Real-life data does not arrive in a single shape — a survey might give $12$ out of $30$ students, a school report might give a $4.7\\%$ gain in enrolments, and a fundraiser might report a $\\$35$ profit on a $\\$50$ outlay. The model picks the **best representation** for the question.

### Choosing the representation
- **Fraction / decimal**: exact comparisons, raw counts, "$\\frac{2}{3}$ of the class…".
- **Percentage**: comparing parts from different-sized wholes ("$55\\%$ of Year 7 attended the disco" — even if the year level has $400$ or $40$ students).
- **Ratio**: comparing one group with another ("$2$ girls for every $3$ boys").
- **Difference (signed number)**: changes up or down ("the lift went from floor $-2$ to floor $5$").

### Modelling additive contexts
- A **lift** at floor $3$ that goes down $5$ floors ends at floor $-2$. Floors below the ground floor are negative.
- **Altitude** is positive above sea level, negative below (the Dead Sea is about $-430\\text{ m}$).
- **Credits and debits** in a bank account: credits add, debits subtract, the running balance can be negative (overdrawn).

### Modelling proportional contexts
- "$55\\%$ of the $400$ Year 7s attended the disco" — find the number: $0.55 \\times 400 = 220$ students.
- "$23\\%$ of the school voted yes on the uniform change" — interpret: about a quarter of the school, not just a quarter of a year level.

> [!warning] Watch out
> Always **state the whole** when you report a percentage. "$25\\%$ of the school" is meaningless if the school has $1000$ or $200$ students — the percentage must be tied to the base.`,
      examples: [
        {
          id: 'ex-lift',
          statement:
            'A lift starts at ground floor (interpreted as $0$). It goes up $6$ floors, then down $9$ floors. Which floor is it on now?',
          steps: [
            'Start: $0$.',
            'After $6$ up: $+6$.',
            'After $9$ down: $6 + (-9) = -3$.',
            'Result: $3$ floors below the ground floor (often labelled B3 or $-3$).',
          ],
        },
        {
          id: 'ex-percent-context',
          statement:
            '$55\\%$ of the $400$ Year 7 students attended the end-of-term disco. How many students is that?',
          steps: [
            'Convert the percentage: $55\\% = 0.55$.',
            'Multiply by the whole: $0.55 \\times 400$.',
            '$0.55 \\times 400 = 55 \\times 4 = 220$.',
            'Result: $220$ students attended.',
          ],
        },
        {
          id: 'ex-evaluate-model',
          statement:
            'A class uses the model "Year 7 disco attendance = $55\\%$ of the whole school" to estimate the disco crowd. The actual crowd is $220$ Year 7s and $30$ older students. What is wrong with the model?',
          steps: [
            'The model assumes the percentage applies to the **whole school** — but the survey only covered Year 7.',
            'Mixing Year 7 attendance data with the whole-school population is a category mismatch.',
            'A better model would either: (a) restrict the question to Year 7, or (b) gather attendance data from every year level.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-percent-of-context',
          difficulty: 'intro',
          instance: {
            prompt:
              'A school of $800$ students reports that $23\\%$ voted "yes" to a uniform change. How many students is that?',
            answer: '184',
            answerType: 'numeric',
            hint: 'Convert $23\\%$ to a decimal and multiply by $800$.',
            solution: [
              '$0.23 \\times 800 = 23 \\times 8 = 184$ students.',
            ],
          },
        },
      ],
    },
  ],
}
