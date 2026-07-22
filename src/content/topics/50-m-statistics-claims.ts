import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Statistics · VC2M10ST04.
// Analyse claims, inferences and conclusions of statistical reports in
// the media and other places, by linking claims to displays, statistics
// and representative data, including ethical considerations and
// identification of potential sources of bias.

export const statisticsClaims: Topic = {
  id: 'm10-statistics-claims',
  unit: 10,
  order: 28,
  title: 'Reading media claims critically',
  blurb:
    'Spot broken axes, cherry-picked data, biased samples and other tricks that distort the story a chart is telling.',
  dotPoints: ['m10-st-4'],

  lessons: [
    {
      id: 'spotting-bias',
      heading: 'Spotting misleading graphs and bias',
      summary: 'Check the axes, the sample, and the context — the three places a chart can mislead.',
      body: `Statistical claims in the media can mislead. Three common places to check:

### 1. The axes
- **Truncated $y$-axis**: a bar chart that starts at $50$ instead of $0$ makes a small change look enormous.
- **Non-zero baseline / broken axis**: same trick.
- **Asymmetric or logarithmic axes** can be legitimate but need to be flagged clearly.

### 2. The sample
- **Selection bias**: was the sample chosen fairly? E.g. a poll of newspaper readers skews politically.
- **Sample size**: a poll of $30$ people is much less reliable than a poll of $3000$.
- **Population match**: don't generalise from cats to dogs.

### 3. The conclusion
- **Correlation vs causation**: two correlated variables may be linked by a third (lurking) variable.
- **Cherry-picking**: showing only the data that supports the claim.
- **Loaded questions in surveys**: wording that nudges the responder.

### Ethics
If a statistic affects people's lives (medical claims, public policy), the ethical bar is higher — both the data and its interpretation should be open to scrutiny.`,
      examples: [
        {
          id: 'ex-truncated',
          statement:
            "A bar chart shows the bar for last year at $50$ and the bar for this year at $55$. The $y$-axis is truncated to start at $45$. By what visual factor does this year's bar look bigger?",
          steps: [
            'True ratio: $55/50 = 1.1$ (10% bigger).',
            'Visual: bars start at $45$, so the visible heights are $5$ vs $10$ — the bar looks $2$ times bigger.',
            "That's a $20\\times$ visual exaggeration of a real $10\\%$ change.",
          ],
        },
        {
          id: 'ex-causation',
          statement:
            'A study finds that cities with more ice-cream sales have more drownings. Does eating ice-cream cause drowning?',
          steps: [
            'No — a lurking variable (hot weather) drives both.',
            'Hot weather → more ice-cream sales AND more swimming → more drownings.',
            "The correlation is real, but the causation is wrong.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-truncated',
          difficulty: 'intro',
          instance: {
            prompt:
              "A bar chart's $y$-axis is truncated to start at $90$ instead of $0$. Bar $A$ is at $95$ and bar $B$ is at $100$. By what visual factor does $B$ look larger than $A$? (As a decimal.)",
            answer: '2',
            answerType: 'numeric',
            hint: 'Visible heights are $5$ and $10$.',
            solution: [
              "Visible ratio $= 10/5 = 2$. So $B$ looks twice as tall as $A$.",
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sample-size',
          difficulty: 'core',
          instance: {
            prompt:
              'A study surveys $20$ people and reports a "finding". What is the smallest sample size that would be considered a more reliable survey? (As an integer.)',
            answer: '100',
            answerType: 'numeric',
            hint: 'A common rule of thumb: at least $100$ for reasonable reliability.',
            solution: [
              "A sample of at least $100$ (and ideally several hundred) is generally considered reliable for simple surveys.",
            ],
          },
        },
      ],
    },
  ],
}