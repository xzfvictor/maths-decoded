import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Statistics · l9-st-5 (VC2M9ST05).
// Statistical investigations.

export const l9StStatisticalInvestigations: Topic = {
  id: 'l9-st-statistical-investigations',
  unit: 9,
  order: 21,
  title: 'Statistical investigations',
  blurb:
    'Plan and conduct statistical investigations involving the collection and analysis of different kinds of data, and report findings while discussing the strength of evidence supporting any conclusions.',
  dotPoints: ['l9-st-5'],

  lessons: [
    {
      id: 'plan-investigation',
      heading: 'Planning a statistical investigation',
      summary: 'Pose a question, choose a sample, decide what to measure, collect, then analyse.',
      body: `A statistical investigation has a recognisable shape. Doing the steps in order avoids the common trap of "collect first, decide what to ask later".

### The cycle
1. **Pose a question** that can be answered with data.
2. **Choose the variables** you need (numerical, categorical, both).
3. **Decide on a population and a sampling method**.
4. **Plan the data collection**: who, what, when, how.
5. **Collect** the data carefully and honestly.
6. **Analyse** with appropriate displays and summary statistics.
7. **Interpret** in the context of the original question.
8. **Communicate** the findings and their limitations.`,
      examples: [
        {
          id: 'ex-plan',
          statement:
            'Your class wonders whether year-9 students sleep more than year-10 students. Sketch the investigation plan.',
          steps: [
            'Question: "Do year-9 students sleep more than year-10 students at our school?"',
            'Variable: hours of sleep last school night (numerical).',
            'Population: year-9 and year-10 students. Sampling: stratified, with random selection within each year.',
            'Collection: anonymous survey, or ask each student to record their own sleep time for a week.',
            'Analysis: side-by-side boxplots, compare medians and IQRs.',
            'Communicate: state the result, the size of the difference, and the limitations (self-report, one school).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-first-step',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the first step of a statistical investigation? Answer "collect data", "pose a question", or "analyse the data".',
            answer: 'pose a question',
            answerType: 'exact',
            hint: 'Start with what you want to know.',
            solution: [
              '**Pose a question** — the rest of the investigation is shaped by it.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-method-choose',
          difficulty: 'core',
          instance: {
            prompt:
              'You want to compare the average sleep of year-9 and year-10 students at your school. Which sampling method fits best? Answer: "simple random", "stratified by year", or "convenience".',
            answer: 'stratified by year',
            answerType: 'exact',
            hint: 'You want both years represented fairly.',
            solution: [
              '**Stratified by year** — you want both groups fairly represented, then random selection within each.',
            ],
          },
        },
      ],
    },

    {
      id: 'strength-of-evidence',
      heading: 'Strength of evidence & reporting',
      summary: 'Big random samples give strong evidence; small or biased samples give weak evidence — even if the result is dramatic.',
      body: `After you have a result, ask: **how strong is the evidence** that the pattern is real and not just sampling noise?

### What strengthens the evidence
- A **larger** random sample.
- A **replication** — the same result from a different sample.
- A **large effect size** — a $5$ cm height difference between classes is more striking than a $0.1$ cm difference.
- An **appropriate** analysis (matched to the data type).

### What weakens the evidence
- A small or biased sample.
- A single observation (anecdote).
- A pattern that **disappears** when you re-measure.
- Heavy reliance on **self-report** (people misremember or misrepresent).

### Reporting findings
State the result, the size of the effect, the sample size and method, and any **limitations**. Don't claim more than the data supports.`,
      examples: [
        {
          id: 'ex-strong',
          statement:
            'A random sample of $2000$ adults finds $62\\%$ support a policy. A separate random sample of $50$ adults in one suburb finds $75\\%$ support. Which is stronger evidence about the national view?',
          steps: [
            'The national $2000$-person sample is stronger — bigger and random.',
            'The $50$-person suburb result is more variable and may not generalise.',
          ],
        },
        {
          id: 'ex-claim',
          statement:
            'A study of $10$ students found the new app raised test scores by $15$ points. The app\'s website calls this "proven to boost results". Is the claim justified?',
          steps: [
            'No — $n = 10$ is tiny, no control group, no randomisation. The difference could easily be sampling noise.',
            'The evidence is **weak**; the website\'s claim overstates the result.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-strong',
          difficulty: 'core',
          instance: {
            prompt:
              'A result comes from a sample of $5$ people. Compared with a result from a random sample of $1000$, is the small-sample result stronger or weaker evidence? Answer "stronger" or "weaker".',
            answer: 'weaker',
            answerType: 'exact',
            hint: 'Bigger random samples give more reliable results.',
            solution: [
              '**Weaker** — $n = 5$ is much more affected by sampling noise than $n = 1000$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-report',
          difficulty: 'intro',
          instance: {
            prompt:
              'When reporting findings, you should mention the sample size, limitations, and: "your opinion", "the effect size", or "a poem"?',
            answer: 'the effect size',
            answerType: 'exact',
            hint: 'How big is the difference you found?',
            solution: [
              '**The effect size** — how big the difference is, not just whether it exists.',
            ],
          },
        },
      ],
    },
  ],
}
