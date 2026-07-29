import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Probability · l10a-ap-2 (VC2M10AP02).
// Investigating reports of studies.

export const l10aApInvestigatingReports: Topic = {
  id: 'l10a-ap-investigating-reports',
  unit: '10A',
  order: 26,
  title: 'Investigating reports of studies',
  blurb:
    'Investigate reports of studies in digital media and elsewhere for information on their planning and implementation, evaluating the appropriateness of sampling methods and the support for claims.',
  dotPoints: ['l10a-ap-2'],

  lessons: [
    {
      id: 'reading-a-report',
      heading: 'Reading a study report critically',
      summary: 'Identify the claim, the sample, the method, and any limits the authors admit.',
      body: `A statistical study in the media makes a **claim**. To judge the claim, you need to know:

### The five questions
1. **What is the claim?** Restate it in your own words — what's being asserted, about whom?
2. **Who was studied?** The **population** vs the **sample** — the claim is only as good as the sample.
3. **How were they chosen?** Random? Voluntary? Convenience? Each has different biases.
4. **What was measured?** Variables, units, instruments, sample size $n$.
5. **What's the uncertainty?** Confidence intervals, margin of error, $p$-values if present.

### Red flags to look for
- Tiny sample sizes ($n < 30$).
- "Voluntary response" — only people who felt strongly responded.
- Vague "X% of people" with no sample size.
- Headline overreaching the data ("studies prove" vs "studies suggest").
- No control group, or a poorly-matched one.

### The skill
Spotting the gap between *claim* and *evidence*. A great headline can dress up weak data; your job is to look at the method, not just the conclusion.`,
      examples: [
        {
          id: 'ex-five-qs',
          statement:
            'A headline reads "8 in 10 Australians prefer Brand X". State the five questions you would ask to evaluate this claim.',
          steps: [
            '1. Claim: Brand X is preferred by 80% of Australians.',
            '2. Who was studied? Which Australians — adults? In what states?',
            '3. How were they chosen? Random sample? Voluntary?',
            '4. What was measured? Single question? Multiple? Scale?',
            '5. What\'s the uncertainty? Sample size $n$? Margin of error?',
          ],
        },
        {
          id: 'ex-red-flag',
          statement:
            'A website claims "Our new diet works! 90% of users lost weight!" based on responses from $50$ people who signed up for the diet. Name one red flag.',
          steps: [
            'Self-selection: only people who signed up could respond, so the sample is biased toward those already motivated.',
            '(Also small $n$.)',
          ],
        },
        {
          id: 'ex-control',
          statement:
            'A study compares a new drug to "no treatment". Why is this a weak design?',
          steps: [
            'Without a placebo group, you can\'t tell whether improvements are from the drug or from simply *believing* one is being treated (placebo effect).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pop-vs-sample',
          difficulty: 'intro',
          instance: {
            prompt:
              'A study surveys $200$ Year 10 students about their favourite subject and concludes "most teenagers prefer maths". What\'s wrong? Answer with one or two words (e.g. "sample size", "biased sample", "generalisation", "no control").',
            answer: 'biased sample',
            answerType: 'exact',
            hint: 'The sample doesn\'t represent all teenagers.',
            solution: [
              'The sample is **biased** — Year 10 students only, not all teenagers; and maths preference may differ from older teens.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sample-size',
          difficulty: 'core',
          instance: {
            prompt:
              'A study makes a sweeping national claim from a survey of just $12$ people. What\'s the most important limitation? Answer with one or two words.',
            answer: 'small sample',
            answerType: 'exact',
            hint: 'Think about how much you can generalise from 12 responses.',
            solution: [
              '**Small sample size** — 12 people cannot reliably represent an entire nation.',
            ],
          },
        },
      ],
    },

    {
      id: 'sampling-bias-ethics',
      heading: 'Sampling, bias & ethics',
      summary: 'Match the sampling method to the population, and watch for bias.',
      body: `The sample must mirror the population you want to make claims about. A **biased sample** systematically over- or under-represents some group.

### Common sampling methods
- **Simple random sampling (SRS)**: every member of the population has an equal chance of selection.
- **Stratified sampling**: split the population into groups (strata), then randomly sample within each — preserves group proportions.
- **Cluster sampling**: randomly pick groups, then sample everyone in those groups.
- **Convenience sampling**: take whoever is easiest to reach — usually biased.
- **Voluntary response**: people opt in — usually biased toward those with strong opinions.

### Sources of bias
- **Selection bias**: the sampling method favours some groups.
- **Non-response bias**: those who don't respond differ from those who do.
- **Response bias**: the question wording pushes towards a particular answer.
- **Confirmation bias**: researchers (unconsciously) emphasise results that match their hypothesis.

### Ethics
- **Informed consent**: participants know what they're agreeing to.
- **Anonymity / confidentiality**: data isn't linked back to individuals.
- **Right to withdraw**: participants can leave at any time.
- **No harm**: physical, psychological, social or financial.

### Reporting
A study report should disclose: sample size, how the sample was chosen, the response rate, and any limitations. If it's vague, be suspicious.`,
      examples: [
        {
          id: 'ex-stratified',
          statement:
            'A school has $400$ Year 10 students in $4$ classes of $100$. You want a sample of $40$ students that mirrors the class sizes. Which method?',
          steps: [
            '**Stratified sampling** — each class is a stratum; sample $10$ from each class.',
            'This preserves the equal class sizes in the sample.',
          ],
        },
        {
          id: 'ex-non-response',
          statement:
            'An online survey has a $5\\%$ response rate. Only people with strong opinions tend to respond. What kind of bias?',
          steps: [
            '**Non-response bias** (a kind of selection bias).',
            'The sample over-represents people with strong views.',
          ],
        },
        {
          id: 'ex-ethical',
          statement:
            'A researcher publishes the names of students who admitted to cheating in a school survey. What ethical principle did they breach?',
          steps: [
            '**Confidentiality / anonymity** — participants were not promised anonymity.',
            'Also potentially **informed consent** (depending on what they agreed to).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-method-name',
          difficulty: 'intro',
          instance: {
            prompt:
              'A researcher chooses students by picking every 10th name from a sorted list. Which sampling method is closest: "random", "stratified", "systematic", or "convenience"? Answer with one word.',
            answer: 'systematic',
            answerType: 'exact',
            hint: 'Every 10th from an ordered list — that\'s a rule.',
            solution: [
              '**Systematic sampling** — every $k$th element from a sorted list.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-ethical-principle',
          difficulty: 'core',
          instance: {
            prompt:
              'Participants in a study were not told they were part of an experiment on persuasion. Which ethical principle was breached: "informed consent", "anonymity", "right to withdraw", or "no harm"? Answer with one or two words.',
            answer: 'informed consent',
            answerType: 'exact',
            hint: 'They didn\'t know what they were agreeing to.',
            solution: [
              '**Informed consent** — participants must know they\'re in a study and what it involves.',
            ],
          },
        },
      ],
    },
  ],
}