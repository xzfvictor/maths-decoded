import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Number · l8-n-3 (VC2M8N03).
// Convert between fractions and terminating or recurring decimals, using
// digital tools as appropriate.

export const l8NFractionsDecimals: Topic = {
  id: 'l8-n-fractions-decimals',
  unit: 8,
  order: 3,
  title: 'Fractions, terminating and recurring decimals',
  blurb:
    'Convert between fractions and terminating or recurring decimals, using digital tools as appropriate.',
  dotPoints: ['l8-n-3'],
  lessons: [
    {
      id: 'terminating',
      heading: 'Fractions to terminating decimals',
      summary:
        'Divide the numerator by the denominator. If the denominator has only 2 and 5 as prime factors, the decimal terminates.',
      body: `A fraction $\\dfrac{a}{b}$ can be turned into a decimal by **dividing** $a$ by $b$. The decimal will **terminate** if the only prime factors in $b$ are $2$s and $5$s.

### The rule
A fraction $\\dfrac{p}{q}$ (in lowest terms) has a **terminating** decimal expansion if and only if the prime factors of $q$ are all $2$s and $5$s.

- $\\dfrac{3}{4} = 3 \\div 4 = 0.75$ — terminates (only factor is $2$).
- $\\dfrac{7}{20} = 7 \\div 20 = 0.35$ — terminates (factors $2$ and $5$).
- $\\dfrac{1}{3} = 0.333\\ldots$ — does **not** terminate (factor $3$).
- $\\dfrac{5}{6} = 0.8333\\ldots$ — does **not** terminate (factor $3$).

### How to convert by hand
1. Set up the long division: $a \\div b$.
2. Bring down decimal points as needed.
3. Continue until either the remainder is $0$ (terminating) or a remainder repeats (recurring).

> [!definition] Recurring decimal
> A **recurring decimal** has a block of digits that repeats forever. We write it with a bar over the repeating block, e.g. $0.\\overline{3} = 0.333\\ldots$ and $0.1\\overline{6} = 0.1666\\ldots$.`,
      examples: [
        {
          id: 'ex-terminating',
          statement: 'Convert $\\dfrac{3}{8}$ to a decimal.',
          steps: [
            'Divide $3$ by $8$.',
            '$3.000 \\div 8 = 0$ remainder $3$.',
            '$30 \\div 8 = 3$ remainder $6$.',
            '$60 \\div 8 = 7$ remainder $4$.',
            '$40 \\div 8 = 5$ remainder $0$.',
            'Result: $0.375$.',
          ],
        },
        {
          id: 'ex-terminates-check',
          statement:
            'Does $\\dfrac{9}{40}$ have a terminating decimal? If so, write it.',
          steps: [
            '$40 = 2^3 \\times 5$ — only $2$s and $5$s, so yes, it terminates.',
            '$9 \\div 40$: $90 \\div 40 = 2$ remainder $10$, $100 \\div 40 = 2$ remainder $20$, $200 \\div 40 = 5$ remainder $0$.',
            'Result: $0.225$.',
          ],
        },
        {
          id: 'ex-non-terminating',
          statement: 'Convert $\\dfrac{2}{3}$ to a decimal. Does it terminate?',
          steps: [
            'Denominator $3$ is not just $2$s and $5$s, so the decimal will recur.',
            '$2 \\div 3 = 0$ remainder $2$. Then $20 \\div 3 = 6$ remainder $2$ again — the pattern locks in.',
            'Result: $0.\\overline{6}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-terminate',
          difficulty: 'intro',
          instance: {
            prompt: 'Convert $\\dfrac{7}{8}$ to a decimal.',
            answer: '0.875',
            answerType: 'numeric',
            hint: 'Divide $7$ by $8$ using long division.',
            solution: [
              '$7 \\div 8 = 0$ r $7$, $70 \\div 8 = 8$ r $6$, $80 \\div 8 = 10$ r $0$. So $0.875$.',
            ],
          },
        },
      ],
    },
    {
      id: 'recurring',
      heading: 'Recurring decimals back to fractions',
      summary:
        'Set x equal to the decimal, multiply by 10^k where k is the block length, then subtract to clear the recurring block.',
      body: `A recurring decimal is also a fraction in disguise. To convert it back, use the **multiply and subtract** trick.

### The method
Let $x$ be the recurring decimal.

1. Multiply $x$ by $10^k$, where $k$ is the length of the repeating block. This shifts the block to the left of the decimal point.
2. Multiply $x$ by $10^j$ for the **non-repeating** part (if any), so the block lines up after the decimal point.
3. Subtract to clear the recurring part.
4. Solve for $x$.

### Simple case: $0.\\overline{a}$
- Let $x = 0.\\overline{a}$.
- $10x = a.\\overline{a}$.
- $10x - x = a \\Rightarrow 9x = a \\Rightarrow x = \\dfrac{a}{9}$.

So $0.\\overline{3} = \\dfrac{3}{9} = \\dfrac{1}{3}$, and $0.\\overline{7} = \\dfrac{7}{9}$.

> [!warning] Watch out
> Always reduce the fraction. $0.\\overline{3} = \\dfrac{3}{9} = \\dfrac{1}{3}$, not $\\dfrac{3}{9}$.`,
      examples: [
        {
          id: 'ex-recurring-simple',
          statement: 'Convert $0.\\overline{6}$ to a fraction in lowest terms.',
          steps: [
            'Let $x = 0.\\overline{6}$.',
            'Multiply by $10$: $10x = 6.\\overline{6}$.',
            'Subtract: $10x - x = 6 \\Rightarrow 9x = 6$.',
            'Solve: $x = \\dfrac{6}{9} = \\dfrac{2}{3}$.',
          ],
        },
        {
          id: 'ex-recurring-block',
          statement: 'Convert $0.\\overline{45}$ to a fraction in lowest terms.',
          steps: [
            'Let $x = 0.\\overline{45}$. The block has length $2$.',
            'Multiply by $100$: $100x = 45.\\overline{45}$.',
            'Subtract: $100x - x = 45 \\Rightarrow 99x = 45$.',
            'Solve: $x = \\dfrac{45}{99} = \\dfrac{5}{11}$ (dividing top and bottom by $9$).',
          ],
        },
        {
          id: 'ex-with-prefix',
          statement: 'Convert $0.1\\overline{6}$ to a fraction.',
          steps: [
            'The non-repeating part has $1$ digit, the block has $1$ digit.',
            'Let $x = 0.1\\overline{6}$.',
            '$10x = 1.\\overline{6}$, and $100x = 16.\\overline{6}$.',
            'Subtract: $100x - 10x = 16 - 1 \\Rightarrow 90x = 15$.',
            'Solve: $x = \\dfrac{15}{90} = \\dfrac{1}{6}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-recurring',
          difficulty: 'intro',
          instance: {
            prompt:
              'Convert $0.\\overline{7}$ to a fraction in lowest terms. Type as "a/b".',
            answer: '7/9',
            answerType: 'exact',
            hint: 'Let $x = 0.\\overline{7}$, then $10x - x = 7$.',
            solution: [
              '$10x - x = 7 \\Rightarrow 9x = 7 \\Rightarrow x = \\dfrac{7}{9}$.',
            ],
          },
        },
      ],
    },
  ],
}
