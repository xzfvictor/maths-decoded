import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Statistics · l9-st-4 (VC2M9ST04).
// Choosing data displays.

export const l9StChoosingDisplays: Topic = {
  id: 'l9-st-choosing-displays',
  unit: 9,
  order: 20,
  title: 'Choosing data displays',
  blurb:
    'Choose an appropriate form of display or visualisation for a given type of data, justify the selection, and interpret the display in its context.',
  dotPoints: ['l9-st-4'],

  lessons: [
    {
      id: 'data-type-display',
      heading: 'Matching the data type to the display',
      summary: 'Categorical → bar/pie; one numerical → histogram or dot plot; two numerical → scatterplot; time series → line graph.',
      body: `The right display depends on what kind of data you have and what question you're asking.

### Categorical data
- **Bar chart** — counts or percentages per category. Easy to compare.
- **Pie chart** — parts of a whole, when categories sum to $100\\%$.
- **Two-way table** — two categorical variables side by side.

### One numerical variable
- **Histogram** — shape of a continuous distribution.
- **Dot plot** — small data sets, every observation visible.
- **Stem-and-leaf plot** — keeps the values, shows the shape.
- **Boxplot** — five-number summary, easy comparison of groups.

### Two numerical variables
- **Scatterplot** — show the relationship between $x$ and $y$.

### Over time
- **Line graph** — time on the $x$-axis, quantity on the $y$-axis.`,
      examples: [
        {
          id: 'ex-choose',
          statement:
            'You want to show how a city\'s population has changed each year for the last $20$ years. What is the best display?',
          steps: [
            'Time series of one numerical variable → **line graph**.',
          ],
        },
        {
          id: 'ex-pie',
          statement:
            'You have survey responses to the categorical question "What is your favourite fruit?", with five options. Which display lets you show each fruit as a part of the whole?',
          steps: [
            'A **pie chart** — each slice is one fruit\'s percentage of all responses.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-which-display',
          difficulty: 'intro',
          instance: {
            prompt:
              'You want to compare the heights of two groups of students side by side. Best display: "scatterplot", "back-to-back boxplot", or "pie chart"?',
            answer: 'back-to-back boxplot',
            answerType: 'exact',
            hint: 'Boxplots summarise a distribution and are easy to compare side by side.',
            solution: [
              '**Back-to-back boxplot** — five-number summaries make group-by-group comparison clean.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-time',
          difficulty: 'core',
          instance: {
            prompt:
              'You have monthly rainfall totals for a year. Best display: "pie chart", "line graph", or "scatterplot"?',
            answer: 'line graph',
            answerType: 'exact',
            hint: 'Time on the $x$-axis, totals on the $y$-axis.',
            solution: [
              '**Line graph** — best for showing a quantity changing over time.',
            ],
          },
        },
      ],
    },

    {
      id: 'interpret-justify',
      heading: 'Interpreting and justifying the display',
      summary: 'A good display answers the question; say what the display shows and why it is the right choice.',
      body: `A good answer to "which display?" has two parts: **what the display shows**, and **why that display fits the data and the question**.

### Justification template
"The data is [type], the question is [question], so a [display] is appropriate because it [reason]."

### Reading a display
- Always state **what the axes represent** and the **units**.
- Identify the **centre**, **spread** and **shape**.
- Note any **outliers** and explain why they matter.
- Relate the pattern back to the **context** (the data was about $X$, so the peak at $Y$ means...).`,
      examples: [
        {
          id: 'ex-justify',
          statement:
            'You choose a histogram to display the ages of $500$ visitors to a museum. Justify the choice.',
          steps: [
            'Data is one numerical variable, continuous. The question is "what is the shape of the visitor age distribution?".',
            'A histogram shows the shape of a continuous distribution; counts in age bins. A pie chart would be meaningless, a boxplot would lose detail.',
          ],
        },
        {
          id: 'ex-read',
          statement:
            'A scatterplot of study hours (x) vs exam score (y) shows points trending up to the right, with one student at $(30, 55)$. Interpret.',
          steps: [
            'Positive association: more study tends to mean higher score.',
            'The point $(30, 55)$ — studied a lot but scored low — is an outlier; maybe a difficult exam or an off day.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-justify',
          difficulty: 'core',
          instance: {
            prompt:
              'You want to show the relationship between a student\'s hours of TV watched per day and their exam score. Best display? Answer with one word.',
            answer: 'scatterplot',
            answerType: 'exact',
            hint: 'Two numerical variables; we want to see how one varies with the other.',
            solution: [
              '**Scatterplot** — pairs of $(x, y)$ values let you see the relationship between two numerical variables.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-axes',
          difficulty: 'intro',
          instance: {
            prompt:
              'When interpreting a graph, you should first state what each axis represents. Answer "true" or "false".',
            answer: 'true',
            answerType: 'exact',
            hint: 'Without axes, the picture is just a picture.',
            solution: [
              '**True** — always start by naming the axes and units so the reader knows what is being shown.',
            ],
          },
        },
      ],
    },
  ],
}
