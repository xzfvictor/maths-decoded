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
      id: 'scatter-fit',
      heading: 'Drawing scatterplots & lines of best fit',
      summary: 'Pair the variables; plot points; eyeball a line; describe by strength, direction and shape.',
      body: `A **scatterplot** shows two numerical variables — one on each axis — with each observation plotted as a single point.

### Drawing one
1. Decide which variable is the **explanatory** (independent) — put it on the $x$-axis.
2. The other is the **response** (dependent) — put it on the $y$-axis.
3. Plot each pair $(x_i, y_i)$ as a dot.

### Line of best fit
- A **line of best fit** (or "line of good fit") passes as close as possible to all the points, with roughly equal numbers above and below.
- Use the line to **interpolate** (estimate between data points) — fairly reliable.
- Be careful with **extrapolation** (estimate outside the data range) — the model may not hold.`,
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
        {
          kind: 'curated',
          id: 'c-positive',
          difficulty: 'intro',
          instance: {
            prompt:
              "A scatterplot of study hours vs exam score shows points going up-right. What kind of association is this? Answer \"positive\" or \"negative\".",
            answer: 'positive',
            answerType: 'exact',
            hint: 'Higher $x$ → higher $y$ means positive correlation.',
            solution: [
              'More study → higher score → positive association.',
            ],
          },
        },
      ],
    },

    {
      id: 'interpolation-causation',
      heading: 'Interpolation, extrapolation & causation',
      summary: 'Interpolation is reliable; extrapolation is risky. Correlation is not causation.',
      body: `Once you have a line of best fit, you can use it to **predict** values of $y$ from values of $x$.

### Interpolation
Predicting **between** data points. The model is well-tested there — usually reliable.

### Extrapolation
Predicting **outside** the data range. Risky — the relationship may not hold far from where it was measured.

### Correlation ≠ causation
A strong correlation between $A$ and $B$ doesn't prove $A$ causes $B$ — there may be a lurking variable $C$ that drives both.

### Ice-cream / drownings example
Ice-cream sales and drownings both rise in summer — but ice-cream doesn't cause drownings. Heat is the lurking variable.`,
      examples: [
        {
          id: 'ex-causation',
          statement:
            'A study finds a strong positive correlation between a country\'s chocolate consumption and its number of Nobel laureates. Does eating chocolate cause Nobel prizes?',
          steps: [
            'No — likely a lurking variable like national wealth drives both.',
            'Correlation is real; causation is not established.',
          ],
        },
        {
          id: 'ex-extrap',
          statement:
            "A line of best fit has equation $y = 2x + 1$, fit on data with $x$ in $[0, 5]$. Predict $y$ at $x = 100$.",
          steps: [
            'Plug in: $y = 2(100) + 1 = 201$.',
            "But $x = 100$ is far outside $[0, 5]$ — extrapolation. The linear relationship may not hold, so the prediction is unreliable.",
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
          id: 'c-lurking',
          difficulty: 'core',
          instance: {
            prompt:
              'A study finds ice-cream sales and sunburn rates are strongly positively correlated. Does ice-cream cause sunburn? Answer "yes" or "no".',
            answer: 'no',
            answerType: 'exact',
            hint: 'A lurking variable (sunny weather) likely drives both.',
            solution: [
              'Sunny/hot weather drives both — ice-cream sales and sunburn go up together, but one does not cause the other.',
            ],
          },
        },
      ],
    },
  ],
}