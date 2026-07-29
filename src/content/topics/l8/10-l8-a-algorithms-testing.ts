import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Algebra · l8-a-4 (VC2M8A04).
// Use algorithms and related testing procedures to identify and correct
// errors — for example, in search-and-sort programs and divisibility checks.

export const l8AAlgorithmsTesting: Topic = {
  id: 'l8-a-algorithms-testing',
  unit: 8,
  order: 10,
  title: 'Algorithms and testing procedures',
  blurb:
    'Use algorithms and related testing procedures to identify and correct errors — for example, in search-and-sort programs and divisibility checks.',
  dotPoints: ['l8-a-4'],
  lessons: [
    {
      id: 'what-is-an-algorithm',
      heading: 'What is an algorithm?',
      summary:
        'An algorithm is a finite, ordered set of clear steps that always produces the same result for the same input.',
      body: `An **algorithm** is a precise, step-by-step procedure that takes some input, follows a fixed set of rules, and produces an output. Recipes, driving directions, and long-division procedures are all algorithms.

### Three requirements
A genuine algorithm is:
1. **Unambiguous** — every step is clear and has only one possible meaning.
2. **Finite** — it finishes after a bounded number of steps.
3. **Effective** — each step can actually be carried out.

### Algorithms in maths
- The long-division algorithm.
- The Euclidean algorithm for the greatest common divisor.
- A linear search through a list.
- A sorting procedure like bubble sort.
- A divisibility test (e.g. "is this number divisible by $3$?").

> [!definition] Pseudocode
> **Pseudocode** is a half-English, half-code way of writing an algorithm. It is precise enough to follow but not tied to any programming language.

### A simple example: testing divisibility by 3
> Add the digits of the number. If the result is divisible by 3, the original number is. Repeat if needed.

This is an algorithm because every step is clear, it terminates (the running total shrinks), and it works.`,
      examples: [
        {
          id: 'ex-div3-algorithm',
          statement:
            'Apply the "sum the digits" algorithm to $243$ to check if it is divisible by $3$.',
          steps: [
            'Sum the digits: $2 + 4 + 3 = 9$.',
            'Is $9$ divisible by $3$? Yes.',
            'So $243$ is divisible by $3$.',
            'Check: $243 \\div 3 = 81$ ✓.',
          ],
        },
        {
          id: 'ex-linear-search',
          statement:
            'Apply linear search to find $7$ in the list $[3, 5, 7, 9, 11]$.',
          steps: [
            'Step 1: is the first item $7$? No (it is $3$). Move on.',
            'Step 2: is the second item $7$? No (it is $5$). Move on.',
            'Step 3: is the third item $7$? Yes — stop.',
            'Position: $3$ (or "found").',
          ],
        },
        {
          id: 'ex-euclid',
          statement:
            'Use the Euclidean algorithm to find the GCD of $24$ and $18$.',
          steps: [
            '$24 = 1 \\times 18 + 6$.',
            '$18 = 3 \\times 6 + 0$.',
            'The remainder is $0$, so the GCD is the last non-zero remainder: $6$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-div3',
          difficulty: 'intro',
          instance: {
            prompt:
              'Apply the "sum the digits" divisibility test: is $372$ divisible by $3$? Answer "yes" or "no".',
            answer: 'yes',
            answerType: 'exact',
            hint: 'Sum the digits: $3 + 7 + 2 = 12$.',
            solution: [
              '$3 + 7 + 2 = 12$, and $12$ is divisible by $3$, so yes — $372$ is divisible by $3$.',
            ],
          },
        },
      ],
    },
    {
      id: 'testing-and-debugging',
      heading: 'Testing and debugging algorithms',
      summary:
        'Run the algorithm on chosen inputs; use boundary and edge cases to find errors, then fix and re-test.',
      body: `An algorithm isn't useful if it has **bugs**. **Testing** means running the algorithm on known inputs and checking the output. **Debugging** means finding and fixing errors when the output is wrong.

### What makes a good test case?
- **Typical input**: a regular case, like sorting $[3, 1, 2]$.
- **Boundary case**: an input at the edge of what the algorithm should handle, like an empty list or a list of $1$ element.
- **Edge case**: an unusual but valid input, like a list with duplicates.

### Common bug types
- **Off-by-one**: the loop runs one too many (or too few) times.
- **Wrong operator**: $<$ instead of $\\le$, or $+$ instead of $\\times$.
- **Misinitialised variable**: starting from the wrong value.
- **Wrong step order**: doing step $B$ before step $A$ when the order matters.

### The fix-and-retest loop
1. Run the algorithm on a test case.
2. If the output is wrong, find the line where the first mistake happens.
3. Fix the line.
4. Re-test — both the failing test and the ones that passed before, to make sure the fix didn't break anything.

> [!warning] Watch out
> A test that passes only on "nice" inputs isn't really a test. Push the algorithm with empty lists, single items, duplicates and very large inputs.`,
      examples: [
        {
          id: 'ex-find-bug',
          statement:
            'A student writes an algorithm to find the larger of two numbers: "if $a > b$ then output $a$, otherwise output $b$." Test it on $(a, b) = (3, 5)$ and $(5, 3)$.',
          steps: [
            'Case 1: $3 > 5$? No. Output $b = 5$. Correct.',
            'Case 2: $5 > 3$? Yes. Output $a = 5$. Correct.',
            'Both cases pass — algorithm is correct.',
          ],
        },
        {
          id: 'ex-off-by-one',
          statement:
            'An algorithm is meant to print the numbers $1$ to $5$ but prints $1$ to $4$. The condition is `while n < 5: print(n); n = n + 1`. Where is the bug?',
          steps: [
            'When $n = 5$, the condition $n < 5$ is false, so the loop stops without printing $5$.',
            'Fix: change the condition to `while n <= 5`.',
            'Re-test: $n$ takes values $1, 2, 3, 4, 5$ — all five numbers print.',
          ],
        },
        {
          id: 'ex-divisibility-fix',
          statement:
            'A divisibility test by $5$ returns "yes" for $13$ and "no" for $25$. The algorithm is `if n mod 2 == 0: return yes, else: return no`. Find and fix the bug.',
          steps: [
            'The condition checks the **wrong** divisibility — it tests evenness, not divisibility by $5$.',
            'Fix: `if n mod 5 == 0: return yes, else: return no`.',
            'Re-test: $13 \\bmod 5 = 3$ (no, correct), $25 \\bmod 5 = 0$ (yes, correct).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-div-test',
          difficulty: 'intro',
          instance: {
            prompt:
              'A divisibility test for $4$ uses `n mod 2 == 0`. Is this test correct? Answer "yes" or "no".',
            answer: 'no',
            answerType: 'exact',
            hint: 'The test checks for divisibility by $2$, not $4$.',
            solution: [
              'It checks divisibility by $2$. For example, $6$ passes the test but is not divisible by $4$. The test is incorrect.',
            ],
          },
        },
      ],
    },
  ],
}
