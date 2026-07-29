import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Algebra · l7-a-2 (VC2M7A02).
// Apply the associative, commutative and distributive laws to aid mental
// and written computation, and formulate algebraic expressions using
// constants, variables, operations and brackets.

export const l7ALawsExpressions: Topic = {
  id: 'l7-a-laws-expressions',
  unit: 7,
  order: 12,
  title: 'Laws and algebraic expressions',
  blurb:
    'Apply the associative, commutative and distributive laws in computation, and write algebraic expressions with constants, variables, operations and brackets.',
  dotPoints: ['l7-a-2'],
  lessons: [
    {
      id: 'commutative-and-associative',
      heading: 'Commutative and associative laws',
      summary:
        'Reorder and regroup addition and multiplication without changing the result.',
      body: `Two simple rules let you rearrange a calculation to make it easier in your head.

### Commutative law
You can **swap the order** of an addition or multiplication and still get the same answer.

- Addition: $a + b = b + a$. So $3 + 17 = 17 + 3$.
- Multiplication: $a \\times b = b \\times a$. So $4 \\times 25 = 25 \\times 4$.

Subtraction and division are **not** commutative: $5 - 3 \\ne 3 - 5$.

### Associative law
You can **regroup** an addition or multiplication and the answer stays the same.

- Addition: $(a + b) + c = a + (b + c)$. So $(2 + 8) + 35 = 2 + (8 + 35)$.
- Multiplication: $(a \\times b) \\times c = a \\times (b \\times c)$. So $(4 \\times 5) \\times 7 = 4 \\times (5 \\times 7)$.

> [!definition] Mental-math trick
> Reorder and regroup so the numbers pair up nicely: $25 + 17 + 75 = 25 + 75 + 17 = 100 + 17 = 117$.

### Why these matter
With one tricky number, swapping and regrouping turns a hard mental sum into an easy one. The same rules carry over to algebra: $2x + 7y + 8x = 2x + 8x + 7y = 10x + 7y$.`,
      examples: [
        {
          id: 'ex-mental-add',
          statement: 'Compute $25 + 67 + 75$ using the commutative and associative laws.',
          steps: [
            'Spot the friendly pair: $25$ and $75$ make $100$.',
            'Reorder: $25 + 75 + 67$.',
            'Regroup: $(25 + 75) + 67 = 100 + 67$.',
            'Result: $167$.',
          ],
        },
        {
          id: 'ex-mental-multiply',
          statement: 'Compute $4 \\times 17 \\times 25$ in your head.',
          steps: [
            'Reorder: $4 \\times 25 \\times 17$.',
            'Regroup: $(4 \\times 25) \\times 17 = 100 \\times 17$.',
            'Result: $1700$.',
          ],
        },
        {
          id: 'ex-algebra-rearrange',
          statement: 'Simplify $3x + 5 + 7x + 2$ by collecting like terms.',
          steps: [
            'Reorder so like terms sit next to each other: $3x + 7x + 5 + 2$.',
            'Group: $(3x + 7x) + (5 + 2)$.',
            'Combine: $10x + 7$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-mental-add',
          difficulty: 'intro',
          instance: {
            prompt: 'Use the commutative and associative laws to compute $50 + 27 + 50$.',
            answer: '127',
            answerType: 'numeric',
            hint: 'Pair the two $50$s first.',
            solution: [
              '$50 + 50 + 27 = 100 + 27 = 127$.',
            ],
          },
        },
      ],
    },

    {
      id: 'distributive-law',
      heading: 'The distributive law and writing expressions',
      summary:
        'Distribute multiplication over addition to expand, or factor out a common piece to contract.',
      body: `The **distributive law** is the bridge between multiplication and addition.

### The law
$$a(b + c) = ab + ac.$$

You can **expand** a bracket by multiplying each term inside, or **factor** by pulling a common piece out of every term.

### Expanding (multiply out)
- $3(x + 4) = 3x + 12$.
- $5(2y - 7) = 10y - 35$.

### Factoring (share a common factor)
- $6x + 9 = 3(2x + 3)$.
- $4a + 10b = 2(2a + 5b)$.

> [!warning] Watch out
> Only **multiply** distributes over addition. $a + (b \\times c)$ is not the same as $(a + b) \\times (a + c)$.

### Writing expressions from words
Translating prose to algebra is part of the dot point. Read the words and pick the operation:

- "5 more than $x$" → $x + 5$.
- "3 less than $y$" → $y - 3$.
- "twice $n$" → $2n$.
- "half of $m$" → $\\dfrac{m}{2}$.
- "the product of $p$ and $q$" → $pq$.`,
      examples: [
        {
          id: 'ex-expand',
          statement: 'Expand $4(x + 3)$.',
          steps: [
            'Multiply $4$ by each term inside the bracket.',
            '$4 \\times x = 4x$, $4 \\times 3 = 12$.',
            'Result: $4x + 12$.',
          ],
        },
        {
          id: 'ex-factor',
          statement: 'Factor $15x - 10$.',
          steps: [
            'Find the common factor of $15$ and $10$: $5$.',
            'Pull it out: $5(3x - 2)$.',
            'Check: $5 \\times 3x = 15x$, $5 \\times (-2) = -10$ ✓.',
          ],
        },
        {
          id: 'ex-words-to-expression',
          statement:
            'A taxi charges $\\$2$ flag-fall plus $\\$1.50$ per km. Write an expression for the cost of a trip of $k$ km.',
          steps: [
            'Cost = flag-fall + (rate × km).',
            'Substitute: $C = 2 + 1.5k$.',
            'This is the formula $\\$2 + \\$1.50 \\times k$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-expand-bracket',
          difficulty: 'intro',
          instance: {
            prompt: 'Expand $5(x + 4)$. Type as an expression like 5x+20.',
            answer: '5x+20',
            answerType: 'polynomial',
            hint: 'Multiply $5$ by each term inside the brackets.',
            solution: [
              '$5 \\times x = 5x$, $5 \\times 4 = 20$. So $5(x + 4) = 5x + 20$.',
            ],
          },
        },
      ],
    },
  ],
}
