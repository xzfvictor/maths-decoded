import type { Topic } from '../types'
import { signed } from '../../exercises/format'

// Unit 1 · Topic 5 — Power functions x^n and transformations to a(x+b)^n + c.

export const powerFunctions: Topic = {
  id: 'power-functions',
  unit: 1,
  order: 5,
  title: 'Power functions & transformations',
  blurb:
    'The power functions x^n for n = ±2, ±1, ½, 1, 2, 3, 4, their shapes and key features, and transformations to the form a(x+b)^n + c.',
  dotPoints: ['u1-fr-3'],

  lessons: [
    {
      id: 'positive-powers',
      heading: 'Positive integer powers',
      summary: 'The shapes of x, x², x³, x⁴ and the odd/even distinction.',
      body: `A **power function** has the form $y = x^n$. The positive whole-number powers split into two families by the parity of $n$.

### Even powers ($x^2$, $x^4$)
- Both are **U-shaped**, symmetric about the $y$-axis (they are **even** functions: $f(-x) = f(x)$).
- They pass through $(0,0)$, $(1,1)$ and $(-1,1)$.
- Higher even powers are **flatter** near the origin and **steeper** outside $[-1, 1]$. So $x^4$ hugs the axis more tightly than $x^2$ near $0$.

### Odd powers ($x$, $x^3$)
- These have **rotational symmetry** about the origin (they are **odd**: $f(-x) = -f(x)$).
- They pass through $(0,0)$, $(1,1)$ and $(-1,-1)$.
- $y = x^3$ is increasing everywhere, with a **stationary point of inflection** at the origin (it flattens then continues rising).

### Domain and range
All of $x, x^2, x^3, x^4$ have domain $\\mathbb{R}$. Odd powers have range $\\mathbb{R}$; even powers have range $[0, \\infty)$.`,
      examples: [
        {
          id: 'ex-odd-even',
          statement: 'Is $f(x) = x^4$ odd, even, or neither? Justify.',
          steps: [
            'Compute $f(-x) = (-x)^4 = x^4$.',
            'Since $f(-x) = f(x)$, the function is **even**.',
            'Its graph is symmetric about the $y$-axis.',
          ],
        },
        {
          id: 'ex-key-points',
          statement:
            'Which of these are on the graph of $y = x^3$: $(2, 8)$, $(-1, 1)$, $(0, 0)$, $(-3, -27)$?',
          steps: [
            '$(2, 8)$: $2^3 = 8$ ✓',
            '$(-1, 1)$: $(-1)^3 = -1 \\ne 1$ ✗',
            '$(0, 0)$: ✓',
            '$(-3, -27)$: $(-3)^3 = -27$ ✓',
          ],
        },
        {
          id: 'ex-even-range',
          statement:
            'What is the range of $y = x^2$ and why does it differ from the range of $y = x^3$?',
          steps: [
            'For $y = x^2$, every value is non-negative: $y \\ge 0$. So the range is $[0, \\infty)$.',
            'For $y = x^3$, every real number is achieved (the function is strictly increasing across $\\mathbb{R}$). So the range is $\\mathbb{R}$.',
            'The difference comes from the odd vs. even nature of the exponent.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-flattest',
          difficulty: 'intro',
          instance: {
            prompt:
              'Near the origin (for $x$ between $-1$ and $1$), which is flatter: $y = x^2$ or $y = x^4$? Answer "x^2" or "x^4".',
            answer: 'x^4',
            answerType: 'exact',
            hint: 'For $|x| < 1$, raising to a higher power makes the value smaller.',
            solution: [
              'For $0 < x < 1$, $x^4 < x^2$ (higher powers of a fraction are smaller).',
              'So $y = x^4$ stays closer to the axis — it is flatter near the origin.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-parity',
          difficulty: 'core',
          build: (seed) => {
            const n = [2, 3, 4][seed % 3]
            const even = n % 2 === 0
            return {
              prompt: `Is $y = x^{${n}}$ an odd or even function? Answer "odd" or "even".`,
              answer: even ? 'even' : 'odd',
              answerType: 'exact',
              hint: 'Even powers give even functions (symmetric about the $y$-axis); odd powers give odd functions.',
              solution: [
                `$f(-x) = (-x)^{${n}} = ${even ? '' : '-'}x^{${n}}$.`,
                even
                  ? `Since $f(-x) = f(x)$, it is even.`
                  : `Since $f(-x) = -f(x)$, it is odd.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-graph-shape',
          difficulty: 'intro',
          instance: {
            prompt:
              'Which graph is U-shaped, lying entirely above the $x$-axis: $y = x^2$ or $y = x^3$?',
            answer: 'y=x^2',
            answerType: 'exact',
            hint: 'U-shape means non-negative values.',
            solution: [
              '$y = x^3$ takes negative values for $x < 0$.',
              '$y = x^2$ is non-negative for all $x$, so it sits entirely above the $x$-axis and is U-shaped.',
            ],
          },
        },
      ],
    },

    {
      id: 'negative-fractional',
      heading: 'Negative & fractional powers',
      summary: 'Reciprocal powers x⁻¹, x⁻², and the square-root power x^½.',
      body: `Beyond whole numbers, the study design includes $n = -1, -2$ and $n = \\tfrac{1}{2}$.

### Reciprocal: $y = x^{-1} = \\dfrac{1}{x}$
- A **hyperbola**. Domain $\\mathbb{R}\\setminus\\{0\\}$, range $\\mathbb{R}\\setminus\\{0\\}$.
- **Asymptotes**: the $x$-axis ($y = 0$) and $y$-axis ($x = 0$). The curve never touches them.
- Odd function, in the first and third quadrants.

### Reciprocal square: $y = x^{-2} = \\dfrac{1}{x^2}$
- Domain $\\mathbb{R}\\setminus\\{0\\}$, range $(0, \\infty)$ — always positive.
- Same asymptotes ($x = 0$, $y = 0$), but both branches sit **above** the $x$-axis. Even function.

### Square root: $y = x^{1/2} = \\sqrt{x}$
- Domain $[0, \\infty)$ (can't take the square root of a negative), range $[0, \\infty)$.
- Starts at the origin and increases, but ever more slowly — it is the top half of a sideways parabola.`,
      examples: [
        {
          id: 'ex-asymptote',
          statement: 'State the equations of the asymptotes of $y = \\dfrac{1}{x}$.',
          steps: [
            'As $x \\to \\pm\\infty$, $y \\to 0$: the horizontal asymptote is $y = 0$.',
            'As $x \\to 0$, $|y| \\to \\infty$: the vertical asymptote is $x = 0$.',
            'Asymptotes: $x = 0$ and $y = 0$.',
          ],
        },
        {
          id: 'ex-reciprocal-square',
          statement:
            'Why is the range of $y = x^{-2}$ equal to $(0, \\infty)$ and not $\\mathbb{R}$?',
          steps: [
            '$x^{-2} = \\dfrac{1}{x^2}$.',
            'A fraction with a real denominator is non-negative (in fact positive) for all $x \\ne 0$.',
            'It never reaches $0$, and grows without bound as $x \\to 0$.',
            "So the range is the open interval $(0, \\infty)$.",
          ],
        },
        {
          id: 'ex-sqrt-shape',
          statement:
            'Sketch the key features of $y = \\sqrt{x}$ in words: domain, range, end behaviour.',
          steps: [
            'Domain $x \\ge 0$ (no real square root of a negative).',
            'Range $y \\ge 0$ (output is the non-negative root).',
            'Starts at $(0, 0)$, increasing everywhere on its domain.',
            'As $x \\to \\infty$, $y \\to \\infty$ but ever more slowly (concave down).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sqrt-domain',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the maximal domain of $y = \\sqrt{x}$? Enter using interval notation like [a,∞).',
            answer: '[0,∞)',
            answerType: 'exact',
            hint: 'The expression under a square root must be $\\ge 0$.',
            solution: [
              'We need $x \\ge 0$ for $\\sqrt{x}$ to be real.',
              'So the maximal domain is $[0, \\infty)$.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-reciprocal-value',
          difficulty: 'core',
          build: (seed) => {
            const x = ((seed % 4) + 2) // 2..5
            // y = 1/x^2 ; ask for value at x (as a fraction 1/x^2)
            return {
              prompt: `For $y = \\dfrac{1}{x^2}$, find $y$ when $x = ${x}$. Enter as a fraction.`,
              answer: `1/${x * x}`,
              answerType: 'numeric',
              hint: 'Substitute and square the denominator.',
              solution: [
                `$y = \\dfrac{1}{(${x})^2} = \\dfrac{1}{${x * x}}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-1-over-x-sign',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $x > 0$, is $\\dfrac{1}{x}$ positive or negative? Answer "positive" or "negative".',
            answer: 'positive',
            answerType: 'exact',
            hint: 'Dividing positives by positives...',
            solution: [
              'For $x > 0$, both numerator and denominator are positive.',
              'So $\\dfrac{1}{x} > 0$ — it is positive.',
            ],
          },
        },
      ],
    },

    {
      id: 'transformations',
      heading: 'Transforming to a(x+b)ⁿ + c',
      summary: 'Reading dilation, reflection and translation from the transformed form.',
      body: `Any of these basic power graphs can be shifted, stretched and flipped into the form
$$y = a(x + b)^n + c.$$
Each constant does one job.

### The role of each constant
- $\\boldsymbol{c}$ — **vertical translation**: moves the graph **up** by $c$ (down if $c < 0$).
- $\\boldsymbol{b}$ — **horizontal translation**: moves the graph **left** by $b$ (right if $b < 0$). Note the sign flip: $(x + 3)^2$ is shifted **left** 3.
- $\\boldsymbol{a}$ — **dilation** from the $x$-axis by factor $|a|$ (a vertical stretch). If $a < 0$, there is also a **reflection in the $x$-axis**.

### Reference point
The point that was at the origin of $y = x^n$ moves to $(-b, c)$. For even powers and $x^3$ this is the "corner"/turning/inflection point — a quick anchor for sketching.

### Example
$y = 2(x - 1)^2 + 3$ is $y = x^2$ stretched by $2$, moved right $1$ and up $3$; its turning point is $(1, 3)$.`,
      examples: [
        {
          id: 'ex-identify-transform',
          statement: 'Describe the transformations taking $y = x^2$ to $y = -(x + 4)^2 - 1$.',
          steps: [
            '$a = -1$: reflect in the $x$-axis (no stretch since $|a| = 1$).',
            '$b = 4$: translate left $4$.',
            '$c = -1$: translate down $1$.',
            'The turning point moves from $(0,0)$ to $(-4, -1)$, opening downward.',
          ],
        },
        {
          id: 'ex-shift-direction',
          statement:
            'Does the graph of $y = (x - 5)^2$ shift left or right compared to $y = x^2$, and by how much?',
          steps: [
            'Inside the bracket is $x - 5$, which is zero when $x = 5$.',
            'So features of $y = x^2$ that were at $x = 0$ now occur at $x = 5$.',
            "It's shifted **right** by $5$.",
          ],
        },
        {
          id: 'ex-stretch-factor',
          statement:
            'For $y = 3(x + 1)^2 - 2$, identify the dilation, the translations, and the turning point.',
          steps: [
            'Dilation: factor $|a| = 3$ from the $x$-axis (stretch).',
            'Horizontal translation: left by $1$ (from $x + 1$).',
            'Vertical translation: down by $2$.',
            'Turning point: at $(-1, -2)$, opening upward.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-turning-point',
          difficulty: 'core',
          build: (seed) => {
            const a = [1, 2, -1, -2][seed % 4]
            const b = ((Math.floor(seed / 4) % 6) - 3) || -3 // -3..2, avoid 0
            const c = ((Math.floor(seed / 28) % 6) - 3) || -3 // -3..2, avoid 0
            // y = a(x + b)^2 + c, turning point at (-b, c)
            const lead = a === 1 ? '' : a === -1 ? '-' : `${a}`
            return {
              prompt: `State the turning point of $y = ${lead}(x ${signed(b)})^2 ${signed(c)}$ as $(h, k)$.`,
              answer: `(${-b},${c})`,
              answerType: 'exact',
              hint: 'For $a(x + b)^2 + c$ the turning point is at $(-b, c)$.',
              solution: [
                `Comparing with $a(x + b)^n + c$: $b = ${b}$, $c = ${c}$.`,
                `The turning point is at $(-b, c) = (${-b}, ${c})$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-vertical-shift',
          difficulty: 'intro',
          build: (seed) => {
            const c = ((seed % 9) - 4) || 3 // -4..4 nonzero
            const dir = c > 0 ? 'up' : 'down'
            return {
              prompt: `The graph of $y = x^3 ${signed(c)}$ is the graph of $y = x^3$ translated in which direction, and by how much? Answer like "up 3" or "down 2".`,
              answer: `${dir} ${Math.abs(c)}`,
              answerType: 'exact',
              hint: 'A constant added at the end shifts the graph vertically.',
              solution: [
                `Adding $${c}$ shifts every point vertically by $${c}$.`,
                `So the graph moves ${dir} by $${Math.abs(c)}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-shift-amount',
          difficulty: 'core',
          instance: {
            prompt:
              'In $y = (x + 7)^3$, the graph of $y = x^3$ has been shifted left by how many units?',
            answer: '7',
            answerType: 'numeric',
            hint: '$y = (x + 7)^3$ is zero when $x = -7$; that is the new location of features that were at $x = 0$.',
            solution: [
              'The bracket $x + 7 = 0$ at $x = -7$.',
              'So features that were at $x = 0$ shift to $x = -7$ — a shift of **left 7**.',
            ],
          },
        },
      ],
    },
  ],
}
