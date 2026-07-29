import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Statistics · l10a-ast-3 (VC2M10AST03).
// Bivariate data and lines of best fit.

export const l10aAstBivariateLines: Topic = {
  id: 'l10a-ast-bivariate-lines',
  unit: '10A',
  order: 24,
  title: 'Bivariate data and lines of best fit',
  blurb:
    'Use digital tools to investigate bivariate numerical data sets; where appropriate, use a straight line to describe the relationship allowing for variation, make predictions, and discuss limitations.',
  dotPoints: ['l10a-ast-3'],

  lessons: [
    {
      id: 'linear-fit-equation',
      heading: 'Finding the least-squares line',
      summary: 'Computer/software gives the slope and intercept; you interpret them.',
      body: `For bivariate data $(x_i, y_i)$, the **line of best fit** (or *least-squares regression line*) minimises the sum of squared vertical distances from the points to the line:

$$y = a + bx$$

### The formulas
$$b = \\dfrac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2}, \\quad a = \\bar{y} - b\\bar{x}$$

### By hand vs by software
Computing these by hand is tedious. In practice:
- Use a **spreadsheet** (Excel, Google Sheets): =SLOPE(y-range, x-range) and =INTERCEPT(y-range, x-range).
- Use a **graphing calculator**'s linear-regression function.
- Use **desmos** or **GeoGebra**.

### Interpreting the slope
"Each additional unit of $x$ is associated with an additional $b$ units of $y$ (on average)."

### Interpreting the intercept
"When $x = 0$, the model predicts $y = a$." Only meaningful if $x = 0$ is in or near the data range.`,
      examples: [
        {
          id: 'ex-simple-table',
          statement:
            'Data: $(1, 2), (2, 3), (3, 5), (4, 4)$. Compute the slope $b$ (round to 2 dp).',
          steps: [
            '$\\bar{x} = 2.5$, $\\bar{y} = 3.5$.',
            '$\\sum (x_i - \\bar{x})(y_i - \\bar{y}) = (-1.5)(-1.5) + (-0.5)(-0.5) + (0.5)(1.5) + (1.5)(0.5) = 2.25 + 0.25 + 0.75 + 0.75 = 4$.',
            '$\\sum (x_i - \\bar{x})^2 = 2.25 + 0.25 + 0.25 + 2.25 = 5$.',
            '$b = 4/5 = 0.8$.',
          ],
        },
        {
          id: 'ex-interpret',
          statement:
            'A least-squares line for ice-cream sales ($y$ in $\\$$k) vs temperature ($x$ in $°$C) is $y = 0.5 + 0.15 x$. Interpret the slope.',
          steps: [
            'Each $1°$C increase in temperature is associated with a $\\$0.15$k (\\$150) increase in ice-cream sales.',
          ],
        },
        {
          id: 'ex-software',
          statement:
            'In a spreadsheet, what function gives the slope of the least-squares line for $y$-range `B2:B11` and $x$-range `A2:A11`?',
          steps: [
            '`=SLOPE(B2:B11, A2:A11)`.',
            'The $y$-range comes first in the function arguments.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-slope-table',
          difficulty: 'intro',
          instance: {
            prompt:
              'Data: $(1, 1), (2, 3), (3, 5), (4, 7)$. Find the slope $b$ of the least-squares line.',
            answer: '2',
            answerType: 'numeric',
            hint: '$\\bar{x} = 2.5$, $\\bar{y} = 4$. Compute the formula.',
            solution: [
              '$\\sum (x - \\bar{x})(y - \\bar{y}) = (-1.5)(-3) + (-0.5)(-1) + (0.5)(1) + (1.5)(3) = 4.5 + 0.5 + 0.5 + 4.5 = 10$.',
              '$\\sum (x - \\bar{x})^2 = 2.25 + 0.25 + 0.25 + 2.25 = 5$.',
              '$b = 10 / 5 = 2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-predict',
          difficulty: 'core',
          instance: {
            prompt:
              'A least-squares line is $y = 2 + 3x$. Predict $y$ at $x = 5$.',
            answer: '17',
            answerType: 'numeric',
            hint: 'Substitute $x = 5$.',
            solution: [
              '$y = 2 + 3 \\times 5 = 2 + 15 = 17$.',
            ],
          },
        },
      ],
    },

    {
      id: 'predictions-caveats',
      heading: 'Predictions & limitations',
      summary: 'Use the line within the data range; be wary of extrapolation and non-linearity.',
      body: `The line of best fit is a **model** — a useful simplification, not a physical law. Two common caveats:

### Interpolation vs extrapolation
- **Interpolation** (predicting between data points): usually reliable.
- **Extrapolation** (predicting outside the data range): the linear relationship may not hold.

### When a line isn't appropriate
A line only makes sense if the underlying relationship is roughly linear. A scatterplot that curves (e.g. quadratic, exponential) shouldn't be forced into a straight line. In those cases, fit the appropriate curve, or split the data into linear segments.

### Communicating uncertainty
A prediction $\\hat{y}$ is an *estimate*. The points scatter around the line, so the true $y$ for a given $x$ is probably close to but not exactly $\\hat{y}$.

### Residuals
A **residual** is the vertical distance from a data point to the line: $e_i = y_i - \\hat{y}_i$.
- Positive residual = point above the line.
- Negative residual = point below.
- Plotting residuals vs $x$ shows whether the fit is good (random scatter) or bad (a pattern).`,
      examples: [
        {
          id: 'ex-interp-good',
          statement:
            'A line of best fit was fit on data with $x$ ranging from $2$ to $10$. Predict $y$ at $x = 6$. Is this interpolation or extrapolation?',
          steps: [
            '$x = 6$ is in $[2, 10]$ — this is interpolation.',
            'Prediction should be reasonably reliable.',
          ],
        },
        {
          id: 'ex-extrap',
          statement:
            'Same line, predict $y$ at $x = 100$. Is this reliable?',
          steps: [
            '$x = 100$ is way outside $[2, 10]$ — extrapolation.',
            'The linear trend almost certainly does not hold that far out.',
          ],
        },
        {
          id: 'ex-residual',
          statement:
            'A data point has $y_i = 8$ and the model predicts $\\hat{y}_i = 5$. What is the residual?',
          steps: [
            'Residual $= y_i - \\hat{y}_i = 8 - 5 = 3$.',
            'Positive — point sits above the line.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-interp-or-extrap',
          difficulty: 'intro',
          instance: {
            prompt:
              'A line of best fit was fit on data with $x \\in [0, 5]$. Predicting $y$ at $x = 3$ is "interpolation" or "extrapolation"?',
            answer: 'interpolation',
            answerType: 'exact',
            hint: 'Is $x = 3$ inside the data range?',
            solution: [
              'Yes, $3 \\in [0, 5]$, so this is **interpolation**.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-residual',
          difficulty: 'core',
          instance: {
            prompt:
              'A point has $y = 12$ and the line predicts $\\hat{y} = 9$. What is the residual?',
            answer: '3',
            answerType: 'numeric',
            hint: 'Residual $= y - \\hat{y}$.',
            solution: [
              'Residual $= 12 - 9 = 3$.',
            ],
          },
        },
      ],
    },
  ],
}