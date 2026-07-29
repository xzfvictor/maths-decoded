import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-3 (VC2M7N03).
// Equivalent representations of rational numbers and the number line.

export const l7NEquivalentFractions: Topic = {
  id: 'l7-n-equivalent-fractions',
  unit: 7,
  order: 3,
  title: 'Equivalent fractions and the number line',
  blurb:
    'Find equivalent fractions, simplify them, and place positive and negative rationals and mixed numerals on a number line.',
  dotPoints: ['l7-n-3'],
  lessons: [
    {
      id: 'equivalent-fractions-number-line',
      heading: 'Equivalent fractions and the number line',
      summary: 'Simplify by dividing, build by multiplying, then place any rational on a number line.',
      body: `Two fractions are **equivalent** if they sit at the same spot on the number line — they name the same amount in different ways.

### Finding equivalent fractions
- **Build up**: multiply the numerator and denominator by the same number.
  $\\dfrac{1}{3} = \\dfrac{1 \\times 4}{3 \\times 4} = \\dfrac{4}{12}$.
- **Simplify down**: divide the numerator and denominator by a common factor.
  $\\dfrac{8}{12} = \\dfrac{8 \\div 4}{12 \\div 4} = \\dfrac{2}{3}$.

A fraction is in **simplest form** when the numerator and denominator share no common factor other than $1$ (use the HCF from prime factorisation).

### Mixed numerals
A **mixed numeral** combines a whole number with a fraction: $2\\dfrac{3}{5}$ means $2 + \\dfrac{3}{5}$.
- To convert a mixed numeral to an improper fraction: multiply and add: $2\\dfrac{3}{5} = \\dfrac{2 \\times 5 + 3}{5} = \\dfrac{13}{5}$.
- To convert an improper fraction to a mixed numeral: divide and remainder: $\\dfrac{17}{4} = 4\\dfrac{1}{4}$ because $17 = 4 \\times 4 + 1$.

### The number line
A **number line** is a straight line marked with equally-spaced points. Use it to:
- **Compare** two numbers — whichever is further right is larger.
- **Place** a fraction by splitting the gap between two whole numbers into the right number of equal parts.
- **Place a negative fraction** the same way, on the left of zero: $-\\dfrac{1}{4}$ is one quarter of the way from $0$ to $-1$.

> [!warning] Watch out
> A number line is not always symmetric about zero. The interval from $-2$ to $3$ is split into **5** equal parts, not $4$ — count the **gaps**, not the labelled points.`,
      examples: [
        {
          id: 'ex-simplify',
          statement: 'Write $\\dfrac{24}{36}$ in simplest form.',
          steps: [
            'Find the HCF of $24$ and $36$: $24 = 2^3 \\times 3$, $36 = 2^2 \\times 3^2$, so HCF $= 2^2 \\times 3 = 12$.',
            'Divide both by $12$: $\\dfrac{24 \\div 12}{36 \\div 12} = \\dfrac{2}{3}$.',
            'Result: $\\dfrac{24}{36} = \\dfrac{2}{3}$.',
          ],
        },
        {
          id: 'ex-mixed-to-improper',
          statement: 'Convert $3\\dfrac{2}{7}$ to an improper fraction.',
          steps: [
            'Multiply the whole number by the denominator: $3 \\times 7 = 21$.',
            'Add the numerator: $21 + 2 = 23$.',
            'Keep the denominator $7$: $3\\dfrac{2}{7} = \\dfrac{23}{7}$.',
          ],
        },
        {
          id: 'ex-number-line',
          statement:
            'Plot $-\\dfrac{3}{5}$ on a number line running from $-2$ to $1$, with every whole number marked.',
          steps: [
            'The gap from $-1$ to $0$ is one whole unit; split it into $5$ equal parts.',
            'Move **left** from $0$ — negative direction.',
            'Mark the point $3$ parts to the left of $0$: that is $-\\dfrac{3}{5}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-simplify-18-30',
          difficulty: 'intro',
          instance: {
            prompt: 'Write $\\dfrac{18}{30}$ in simplest form. Type as "a/b".',
            answer: '3/5',
            answerType: 'numeric',
            hint: 'Divide top and bottom by the HCF.',
            solution: [
              'HCF of $18$ and $30$ is $6$, so $\\dfrac{18}{30} = \\dfrac{3}{5}$.',
            ],
          },
        },
      ],
    },
  ],
}
