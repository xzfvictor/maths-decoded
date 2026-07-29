import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Number · l10a-an-1 (VC2M10AN01).
// Define rational and irrational numbers and perform operations with
// surds and fractional indices.

export const l10aAnSurds: Topic = {
  id: 'l10a-an-surds',
  unit: '10A',
  order: 1,
  title: 'Surds and fractional indices',
  blurb:
    'Define rational and irrational numbers and perform operations with surds and fractional indices.',
  dotPoints: ['l10a-an-1'],

  lessons: [
    {
      id: 'rational-irrational',
      heading: 'Rational and irrational numbers',
      summary: 'Real numbers split into rational (ratios of integers) and irrational (everything else, e.g. square roots of non-squares).',
      body: `Every real number on the number line is either **rational** or **irrational**. Recognising which is which is the first step in working confidently with surds.

### Rational numbers
A **rational number** is anything that can be written as $\\dfrac{p}{q}$ where $p$ and $q$ are integers with $q \\ne 0$. In decimal form, a rational number either **terminates** ($0.5$) or **repeats** ($0.333\\dots$).

### Irrational numbers
An **irrational number** cannot be written as $\\dfrac{p}{q}$. Its decimal goes on forever **without a repeating block**. The most famous irrational numbers are the square roots of non-square integers: $\\sqrt{2}, \\sqrt{3}, \\sqrt{5}, \\ldots$

### Proof idea: $\\sqrt{2}$ is irrational
Suppose $\\sqrt{2} = \\dfrac{p}{q}$ in lowest terms. Then $2q^2 = p^2$, so $p^2$ is even, hence $p$ is even. Write $p = 2k$. Then $2q^2 = 4k^2 \\Rightarrow q^2 = 2k^2$, so $q$ is also even. That contradicts "lowest terms", so no such representation exists.

### A surd is an irrational root
A **surd** is an irrational number written exactly using a root sign, like $\\sqrt{5}$ or $\\sqrt[3]{11}$. Surds are kept in this form so they stay **exact** rather than being truncated to decimals.`,
      examples: [
        {
          id: 'ex-classify-rational',
          statement:
            'Is $0.\\overline{36}$ rational or irrational?',
          steps: [
            'The bar means $36$ repeats forever: $0.363636\\dots$',
            'It can be written as $\\tfrac{36}{99} = \\tfrac{4}{11}$.',
            'Therefore it is **rational**.',
          ],
        },
        {
          id: 'ex-classify-irrational',
          statement: 'Is $\\sqrt{12}$ rational or irrational?',
          steps: [
            '$12$ is not a perfect square, so $\\sqrt{12}$ has no integer form.',
            'Decimal: $3.464101615\\dots$ — no repeating pattern.',
            'Therefore $\\sqrt{12}$ is **irrational**.',
          ],
        },
        {
          id: 'ex-surd-vs-decimal',
          statement:
            'Why do we keep $\\sqrt{5}$ in surd form rather than writing $2.2360679\\dots$?',
          steps: [
            'A decimal is an **approximation** — it stops somewhere and rounds.',
            'The surd $\\sqrt{5}$ is **exact** and exact answers keep error from building up in later steps.',
            'In proofs and exact calculations, surds are safer.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-classify-sqrt7',
          difficulty: 'intro',
          instance: {
            prompt:
              'Is $\\sqrt{7}$ rational or irrational? Answer "rational" or "irrational".',
            answer: 'irrational',
            answerType: 'exact',
            hint: '$7$ is not a perfect square.',
            solution: [
              '$7$ is not a perfect square, so $\\sqrt{7}$ has no integer form and its decimal is non-repeating.',
              'Hence $\\sqrt{7}$ is irrational.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-classify-rep',
          difficulty: 'core',
          instance: {
            prompt:
              'Is $0.\\overline{142857}$ rational or irrational? Answer "rational" or "irrational".',
            answer: 'rational',
            answerType: 'exact',
            hint: 'A bar over digits means the block repeats — express it as a fraction.',
            solution: [
              'Repeating decimals equal a fraction: $0.\\overline{142857} = \\tfrac{142857}{999999} = \\tfrac{1}{7}$.',
              'Hence it is rational.',
            ],
          },
        },
      ],
    },

    {
      id: 'surd-operations',
      heading: 'Operating with surds',
      summary: 'Use the fact that √a · √b = √(ab) and √a / √b = √(a/b); simplify by taking out square factors.',
      body: `Surds obey rules derived from the index laws. The most important ones let us combine, simplify and divide surds.

### The two key identities
For non-negative $a, b$:
$$\\sqrt{a} \\cdot \\sqrt{b} = \\sqrt{ab}, \\qquad \\dfrac{\\sqrt{a}}{\\sqrt{b}} = \\sqrt{\\dfrac{a}{b}}.$$

### Simplifying a surd
Look for perfect square factors inside the root and pull them out:
$$\\sqrt{12} = \\sqrt{4 \\cdot 3} = \\sqrt{4} \\cdot \\sqrt{3} = 2\\sqrt{3}.$$
**Simplify fully** — leave no square factor (other than $1$) under the root.

### Adding and subtracting like surds
$\\sqrt{a}$ and $\\sqrt{b}$ can be combined only when they are **like terms** (i.e. $a = b$). E.g. $3\\sqrt{5} + 2\\sqrt{5} = 5\\sqrt{5}$, but $\\sqrt{2} + \\sqrt{3}$ cannot be simplified further.

### Rationalising the denominator
A **rationalised** fraction has no surd in the denominator. Multiply by a clever form of $1$:
$$\\dfrac{1}{\\sqrt{2}} \\cdot \\dfrac{\\sqrt{2}}{\\sqrt{2}} = \\dfrac{\\sqrt{2}}{2}.$$
For $\\dfrac{1}{a + \\sqrt{b}}$, multiply by $\\dfrac{a - \\sqrt{b}}{a - \\sqrt{b}}$ (a difference of squares trick).`,
      examples: [
        {
          id: 'ex-multiply',
          statement: 'Simplify $\\sqrt{3} \\cdot \\sqrt{12}$.',
          steps: [
            'Combine: $\\sqrt{3 \\cdot 12} = \\sqrt{36} = 6$.',
          ],
        },
        {
          id: 'ex-simplify-18',
          statement: 'Simplify $\\sqrt{18}$ fully.',
          steps: [
            'Largest square factor of $18$ is $9$.',
            '$\\sqrt{18} = \\sqrt{9 \\cdot 2} = \\sqrt{9} \\cdot \\sqrt{2} = 3\\sqrt{2}$.',
          ],
        },
        {
          id: 'ex-rationalise',
          statement: 'Rationalise the denominator of $\\dfrac{3}{\\sqrt{5}}$.',
          steps: [
            'Multiply by $\\dfrac{\\sqrt{5}}{\\sqrt{5}}$.',
            '$\\dfrac{3 \\sqrt{5}}{\\sqrt{5} \\cdot \\sqrt{5}} = \\dfrac{3\\sqrt{5}}{5}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-surd-mult',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $\\sqrt{2} \\cdot \\sqrt{8}$. State the integer answer.',
            answer: '4',
            answerType: 'numeric',
            hint: 'Combine under one root first: $\\sqrt{2 \\cdot 8}$.',
            solution: [
              '$\\sqrt{2} \\cdot \\sqrt{8} = \\sqrt{16} = 4$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-surd-simplify',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $\\sqrt{50}$. Type in the form a*sqrt(b) with no perfect-square factor under the root (e.g. 3*sqrt(2)).',
            answer: '5*sqrt(2)',
            answerType: 'exact',
            hint: 'Largest square factor of $50$ is $25$.',
            solution: [
              '$\\sqrt{50} = \\sqrt{25 \\cdot 2} = 5\\sqrt{2}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-surd-rationalise',
          difficulty: 'core',
          instance: {
            prompt:
              'Rationalise the denominator of $\\dfrac{2}{\\sqrt{3}}$. Type in the form a*sqrt(b)/c.',
            answer: '2*sqrt(3)/3',
            answerType: 'exact',
            hint: 'Multiply top and bottom by $\\sqrt{3}$.',
            solution: [
              '$\\dfrac{2}{\\sqrt{3}} \\cdot \\dfrac{\\sqrt{3}}{\\sqrt{3}} = \\dfrac{2\\sqrt{3}}{3}$.',
            ],
          },
        },
      ],
    },
  ],
}
