import type { Topic } from '../types'
import { gcd } from '../../exercises/format'

// Unit 2 · Topic 11 — Conditional probability, total probability, independence,
// and simulation of selection with/without replacement.

export const conditionalProbability: Topic = {
  id: 'conditional-probability',
  unit: 2,
  order: 11,
  title: 'Conditional probability & independence',
  blurb:
    'Conditional probability in terms of a reduced sample space, the law of total probability, independence, and simulation for selection with and without replacement.',
  dotPoints: ['u2-pr-3', 'u2-pr-4', 'u2-pr-5', 'u2-pr-6'],

  lessons: [
    {
      id: 'conditional',
      heading: 'Conditional probability',
      summary: 'Pr(A|B) — updating belief after learning that B happened.',
      body: `The **conditional probability** of $A$ **given** $B$ is the probability of $A$ once we know that $B$ has occurred. The sample space shrinks to $B$ itself, and we ask which of its outcomes are also in $A$:
$$\\Pr(A \\mid B) = \\dfrac{\\Pr(A \\cap B)}{\\Pr(B)}, \\quad \\text{provided } \\Pr(B) > 0.$$

### Equivalent statement
$$\\Pr(A \\cap B) = \\Pr(A \\mid B) \\cdot \\Pr(B).$$
This rearrangement is what you use to "decompose" a joint probability into a chain of conditionals.

### Reduced sample space
A useful way to *think* about $\\Pr(A \\mid B)$:
1. Imagine you know $B$ happened.
2. Look only at the outcomes in $B$.
3. Count how many of them are also in $A$, divide by total $|B|$.`,
      examples: [
        {
          id: 'ex-conditional-cards',
          statement:
            'A card is drawn at random from a standard $52$-card deck. Given that the card is red, what is the probability that it is a heart?',
          steps: [
            'Total red cards: $26$ (hearts + diamonds).',
            'Hearts among them: $13$.',
            '$\\Pr(\\text{heart} \\mid \\text{red}) = \\dfrac{13}{26} = \\dfrac{1}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-conditional',
          difficulty: 'core',
          build: (seed) => {
            // Bag: a red, b blue, c green. Given red or blue, find red.
            // P(red | red or blue) = a / (a + b)
            const a = (seed % 3) + 2 // 2..4
            const b = (seed % 4) + 1 // 1..4
            const c = (seed % 3) + 1 // 1..3
            const denom = a + b
            const g = gcd(a, denom)
            return {
              prompt: `A bag contains ${a} red, ${b} blue and ${c} green balls. A ball is drawn; given that it is red **or** blue, what is the probability it is red? Give as a fraction in lowest terms.`,
              answer: `${a / g}/${denom / g}`,
              answerType: 'numeric',
              hint: 'Condition on "red or blue" — the new sample space has $a + b$ balls.',
              solution: [
                `Given "red or blue", the sample space has $${a} + ${b} = ${denom}$ balls.`,
                `Of these, $${a}$ are red.`,
                `$\\Pr(\\text{red} \\mid \\text{red or blue}) = \\dfrac{${a}}{${denom}} = \\dfrac{${a / g}}{${denom / g}}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-conditional-from-given',
          difficulty: 'core',
          build: (_seed) => {
            // Pr(A | B) = Pr(A ∩ B) / Pr(B). Choose numbers so result is a simple decimal.
            const pairs: Array<[number, number, number]> = [
              [0.06, 0.2, 0.3], // 0.06 / 0.2 = 0.3
              [0.04, 0.2, 0.2], // 0.04 / 0.2 = 0.2
              [0.1, 0.4, 0.25], // 0.1 / 0.4 = 0.25
              [0.03, 0.1, 0.3], // 0.03 / 0.1 = 0.3
            ]
            const [inter, pB, ans] = pairs[_seed % pairs.length]
            // find pA such that pA * pB = inter; but our formula doesn't need pA.
            return {
              prompt: `Use $\\Pr(A \\mid B) = \\dfrac{\\Pr(A \\cap B)}{\\Pr(B)}$ with $\\Pr(A \\cap B) = ${inter}$ and $\\Pr(B) = ${pB}$. State $\\Pr(A \\mid B)$ as a decimal.`,
              answer: String(ans),
              answerType: 'numeric',
              hint: 'Divide the joint by the conditional base.',
              solution: [
                `$\\Pr(A \\mid B) = \\dfrac{${inter}}{${pB}} = ${ans}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'total-probability',
      heading: 'Law of total probability',
      summary: 'Pr(A) via a partition of the sample space.',
      body: `If $B_1, B_2, \\ldots, B_n$ are mutually exclusive events that **partition** the sample space (every outcome is in exactly one $B_i$) and $\\Pr(B_i) > 0$ for each $i$, then
$$\\Pr(A) = \\sum_{i = 1}^{n} \\Pr(A \\mid B_i) \\cdot \\Pr(B_i).$$
That is, you split the question into cases (the $B_i$), handle each one, and add the pieces back together.

### Why this is useful
Each $\\Pr(A \\mid B_i)$ is often easy to compute (a "given" branch on a tree). Multiplying by $\\Pr(B_i)$ weighs that branch by how likely it is, and summing gives the unconditional probability of $A$.`,
      examples: [
        {
          id: 'ex-total',
          statement:
            'A factory has two machines. Machine 1 produces 60% of items, with a 2% defect rate; machine 2 produces 40%, with a 3% defect rate. Find $\\Pr(\\text{defective})$.',
          steps: [
            '$\\Pr(D) = \\Pr(D \\mid M_1)\\Pr(M_1) + \\Pr(D \\mid M_2)\\Pr(M_2)$.',
            '$= 0.02 \\cdot 0.6 + 0.03 \\cdot 0.4$.',
            '$= 0.012 + 0.012 = 0.024$ — a $2.4\\%$ defect rate.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-total-prob',
          difficulty: 'core',
          build: (seed) => {
            // Two branches; each is small nice decimal.
            const branches: Array<{ p1: number; p2: number; d1: number; d2: number; ans: number }> = [
              { p1: 0.5, p2: 0.5, d1: 0.1, d2: 0.2, ans: 0.15 },
              { p1: 0.3, p2: 0.7, d1: 0.05, d2: 0.1, ans: 0.085 },
              { p1: 0.4, p2: 0.6, d1: 0.02, d2: 0.05, ans: 0.038 },
              { p1: 0.6, p2: 0.4, d1: 0.05, d2: 0.1, ans: 0.07 },
            ]
            const b = branches[seed % branches.length]
            return {
              prompt: `A process has two stages. $P(\\text{stage 1}) = ${b.p1}$ with defect rate $${b.d1}$, and $P(\\text{stage 2}) = ${b.p2}$ with defect rate $${b.d2}$. Find the overall defect probability as a decimal.`,
              answer: String(b.ans),
              answerType: 'numeric',
              hint: 'Total probability: $P(D) = P(D|1)P(1) + P(D|2)P(2)$.',
              solution: [
                `$P(D) = ${b.d1} \\cdot ${b.p1} + ${b.d2} \\cdot ${b.p2} = ${b.d1 * b.p1} + ${b.d2 * b.p2} = ${b.ans}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'independence',
      heading: 'Independence',
      summary: 'Pr(A∩B) = Pr(A)Pr(B); and the conditional test.',
      body: `Two events $A$ and $B$ are **independent** if learning that one happened does not change the probability of the other. There are three equivalent statements:

1. $\\Pr(A \\cap B) = \\Pr(A) \\cdot \\Pr(B)$.
2. $\\Pr(A \\mid B) = \\Pr(A)$ (when $\\Pr(B) > 0$).
3. $\\Pr(B \\mid A) = \\Pr(B)$ (when $\\Pr(A) > 0$).

The first form is the **multiplication rule** and is the easiest for calculation.

### Common settings
- Drawing **with replacement** typically produces independent draws: knowing what was drawn first doesn't change the bag for the second draw.
- Drawing **without replacement** typically does **not** produce independent draws.`,
      examples: [
        {
          id: 'ex-independence-test',
          statement:
            'Two events have $\\Pr(A) = 0.5$, $\\Pr(B) = 0.6$, $\\Pr(A \\cap B) = 0.3$. Are they independent?',
          steps: [
            'Independence test: $\\Pr(A) \\cdot \\Pr(B) = 0.5 \\cdot 0.6 = 0.3$.',
            'This equals $\\Pr(A \\cap B)$, so yes — they are independent.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-independence-test',
          difficulty: 'core',
          build: (seed) => {
            const pairs: Array<[number, number, number, boolean]> = [
              [0.5, 0.4, 0.2, true], // 0.5*0.4 = 0.2 ✓
              [0.5, 0.4, 0.3, false], // 0.5*0.4 = 0.2 ≠ 0.3
              [0.3, 0.6, 0.18, true],
              [0.3, 0.6, 0.2, false],
            ]
            const [pa, pb, inter, indep] = pairs[seed % pairs.length]
            return {
              prompt: `Two events satisfy $\\Pr(A) = ${pa}$, $\\Pr(B) = ${pb}$, $\\Pr(A \\cap B) = ${inter}$. Are they independent? Answer "yes" or "no".`,
              answer: indep ? 'yes' : 'no',
              answerType: 'exact',
              hint: 'Check whether $\\Pr(A) \\cdot \\Pr(B) = \\Pr(A \\cap B)$.',
              solution: [
                `$\\Pr(A) \\cdot \\Pr(B) = ${pa} \\cdot ${pb} = ${pa * pb}$.`,
                `Compare with $\\Pr(A \\cap B) = ${inter}$.`,
                `${indep ? 'They match — independent.' : 'They differ — not independent.'}`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-multiplication-rule',
          difficulty: 'core',
          build: (_seed) => {
            const pairs: Array<[number, number, number]> = [
              [0.4, 0.5, 0.2],
              [0.3, 0.6, 0.18],
              [0.7, 0.2, 0.14],
              [0.5, 0.8, 0.4],
            ]
            const [pa, pb, ans] = pairs[_seed % pairs.length]
            return {
              prompt: `If $A$ and $B$ are independent with $\\Pr(A) = ${pa}$ and $\\Pr(B) = ${pb}$, find $\\Pr(A \\cap B)$. Give a decimal.`,
              answer: String(ans),
              answerType: 'numeric',
              hint: 'Multiplication rule.',
              solution: [
                `$\\Pr(A \\cap B) = ${pa} \\cdot ${pb} = ${ans}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'replacement',
      heading: 'Simulation: with vs. without replacement',
      summary: "Why the rule changes when we don't return the first draw.",
      body: `When running a simulation, **with replacement** means you put the first draw back before the second; **without replacement** means you keep the first out.

### With replacement — independent draws
Each draw sees the same bag. $\\Pr$ for each draw is the same. Drawing an ace, then another ace, has probability $\\tfrac{4}{52} \\cdot \\tfrac{4}{52}$.

### Without replacement — dependent draws
The bag shrinks between draws. $\\Pr$ changes. Two aces in two draws without replacement has probability
$$\\frac{4}{52} \\cdot \\frac{3}{51}.$$
The second draw sees $51$ cards and $3$ aces — not the same as the first draw.

### Simulation with a calculator
- **With replacement**: roll a die (or generate a uniform random) and map digits; rerun for the next draw.
- **Without replacement**: track which draws have already happened (e.g. cards already "removed") and reject duplicates. The relative frequency should approach the theoretical (without-replacement) probability as $n$ grows.`,
      examples: [
        {
          id: 'ex-without-replacement',
          statement:
            'A deck of 52 cards: two cards are drawn **without** replacement. $\\Pr(\\text{both aces})$?',
          steps: [
            'First ace: $\\tfrac{4}{52} = \\tfrac{1}{13}$.',
            'Second ace: $3$ aces left in $51$ cards: $\\tfrac{3}{51} = \\tfrac{1}{17}$.',
            'Multiply: $\\tfrac{1}{13} \\cdot \\tfrac{1}{17} = \\tfrac{1}{221}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-without-replacement',
          difficulty: 'challenge',
          build: (_seed) => {
            // Bag: 1 special ball + (n-1) others, 2 draws without replacement.
            // P(both special) = (1/n) * 0/(n-1) = 0 ... too trivial.
            // Use bag with 2 special and total n.  P(both special) = (2/n)*(1/(n-1)).
            const total = 5 // small
            const special = 2
            const num = special * (special - 1)
            const den = total * (total - 1)
            const g = gcd(num, den)
            return {
              prompt: `A bag has ${special} green balls and ${total - special} others (total ${total}). Two balls are drawn **without** replacement. Find $\\Pr(\\text{both green})$ as a fraction in lowest terms.`,
              answer: `${num / g}/${den / g}`,
              answerType: 'numeric',
              hint: 'The bag shrinks between draws.',
              solution: [
                `First draw green: $\\dfrac{${special}}{${total}}$.`,
                `Second draw green (one fewer green, one fewer total): $\\dfrac{${special - 1}}{${total - 1}}$.`,
                `Multiply: $\\dfrac{${special}}{${total}} \\cdot \\dfrac{${special - 1}}{${total - 1}} = \\dfrac{${num}}{${den}} = \\dfrac{${num / g}}{${den / g}}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-with-replacement',
          difficulty: 'core',
          build: (_seed) => {
            // Same setup but with replacement: P(both green) = (special/total)^2
            const total = 5
            const special = 2
            const num = special * special
            const den = total * total
            const g = gcd(num, den)
            return {
              prompt: `Same bag as before: ${special} green and ${total - special} others. Two balls are drawn **with** replacement. Find $\\Pr(\\text{both green})$ as a fraction in lowest terms.`,
              answer: `${num / g}/${den / g}`,
              answerType: 'numeric',
              hint: 'The bag is the same for each draw.',
              solution: [
                `Each draw is independent.`,
                `$\\Pr(\\text{green}) = \\dfrac{${special}}{${total}}$.`,
                `$\\Pr(\\text{both green}) = \\left(\\dfrac{${special}}{${total}}\\right)^2 = \\dfrac{${num}}{${den}} = \\dfrac{${num / g}}{${den / g}}$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
