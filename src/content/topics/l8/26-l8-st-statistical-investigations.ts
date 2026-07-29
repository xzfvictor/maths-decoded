import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Statistics · l8-st-4 (VC2M8ST04).
// Plan and conduct statistical investigations involving samples of a
// population; use ethical and fair methods to make inferences about the
// population and report findings, acknowledging uncertainty.

export const l8StStatisticalInvestigations: Topic = {
  id: 'l8-st-statistical-investigations',
  unit: 8,
  order: 26,
  title: 'Statistical investigations with samples',
  blurb:
    'Plan and conduct statistical investigations involving samples of a population, using ethical and fair methods to make inferences and report findings while acknowledging uncertainty.',
  dotPoints: ['l8-st-4'],
  lessons: [
    {
      id: 'planning-the-investigation',
      heading: 'Planning a statistical investigation',
      summary:
        'A good investigation starts with a clear question, a fair sample plan, ethical data collection, and a method of analysis.',
      body: `A **statistical investigation** is a structured way to answer a question using data. The plan matters as much as the numbers.

### The four steps
1. **Pose the question** — what do you want to find out? Make it specific.
2. **Plan how to collect data** — define the population, choose a sampling method, decide sample size.
3. **Collect and analyse the data** — gather it, then summarise with statistics and displays.
4. **Report and infer** — write up the findings, link back to the question, and acknowledge uncertainty.

### Choosing the sample
- Define the **population** clearly (who exactly?).
- Pick a **random** method so the sample is representative.
- Pick a **sample size** large enough to give a precise estimate.

### Ethics and fairness
Statistical investigations have ethical responsibilities:
- **Consent**: participants should know they are being studied and may decline.
- **Privacy**: keep individual responses private; report only summaries.
- **Fairness**: do not target or exclude a group without good reason.
- **Honesty**: do not invent, delete or fudge data.

> [!warning] Watch out
> "I asked my three best friends" is not a fair sample. Even with the best analysis, a biased sample gives a biased answer.`,
      examples: [
        {
          id: 'ex-question',
          statement:
            'A Year 8 class wants to know "How much sleep do students at our school get?" Rewrite this as a specific statistical question.',
          steps: [
            'Specify the population: **all students at our school**.',
            'Specify the variable: **average hours of sleep per school night**.',
            'Specific question: "What is the mean number of hours of sleep per school night for students at our school?"',
          ],
        },
        {
          id: 'ex-sample-plan',
          statement:
            'The school has $600$ students across $4$ year levels ($150$ each). Propose a fair sampling plan to estimate mean sleep hours.',
          steps: [
            'Population: all $600$ students.',
            'Use a **stratified sample** with year level as the stratum.',
            'Sample size $n = 100$ → $25$ from each year level.',
            'Pick students at random within each year level.',
          ],
        },
        {
          id: 'ex-ethics',
          statement:
            'Is it ethical to publish individual sleep times and names of students in a school newsletter? Why or why not?',
          steps: [
            'No — individual responses can identify a student and may embarrass them.',
            'Privacy matters: report only **summaries** (means, percentages), never names.',
            'Consent: students should know how their answers will be used before they answer.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-plan',
          difficulty: 'intro',
          instance: {
            prompt:
              'In a statistical investigation, what is the most important first step? Answer "pose the question", "collect the data", or "report findings".',
            answer: 'pose the question',
            answerType: 'exact',
            hint: 'You cannot design a fair sample until you know what you are measuring.',
            solution: [
              'Without a specific question you cannot pick the right population, variable or sampling method.',
              'Always **pose the question** first.',
            ],
          },
        },
      ],
    },
    {
      id: 'reporting-and-uncertainty',
      heading: 'Reporting findings and acknowledging uncertainty',
      summary:
        'State the source, the size, the method and the uncertainty — every honest report includes all four.',
      body: `A statistical report is not just numbers — it is a story about what those numbers mean **and how much we should trust them**.

### What to include in a report
- **Question** — what was being investigated.
- **Population** — who the findings apply to.
- **Sample size** $n$ — how many people responded.
- **Sampling method** — random, stratified, convenience, ...
- **Summary statistics** — mean / median / proportion, with units.
- **Display** — a chart that shows the distribution.
- **Conclusion** — answer the original question in plain English.
- **Uncertainty** — what limits how confident we can be.

### Why uncertainty matters
- Sampling variation means the sample mean is unlikely to **exactly** equal the population mean.
- Biased sampling means the sample may not even be a fair estimate.
- Always say: "Based on this sample, we estimate ..." rather than "It is exactly ...".

### Inferences
An **inference** is a conclusion about the population drawn from the sample. It must be:
- **Warranted** by the data (not over-claimed).
- **Bounded** by the uncertainty.
- **Ethical** (no harm, no targeting).`,
      examples: [
        {
          id: 'ex-write-report',
          statement:
            'A class of $30$ surveys $60$ random Year 8 students and finds a mean of $8.1$ hours sleep per night. Write a one-sentence inference.',
          steps: [
            'Acknowledge the sample: "Based on a random sample of $60$ Year 8 students (out of $300$)..."',
            'State the estimate: "...we estimate the average sleep per school night at our school to be about $8.1$ hours."',
            'Acknowledge uncertainty: "...with some uncertainty due to sampling variation."',
          ],
        },
        {
          id: 'ex-over-claim',
          statement:
            'A school surveys $20$ students and finds a mean of $9.5$ hours sleep. They claim "Students at our school get more than the recommended 8 hours of sleep". Is the claim warranted?',
          steps: [
            'Sample size is only $n = 20$ — small, so estimates are imprecise.',
            'The claim about the **whole school** is too strong for a $20$-person sample.',
            'A safer claim: "In our sample, the mean was $9.5$ hours, but more data would be needed to draw a firm conclusion about the whole school."',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-uncertainty',
          difficulty: 'intro',
          instance: {
            prompt:
              'A report based on a sample of size $5$ claims "the population mean is exactly $X$". What is wrong with this claim? Answer "too imprecise" or "acknowledges uncertainty".',
            answer: 'acknowledges uncertainty',
            answerType: 'exact',
            hint: 'Look at the second word of the answer.',
            solution: [
              'A sample of size $5$ is very small — its mean is a rough estimate, not exact.',
              'The claim fails to **acknowledge uncertainty** — the right phrasing would be "we estimate $X$, with uncertainty due to small sample size".',
            ],
          },
        },
      ],
    },
  ],
}