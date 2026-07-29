import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Statistics · l10a-ast-1 (VC2M10AST01).
// Mean, standard deviation and data sets.

export const l10aAstMeanStandardDeviation: Topic = {
  id: 'l10a-ast-mean-standard-deviation',
  unit: '10A',
  order: 22,
  title: 'Mean, standard deviation and data sets',
  blurb:
    'Calculate and interpret the mean and standard deviation of data, use them to compare data sets, and investigate the effect of individual data values (including outliers) on the standard deviation.',
  dotPoints: ['l10a-ast-1'],

  lessons: [
    {
      id: 'mean-and-stddev',
      heading: 'Mean & standard deviation',
      summary: 'Mean = average; standard deviation = average deviation from the mean.',
      body: `The **mean** is the "balance point" of the data. The **standard deviation** measures how spread out the data is around the mean.

### Mean
$$\\bar{x} = \\dfrac{x_1 + x_2 + \\dots + x_n}{n}$$

### Standard deviation (population formula)
$$\\sigma = \\sqrt{\\dfrac{1}{n} \\sum_{i=1}^{n} (x_i - \\bar{x})^2}$$

### Step-by-step
1. Compute the mean $\\bar{x}$.
2. Find each deviation $x_i - \\bar{x}$.
3. Square each deviation (so signs don't cancel).
4. Average the squared deviations.
5. Take the square root.

### Interpretation
- A **small standard deviation** = data clusters tightly around the mean.
- A **large standard deviation** = data is spread out.

### Sample vs population
Many textbooks use the **sample** version: $\\sqrt{\\tfrac{1}{n-1} \\sum (x_i - \\bar{x})^2}$. The $n-1$ corrects for the fact that the sample mean already used up one degree of freedom. Both definitions appear in Year 10A work.`,
      examples: [
        {
          id: 'ex-mean-small',
          statement:
            'Find the mean of the data set $\\{2, 5, 5, 8\\}$.',
          steps: [
            'Sum $= 2 + 5 + 5 + 8 = 20$.',
            '$n = 4$.',
            '$\\bar{x} = 20/4 = 5$.',
          ],
        },
        {
          id: 'ex-stddev-small',
          statement:
            'Compute the population standard deviation of $\\{2, 4, 4, 4, 5, 5, 7, 9\\}$.',
          steps: [
            'Mean $= (2+4+4+4+5+5+7+9)/8 = 40/8 = 5$.',
            'Squared deviations: $(2-5)^2, (4-5)^2 \\times 3, (5-5)^2 \\times 2, (7-5)^2, (9-5)^2$.',
            'Sum $= 9 + 3 \\cdot 1 + 2 \\cdot 0 + 4 + 16 = 32$.',
            '$\\sigma = \\sqrt{32/8} = \\sqrt{4} = 2$.',
          ],
        },
        {
          id: 'ex-interp-stddev',
          statement:
            'Class A has test scores with mean $70$ and std dev $5$. Class B has mean $70$ and std dev $15$. Which class is more consistent?',
          steps: [
            'Same centre ($70$).',
            'Smaller std dev means tighter spread.',
            'Class A is more consistent.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-mean-basic',
          difficulty: 'intro',
          instance: {
            prompt:
              'Find the mean of $\\{3, 7, 7, 3, 10\\}$.',
            answer: '6',
            answerType: 'numeric',
            hint: '$\\bar{x} = \\dfrac{\\text{sum}}{n}$.',
            solution: [
              'Sum $= 3 + 7 + 7 + 3 + 10 = 30$.',
              '$\\bar{x} = 30 / 5 = 6$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-stddev-equal',
          difficulty: 'core',
          instance: {
            prompt:
              'Compute the population standard deviation of $\\{1, 3, 5, 7, 9\\}$. (Round to 2 dp.)',
            answer: '2.83',
            answerType: 'numeric',
            hint: 'Mean is $5$. Then square deviations from $5$.',
            solution: [
              'Mean $= 5$.',
              'Squared deviations: $16, 4, 0, 4, 16$. Sum $= 40$.',
              '$\\sigma = \\sqrt{40/5} = \\sqrt{8} \\approx 2.83$.',
            ],
          },
        },
      ],
    },

    {
      id: 'outlier-effect',
      heading: 'Effect of outliers on mean and std dev',
      summary: 'Mean and std dev are *not* robust — a single outlier can shift both.',
      body: `Standard deviation is computed using **squared** distances from the mean, so it magnifies large deviations. A single outlier — a value far from the others — pulls the mean towards it and *balloons* the standard deviation.

### Why this matters
Compare two data sets:
- A: $\\{4, 5, 5, 6, 6\\}$ (tight).
- B: $\\{4, 5, 5, 6, 6, 30\\}$ (one outlier).

Both have means near $5$, but B's standard deviation is far larger — because of the single extreme value.

### Robust alternatives
The **median** and **IQR** don't get distorted by a single outlier, so they're the safer summary when outliers are present.

### Investigation recipe
1. Compute the mean and std dev.
2. Plot the data or list it in order.
3. Identify any value more than $1.5 \\times IQR$ outside $Q_1 / Q_3$.
4. Compute summary stats *with* and *without* the outlier.
5. Compare the two to see how much influence that one value has.`,
      examples: [
        {
          id: 'ex-outlier-shift',
          statement:
            'Data: $\\{5, 6, 7, 8, 24\\}$. Compute the mean with and without the $24$. What is the difference?',
          steps: [
            'With $24$: sum $= 50$, mean $= 10$.',
            'Without $24$: sum $= 26$, mean $= 26/4 = 6.5$.',
            'Difference: $10 - 6.5 = 3.5$.',
          ],
        },
        {
          id: 'ex-outlier-stddev',
          statement:
            'Data: $\\{1, 2, 3\\}$. Then add the outlier $100$. By approximately how much does the std dev grow?',
          steps: [
            '$\\{1, 2, 3\\}$: mean $= 2$, $\\sigma = \\sqrt{(1+0+1)/3} = \\sqrt{2/3} \\approx 0.82$.',
            '$\\{1, 2, 3, 100\\}$: mean $= 26.5$, squared deviations: $650.25, 600.25, 552.25, 5402.25$.',
            'Sum $= 7205$, $\\sigma = \\sqrt{7205/4} \\approx 42.4$.',
            'Grew from $\\approx 0.82$ to $\\approx 42.4$ — about $50\\times$.',
          ],
        },
        {
          id: 'ex-robustness',
          statement:
            'Which is more affected by a single outlier: the mean, the median, or both equally?',
          steps: [
            'The **mean** is more affected — every value contributes equally to its computation, so one extreme value shifts it.',
            'The median only cares about the *middle* — a single outlier doesn\'t move it.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-mean-without-outlier',
          difficulty: 'intro',
          instance: {
            prompt:
              'Data: $\\{10, 12, 14, 16, 100\\}$. What is the mean without the outlier $100$?',
            answer: '13',
            answerType: 'numeric',
            hint: 'Sum the four remaining values and divide by $4$.',
            solution: [
              'Without $100$: sum $= 10 + 12 + 14 + 16 = 52$.',
              'Mean $= 52/4 = 13$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-robust-choice',
          difficulty: 'core',
          instance: {
            prompt:
              'When a data set contains one extreme outlier, which summary is most distorted: "mean" or "median"? Answer with one word.',
            answer: 'mean',
            answerType: 'exact',
            hint: 'One of these depends on every value, the other only on the order.',
            solution: [
              'The **mean** is most distorted, because it depends on every value (and is pulled by extreme values).',
              'The median is robust to outliers.',
            ],
          },
        },
      ],
    },
  ],
}