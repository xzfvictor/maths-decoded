import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Algebra · VC2M10A06.
// Implement algorithms that use data structures using pseudocode or a
// general purpose programming language.

export const algebraAlgorithms: Topic = {
  id: 'm10-algebra-algorithms',
  unit: 10,
  order: 12,
  title: 'Algorithms and data structures',
  blurb:
    'Use arrays, matrices and pointers in pseudocode to implement sequences of transformations on data.',
  dotPoints: ['m10-a-6'],

  lessons: [
    {
      id: 'arrays-matrices',
      heading: 'Arrays and matrices',
      summary: 'Arrays store lists; matrices store 2-D tables and represent transformations.',
      body: `An **algorithm** is a finite, ordered list of unambiguous steps that solves a problem. Three data structures appear most often at this level.

### 1. Arrays
A list of values at consecutive indices: \`a[0], a[1], ..., a[n-1]\`. Use a loop to traverse. Useful for sequences of numbers, strings, or objects.

### 2. Matrices (2-D arrays)
A grid \`m[i][j]\` of rows \`i\` and columns \`j\`. Useful for grids, tables, and **transformations**:
- Translation: $\\begin{pmatrix} 1 & 0 & t_x \\\\ 0 & 1 & t_y \\end{pmatrix}$ shifts the plane by $(t_x, t_y)$.
- Rotation / reflection: matrices multiply points to rotate or reflect them.

### 3. Pointers
A pointer stores the address of another element. Linked lists, trees, and graphs all rely on pointers. At this level, you mostly need to understand that **a pointer points to** something — reading or writing through it changes that something.`,
      examples: [
        {
          id: 'ex-translate',
          statement:
            'A point $P = (x, y)$ is translated by $(3, -2)$. What are its new coordinates?',
          steps: [
            'Translation: add to each coordinate.',
            '$x_{new} = x + 3$, $y_{new} = y - 2$.',
            "So $P_{new} = (x + 3, y - 2)$.",
          ],
        },
        {
          id: 'ex-array-sum',
          statement:
            "Pseudocode:\n```\nSET total TO 0\nFOR i FROM 0 TO 4\n  SET total TO total + a[i]\nEND FOR\n```\nFor $a = [3, 5, 7, 2, 4]$, what is the final value of \`total\`?",
          steps: [
            'Add all five values: $3 + 5 + 7 + 2 + 4 = 21$.',
            "Final value: $21$.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-translate',
          difficulty: 'intro',
          instance: {
            prompt:
              'The point $(2, 5)$ is translated by $(4, -3)$. What is the new $x$-coordinate?',
            answer: '6',
            answerType: 'numeric',
            hint: 'Add the translation $x$-component.',
            solution: [
              '$2 + 4 = 6$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-translate-y',
          difficulty: 'intro',
          instance: {
            prompt:
              'The point $(2, 5)$ is translated by $(4, -3)$. What is the new $y$-coordinate?',
            answer: '2',
            answerType: 'numeric',
            hint: 'Add the translation $y$-component.',
            solution: [
              '$5 + (-3) = 2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'pseudocode-loops',
      heading: 'Pseudocode and loops',
      summary: 'Plain language with assignment, loops and conditionals — the building blocks of any algorithm.',
      body: `**Pseudocode** lets you describe an algorithm without committing to a particular programming language's syntax. The usual building blocks:

### Assignment
\`SET x TO 5\` — store a value in a variable.

### Loops
\`FOR i FROM 1 TO 10\` — repeat once per value of $i$.
\`WHILE condition DO ... END WHILE\` — repeat as long as something is true.

### Conditionals
\`IF condition THEN ... ELSE ... END IF\` — branch on a true/false test.

### Tracing
To follow an algorithm, keep a table of variables' values as each line runs. Update each variable in order.`,
      examples: [
        {
          id: 'ex-loop',
          statement:
            'What does this pseudocode compute?\n\n```\nSET total TO 0\nFOR i FROM 1 TO 10\n  SET total TO total + i\nEND FOR\n```',
          steps: [
            "It adds the integers from 1 to 10.",
            "Result: $1 + 2 + 3 + \\dots + 10 = 55$.",
          ],
        },
        {
          id: 'ex-conditional',
          statement:
            "What does this pseudocode compute?\n\n```\nSET m TO 0\nFOR i FROM 1 TO 5\n  IF a[i] > m THEN\n    SET m TO a[i]\n  END IF\nEND FOR\n```",
          steps: [
            'It walks through the array, updating \`m\` whenever a larger value is found.',
            'At the end, \`m\` is the **maximum** value in the array.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sum-to-100',
          difficulty: 'core',
          instance: {
            prompt:
              "What does the following pseudocode compute? Type one word: 'sum', 'product', 'max', or 'min'.\n\n```\nSET total TO 0\nFOR i FROM 1 TO 100\n  SET total TO total + i\nEND FOR\n```",
            answer: 'sum',
            answerType: 'exact',
            hint: 'Each iteration adds the next $i$ to a running total.',
            solution: [
              'Running sum of integers $1$ to $100$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-product',
          difficulty: 'core',
          instance: {
            prompt:
              "What does this pseudocode compute? Type one word: 'sum', 'product', 'max', or 'min'.\n\n```\nSET total TO 1\nFOR i FROM 1 TO 6\n  SET total TO total * i\nEND FOR\n```",
            answer: 'product',
            answerType: 'exact',
            hint: 'Each iteration multiplies the running value by $i$.',
            solution: [
              '$1 \\cdot 2 \\cdot 3 \\cdot 4 \\cdot 5 \\cdot 6 = 720$. A running product.',
            ],
          },
        },
      ],
    },
  ],
}