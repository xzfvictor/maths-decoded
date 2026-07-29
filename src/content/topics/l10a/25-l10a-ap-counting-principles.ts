import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Probability · l10a-ap-1 (VC2M10AP01).
// Counting principles and factorial notation.

export const l10aApCountingPrinciples: Topic = {
  id: 'l10a-ap-counting-principles',
  unit: '10A',
  order: 25,
  title: 'Counting principles and factorial notation',
  blurb:
    'Explore counting principles and factorial notation as efficient ways to count in multiplicative contexts, including calculations of probabilities.',
  dotPoints: ['l10a-ap-1'],

  lessons: [
    {
      id: 'multiplication-addition',
      heading: 'Multiplication & addition principles',
      summary: 'Sequential choices multiply; mutually exclusive choices add.',
      body: `Two counting principles cover most of what you'll see at Year 10A level.

### Multiplication principle
If a task has $k$ stages and stage $i$ has $n_i$ choices, the total number of ways to complete the task is:

$$n_1 \\times n_2 \\times \\dots \\times n_k$$

### Addition principle
If two (or more) tasks are **mutually exclusive** (you do exactly one), the total is the **sum** of the counts:

$$n_1 + n_2 + \\dots + n_k$$

### When to use which
- **"and then"** (sequential) → **multiply**.
- **"or"** (mutually exclusive) → **add**.

### Worked shape
"How many outfits?" — $3$ shirts $\\times 4$ pants = $12$ outfits (multiplication).
"Travel by bus or train?" — $5$ buses $+ 8$ trains = $13$ options (addition).`,
      examples: [
        {
          id: 'ex-outfits',
          statement:
            'A wardrobe has $4$ shirts, $3$ pants and $2$ pairs of shoes. How many complete outfits (one of each)?',
          steps: [
            'Sequential choices: shirt $\\times$ pants $\\times$ shoes.',
            '$4 \\times 3 \\times 2 = 24$ outfits.',
          ],
        },
        {
          id: 'ex-pin',
          statement:
            'A 4-digit PIN has each digit from $0$–$9$. How many possible PINs?',
          steps: [
            'Each of 4 positions: $10$ choices.',
            '$10 \\times 10 \\times 10 \\times 10 = 10^4 = 10000$ PINs.',
          ],
        },
        {
          id: 'ex-menu',
          statement:
            'A cafe sells $6$ hot drinks and $4$ cold drinks. A customer buys one drink. How many options?',
          steps: [
            'Hot or cold — mutually exclusive.',
            '$6 + 4 = 10$ options.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-plate',
          difficulty: 'intro',
          instance: {
            prompt:
              'A licence plate has $3$ letters followed by $3$ digits (each from $0$–$9$). How many plates are possible?',
            answer: '17576000',
            answerType: 'numeric',
            hint: 'Multiply $26 \\times 26 \\times 26 \\times 10 \\times 10 \\times 10$.',
            solution: [
              'Letters: $26^3 = 17576$. Digits: $10^3 = 1000$.',
              'Total: $17576 \\times 1000 = 17576000$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-or-and',
          difficulty: 'core',
          instance: {
            prompt:
              'A restaurant offers $5$ starters, $8$ mains and $3$ desserts. How many three-course meals (one of each)?',
            answer: '120',
            answerType: 'numeric',
            hint: 'Three sequential choices: multiply.',
            solution: [
              '$5 \\times 8 \\times 3 = 120$ meals.',
            ],
          },
        },
      ],
    },

    {
      id: 'factorial-permutations',
      heading: 'Factorials & permutations',
      summary: '$n! = n \\times (n-1) \\times \\dots \\times 1$; permutations count orderings.',
      body: `**Factorial notation** is shorthand for repeated multiplication when we count arrangements.

### Definition
$$n! = n \\times (n - 1) \\times (n - 2) \\times \\dots \\times 2 \\times 1$$

By convention $0! = 1$.

### Permutations
The number of ways to arrange $r$ items **in order** from $n$ distinct items (no repetition):

$$^nP_r = \\dfrac{n!}{(n - r)!}$$

The number of ways to arrange all $n$ items is just $n!$.

### Connection to probability
If every arrangement is equally likely, the probability of any specific one is $1 / n!$. For a specific ordered subset of $r$, it's $1 / \,^nP_r$.

### Examples
- $5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120$.
- $^{10}P_3 = 10 \\times 9 \\times 8 = 720$ (10 choose 3, then arrange).`,
      examples: [
        {
          id: 'ex-factorial',
          statement:
            'Compute $6!$.',
          steps: [
            '$6! = 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1 = 720$.',
          ],
        },
        {
          id: 'ex-permutation',
          statement:
            'In how many ways can the first three places in a race of $8$ runners be filled (no ties)?',
          steps: [
            '$^8P_3 = \\dfrac{8!}{5!} = 8 \\times 7 \\times 6 = 336$.',
          ],
        },
        {
          id: 'ex-prob-factorial',
          statement:
            'A 5-letter "word" is formed by shuffling the letters A, B, C, D, E at random. What is the probability it spells "CABDE"?',
          steps: [
            'Total arrangements $= 5! = 120$, all equally likely.',
            'Just one of them is "CABDE".',
            '$\\Pr = 1/120$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-factorial-7',
          difficulty: 'intro',
          instance: {
            prompt:
              'Compute $7!$.',
            answer: '5040',
            answerType: 'numeric',
            hint: '$7! = 7 \\times 6 \\times 5 \\times 4 \\times 3 \\times 2 \\times 1$.',
            solution: [
              '$7! = 5040$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-perm-9-4',
          difficulty: 'core',
          instance: {
            prompt:
              'How many ways can $4$ different books be arranged on a shelf if chosen from $9$ distinct books (so $r = 4$ from $n = 9$)?',
            answer: '3024',
            answerType: 'numeric',
            hint: '$^9P_4 = 9 \\times 8 \\times 7 \\times 6$.',
            solution: [
              '$^9P_4 = 9 \\times 8 \\times 7 \\times 6 = 3024$.',
            ],
          },
        },
      ],
    },
  ],
}