import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Probability · l8-p-2 (VC2M8P02).
// Determine all possible outcome combinations for 2 events, using two-way
// tables, tree diagrams and Venn diagrams, and use these to determine
// probabilities of specific events in practical situations.

export const l8PTwoEventOutcomes: Topic = {
  id: 'l8-p-two-event-outcomes',
  unit: 8,
  order: 28,
  title: 'Outcome combinations for two events',
  blurb:
    'Determine all possible outcome combinations for two events using two-way tables, tree diagrams and Venn diagrams, and use these to find probabilities in practical situations.',
  dotPoints: ['l8-p-2'],
  lessons: [
    {
      id: 'two-way-tables',
      heading: 'Two-way tables for two events',
      summary:
        'Lay out two categorical variables in a grid; the four cells cover every possible combination.',
      body: `A **two-way table** cross-tabulates two categorical variables. With two events $A$ and $B$, the four cells cover **every** possible outcome combination.

### The four cells
For two events $A$ and $B$:
- $A \\cap B$: both happen.
- $A \\cap B'$: $A$ happens, $B$ does not.
- $A' \\cap B$: $A$ does not, $B$ happens.
- $A' \\cap B'$: neither happens.

The four cells together account for every outcome. Their probabilities (or counts) sum to $1$ (or to the grand total):

$$\\Pr(A \\cap B) + \\Pr(A \\cap B') + \\Pr(A' \\cap B) + \\Pr(A' \\cap B') = 1.$$

### Reading probabilities
From the four cells you can compute anything about $A$ or $B$ or both:
- $\\Pr(A) = \\Pr(A \\cap B) + \\Pr(A \\cap B')$ (sum the $A$ row).
- $\\Pr(B) = \\Pr(A \\cap B) + \\Pr(A' \\cap B)$ (sum the $B$ column).
- $\\Pr(A \\cap B)$ = the joint cell.
- $\\Pr(\\text{neither}) = \\Pr(A' \\cap B')$ = the bottom-right cell.

### Special case: mutually exclusive
Two events are **mutually exclusive** when they cannot both happen, so $\\Pr(A \\cap B) = 0$. In a two-way table the joint cell is empty.`,
      examples: [
        {
          id: 'ex-build',
          statement:
            'In a class of $30$, $12$ students play sport ($S$) and $8$ play music ($M$). $4$ do both. How many do neither?',
          steps: [
            'Joint $S \\cap M = 4$.',
            'Sport only: $12 - 4 = 8$.',
            'Music only: $8 - 4 = 4$.',
            'Total doing at least one: $4 + 8 + 4 = 16$.',
            'Neither: $30 - 16 = 14$.',
          ],
        },
        {
          id: 'ex-read-prob',
          statement:
            'In a two-way table, $\\Pr(A \\cap B) = 0.2$, $\\Pr(A \\cap B\') = 0.3$, $\\Pr(A\' \\cap B) = 0.1$. What is $\\Pr(A\' \\cap B\')$?',
          steps: [
            'The four cells sum to $1$.',
            '$\\Pr(A\' \\cap B\') = 1 - (0.2 + 0.3 + 0.1) = 1 - 0.6 = 0.4$.',
          ],
        },
        {
          id: 'ex-mutually-exclusive',
          statement:
            'Two events are **mutually exclusive**. In a two-way table, which cell must be empty?',
          steps: [
            'Mutually exclusive = cannot both happen.',
            'The $A \\cap B$ cell is the "both happen" cell — it must be $0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-fill-cell',
          difficulty: 'intro',
          instance: {
            prompt:
              'In a two-way table the four cells sum to $1$. Three cells are $0.1$, $0.4$, $0.3$. What is the fourth cell?',
            answer: '0.2',
            answerType: 'numeric',
            hint: 'Sum to $1$.',
            solution: [
              '$0.1 + 0.4 + 0.3 + x = 1 \\Rightarrow x = 0.2$.',
            ],
          },
        },
      ],
    },
    {
      id: 'tree-and-venn',
      heading: 'Tree diagrams & Venn diagrams',
      summary:
        'Trees list every ordered outcome step by step; Venn diagrams highlight the overlap between two events.',
      body: `For two events, a **tree diagram** or a **Venn diagram** can show every outcome combination — often more visually than a table.

### Tree diagram
A tree has **two sets of branches**: one for $A$ (or not $A$) at the first step, one for $B$ (or not $B$) at the second. The four endpoints correspond exactly to the four cells of a two-way table.

- Multiply **along** a branch to get the probability of that path.
- Add **across** paths to combine alternatives.

### Venn diagram
Two overlapping circles inside a rectangle of "all outcomes". The four regions are:
- Inside $A$ only.
- Inside $B$ only.
- Inside both $A$ and $B$.
- Outside both circles (neither).

### Choosing a representation
- **Two-way table**: best for **counts** of categorical data.
- **Tree diagram**: best for **step-by-step** experiments and multiplying probabilities along paths.
- **Venn diagram**: best for emphasising the **overlap** between two events (mutually exclusive ↔ no overlap).`,
      examples: [
        {
          id: 'ex-tree',
          statement:
            'A coin is tossed, then a die is rolled. How many possible outcomes are there? List one example.',
          steps: [
            'Coin: $2$ outcomes (H, T). Die: $6$ outcomes (1–6).',
            'Total: $2 \\times 6 = 12$ outcomes.',
            'Example outcome: (H, 4).',
          ],
        },
        {
          id: 'ex-venn',
          statement:
            'In a class, $18$ students play sport, $10$ play music, $4$ play both. How many play **only** music?',
          steps: [
            'Music total = $10$. Both = $4$.',
            'Music only = $10 - 4 = 6$.',
          ],
        },
        {
          id: 'ex-mutually-exclusive-venn',
          statement:
            'On a Venn diagram, what does it look like when two events are mutually exclusive?',
          steps: [
            'The two circles do **not overlap** — they share no common region.',
            'Their interiors are disjoint; the joint cell is empty.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-tree-count',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two coins are tossed. How many possible outcomes are there? (Enter the number.)',
            answer: '4',
            answerType: 'numeric',
            hint: 'Each coin has $2$ outcomes — HH, HT, TH, TT.',
            solution: [
              'HH, HT, TH, TT — that is $4$ outcomes.',
            ],
          },
        },
      ],
    },
  ],
}