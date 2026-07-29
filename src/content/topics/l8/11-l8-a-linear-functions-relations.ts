import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Algebra · l8-a-5 (VC2M8A05).
// Experiment with linear functions and relations using digital tools, making
// and testing conjectures and generalising emerging patterns.

export const l8ALinearFunctionsRelations: Topic = {
  id: 'l8-a-linear-functions-relations',
  unit: 8,
  order: 11,
  title: 'Linear functions and relations',
  blurb:
    'Experiment with linear functions and relations using digital tools, making and testing conjectures and generalising emerging patterns.',
  dotPoints: ['l8-a-5'],
  lessons: [
    {
      id: 'making-conjectures',
      heading: 'Making and testing conjectures',
      summary:
        'Guess the rule from a pattern, then test it on new data; a single counter-example is enough to disprove.',
      body: `A **conjecture** is a guess that something is true. In maths, you don't just make the guess — you **test** it. A conjecture that survives many tests becomes a theorem. A single **counter-example** is enough to show a conjecture is **false**.

### How to make a conjecture
1. Look at a pattern (a list, a table, a graph).
2. Guess the rule that connects the inputs to the outputs.
3. State the guess clearly: "For all $x$, I think $y = \\ldots$".
4. Test the guess on new data.

### Where linear functions appear
Whenever a quantity grows (or shrinks) by the **same amount** each step, the relation is linear. The pattern is:
- Step from $x$ to $x + 1$ adds the same $m$ to $y$.
- Going back $n$ steps subtracts $n \\times m$ from $y$.

### Using a digital tool
A graphing app or spreadsheet lets you change the values of $m$ and $c$ and watch the line move. This is the fastest way to form and test a conjecture about what each part does.

> [!definition] Conjecture
> A **conjecture** is a statement believed to be true but not yet proved. To accept it, prove it. To reject it, find a single counter-example.`,
      examples: [
        {
          id: 'ex-from-table',
          statement:
            'A table shows $x = 1, 2, 3, 4$ giving $y = 5, 8, 11, 14$. Conjecture the rule.',
          steps: [
            'Differences: $8 - 5 = 3$, $11 - 8 = 3$, $14 - 11 = 3$. Constant difference of $3$ — linear.',
            'Conjecture: $y = 3x + b$ for some $b$.',
            'Plug in $x = 1, y = 5$: $5 = 3(1) + b \\Rightarrow b = 2$.',
            'Conjecture: $y = 3x + 2$.',
            'Test on $x = 5$: $y = 3(5) + 2 = 17$. New $y$-values would be $17$.',
          ],
        },
        {
          id: 'ex-falsify',
          statement:
            'A student conjectures "all prime numbers are odd." Test it.',
          steps: [
            'The first few primes are $2, 3, 5, 7, 11, \\ldots$',
            '$2$ is prime and is even.',
            'Counter-example found — the conjecture is false.',
          ],
        },
        {
          id: 'ex-prove',
          statement:
            'Conjecture: "if $n$ is even, then $n^2$ is even."',
          steps: [
            'Test: $n = 2 \\Rightarrow n^2 = 4$ (even) ✓. $n = 4 \\Rightarrow 16$ (even) ✓.',
            'Algebra: $n = 2k$ for some integer $k$. Then $n^2 = (2k)^2 = 4k^2 = 2(2k^2)$, which is even.',
            'No counter-example exists, and the algebra proves it. The conjecture is true.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-conjecture',
          difficulty: 'intro',
          instance: {
            prompt:
              'A table shows $x = 0, 1, 2, 3$ giving $y = 4, 7, 10, 13$. Which linear rule fits?',
            answer: 'y=3x+4',
            answerType: 'exact',
            hint: 'Differences of $3$ suggest $m = 3$. Use $y = 3x + b$ and one data point to find $b$.',
            solution: [
              'Differences are $3$ each time, so $m = 3$. Plug in $x = 0, y = 4$: $b = 4$. So $y = 3x + 4$.',
            ],
          },
        },
      ],
    },
    {
      id: 'generalising-patterns',
      heading: 'Generalising patterns to formulas',
      summary:
        'Replace specific numbers with variables; the pattern that worked for the examples works for every case.',
      body: `When a pattern works for a few specific cases, the next step is to **generalise** it: turn the numbers into variables and write a single rule that covers every case.

### The generalising habit
1. Compute a few specific cases.
2. Look for the pattern (constant difference, constant ratio, or another rule).
3. Replace the specific numbers with letters to write a **general formula**.

### Two common patterns
- **Constant difference** → linear: $y = mx + c$.
- **Constant ratio** → exponential: $y = a \\times r^x$ (studied in later years).

### Why it matters
A general formula lets you predict the $100$th or the $-7$th term without computing every case in between.

> [!warning] Watch out
> Two or three examples aren't always enough. The first few terms of $1, 2, 4, 8, \\ldots$ look linear, but the actual rule is exponential: $2^{n-1}$.

### Checking with a digital tool
A graphing app confirms the generalisation: plot both the specific points and the general curve, and check they line up.`,
      examples: [
        {
          id: 'ex-arithmetic',
          statement:
            'Find the general formula for the sequence $3, 7, 11, 15, 19, \\ldots$',
          steps: [
            'Differences: $4$ each time. Linear.',
            'Conjecture: $a_n = 4n + b$.',
            'Use $n = 1, a_1 = 3$: $3 = 4 + b \\Rightarrow b = -1$.',
            'General formula: $a_n = 4n - 1$.',
            'Test: $n = 5$ gives $19$ ✓.',
          ],
        },
        {
          id: 'ex-tiling',
          statement:
            'A pattern of squares is built row by row: row $1$ has $2$ tiles, row $2$ has $4$, row $3$ has $6$. Find a general formula for the number of tiles in row $n$.',
          steps: [
            'Differences: $2$ each time. Linear.',
            'Conjecture: $T_n = 2n + b$.',
            'Use $n = 1, T_1 = 2$: $2 = 2 + b \\Rightarrow b = 0$.',
            'General formula: $T_n = 2n$.',
            'Test: row $4$ should have $8$ tiles. $2(4) = 8$ ✓.',
          ],
        },
        {
          id: 'ex-perimeter',
          statement:
            'A rectangle has length $5$ cm more than its width $w$. Find a general formula for its perimeter.',
          steps: [
            'Length $= w + 5$.',
            'Perimeter $= 2(\\text{length}) + 2(\\text{width}) = 2(w + 5) + 2w = 4w + 10$.',
            'So the general formula is $P = 4w + 10$.',
            'Check $w = 3$: rectangle is $3$ by $8$, perimeter $= 22$. $4(3) + 10 = 22$ ✓.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-generalise',
          difficulty: 'intro',
          instance: {
            prompt:
              'A sequence starts $5, 9, 13, 17, \\ldots$ Find a general formula for the $n$-th term $a_n$ (as an expression like "4n+1").',
            answer: '4n+1',
            answerType: 'exact',
            hint: 'Differences are $4$. Use $a_n = 4n + b$ and the first term to find $b$.',
            solution: [
              'Differences are $4$ each time, so $m = 4$. Using $a_1 = 5$: $5 = 4(1) + b \\Rightarrow b = 1$. So $a_n = 4n + 1$.',
            ],
          },
        },
      ],
    },
  ],
}
