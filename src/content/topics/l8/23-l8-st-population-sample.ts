import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Statistics · l8-st-1 (VC2M8ST01).
// Distinguish between a population and a sample, and investigate techniques for
// data collection including census, sampling, experiment and observation, and
// explain the practicalities and implications of obtaining data through these
// techniques.

export const l8StPopulationSample: Topic = {
  id: 'l8-st-population-sample',
  unit: 8,
  order: 23,
  title: 'Populations, samples and data collection',
  blurb:
    'Distinguish between a population and a sample, investigate techniques for data collection (census, sampling, experiment, observation), and explain their practicalities and implications.',
  dotPoints: ['l8-st-1'],
  lessons: [
    {
      id: 'population-vs-sample',
      heading: 'Populations vs. samples',
      summary:
        'A population is the entire group you want to know about; a sample is the smaller group you actually measure.',
      body: `When we collect data, the first question is: **who do we actually want to learn about?**

### Population
The **population** is the **entire** group of individuals (people, objects, events) about which we want information. Every member of the group counts.

### Sample
A **sample** is a **subset** of the population — the smaller group we actually collect data from.

### Why it matters
Any number you compute (a mean, a percentage) is either a **parameter** (computed on the whole population) or a **statistic** (computed on a sample). Conclusions about a population are only as good as the sample that represents it.

### Examples
- Want to know the average height of all Year 8 students in a school?
  - **Population**: every Year 8 student in the school.
  - **Sample**: the $40$ Year 8 students you actually measure.
- Want to know what fraction of Australians prefer a certain brand of cereal?
  - **Population**: all Australians.
  - **Sample**: the $2000$ people you survey.

### Practicalities
Populations are often too big, too far away, or too costly to reach. That is why we use samples — but every shortcut introduces **uncertainty**, which is why we acknowledge it in our conclusions.`,
      examples: [
        {
          id: 'ex-identify',
          statement:
            'A school wants to know the average sleep time of its $1200$ students. They survey $200$ of them. Identify the population and the sample.',
          steps: [
            'Population: **all $1200$ students** at the school.',
            'Sample: the **$200$ students** who answered the survey.',
            'The sample mean estimates the population mean.',
          ],
        },
        {
          id: 'ex-parameter-vs-statistic',
          statement:
            'Every student at a school of $800$ is surveyed, and the average sleep time is found to be $8.2$ hours. Is the $8.2$ a parameter or a statistic?',
          steps: [
            'A **parameter** is computed on the **whole population**.',
            'Every student was surveyed, so the population was measured directly.',
            '$8.2$ hours is a **parameter**.',
          ],
        },
        {
          id: 'ex-cost',
          statement:
            'Why is it usually impractical to measure a whole population?',
          steps: [
            'Populations are often very large — measuring each person is slow.',
            'It is expensive — surveys, lab tests and interviews all cost money.',
            'Sometimes impossible — e.g. you cannot test every Australian for a rare disease.',
            'So we use **samples** and accept the uncertainty that comes with them.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-identify',
          difficulty: 'intro',
          instance: {
            prompt:
              'A factory tests $50$ of $5000$ light bulbs for how long they last. The $5000$ bulbs are the ______ and the $50$ tested are the ______. Answer with the two missing words separated by a comma, e.g. "word1, word2".',
            answer: 'population, sample',
            answerType: 'exact',
            hint: 'Which group is the whole group you want to know about?',
            solution: [
              'The $5000$ bulbs are the **population** (the whole group of interest).',
              'The $50$ tested bulbs are the **sample** (the subset actually measured).',
            ],
          },
        },
      ],
    },
    {
      id: 'data-collection-techniques',
      heading: 'Data collection: census, sample, experiment, observation',
      summary:
        'Four ways to collect data — each has practicalities (cost, time) and implications (bias, ethics).',
      body: `Statisticians collect data in **four main ways**. Each has trade-offs.

### Census
Measure **every** member of the population.
- **Practicalities**: very expensive and slow for large populations. Usually only done for whole countries (a national census).
- **Implications**: gives exact population parameters; no sampling uncertainty.

### Sampling
Measure a **subset** of the population and use the result to infer things about the whole.
- **Practicalities**: cheaper and faster than a census; the sample must be chosen carefully so it represents the population.
- **Implications**: introduces uncertainty — the sample may differ from the population by chance (called **sampling variation**).

### Experiment
Apply a **treatment** to some subjects and compare outcomes with a control group.
- **Practicalities**: needs careful design (control group, random allocation) to isolate cause and effect.
- **Implications**: can establish **cause**, not just association. But experiments may be unethical (e.g. forcing people to smoke).

### Observation
Watch and record what subjects do — **without** intervening.
- **Practicalities**: easier than experiments; the observer just watches.
- **Implications**: only shows **association**, never cause — you cannot tell whether $A$ caused $B$ or they are just linked.

### Bias
All four techniques can introduce **bias** if not done carefully. **Sampling bias** occurs when some members of the population are more likely to be chosen than others — e.g. surveying shoppers at a single shopping centre ignores people who shop elsewhere. **Response bias** happens when questions are worded in a way that nudges a particular answer.`,
      examples: [
        {
          id: 'ex-choose-method',
          statement:
            'A researcher wants to find out whether drinking coffee improves test scores. Should they use a sample, an experiment or an observation?',
          steps: [
            'They want to test a **cause-and-effect** claim ("coffee **causes** better scores").',
            'Only an **experiment** can establish cause — randomly give some students coffee, others none, then compare.',
            'Sample alone or observation only shows association ("coffee drinkers scored higher").',
          ],
        },
        {
          id: 'ex-shopping-centre-bias',
          statement:
            'A news show surveys $200$ shoppers at one suburban shopping centre about their weekly spending. What kind of bias is this?',
          steps: [
            'Only people who shop at **that one centre** are asked — many Australians are missed.',
            'Shoppers at suburban centres may not represent the wider population (different age, income, location).',
            'This is **sampling bias** — some members of the population are far more likely to be picked than others.',
          ],
        },
        {
          id: 'ex-census-vs-sample',
          statement:
            'Why does a national census cost much more than a typical opinion poll?',
          steps: [
            'A census measures **every** citizen — millions of people.',
            'An opinion poll measures a **sample** of perhaps $1000$ people.',
            'The census needs many more interviewers, much more time, and huge administrative cost.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-method',
          difficulty: 'intro',
          instance: {
            prompt:
              'To test whether a new fertiliser makes plants grow taller, a gardener plants $20$ seeds with the fertiliser and $20$ without, and measures their heights. This is a (sample / experiment / observation)?',
            answer: 'experiment',
            answerType: 'exact',
            hint: 'The gardener is **applying a treatment** to one group and comparing with a control.',
            solution: [
              'The gardener **applies a treatment** (the new fertiliser) and compares with a control group (no fertiliser).',
              'This is an **experiment** — and the only way to test cause and effect.',
            ],
          },
        },
      ],
    },
  ],
}