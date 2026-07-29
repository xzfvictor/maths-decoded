import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Statistics · l8-st-3 (VC2M8ST03).
// Compare variations in distributions and proportions obtained from random
// samples of the same size drawn from a population and recognise the effect of
// sample size on this variation.

export const l8StComparingSamples: Topic = {
  id: 'l8-st-comparing-samples',
  unit: 8,
  order: 25,
  title: 'Comparing sample distributions',
  blurb:
    'Compare variations in distributions and proportions obtained from random samples of the same size drawn from a population, and recognise the effect of sample size.',
  dotPoints: ['l8-st-3'],
  lessons: [
    {
      id: 'sampling-variation',
      heading: 'Sampling variation',
      summary:
        'Two random samples from the same population will not give identical results — the variation between them is called sampling variation.',
      body: `Take two random samples of the **same size** from the same population and you almost never get the same mean, median or proportion. That natural difference is called **sampling variation** — and it is not a mistake.

### What it looks like
- Class A's sample has a mean of $164$ cm; Class B's sample has a mean of $166$ cm — both samples from the same Year 8 cohort.
- $48\\%$ of one sample prefer Brand X; $52\\%$ of another do — same population, different samples.

### Why it happens
Each random sample is a different mix of individuals. Statistics from one sample will differ from statistics from another sample **by chance**.

### Two key facts
1. **Random samples vary from each other.** The variation shrinks as the sample size grows.
2. **The sample statistic is an estimate of the population parameter**, not the parameter itself.

### What to do with this
- Always quote **sample size** $n$ alongside any sample statistic.
- Treat the sample mean / proportion as an **estimate**, not an exact value.
- If two samples disagree, the difference may be just sampling variation — not a real population difference.`,
      examples: [
        {
          id: 'ex-two-samples',
          statement:
            'Two random samples of $50$ students each are drawn from a school. Sample 1 has mean height $165.2$ cm, Sample 2 has mean $163.8$ cm. The true school mean is $164.5$ cm. Are these consistent?',
          steps: [
            'Both sample means ($165.2$ and $163.8$) are close to the true mean ($164.5$).',
            'Their difference ($1.4$ cm) is typical of **sampling variation** for samples of size $50$.',
            'Yes — both are reasonable estimates of the population mean.',
          ],
        },
        {
          id: 'ex-proportion',
          statement:
            'Two random samples of $100$ students each are asked whether they prefer the new canteen menu. Sample 1 says yes $54$ times, Sample 2 says yes $48$ times. Comment on the variation.',
          steps: [
            'Sample proportions: $54\\%$ and $48\\%$.',
            'Difference of $6$ percentage points is normal sampling variation at $n = 100$.',
            'We cannot conclude the population preference is changing — both samples plausibly estimate the same underlying proportion.',
          ],
        },
        {
          id: 'ex-recognise',
          statement:
            'A newspaper claims two random samples "prove" that boys and girls have different heights. Two samples of $20$ each had means $165$ cm and $160$ cm. Is this convincing?',
          steps: [
            'A $5$ cm gap is small. Sample size $20$ is tiny — sampling variation is large.',
            'The two samples may have included very different mixes of individuals by chance.',
            'We cannot conclude boys are taller from these two samples — the difference may be pure sampling variation.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-variation',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two random samples of size $50$ from the same population produce slightly different sample means. This difference is called?',
            answer: 'sampling variation',
            answerType: 'exact',
            hint: 'It is the natural difference between random samples — not a mistake.',
            solution: [
              'Natural differences between random samples are called **sampling variation**.',
            ],
          },
        },
      ],
    },
    {
      id: 'effect-of-sample-size',
      heading: 'Effect of sample size',
      summary:
        'Bigger samples have less sampling variation — their statistics sit closer to the population parameter.',
      body: `Sample size is the most powerful tool for reducing sampling variation.

### The big idea
As the sample size $n$ **grows**, the sample mean / proportion **homes in** on the true population value. As $n$ shrinks, sample statistics become more variable.

### What it looks like
- $10$ samples of size $n = 5$: means scatter from $148$ cm to $180$ cm.
- $10$ samples of size $n = 50$: means cluster tightly around $164$ cm.
- $10$ samples of size $n = 500$: means are almost identical.

### Practical rule of thumb
Doubling the sample size roughly **divides the spread of sample means by $\\sqrt{2}$**. So $n = 100$ has about half the spread of $n = 50$, not twice the precision.

### What it means for decisions
- **Bigger samples** give more **precise** estimates and **narrower** prediction intervals.
- **Smaller samples** are cheaper but **less reliable** — their estimates are easily off by chance.

### Choosing sample size
Before collecting data, ask: "How precise do I need my estimate to be?" Then pick $n$ large enough to give that precision.

> [!warning] Watch out
> A bigger sample fixes **sampling variation**, not **bias**. If your sampling method is biased (e.g. surveying only one suburb), making the sample bigger just gives a more precise estimate of the **wrong thing**.`,
      examples: [
        {
          id: 'ex-compare',
          statement:
            'Sample A has $n = 10$, mean $= 70$. Sample B has $n = 100$, mean $= 75$. Both samples are from the same population. Which estimate is likely closer to the true mean?',
          steps: [
            'Bigger samples vary less around the true mean.',
            'Sample B ($n = 100$) is the more **precise** estimate.',
            'Sample B is likely closer to the true mean than Sample A.',
          ],
        },
        {
          id: 'ex-doubling',
          statement:
            'Roughly how much does the spread of sample means shrink when sample size goes from $100$ to $400$?',
          steps: [
            'New size is $4 \\times$ the old size.',
            'Spread shrinks by a factor of $\\sqrt{4} = 2$.',
            'Sample means are about **twice as close** to the true mean on average.',
          ],
        },
        {
          id: 'ex-bias-vs-size',
          statement:
            'A school surveys $5000$ students but only those who walk past the front office. The sample is large. Will it give a good estimate of the whole school?',
          steps: [
            'Bigger $n$ reduces sampling variation, but not **bias**.',
            'The sample is biased — it misses students who don\'t walk past the office (e.g. seniors in other buildings).',
            'The result may be **precise but wrong** — close to the wrong number, not the true one.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sample-size',
          difficulty: 'intro',
          instance: {
            prompt:
              'Sample size goes from $n = 25$ to $n = 100$ (four times larger). Roughly how much does the spread of sample means shrink? Answer "halved", "quartered", or "same".',
            answer: 'halved',
            answerType: 'exact',
            hint: 'Spread shrinks by a factor of $\\sqrt{4}$.',
            solution: [
              'Spread shrinks by $\\sqrt{4} = 2$, so the spread is **halved**.',
            ],
          },
        },
      ],
    },
  ],
}