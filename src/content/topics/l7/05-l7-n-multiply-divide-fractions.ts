import type { Topic } from '../../types'

// Foundation (Year 7) · Strand: Number · l7-n-5 (VC2M7N05).
// Multiply and divide fractions and decimals.

export const l7NMultiplyDivideFractions: Topic = {
  id: 'l7-n-multiply-divide-fractions',
  unit: 7,
  order: 5,
  title: 'Multiply and divide fractions and decimals',
  blurb:
    'Multiply and divide fractions and decimals using efficient mental, written, and digital strategies.',
  dotPoints: ['l7-n-5'],
  lessons: [
    {
      id: 'multiply-divide-fractions-decimals',
      heading: 'Multiplying and dividing fractions and decimals',
      summary: '"Of" means multiply, flip to divide, and shift decimals to multiply and divide by powers of 10.',
      body: `Multiplication and division with fractions and decimals follow a few reliable rules that let you work both on paper and mentally.

### Multiplying fractions
$$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{a \\times c}{b \\times d}.$$
You can **cancel common factors** before multiplying to keep the numbers small.
$\\dfrac{2}{9} \\times \\dfrac{3}{4} = \\dfrac{\\cancel{2} \\times 3}{9 \\times \\cancel{4} \\times 2} = \\dfrac{1}{6}$.

### Dividing fractions
Division is the inverse of multiplication, so flip the second fraction and multiply:
$$\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c}.$$
"Keep, change, flip" is the memory trick — keep the first fraction, change $\\div$ to $\\times$, flip the second.

### Multiplying decimals
- Multiply the numbers as if they were whole numbers.
- Count the total number of decimal places in the two factors, then put that many decimal places in the answer.

Example: $1.4 \\times 2.5$. As whole numbers: $14 \\times 25 = 350$. Two decimal places total $\\Rightarrow$ $3.50 = 3.5$.

### Dividing decimals
Move the decimal point in **both** numbers until the divisor is a whole number, then divide normally.
$6.3 \\div 0.15 \\Rightarrow$ move two places $\\Rightarrow 630 \\div 15 = 42$.

> [!warning] Watch out
> When multiplying, "of" a fraction means multiply. "$\\dfrac{1}{2}$ **of** $40$" is $\\dfrac{1}{2} \\times 40 = 20$.`,
      examples: [
        {
          id: 'ex-multiply-fraction',
          statement: 'Find $\\dfrac{3}{5} \\times \\dfrac{2}{9}$.',
          steps: [
            'Multiply tops: $3 \\times 2 = 6$. Multiply bottoms: $5 \\times 9 = 45$.',
            '$\\dfrac{6}{45}$ — both share a factor of $3$.',
            'Simplify: $\\dfrac{6 \\div 3}{45 \\div 3} = \\dfrac{2}{15}$.',
          ],
        },
        {
          id: 'ex-divide-fraction',
          statement: 'Find $\\dfrac{4}{7} \\div \\dfrac{2}{5}$.',
          steps: [
            'Keep the first fraction: $\\dfrac{4}{7}$.',
            'Change $\\div$ to $\\times$, flip the second: $\\times \\dfrac{5}{2}$.',
            'Multiply: $\\dfrac{4 \\times 5}{7 \\times 2} = \\dfrac{20}{14} = \\dfrac{10}{7} = 1\\dfrac{3}{7}$.',
          ],
        },
        {
          id: 'ex-decimal',
          statement: 'Find $0.6 \\times 0.45$.',
          steps: [
            'As whole numbers: $6 \\times 45 = 270$.',
            'Total decimal places: $1 + 2 = 3$.',
            'Place the decimal: $0.270 = 0.27$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-divide-fraction',
          difficulty: 'intro',
          instance: {
            prompt: 'Find $\\dfrac{1}{2} \\div \\dfrac{1}{4}$. Type as an integer or a/b.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Keep, change, flip.',
            solution: [
              '$\\dfrac{1}{2} \\div \\dfrac{1}{4} = \\dfrac{1}{2} \\times \\dfrac{4}{1} = \\dfrac{4}{2} = 2$.',
            ],
          },
        },
      ],
    },
  ],
}
