import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Statistics · VC2M10ST05.
// Plan and conduct statistical investigations of situations that involve
// bivariate data, including where the independent variable is time;
// evaluate and report findings of any inferences.

export const statisticsInvestigations: Topic = {
  id: 'm10-statistics-investigations',
  unit: 10,
  order: 29,
  title: 'Bivariate investigations',
  blurb:
    'Plan and run a statistical investigation involving two variables, with time as a common explanatory variable.',
  dotPoints: ['m10-st-5'],

  lessons: [
    {
      id: 'investigation-cycle',
      heading: 'The statistical investigation cycle',
      summary: 'Pose a question, collect data, represent, analyse, conclude, reflect.',
      body: `A complete statistical investigation follows a clear cycle:

1. **Pose a question** — what's the variable of interest, and what is its relationship to another (the explanatory variable)?
2. **Collect data** — primary (your own survey or experiment) or secondary (existing data set).
3. **Represent** — scatterplot, two-way table, time-series plot.
4. **Analyse** — describe the distribution; fit a model (linear, exponential, etc.); check residuals.
5. **Conclude** — answer the original question; report assumptions, methods, and findings.
6. **Reflect** — discuss limitations: sample size, bias, generalisability, lurking variables.

### Time as an explanatory variable
A very common setting: track a quantity over time (e.g. monthly rainfall, share price, population). The independent variable is **time**. Watch for:
- Trends (linear, exponential, periodic).
- Seasonal patterns.
- Outliers or sudden changes (often an event worth investigating).`,
      examples: [
        {
          id: 'ex-design',
          statement:
            "You want to know if Year 10 students' weekly screen time has changed over the past 5 years. Outline the variables and the data collection.",
          steps: [
            'Explanatory variable: **year** (2019, 2020, 2021, 2022, 2023).',
            'Response variable: **average weekly screen time in hours** for a representative sample of Year 10s.',
            'Use a time-series plot; model with a line of best fit.',
          ],
        },
        {
          id: 'ex-lurking',
          statement:
            'A study finds a strong positive correlation between ice-cream sales and drowning deaths. What lurking variable is the most likely cause?',
          steps: [
            "Hot weather — drives both ice-cream sales and swimming (which causes drownings).",
            "The correlation is real but **causation** is via the lurking variable.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-time-var',
          difficulty: 'intro',
          instance: {
            prompt:
              "If you plot **monthly sales** over a year, which variable is the explanatory one? Answer as one word.",
            answer: 'time',
            answerType: 'exact',
            hint: "The thing you vary deliberately to see how the response changes.",
            solution: [
              'Time is the explanatory variable (the $x$-axis).',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cycle',
          difficulty: 'core',
          instance: {
            prompt:
              "In the statistical investigation cycle, which step comes **first**? Answer: 'pose', 'collect', 'represent', or 'analyse'.",
            answer: 'pose',
            answerType: 'exact',
            hint: 'You start with a question before doing anything else.',
            solution: [
              "First you **pose** the question — without it the rest of the cycle has no direction.",
            ],
          },
        },
      ],
    },
  ],
}