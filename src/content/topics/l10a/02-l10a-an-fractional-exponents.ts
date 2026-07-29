import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Number · l10a-an-2 (VC2M10AN02).
// Perform operations on numbers involving fractional exponents and surds.

export const l10aAnFractionalExponents: Topic = {
  id: 'l10a-an-fractional-exponents',
  unit: '10A',
  order: 2,
  title: 'Operations with fractional exponents and surds',
  blurb:
    'Perform operations on numbers involving fractional exponents and surds, applying the index laws fluently.',
  dotPoints: ['l10a-an-2'],

  lessons: [
    {
      id: 'fractional-index-definition',
      heading: 'Fractional indices defined',
      summary: 'a^(m/n) is the n-th root of a^m — the index "splits" between a power and a root.',
      body: `The exponent laws you already know extend to **fractional exponents**. The rule that ties them to surds is:
$$a^{m/n} = \\sqrt[n]{a^m} = \\bigl(\\sqrt[n]{a}\\bigr)^m.$$

For positive $a$, this gives a clean way to write roots using power notation:
- $\\sqrt{a} = a^{1/2}$
- $\\sqrt[3]{a} = a^{1/3}$
- $\\dfrac{1}{\\sqrt{a}} = a^{-1/2}$

### Re-writing as a power
Convert any surd to a fractional index by asking "which root, which power?".

### Operations stay the same
Once a number is written as $a^k$, all five index laws apply:
1. $a^m \\cdot a^n = a^{m+n}$
2. $\\dfrac{a^m}{a^n} = a^{m - n}$
3. $(a^m)^n = a^{mn}$
4. $(ab)^n = a^n b^n$
5. $a^0 = 1$`,
      examples: [
        {
          id: 'ex-surd-to-power',
          statement: 'Rewrite $\\sqrt[3]{7^2}$ using a fractional index.',
          steps: [
            'Cube root of $7$-squared: $\\sqrt[3]{7^2} = 7^{2/3}$.',
          ],
        },
        {
          id: 'ex-power-to-surd',
          statement: 'Rewrite $8^{2/3}$ as a surd and evaluate.',
          steps: [
            'Cube root of $8$-squared: $\\sqrt[3]{8^2} = \\sqrt[3]{64} = 4$.',
            'Equivalently: $(8^{1/3})^2 = 2^2 = 4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-rewrite-power',
          difficulty: 'intro',
          instance: {
            prompt:
              'Rewrite $\\sqrt{11}$ using a fractional index. Type as 11^(k) where k is a fraction like 1/2.',
            answer: '11^(1/2)',
            answerType: 'exact',
            hint: 'Square root = first power, half.',
            solution: [
              '$\\sqrt{11} = 11^{1/2}$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-evaluate-power',
          difficulty: 'core',
          instance: {
            prompt:
              'Evaluate $27^{2/3}$. State the integer answer.',
            answer: '9',
            answerType: 'numeric',
            hint: 'Cube root of $27$ is $3$, then square it.',
            solution: [
              '$27^{1/3} = 3$, so $27^{2/3} = 3^2 = 9$.',
            ],
          },
        },
      ],
    },

    {
      id: 'combining-laws',
      heading: 'Combining fractional indices',
      summary: 'Mix all five index laws on expressions like 4^(1/2) · 16^(1/4); write final answers using surds.',
      body: `When fractional indices are mixed with the other index laws, everything works the same way — just keep base, exponent, and sign consistent.

### Strategy
1. Rewrite every term with the **same base** if possible.
2. Apply the laws to combine exponents.
3. Convert back to surd form if the question asks for it.

### Negative fractional index
The rule $a^{-n} = \\dfrac{1}{a^n}$ still works:
$$a^{-1/2} = \\dfrac{1}{\\sqrt{a}}.$$

### Zero fractional index
$a^0 = 1$ for any exponent, even $0$. So $\\sqrt{a} \\cdot a^{-1/2} = a^{1/2 - 1/2} = a^0 = 1$.`,
      examples: [
        {
          id: 'ex-mixed-1',
          statement: 'Simplify $16^{1/2} \\cdot 16^{1/4}$.',
          steps: [
            'Same base — add exponents: $1/2 + 1/4 = 3/4$.',
            'So $16^{3/4} = \\sqrt[4]{16^3} = \\sqrt[4]{4096} = 8$.',
            '(Check: $16^{1/2} = 4$, $16^{1/4} = 2$, product $= 8$.)',
          ],
        },
        {
          id: 'ex-mixed-2',
          statement: 'Simplify $\\dfrac{9^{3/2}}{9}$.',
          steps: [
            '$9 = 9^1$, so divide: $9^{3/2 - 1} = 9^{1/2}$.',
            'Result: $\\sqrt{9} = 3$.',
          ],
        },
        {
          id: 'ex-negative',
          statement: 'Simplify $25^{-1/2}$.',
          steps: [
            '$25^{-1/2} = \\dfrac{1}{25^{1/2}} = \\dfrac{1}{\\sqrt{25}} = \\dfrac{1}{5}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-combine-powers',
          difficulty: 'core',
          instance: {
            prompt:
              'Simplify $\\sqrt{8} \\cdot 8^{1/2}$. State the integer answer.',
            answer: '8',
            answerType: 'numeric',
            hint: '$\\sqrt{8} = 8^{1/2}$.',
            solution: [
              '$8^{1/2} \\cdot 8^{1/2} = 8^{1/2 + 1/2} = 8^1 = 8$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-combine-quotient',
          difficulty: 'intro',
          instance: {
            prompt:
              'Simplify $\\dfrac{16^{3/4}}{16^{1/2}}$. State the integer answer.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Same base — subtract the exponents.',
            solution: [
              '$16^{3/4 - 1/2} = 16^{1/4} = \\sqrt[4]{16} = 2$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-negative-fractional',
          difficulty: 'challenge',
          instance: {
            prompt:
              'Simplify $4^{-1/2}$. State as a fraction like 1/n.',
            answer: '1/2',
            answerType: 'exact',
            hint: 'Take the reciprocal of $\\sqrt{4}$.',
            solution: [
              '$4^{-1/2} = \\dfrac{1}{4^{1/2}} = \\dfrac{1}{\\sqrt{4}} = \\dfrac{1}{2}$.',
            ],
          },
        },
      ],
    },
  ],
}
