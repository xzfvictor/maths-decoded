import type { Topic } from '../types'
import { signed, quadratic, appendTerm } from '../../exercises/format'

// Unit 1 · Topic 4 — Cubic & quartic polynomials: expanding, factorising, the
// remainder/factor/rational-root theorems, solving, and sketching.

export const cubicQuartic: Topic = {
  id: 'cubic-quartic',
  unit: 1,
  order: 4,
  title: 'Cubic & quartic polynomials',
  blurb:
    'Expanding and factorising higher-degree polynomials, the remainder, factor and rational-root theorems, and sketching cubics and quartics from their factors.',
  dotPoints: ['u1-fr-4', 'u1-al-3', 'u1-al-6'],

  lessons: [
    {
      id: 'expand-factorise',
      heading: 'Expanding & factorising',
      summary: 'Multiplying out products of linear factors and taking out common factors.',
      body: `A **polynomial** is a sum of terms $a_n x^n + \\dots + a_1 x + a_0$. The **degree** is the highest power: degree 3 is a **cubic**, degree 4 a **quartic**.

### Expanding
To expand a product, multiply every term in one bracket by every term in the other, then collect like terms. For three factors, expand two first, then multiply the result by the third.
$$(x + 2)(x - 3) = x^2 - x - 6.$$

### Factorising
Factorising reverses this. Always look first for a **common factor**:
$$2x^3 - 8x = 2x(x^2 - 4) = 2x(x-2)(x+2).$$
Here we also used the **difference of two squares**, $a^2 - b^2 = (a-b)(a+b)$.

### Grouping
Four-term expressions can sometimes be factorised in pairs:
$$x^3 + x^2 + 3x + 3 = x^2(x+1) + 3(x+1) = (x+1)(x^2+3).$$`,
      examples: [
        {
          id: 'ex-expand-three',
          statement: 'Expand $(x + 1)(x - 2)(x + 3)$.',
          steps: [
            'Expand the first two factors: $(x+1)(x-2) = x^2 - x - 2$.',
            'Multiply by $(x+3)$: $(x^2 - x - 2)(x + 3)$.',
            '$= x^3 + 3x^2 - x^2 - 3x - 2x - 6$.',
            'Collect like terms: $x^3 + 2x^2 - 5x - 6$.',
          ],
        },
        {
          id: 'ex-common-factor',
          statement: 'Factorise $3x^3 - 12x$ fully.',
          steps: [
            'Take out the common factor $3x$: $3x(x^2 - 4)$.',
            '$x^2 - 4$ is a difference of two squares: $x^2 - 4 = (x-2)(x+2)$.',
            'So $3x^3 - 12x = 3x(x-2)(x+2)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-expand-square-linear',
          difficulty: 'core',
          instance: {
            prompt: 'Expand and simplify $(x - 1)(x^2 + 2x + 5)$. Enter the polynomial.',
            answer: 'x^3 + x^2 + 3x - 5',
            answerType: 'polynomial',
            hint: 'Multiply each term of the quadratic by $x$, then by $-1$, and collect.',
            solution: [
              '$x(x^2 + 2x + 5) = x^3 + 2x^2 + 5x$.',
              '$-1(x^2 + 2x + 5) = -x^2 - 2x - 5$.',
              'Add: $x^3 + (2-1)x^2 + (5-2)x - 5 = x^3 + x^2 + 3x - 5$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-expand-two-linear',
          difficulty: 'intro',
          build: (seed) => {
            // (x + p)(x + q) = x^2 + (p+q)x + pq
            const p = ((seed % 7) - 3) || 2 // -3..3, avoid 0
            const q = ((Math.floor(seed / 7) % 7) - 3) || -2
            const b = p + q
            const c = p * q
            return {
              prompt: `Expand $(x ${signed(p)})(x ${signed(q)})$. Enter the quadratic.`,
              answer: quadratic(1, b, c),
              answerType: 'polynomial',
              hint: 'Use $(x+p)(x+q) = x^2 + (p+q)x + pq$.',
              solution: [
                `Here $p = ${p}$ and $q = ${q}$.`,
                `Middle coefficient $p + q = ${b}$; constant $pq = ${c}$.`,
                `So the expansion is $${quadratic(1, b, c)}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'remainder-factor',
      heading: 'The remainder & factor theorems',
      summary: 'Finding remainders by substitution and testing for factors.',
      body: `Dividing a polynomial $P(x)$ by $(x - a)$ leaves a remainder. The **remainder theorem** gives it without doing the division:

> The remainder when $P(x)$ is divided by $(x - a)$ is $P(a)$.

The special case where the remainder is zero is the **factor theorem**:

> $(x - a)$ is a factor of $P(x)$ **if and only if** $P(a) = 0$.

So to test whether $(x - a)$ divides $P(x)$, just evaluate $P(a)$. If it is $0$, then $(x-a)$ is a factor and $x = a$ is a root.

### Watch the sign
For a factor $(x + 3)$, write it as $(x - (-3))$, so you substitute $a = -3$.

For a factor $(bx - a)$, the corresponding root is $x = \\dfrac{a}{b}$.`,
      examples: [
        {
          id: 'ex-remainder',
          statement: 'Find the remainder when $P(x) = x^3 - 2x^2 + 4$ is divided by $(x - 3)$.',
          steps: [
            'By the remainder theorem, the remainder is $P(3)$.',
            '$P(3) = 3^3 - 2(3)^2 + 4 = 27 - 18 + 4$.',
            '$= 13$. The remainder is $13$.',
          ],
        },
        {
          id: 'ex-factor-test',
          statement: 'Is $(x + 2)$ a factor of $P(x) = x^3 + 3x^2 - 4$?',
          steps: [
            'For $(x + 2) = (x - (-2))$, evaluate $P(-2)$.',
            '$P(-2) = (-2)^3 + 3(-2)^2 - 4 = -8 + 12 - 4 = 0$.',
            'Since $P(-2) = 0$, yes — $(x + 2)$ is a factor.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-remainder',
          difficulty: 'core',
          build: (seed) => {
            // P(x) = x^3 + b x + c ; remainder on division by (x - a) is P(a)
            const a = ((seed % 5) - 2) || 1 // -2..2, avoid 0
            const b = (Math.floor(seed / 5) % 6) - 3 || -3 // -3..2, avoid 0
            const c = (Math.floor(seed / 35) % 6) - 3 || -3 // -3..2, avoid 0
            const rem = a * a * a + b * a + c
            return {
              prompt: `Find the remainder when $P(x) = x^3${appendTerm(b, 'x')}${appendTerm(c, '')}$ is divided by $(x ${signed(-a)})$.`,
              answer: String(rem),
              answerType: 'numeric',
              hint: 'The remainder equals $P(a)$, where $x - a$ is the divisor.',
              solution: [
                `The divisor is $(x ${signed(-a)})$, so $a = ${a}$.`,
                `$P(${a}) = (${a})^3 ${signed(b)}(${a}) ${signed(c)} = ${a * a * a} ${signed(b * a)} ${signed(c)}$.`,
                `$= ${rem}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-factor-test',
          difficulty: 'core',
          build: (seed) => {
            // Build P(x) = (x - r)(x^2 + 1) + k, ask whether (x - a) is a factor.
            // Simpler: P(x) = x^3 + m x^2 + n; test value a; answer yes iff P(a)=0.
            const r = ((seed % 5) - 2) || 1 // integer root -2..2 (nonzero)
            // P(x) = x^2(x - r) = x^3 - r x^2, whose roots are 0 and r.
            // Test a = r (yes) or a non-root (no). Choose the non-root to avoid both
            // 0 and r, so it never renders as "(x + 0)".
            const askRoot = seed % 2 === 0
            const nonRoot = r + 1 === 0 ? r + 2 : r + 1 // never 0 or r
            const a = askRoot ? r : nonRoot
            const isFactor = askRoot
            return {
              prompt: `Given $P(x) = x^3${appendTerm(-r, 'x^2')}$, is $(x ${signed(-a)})$ a factor? Answer "yes" or "no".`,
              answer: isFactor ? 'yes' : 'no',
              answerType: 'exact',
              hint: 'Evaluate $P(a)$. It is a factor exactly when $P(a) = 0$.',
              solution: [
                `$P(x) = x^3${appendTerm(-r, 'x^2')} = x^2(x ${signed(-r)})$.`,
                `Evaluate $P(${a}) = (${a})^2(${a} ${signed(-r)}) = ${a * a} \\times ${a - r} = ${a * a * (a - r)}$.`,
                isFactor
                  ? `Since $P(${a}) = 0$, $(x ${signed(-a)})$ is a factor.`
                  : `Since $P(${a}) \\ne 0$, $(x ${signed(-a)})$ is not a factor.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'rational-root',
      heading: 'Factorising with the rational-root theorem',
      summary: 'Finding a first root to factorise a cubic completely.',
      body: `To factorise a cubic that has no obvious common factor, we hunt for one root, then divide.

### The rational-root theorem
If a polynomial with integer coefficients has a rational root $\\dfrac{p}{q}$ (in lowest terms), then $p$ divides the **constant term** and $q$ divides the **leading coefficient**.

For a **monic** cubic (leading coefficient $1$), any rational root must be a **whole-number factor of the constant term**. So test the divisors of the constant term: $\\pm 1, \\pm 2, \\dots$

### The method
1. Test small factors of the constant term until $P(a) = 0$ — then $(x - a)$ is a factor.
2. Divide $P(x)$ by $(x - a)$ (long division or inspection) to get a quadratic.
3. Factorise the quadratic if possible.

$$x^3 - 7x + 6 = (x - 1)(x^2 + x - 6) = (x-1)(x-2)(x+3).$$`,
      examples: [
        {
          id: 'ex-full-factor',
          statement: 'Factorise $P(x) = x^3 - 2x^2 - 5x + 6$ completely.',
          steps: [
            'Test factors of $6$. $P(1) = 1 - 2 - 5 + 6 = 0$, so $(x - 1)$ is a factor.',
            'Divide: $x^3 - 2x^2 - 5x + 6 = (x - 1)(x^2 - x - 6)$.',
            'Factorise the quadratic: $x^2 - x - 6 = (x - 3)(x + 2)$.',
            'So $P(x) = (x - 1)(x - 3)(x + 2)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-find-root',
          difficulty: 'core',
          instance: {
            prompt:
              'A first step in factorising $P(x) = x^3 - 4x^2 + x + 6$ is to find an integer root. Testing shows one root is a small integer. Enter a root of $P$.',
            answer: '-1,2,3',
            answerType: 'set',
            hint: 'Test $x = \\pm 1, \\pm 2, \\pm 3, \\pm 6$ (factors of 6). Any root that works is accepted.',
            solution: [
              '$P(-1) = -1 - 4 - 1 + 6 = 0$, so $x = -1$ is a root.',
              'Continuing, $P(2) = 8 - 16 + 2 + 6 = 0$ and $P(3) = 27 - 36 + 3 + 6 = 0$.',
              'The roots are $x = -1, 2, 3$, i.e. $P(x) = (x+1)(x-2)(x-3)$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-rational-root-candidates',
          difficulty: 'intro',
          build: (seed) => {
            // Ask for the number that a rational root's numerator must divide (constant term)
            // for a monic cubic x^3 + ... + c.
            const c = ((seed % 6) + 1) * (seed % 2 === 0 ? 1 : -1) // ±1..±6
            return {
              prompt: `For the monic cubic $P(x) = x^3 + 2x^2 - x ${signed(c)}$, any integer root must be a factor of which number?`,
              answer: String(c),
              answerType: 'numeric',
              hint: 'For a monic polynomial, integer roots divide the constant term.',
              solution: [
                'The rational-root theorem: for a monic polynomial, any integer root divides the constant term.',
                `The constant term here is $${c}$, so test the factors of $${c}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'null-factor-solve',
      heading: 'Solving with the null factor law',
      summary: 'From factors to roots: setting each factor to zero.',
      body: `Once a polynomial is written as a product of factors, solving $P(x) = 0$ is immediate.

### The null factor law
If a product equals zero, at least one factor is zero:
$$AB = 0 \\iff A = 0 \\text{ or } B = 0.$$

So from $(x - 1)(x - 3)(x + 2) = 0$ we read off the roots $x = 1,\\ 3,\\ -2$ — each factor $(x - a)$ contributes the root $x = a$.

### Repeated factors
A **repeated** factor gives a repeated root. For $(x - 2)^2(x + 1) = 0$ the roots are $x = 2$ (twice) and $x = -1$. The repeated root is where the graph *touches* the axis rather than crossing it.

### Connecting roots, factors and intercepts
The roots of $P$, the linear factors of $P$, and the **$x$-intercepts** of $y = P(x)$ are three views of the same thing: $x = a$ is a root $\\iff (x - a)$ is a factor $\\iff (a, 0)$ is an $x$-intercept.`,
      examples: [
        {
          id: 'ex-solve-factored',
          statement: 'Solve $(2x - 1)(x + 4) = 0$.',
          steps: [
            'By the null factor law, $2x - 1 = 0$ or $x + 4 = 0$.',
            'From $2x - 1 = 0$: $x = \\tfrac{1}{2}$.',
            'From $x + 4 = 0$: $x = -4$.',
            'Solutions: $x = \\tfrac{1}{2}$ or $x = -4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-roots-from-factors',
          difficulty: 'core',
          build: (seed) => {
            const r1 = ((seed % 5) - 2) // -2..2
            const r2 = ((Math.floor(seed / 5) % 5) - 2)
            const r3 = ((Math.floor(seed / 25) % 5) - 2)
            const roots = Array.from(new Set([r1, r2, r3]))
            const factorStr = [r1, r2, r3]
              .map((r) => (r === 0 ? '(x)' : `(x ${signed(-r)})`))
              .join('')
            return {
              prompt: `Solve $${factorStr} = 0$. List all distinct solutions separated by commas.`,
              answer: roots.join(','),
              answerType: 'set',
              hint: 'Set each factor to zero; a factor $(x - a)$ gives the root $x = a$.',
              solution: [
                'By the null factor law, set each factor to zero.',
                `The factors give $x = ${r1},\\ ${r2},\\ ${r3}$.`,
                `The distinct solutions are $${roots.join(',\\ ')}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-repeated-root',
          difficulty: 'core',
          instance: {
            prompt:
              'How many distinct $x$-intercepts does $y = (x - 3)^2(x + 1)$ have?',
            answer: '2',
            answerType: 'numeric',
            hint: 'A repeated factor still gives just one intercept (a touch point).',
            solution: [
              'The factors are $(x-3)$ (repeated) and $(x+1)$.',
              'Distinct roots are $x = 3$ and $x = -1$.',
              'So there are $2$ distinct $x$-intercepts (the graph touches at $x = 3$).',
            ],
          },
        },
      ],
    },

    {
      id: 'sketching',
      heading: 'Sketching cubics & quartics',
      summary: 'Shape, end behaviour, intercepts and the effect of repeated factors.',
      body: `To sketch a factorised polynomial, combine four ideas.

### 1. End behaviour (from the leading term)
For large $|x|$ the highest-power term dominates.
- **Cubic**, positive leading coefficient: down on the left, up on the right ($\\nearrow$).
- **Cubic**, negative: up on the left, down on the right.
- **Quartic**, positive: up at both ends (like a wide parabola); negative: down at both ends.

### 2. Intercepts
The $y$-intercept is $P(0)$. The $x$-intercepts are the roots.

### 3. Behaviour at each root
- A **single** factor $(x - a)$: the graph **crosses** the axis at $x = a$.
- A **squared** factor $(x - a)^2$: the graph **touches** the axis (a turning point on the axis).
- A **cubed** factor $(x - a)^3$: the graph **flattens and crosses** — a stationary point of inflection.

### 4. Join smoothly
Draw a smooth curve through the intercepts respecting the end behaviour and the touch/cross rules. A cubic has at most $2$ turning points; a quartic at most $3$.`,
      examples: [
        {
          id: 'ex-sketch-cubic',
          statement: 'Describe the key features of $y = (x + 2)(x - 1)^2$.',
          steps: [
            'Leading term: expanding gives $x^3 + \\dots$, positive cubic — down-left, up-right.',
            '$y$-intercept: $y = (2)(-1)^2 = 2$, so $(0, 2)$.',
            '$x$-intercepts: $x = -2$ (single factor → crosses) and $x = 1$ (squared → touches).',
            'Sketch: comes up from bottom-left, crosses at $x = -2$, turns, touches the axis at $x = 1$, then rises.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-end-behaviour',
          difficulty: 'intro',
          instance: {
            prompt:
              'As $x \\to +\\infty$, what happens to $y = -x^3 + 5x$? Answer "y → +∞" or "y → -∞".',
            answer: 'y → -∞',
            answerType: 'exact',
            hint: 'The leading term $-x^3$ dominates for large $x$.',
            solution: [
              'For large $x$ the $-x^3$ term dominates.',
              'A negative cubic goes up on the left and down on the right.',
              'So as $x \\to +\\infty$, $y \\to -\\infty$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-y-intercept',
          difficulty: 'intro',
          build: (seed) => {
            const p = ((seed % 5) - 2) || 1 // -2..2
            const q = ((Math.floor(seed / 5) % 5) - 2) || 2
            const r = ((Math.floor(seed / 25) % 5) - 2) || -1
            // y = (x - p)(x - q)(x - r); y-intercept = (-p)(-q)(-r)
            const yInt = -p * -q * -r
            return {
              prompt: `Find the $y$-intercept of $y = (x ${signed(-p)})(x ${signed(-q)})(x ${signed(-r)})$.`,
              answer: String(yInt),
              answerType: 'numeric',
              hint: 'Substitute $x = 0$.',
              solution: [
                `Set $x = 0$: $y = (${-p})(${-q})(${-r})$.`,
                `$= ${yInt}$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
