import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Algebra · l7-a-4 (VC2M7A04).
// Investigate, interpret and describe relationships between variables
// represented in graphs of functions developed from authentic data.

export const l7AGraphsAuthenticData: Topic = {
  id: 'l7-a-graphs-authentic-data',
  unit: 7,
  order: 14,
  title: 'Graphs of relationships in authentic data',
  blurb:
    'Investigate, interpret and describe the relationship between variables shown in graphs of authentic data.',
  dotPoints: ['l7-a-4'],
  lessons: [
    {
      id: 'interpreting-graphs',
      heading: 'Reading and interpreting graphs of real data',
      summary:
        'Identify the variables, read values from the graph, and describe how one variable changes as the other changes.',
      body: `When real data is collected, the **graph** is where patterns jump out. A line graph plots one variable on the horizontal axis and another on the vertical axis.

### Which is which?
- The **independent variable** is the one we change or measure first. It goes on the **horizontal axis** (x-axis).
- The **dependent variable** is the one that responds. It goes on the **vertical axis** (y-axis).

> [!definition] Authentic data
> **Authentic data** comes from a real-world source — temperature readings, ticket sales, water usage, journey times — not from a textbook rule.

### Reading the graph
- To find a $y$-value for a given $x$: go up from $x$ on the horizontal axis to the line, then across to the vertical axis.
- To find an $x$-value for a given $y$: go across from $y$ to the line, then down to the horizontal axis.

### Describing the relationship
Look for these features:

- **Trend**: is the line going up, going down, or staying flat?
- **Shape**: is it a straight line, a curve, a step?
- **Key points**: where does the line start, where does it cross an axis, where is the highest or lowest point?
- **Rate**: how fast does $y$ change when $x$ changes by one unit?

> [!warning] Watch out
> "As $x$ goes up, $y$ goes up" is a **correlation**, not a cause. Two things can move together without one causing the other.`,
      examples: [
        {
          id: 'ex-read-value',
          statement:
            'A water tank graph shows level (L) vs time (min). At $t = 4$ min, the line is at $40$ L. At $t = 10$ min, it is at $100$ L. How much did the level rise in those $6$ minutes?',
          steps: [
            'Read the two levels: $40$ L and $100$ L.',
            'Subtract: $100 - 40 = 60$ L.',
            'The level rose by $60$ L over $6$ minutes.',
          ],
        },
        {
          id: 'ex-describe-trend',
          statement:
            'A line graph of ice-cream sales (y) against maximum daily temperature (x) shows points in a clear upward line. Describe the relationship.',
          steps: [
            'As the temperature increases, ice-cream sales also increase.',
            'The relationship is **positive** (both move the same way).',
            'The shape is roughly a straight line — sales grow at a steady rate per degree.',
          ],
        },
        {
          id: 'ex-axis-variables',
          statement:
            'A bus company plots journey time (y-axis) against distance travelled (x-axis). Identify the independent and dependent variables.',
          steps: [
            'The driver chooses the distance, so **distance** is the independent variable — it goes on the x-axis.',
            'Journey time depends on the distance, so **time** is the dependent variable — y-axis.',
            'The graph lets the company read the expected time for any new route length.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-read-rise',
          difficulty: 'intro',
          instance: {
            prompt:
              'A graph of plant height (cm) vs weeks shows the plant is $5$ cm tall at week $2$ and $11$ cm tall at week $5$. How much did it grow between week $2$ and week $5$?',
            answer: '6',
            answerType: 'numeric',
            hint: 'Subtract the earlier height from the later height.',
            solution: [
              '$11 - 5 = 6$ cm. The plant grew $6$ cm in those $3$ weeks.',
            ],
          },
        },
      ],
    },
  ],
}
