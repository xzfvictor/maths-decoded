import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Statistics · l7-st-3 (VC2M7ST03).
// Plan and conduct statistical investigations for issues involving
// discrete and continuous numerical data, and data collected from primary
// and secondary sources; analyse and interpret distributions of data and
// report findings.

export const l7StStatisticalInvestigations: Topic = {
  id: 'l7-st-statistical-investigations',
  unit: 7,
  order: 29,
  title: 'Statistical investigations',
  blurb:
    'Plan and conduct statistical investigations using discrete and continuous data from primary and secondary sources, and report findings in terms of shape and summary statistics.',
  dotPoints: ['l7-st-3'],
  lessons: [
    {
      id: 'planning-an-investigation',
      heading: 'Planning a statistical investigation',
      summary:
        'Pose a clear question, choose primary or secondary data, and plan how you will collect a representative sample.',
      body: `A statistical investigation answers a real question with data. It has five stages: **pose**, **collect**, **organise**, **analyse**, **report**. The first step is the most important — without a clear question, the data doesn't lead anywhere.

### Stage 1: Pose a question

The question should be **specific** and **answerable with data**.
- "How long do Year 7 students sleep on a school night?" — good.
- "Is sleep good for you?" — too vague to answer with numbers.

### Stage 2: Plan the data

Decide what you need:
- **Population**: the whole group you care about (e.g. all Year 7 students in the school).
- **Sample**: the smaller group you'll actually measure.
- **Variable**: the thing you'll measure — is it **discrete** (whole numbers like "number of siblings") or **continuous** (any value like "height in cm")?

### Stage 3: Primary vs. secondary data

- **Primary data**: you collect it yourself (survey, experiment, measurement).
- **Secondary data**: you get it from somewhere else (ABS, a published table, an existing study).

Both are useful — but secondary data was collected for a different purpose, so check it really answers your question.

> [!warning] Sample bias
> A sample should be **representative** of the population. Asking only your football team whether they like sport gives biased results.`,
      examples: [
        {
          id: 'ex-good-question',
          statement:
            'Which of these is the better statistical question for a Year 7 investigation: "Is Year 7 fun?" or "How many minutes does each Year 7 student spend on homework per night?"',
          steps: [
            '"Is Year 7 fun?" is vague — what does "fun" mean, and how would you measure it?',
            '"How many minutes ... per night?" has a clear variable (minutes) and a clear unit (per night).',
            'The second question is much easier to investigate statistically.',
          ],
        },
        {
          id: 'ex-primary-vs-secondary',
          statement:
            'You want to compare the average heights of Year 7 students in two schools. Should you collect primary or secondary data?',
          steps: [
            "If you have a tape measure and time to visit both schools, primary data (you measure them yourself) is best — you know the method and the units.",
            'If the schools already have records, secondary data (their height records) is faster.',
            'Either way, use the same method to measure both schools so the comparison is fair.',
          ],
        },
        {
          id: 'ex-sample-bias',
          statement:
            'A newspaper reports that "90% of students love school sport" based on a survey of students at one athletics carnival. Why might this be misleading?',
          steps: [
            "The sample only includes students who chose to attend an athletics carnival — they're already interested in sport.",
            "That is a **biased sample** — it doesn't represent all students.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-good-question',
          difficulty: 'intro',
          instance: {
            prompt:
              'Which is a better statistical question: "Do students like maths?" or "How many minutes per week does each Year 7 student spend on maths homework?"',
            answer: 'minutes per week',
            answerType: 'exact',
            hint: 'A good statistical question names a measurable variable.',
            solution: [
              '"How many minutes per week ..." has a clear measurable variable. "Do students like maths?" is too vague to measure.',
            ],
          },
        },
      ],
    },

    {
      id: 'analysing-and-reporting',
      heading: 'Analysing data and reporting findings',
      summary:
        'Choose a display, compute summary statistics, describe shape/centre/spread, and write a clear conclusion that links back to the original question.',
      body: `Once you've collected the data, the next three stages turn numbers into a story.

### Organise — pick a display

- **Dot plot** or **stem-and-leaf plot**: small data sets; shows every value.
- **Histogram**: large data sets or grouped continuous data; shows shape.
- **Two-way table** or **bar chart**: comparing groups.

### Analyse — compute summary statistics

For each group, report:
- **Centre**: mean **and** median (median if there might be outliers).
- **Spread**: range, and IQR for grouped continuous data.
- **Outliers**: any values far from the rest.

### Report — write a clear conclusion

A good report:
1. **Restates the question** at the top.
2. **Names the data source** (primary/secondary, sample size).
3. **Shows a display** of the data.
4. **Describes the distribution** by shape, centre and spread.
5. **Answers the original question** in one or two sentences.

> [!definition] Match the conclusion to the question
> The conclusion should directly answer the question you posed — not a different, easier question. If the data doesn't fully answer it, say so.`,
      examples: [
        {
          id: 'ex-report-findings',
          statement:
            'A class of $25$ students measured how many minutes they spent on homework. The mean was $42$ minutes, median $40$, range $60$. One student reported $180$ minutes. What should the report flag?',
          steps: [
            'Centre: mean $\\approx$ median ($42$ vs $40$) — close together, so the data is roughly symmetric.',
            'Spread: range $= 60$ minutes — wide.',
            'Outlier: $180$ is far above the rest — flag as a possible outlier.',
            'Recommendation: report the **median** ($40$) as the typical value, since the outlier pulls the mean up.',
          ],
        },
        {
          id: 'ex-compare-groups',
          statement:
            'Class A: median homework time $30$ min, range $20$. Class B: median $50$ min, range $40$. What can you say about how the two classes compare?',
          steps: [
            'Centre: Class B has a higher typical homework time ($50$ vs $30$ min).',
            'Spread: Class B is more variable (range $40$ vs $20$).',
            'So Class B has both a higher typical value and more spread.',
          ],
        },
        {
          id: 'ex-report-three-parts',
          statement:
            'You are writing a report on daily screen time for Year 7. Name the three things you should describe about the distribution.',
          steps: [
            '**Shape**: is it symmetric, skewed, unimodal or bimodal?',
            '**Centre**: typical screen time (mean or median).',
            '**Spread**: range or IQR, plus any outliers.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-compare-groups',
          difficulty: 'intro',
          instance: {
            prompt:
              'Class A has median homework time $30$ min and range $20$ min. Class B has median $50$ min and range $40$ min. Which class has more variable (spread out) homework times?',
            answer: 'Class B',
            answerType: 'exact',
            hint: 'Compare the ranges — a larger range means more spread.',
            solution: [
              'Class B has a larger range ($40$ vs $20$), so Class B has more variable homework times.',
            ],
          },
        },
      ],
    },
  ],
}
