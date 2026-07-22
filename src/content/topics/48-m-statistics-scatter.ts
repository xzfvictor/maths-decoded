import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Statistics · VC2M10ST02.
// Construct scatterplots and consider a line of good fit; comment on
// the association between the 2 numerical variables in terms of strength,
// direction and linearity informally using a line of good fit by eye and
// using digital tools to compare and discuss the reliability of any
// predictions.

export const statisticsScatter: Topic = {
  id: 'm10-statistics-scatter',
  unit: 10,
  order: 26,
  title: 'Scatterplots & line of best fit',
  blurb:
    'Plot bivariate data, judge whether a linear fit is appropriate, and read off predictions (with caution outside the data range).',
  dotPoints: ['m10-st-2'],

  lessons: [
    {
      id: 'scatter-and-fit',
      heading: 'Scatterplots and lines of best fit',
      summary: 'Pair the variables; plot points; eyeball a line; describe the association by strength, direction and shape.',
      body: `A **scatterplot** shows two numerical variables — one on each axis — with each observation plotted as a single point.

### Drawing one
1. Decide which variable is the **explanatory** (independent) — put it on the $x$-axis.
2. The other is the **response** (dependent) — put it on the $y$-axis.
3. Plot each pair $(x_i, y_i)$ as a dot.

### Line of best fit
- A **line of best fit** (or "line of good fit") passes as close as possible to all the points, with roughly equal numbers above and below.
- Use the line to **interpolate** (estimate between data points) — fairly reliable.
- Be careful with **extrapolation** (estimate outside the data range) — the model may not hold.

### Describing the association
- **Direction**: positive (upward) or negative (downward).
- **Strength**: how tightly the points hug the line.
- **Shape**: linear, curved, clustered, no pattern.

### Correlation ≠ causation
A strong correlation between $A$ and $B$ doesn't prove $A$ causes $B$ — there may be a lurking variable $C$ that drives both.`,
      examples: [
        {
          id: 'ex-direction',
          statement:
            'A scatterplot of ice-cream sales vs. temperature shows points going up-right. Describe the direction of the association.',
          steps: [
            'Higher $x$ is associated with higher $y$ → **positive** association.',
          ],
        },
        {
          id: 'ex-interpolation',
          statement:
            "A line of best fit predicts $y = 5$ when $x = 0$ and $y = 15$ when $x = 4$. Predict $y$ at $x = 2$.",
          steps: [
            'Linear in $x$: slope $= (15 - 5) / (4 - 0) = 2.5$.',
            'Equation: $y = 5 + 2.5x$.',
            "At $x = 2$: $y = 5 + 5 = 10$.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-extrapolation',
          difficulty: 'intro',
          instance: {
            prompt:
              "A line of best fit has equation $y = 2x + 1$. The data used to fit it had $x$ values from $0$ to $5$. Predict $y$ at $x = 100$. Answer as an integer.",
            answer: '201',
            answerType: 'numeric',
            hint: 'Substitute $x = 100$ into $y = 2x + 1$.',
            solution: [
              '$y = 2(100) + 1 = 201$.',
              "But extrapolation this far outside the data range is risky — the linear relationship may not hold.",
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-direction',
          difficulty: 'core',
          instance: {
            prompt:
              "A scatterplot of car age vs resale price has points going down-right. What kind of association is this? Answer \"positive\" or \"negative\".",
            answer: 'negative',
            answerType: 'exact',
            hint: 'Higher $x$ → lower $y$ means negative correlation.',
            solution: [
              'Older cars are worth less → negative association.',
            ],
          },
        },
      ],
    },
  ],
}