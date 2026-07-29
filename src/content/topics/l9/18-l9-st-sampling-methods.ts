import type { Topic } from '../../types'

// Foundation (Year 9) · Strand: Statistics · l9-st-2 (VC2M9ST02).
// Sampling methods.

export const l9StSamplingMethods: Topic = {
  id: 'l9-st-sampling-methods',
  unit: 9,
  order: 18,
  title: 'Sampling methods',
  blurb:
    'Analyse how different sampling methods — and different samples using the same method — can affect survey results, and how choice of representation can be used to support a particular point of view.',
  dotPoints: ['l9-st-2'],

  lessons: [
    {
      id: 'sampling-methods',
      heading: 'Sampling methods',
      summary: 'Random sampling aims to be unbiased; convenience, voluntary and quota samples trade bias for ease.',
      body: `The way you pick your sample shapes what you can conclude.

### Methods
- **Simple random sampling (SRS)**: every individual in the population has an equal chance; pick $n$ of them. The gold standard.
- **Systematic sampling**: pick every $k$-th item from a list (e.g. every $10$th name).
- **Stratified sampling**: split the population into groups (strata) and randomly sample from each in proportion to its size.
- **Cluster sampling**: randomly pick whole groups (e.g. schools), then survey everyone in them.
- **Convenience / voluntary samples**: whoever is easiest to reach, or who chooses to respond. Often biased.

### When stratified is right
When you suspect the answer differs by group (e.g. urban vs rural, year level) and you want each group's voice in the result.`,
      examples: [
        {
          id: 'ex-stratify',
          statement:
            'A school has $300$ year-9 and $200$ year-10 students. You want a stratified sample of $50$. How many from each year?',
          steps: [
            'Total $500$; sample fraction $= 50/500 = 0.1$.',
            'Year 9: $300 \\times 0.1 = 30$. Year 10: $200 \\times 0.1 = 20$.',
          ],
        },
        {
          id: 'ex-bias',
          statement:
            'A news show asks viewers to text in their opinion. Is this random sampling? Why or why not?',
          steps: [
            'No — it is a **voluntary** sample.',
            'Only viewers who feel strongly enough to text respond, so the answers over-represent strong opinions.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-strat',
          difficulty: 'core',
          instance: {
            prompt:
              'A school has $400$ year-9s and $100$ year-10s. Take a stratified sample of $50$. How many from year 9?',
            answer: '40',
            answerType: 'numeric',
            hint: 'Sample fraction $= 50/500 = 0.1$.',
            solution: [
              'Fraction $= 50 / 500 = 0.1$. Year 9: $400 \\times 0.1 = 40$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-which',
          difficulty: 'intro',
          instance: {
            prompt:
              'Standing outside a single shopping centre to survey shoppers is an example of what kind of sample? Answer "random", "stratified", or "convenience".',
            answer: 'convenience',
            answerType: 'exact',
            hint: 'It\'s the easiest place to stand — not the most representative.',
            solution: [
              'A **convenience** sample — whoever happens to walk by.',
            ],
          },
        },
      ],
    },

    {
      id: 'representations',
      heading: 'Sample variation & the choice of representation',
      summary: 'Different samples from the same population give different numbers; the chosen display can change the impression.',
      body: `Even with the **same** method, two samples will rarely give exactly the same numbers — there is always some **sampling variability**. Bigger samples vary less.

### Different samples, different numbers
- Two random samples of $50$ from the same population can give means that differ by a few percent.
- A single sample's number is **one draw** from a distribution of possible sample numbers.

### Representation and persuasion
- A **truncated axis** makes a small change look huge.
- A **pie chart with too many slices** hides the pattern.
- **Cherry-picking**: picking a sample (or time range) that supports a chosen story.
- The same data can look "alarming" or "trivial" depending on the scale and display.`,
      examples: [
        {
          id: 'ex-var',
          statement:
            'Two random samples of $50$ from the same town give sample means $\\$52\\,000$ and $\\$55\\,000$. Is this surprising?',
          steps: [
            'No — sample means of size $50$ typically vary by a few thousand dollars.',
            'A difference of $\\$3\\,000$ is well within sampling variation.',
          ],
        },
        {
          id: 'ex-axis',
          statement:
            'A bar chart shows quarterly sales. The $y$-axis starts at $\\$1000$ instead of $\\$0$. What is the misleading effect?',
          steps: [
            'Small differences look enormous. The chart exaggerates any change.',
            'A reader may think sales doubled when they only grew by $5\\%$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-var',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two random samples of the same population give slightly different means. Is this "sampling variability" or "sampling bias"?',
            answer: 'sampling variability',
            answerType: 'exact',
            hint: 'Random fluctuation is different from systematic error.',
            solution: [
              '**Sampling variability** — random differences between samples are normal. Bias would mean a systematic error in the method.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-axis',
          difficulty: 'core',
          instance: {
            prompt:
              'To make a tiny change in sales look dramatic, should the $y$-axis start at the smallest value or at zero? Answer "smallest" or "zero".',
            answer: 'smallest',
            answerType: 'exact',
            hint: 'A truncated axis magnifies small differences.',
            solution: [
              'Starting at the **smallest value** (not zero) exaggerates the change — this is a common trick in misleading charts.',
            ],
          },
        },
      ],
    },
  ],
}
