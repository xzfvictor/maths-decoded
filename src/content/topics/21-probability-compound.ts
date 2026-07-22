import type { Topic } from '../types'
import { gcd } from '../../exercises/format'

// Unit 2 · Topic 10 — Probability of compound events. Representations: lists,
// grids (two-way tables), Venn diagrams, tables, and tree diagrams. The addition
// rule and mutual exclusivity.

export const probabilityCompound: Topic = {
  id: 'probability-compound',
  unit: 2,
  order: 10,
  title: 'Probability of compound events',
  blurb:
    'Lists, two-way tables, Venn diagrams and tree diagrams for compound events; the addition rule and mutually exclusive events.',
  dotPoints: ['u2-pr-1', 'u2-pr-2'],

  lessons: [
    {
      id: 'representations',
      heading: 'Representations for compound events',
      summary: 'Picking the right diagram for two events.',
      body: `Compound events involve more than one random quantity. There are several standard ways to draw them, and choosing the right one keeps the algebra clean.

### Lists
- **Ordered pair list**: e.g. $\\{(H, 1), (H, 2), (H, 3), (H, 4), (H, 5), (H, 6), (T, 1), \\ldots\\}$ — coin and die.
- **2-D / sample grid**: rows are one event, columns the other.

### Venn diagrams
Two overlapping circles (or more) for two events, with the overlap representing the **intersection**. Labelled regions let you read off probabilities visually.
- The whole rectangle = sample space (probability $1$).
- $A$ + the overlap = $\\Pr(A)$.
- $B$ + the overlap = $\\Pr(B)$.
- Outside both circles = $\\Pr(\\text{neither})$.

### Two-way tables
A **two-way table** (or **contingency table**) lists outcomes in a grid, with marginal totals. Useful when summing across categories.

### Tree diagrams
A **tree** successively branches through each stage of the experiment; branch probabilities multiply along paths and add for the total of a multi-path event.`,
      examples: [
        {
          id: 'ex-grid',
          statement:
            "A coin and a die are tossed. How many equally likely outcomes are there?",
          steps: [
            '$2 \\times 6 = 12$. List: $\\{(H,1), (H,2), \\ldots, (T, 6)\\}$.',
          ],
        },
        {
          id: 'ex-two-way-table',
          statement:
            'Of 60 students, 25 study biology and 30 study chemistry, with 10 studying both. How many study neither?',
          steps: [
            'Use the addition rule: $|B \\cup C| = |B| + |C| - |B \\cap C| = 25 + 30 - 10 = 45$.',
            'Neither = $60 - 45 = 15$ students.',
          ],
        },
        {
          id: 'ex-venn',
          statement:
            'Two events $A$ and $B$ satisfy $\\Pr(A) = 0.5$, $\\Pr(B) = 0.4$, and $\\Pr(A \\cap B) = 0.2$. Which is bigger: $\\Pr(A)$ or $\\Pr(A \\cap B)$?',
          steps: [
            'A sub-event cannot be more likely than its enclosing event: $\\Pr(A \\cap B) \\le \\Pr(A)$.',
            '$0.2 < 0.5$, so $\\Pr(A)$ is bigger.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-sample-space-size',
          difficulty: 'intro',
          build: (seed: number) => {
            // Two events with result counts a * b.
            const aVals = [2, 4, 6]
            const bVals = [3, 4, 5, 6]
            const a = aVals[seed % aVals.length]
            const b = bVals[Math.floor(seed / aVals.length) % bVals.length]
            return {
              prompt: `Two random experiments are run, with ${a} equally likely outcomes for the first and ${b} for the second. How many equally likely outcomes are there in the combined sample space?`,
              answer: String(a * b),
              answerType: 'numeric',
              hint: 'The combined sample space is the Cartesian product of the two.',
              solution: [
                `By the multiplication principle: $${a} \\times ${b} = ${a * b}$ equally likely outcomes.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-venn-total',
          difficulty: 'core',
          instance: {
            prompt:
              'Two events $A$ and $B$ are drawn on a Venn diagram inside the sample space rectangle. The three labelled regions are $A$ only, $B$ only, and $A \\cap B$. The sum of all labelled region probabilities and the outside rectangle (neither) equals what? (Answer "0", "1", or "infinity".)',
            answer: '1',
            answerType: 'exact',
            hint: 'The whole sample space has probability $1$.',
            solution: [
              'Every outcome belongs to exactly one region.',
              'So the probabilities of all (disjoint) regions sum to $1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-sample-size',
          difficulty: 'intro',
          instance: {
            prompt:
              'A coin is tossed and a 4-sided die is rolled. How many equally likely outcomes are there?',
            answer: '8',
            answerType: 'numeric',
            hint: 'Multiply the choices: $2 \\times 4$.',
            solution: [
              '$2 \\times 4 = 8$ equally likely outcomes.',
            ],
          },
        },
      ],
    },

    {
      id: 'addition-rule',
      heading: 'The addition rule',
      summary: 'Pr(A∪B) = Pr(A) + Pr(B) − Pr(A∩B).',
      body: `For any two events $A$ and $B$:
$$\\Pr(A \\cup B) = \\Pr(A) + \\Pr(B) - \\Pr(A \\cap B).$$

### Why we subtract $\\Pr(A \\cap B)$
$A$ and $B$ may overlap; the overlap has been counted twice in $\\Pr(A) + \\Pr(B)$. Subtract it once to get the probability of $A$ **or** $B$ (or both).

### Mutually exclusive events
Two events are **mutually exclusive** (also: **disjoint**) if they cannot both happen:
$$\\Pr(A \\cap B) = 0.$$

When $A$ and $B$ are mutually exclusive, the addition rule collapses to
$$\\Pr(A \\cup B) = \\Pr(A) + \\Pr(B).$$
This is the **special addition rule** for mutually exclusive events.

### Complement
$\\Pr(A^c) = 1 - \\Pr(A)$, where $A^c$ is everything in the sample space that isn't in $A$.`,
      examples: [
        {
          id: 'ex-overlap',
          statement:
            '$\\Pr(A) = 0.5$, $\\Pr(B) = 0.4$, $\\Pr(A \\cap B) = 0.2$. Find $\\Pr(A \\cup B)$.',
          steps: [
            '$\\Pr(A \\cup B) = \\Pr(A) + \\Pr(B) - \\Pr(A \\cap B) = 0.5 + 0.4 - 0.2$.',
            '$= 0.7$.',
          ],
        },
        {
          id: 'ex-mutually-exclusive',
          statement:
            'A die is rolled. Let $A = \\{2, 4, 6\\}$ (even) and $B = \\{3, 6\\}$ (multiple of 3). Are $A$ and $B$ mutually exclusive? Why?',
          steps: [
            '$A \\cap B = \\{6\\}$ — a single outcome.',
            'So they are not mutually exclusive (there is one overlap).',
          ],
        },
        {
          id: 'ex-mutually-exclusive-2',
          statement:
            'A coin is tossed once. $A = \\{$heads$\\}$ and $B = \\{$tails$\\}$. Are $A$ and $B$ mutually exclusive?',
          steps: [
            'Heads and tails cannot both happen — $\\Pr(A \\cap B) = 0$.',
            'So $A$ and $B$ are mutually exclusive.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-addition-rule',
          difficulty: 'core',
          build: (seed: number) => {
            // Pr(A), Pr(B), Pr(A∩B) chosen so result is a nice decimal.
            const choices: Array<[number, number, number]> = [
              [0.5, 0.4, 0.2], // 0.7
              [0.6, 0.3, 0.1], // 0.8
              [0.7, 0.4, 0.3], // 0.8
              [0.4, 0.3, 0.1], // 0.6
            ]
            const [pa, pb, intersect] = choices[seed % choices.length]
            const union = pa + pb - intersect
            return {
              prompt: `Given $\\Pr(A) = ${pa}$, $\\Pr(B) = ${pb}$, $\\Pr(A \\cap B) = ${intersect}$. Find $\\Pr(A \\cup B)$ as a decimal.`,
              answer: String(union),
              answerType: 'numeric',
              hint: 'Use the addition rule.',
              solution: [
                `$\\Pr(A \\cup B) = ${pa} + ${pb} - ${intersect} = ${union}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-mutually-exclusive',
          difficulty: 'core',
          build: (seed: number) => {
            // Pre-selected pair sums that are always < 1.
            const choices: Array<[number, number]> = [
              [0.2, 0.3],
              [0.1, 0.4],
              [0.3, 0.4],
              [0.2, 0.5],
            ]
            const [pA, pB] = choices[seed % choices.length]
            const ans = pA + pB
            return {
              prompt: `$A$ and $B$ are mutually exclusive with $\\Pr(A) = ${pA}$ and $\\Pr(B) = ${pB}$. Find $\\Pr(A \\cup B)$.`,
              answer: String(ans),
              answerType: 'numeric',
              hint: 'For mutually exclusive events $\\Pr(A \\cup B) = \\Pr(A) + \\Pr(B)$.',
              solution: [
                `$\\Pr(A \\cup B) = ${pA} + ${pB} = ${ans}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-union-overlap',
          difficulty: 'core',
          instance: {
            prompt:
              'For $\\Pr(A) = 0.4$, $\\Pr(B) = 0.5$, $\\Pr(A \\cap B) = 0.2$, find $\\Pr(A \\cup B)$.',
            answer: '0.7',
            answerType: 'numeric',
            hint: 'Addition rule.',
            solution: [
              '$\\Pr(A \\cup B) = 0.4 + 0.5 - 0.2 = 0.7$.',
            ],
          },
        },
      ],
    },

    {
      id: 'tree-diagrams',
      heading: 'Tree diagrams',
      summary: 'Multiply along paths; add branches at the end.',
      body: `A **tree diagram** shows all possible sequences of an experiment. Each branch has its probability, the products along paths are the probabilities of the combined outcomes, and the probabilities at the far-right endpoints sum to $1$.

### Reading rules
- **Branches multiply** along a path.
- **Branches add** to combine alternative paths to the same event.
- Branches from the same node sum to $1$ (one of the listed events is certain to happen at each step).

### Worked example
Toss a coin twice. Branch probabilities: $\\tfrac12, \\tfrac12$ at each toss.
- All four paths: $HH\\ \\tfrac12 \\cdot \\tfrac12 = \\tfrac14$, $HT, TH, TT$ each $\\tfrac14$.
- $\\Pr(\\text{exactly one H}) = \\Pr(HT) + \\Pr(TH) = \\tfrac14 + \\tfrac14 = \\tfrac12$.`,
      examples: [
        {
          id: 'ex-tree-once',
          statement:
            'A bag has 3 red and 2 blue balls. Two are drawn **with replacement**. Draw a tree for the first draw and compute $\\Pr(\\text{RB or BR})$.',
          steps: [
            '$\\Pr(R) = \\tfrac{3}{5}, \\Pr(B) = \\tfrac{2}{5}$.',
            'After replacement, the same probabilities hold for the second draw.',
            '$\\Pr(RB) = \\tfrac{3}{5} \\cdot \\tfrac{2}{5} = \\tfrac{6}{25}$.',
            '$\\Pr(BR) = \\tfrac{2}{5} \\cdot \\tfrac{3}{5} = \\tfrac{6}{25}$.',
            '$\\Pr(\\text{RB or BR}) = \\tfrac{12}{25}$.',
          ],
        },
        {
          id: 'ex-tree-two-coins',
          statement:
            'Two fair coins are tossed. Compute $\\Pr(\\text{exactly one head})$.',
          steps: [
            'Two paths give exactly one head: HT and TH.',
            'Each has probability $\\tfrac{1}{2} \\cdot \\tfrac{1}{2} = \\tfrac{1}{4}$.',
            '$\\Pr(\\text{exactly one H}) = \\tfrac{1}{4} + \\tfrac{1}{4} = \\tfrac{1}{2}$.',
          ],
        },
        {
          id: 'ex-tree-conditional',
          statement:
            'A bag has 3 red, 2 blue. **Without replacement**, what is $\\Pr(\\text{R then B})$?',
          steps: [
            'First red: $\\tfrac{3}{5}$.',
            'Without replacement, 4 balls left, 2 blue: $\\tfrac{2}{4} = \\tfrac{1}{2}$.',
            'Multiply: $\\tfrac{3}{5} \\cdot \\tfrac{1}{2} = \\tfrac{3}{10}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-tree-two-stages',
          difficulty: 'core',
          build: (_seed) => {
            const ans = 0.25
            return {
              prompt: `A fair coin is tossed twice. What is the probability of getting heads both times? Answer as a decimal.`,
              answer: String(ans),
              answerType: 'numeric',
              hint: 'Multiply branch probabilities along the path.',
              solution: [
                'Each branch has probability $\\tfrac12$.',
                '$\\Pr(HH) = \\tfrac12 \\cdot \\tfrac12 = \\tfrac14 = 0.25$.',
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-tree-mixed',
          difficulty: 'core',
          build: (seed: number) => {
            // Bag has r red and b blue. Draw one. P(red) = r/(r+b).
            const r = (seed % 3) + 2 // 2..4
            const b = (seed % 4) + 1 // 1..4
            const total = r + b
            const g = gcd(r, total)
            const num = r / g
            const den = total / g
            return {
              prompt: `A bag has ${r} red and ${b} blue balls. Draw **one** ball. Find $\\Pr(\\text{red})$ as a fraction in lowest terms.`,
              answer: `${num}/${den}`,
              answerType: 'numeric',
              hint: 'Favourable / total.',
              solution: [
                `Favourable: ${r} red balls. Total: ${total} balls.`,
                `$\\Pr(\\text{red}) = \\dfrac{${r}}{${total}} = \\dfrac{${num}}{${den}}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-two-dice-sum-7',
          difficulty: 'core',
          instance: {
            prompt:
              'Two fair dice are rolled. What is $\\Pr(\\text{sum equals } 7)$? Answer as a fraction.',
            answer: '6/36',
            answerType: 'numeric',
            hint: 'There are $6 \\cdot 6 = 36$ equally likely outcomes; how many give sum 7?',
            solution: [
              'Six ordered pairs $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ give sum 7.',
              'So $\\Pr = 6/36 = 1/6$.',
            ],
          },
        },
      ],
    },
  ],
}
