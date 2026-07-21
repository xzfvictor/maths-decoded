import type { Topic } from '../types'

// Unit 2 · Topic 3 — Exponential functions and their graphs; applications:
// initial value, growth/decay rate, half-life, doubling time, long-run value.
// Also covers the exponent laws used to manipulate them.

export const exponentialFunctions: Topic = {
  id: 'exponential-functions',
  unit: 2,
  order: 3,
  title: 'Exponential functions & their graphs',
  blurb:
    'Graphs of $y = a\\cdot b^{n(x+k)} + c$, exponent laws, initial values, growth/decay rates, half-lives, doubling times and long-run values.',
  dotPoints: ['u2-fr-7', 'u2-fr-9', 'u2-al-2'],

  lessons: [
    {
      id: 'exponential-basics',
      heading: 'The basic exponential graph',
      summary: 'Exponential growth versus linear; the y-intercept and the long-run direction.',
      body: `An **exponential function** has the form $y = b^x$ where $b > 0$ and $b \\ne 1$.

### Shape of $y = b^x$
- $y$-intercept is always $1$ (because $b^0 = 1$).
- The curve never touches the $x$-axis: $b^x > 0$ for all real $x$.
- If $b > 1$, the graph **grows** to the right (exponential growth).
- If $0 < b < 1$, the graph **decays** to the right (exponential decay).

### Exponential vs. linear
A linear rule grows by a fixed amount each step (additive). An exponential rule grows by a fixed **factor** each step (multiplicative). So an exponential rule always overtakes a linear rule given enough time — even a tiny interest rate wins eventually.

### Worked example
$y = 2^x$ at $x = 0, 1, 2, 3, 4, \\ldots$ gives $y = 1, 2, 4, 8, 16, \\ldots$ — it doubles each step.`,
      examples: [
        {
          id: 'ex-y-intercept',
          statement: 'What is the $y$-intercept of $y = 3^x$?',
          steps: [
            'At $x = 0$, $y = 3^0 = 1$.',
            'So the $y$-intercept is $(0, 1)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-y-intercept',
          difficulty: 'intro',
          build: (seed) => {
            const bases = [2, 3, 5, 7, 10]
            const b = bases[seed % bases.length]
            return {
              prompt: `What is the $y$-intercept of $y = ${b}^x$? (State the $y$-value as a number.)`,
              answer: '1',
              answerType: 'numeric',
              hint: 'Set $x = 0$. Anything-to-the-zero is $1$.',
              solution: [
                `$y = ${b}^0 = 1$.`,
                'The $y$-intercept is $(0, 1)$.',
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-growth-or-decay',
          difficulty: 'core',
          build: (seed) => {
            const grow = [2, 3, 5]
            const decay = [0.5, 0.25]
            const useGrow = seed % 2 === 0
            const b = useGrow ? grow[seed % grow.length] : decay[seed % decay.length]
            const kind = useGrow ? 'growth' : 'decay'
            return {
              prompt: `Does $y = ${b}^x$ model exponential growth or exponential decay? Answer "growth" or "decay".`,
              answer: kind,
              answerType: 'exact',
              hint: 'Compare the base with $1$.',
              solution: [
                `The base is $${b}$, which is ${useGrow ? 'greater than $1$' : 'between $0$ and $1$'}.`,
                `So the graph models exponential ${kind}.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'transformed-exponential',
      heading: 'Graphs of $y = a\\cdot b^{\\bigl(n(x+k)\\bigr)} + c$',
      summary: 'Effects of $a$, $n$, the inner shift and the outer shift on an exponential.',
      body: `The general transformed form is
$$y = a \\cdot b^{\\bigl(n(x+k)\\bigr)} + c,$$
where $b > 0,\\ b \\ne 1$. Each parameter changes the graph the same way the polynomial-style transformations did in Unit 1, except the shape being stretched and shifted is the exponential curve.

### What each parameter does (starting from $y = b^x$)
- $a$: vertical **dilation** by factor $|a|$ from the $x$-axis; sign flips reflect in the $x$-axis.
- $n$: a **horizontal scaling** by $\\tfrac{1}{|n|}$ — it speeds the exponential up when $|n| > 1$. For instance, $b^{2x}$ grows twice as fast as $b^x$.
- $k$: a **horizontal translation** by $-k$ (left if $k > 0$, right if $k < 0$). The graph still approaches an asymptote, never the axis.
- $c$: a **vertical translation** by $c$. It defines the **horizontal asymptote** for $0 < b < 1$ (the level the graph approaches from above or below as $x \\to \\infty$).

### Asymptote fact
For $0 < b < 1$, $y \\to c$ as $x \\to \\infty$. For $b > 1$, the same constant $c$ is still the asymptote — approached as $x \\to -\\infty$, with $y$ shooting off to $+\\infty$ as $x \\to +\\infty$.`,
      examples: [
        {
          id: 'ex-transformed',
          statement:
            'Describe the graph of $y = 3\\cdot 2^x + 5$ and state the horizontal asymptote.',
          steps: [
            'The factor $3$ dilates the basic exponential vertically from the $x$-axis.',
            'The $+5$ shifts the graph up by $5$.',
            'As $x \\to -\\infty$, $2^x \\to 0$, so $y \\to 5$. Horizontal asymptote: $y = 5$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-asymptote',
          difficulty: 'core',
          build: (seed) => {
            const cVals = [3, 5, 7, -2]
            const c = cVals[seed % cVals.length]
            const aVals = [2, 3, 4]
            const a = aVals[Math.floor(seed / 4) % aVals.length]
            const cPart = c >= 0 ? `+ ${c}` : `- ${Math.abs(c)}`
            return {
              prompt: `For $y = ${a} \\cdot 0.5^x ${cPart}$, state the horizontal asymptote's $y$-value as an integer.`,
              answer: String(c),
              answerType: 'numeric',
              hint: 'For $0 < b < 1$, $b^x \\to 0$ as $x \\to \\infty$.',
              solution: [
                `As $x \\to \\infty$, $0.5^x \\to 0$.`,
                `So $y \\to ${a} \\cdot 0 ${c >= 0 ? '+ ' + c : '- ' + Math.abs(c)} = ${c}$.`,
                `The horizontal asymptote is $y = ${c}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-evaluating',
          difficulty: 'intro',
          instance: {
            prompt:
              'Evaluate $y = 3 \\cdot 2^x - 1$ at $x = 0$. State the $y$-value as an integer.',
            answer: '2',
            answerType: 'numeric',
            hint: 'Set $x = 0$ and use $2^0 = 1$.',
            solution: [
              '$y = 3 \\cdot 2^0 - 1 = 3 \\cdot 1 - 1$.',
              '$y = 2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'exponent-laws',
      heading: 'Exponent laws',
      summary: 'Combining and simplifying expressions with the same base.',
      body: `For $a, b > 0$ (not equal to $1$) and real exponents $m, n$:

| Law | Form |
|---|---|
| Multiplication | $a^m \\cdot a^n = a^{m + n}$ |
| Division | $\\dfrac{a^m}{a^n} = a^{m - n}$ |
| Power of a power | $(a^m)^n = a^{mn}$ |
| Power of a product | $(ab)^n = a^n b^n$ |
| Power of a quotient | $\\left(\\tfrac{a}{b}\\right)^n = \\dfrac{a^n}{b^n}$ |
| Zero exponent | $a^0 = 1$ ($a \\ne 0$) |
| Negative exponent | $a^{-n} = \\dfrac{1}{a^n}$ |

### Combining like bases
The most common use is to **simplify** expressions to a single base raised to a single exponent, or to **collect** terms before solving equations.

### Power-of-a-power makes transformations flexible
Writing $b^{2x} = (b^x)^2 = (b^2)^x$ is the heart of rewriting $y = a \\cdot b^{n(x+k)} + c$: the exponent $n$ can be folded into the base or kept in the bracket as you prefer.`,
      examples: [
        {
          id: 'ex-simplify',
          statement: 'Simplify $\\dfrac{4^x \\cdot 8^{x-1}}{2^{3x}}$.',
          steps: [
            'Write everything as a power of $2$: $4^x = 2^{2x}$, $8^{x-1} = 2^{3(x-1)} = 2^{3x-3}$.',
            'Combine: $\\dfrac{2^{2x} \\cdot 2^{3x-3}}{2^{3x}} = \\dfrac{2^{5x-3}}{2^{3x}}$.',
            'Use $\\dfrac{a^m}{a^n} = a^{m - n}$: $2^{(5x - 3) - 3x} = 2^{2x - 3}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-exponent-multiply',
          difficulty: 'intro',
          build: (seed) => {
            const e1 = (seed % 4) + 1 // 1..4
            const e2 = (Math.floor(seed / 4) % 4) + 1 // 1..4
            const total = e1 + e2
            return {
              prompt: `Simplify $a^${e1} \\cdot a^${e2}$ in terms of $a$. Use the form "a^k".`,
              answer: `a^${total}`,
              answerType: 'polynomial',
              hint: 'When you multiply powers of the same base, you add the exponents.',
              solution: [
                `$a^${e1} \\cdot a^${e2} = a^${e1} \\text{(exponent-sum)}.`,
                `$= a^${total}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-exponent-divide',
          difficulty: 'core',
          build: (seed) => {
            const n = (seed % 4) + 1
            const diff = (Math.floor(seed / 4) % 5) + 1 // 1..5
            const m = n + diff
            return {
              prompt: `Simplify $\\dfrac{a^${m}}{a^${n}}$ in terms of $a$. Use the form "a^k".`,
              answer: `a^${diff}`,
              answerType: 'polynomial',
              hint: 'When you divide powers of the same base, you subtract the exponents.',
              solution: [
                `$\\dfrac{a^${m}}{a^${n}} = a^${m} \\text{(difference)}.`,
                `$= a^${diff}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-negative-exponent',
          difficulty: 'core',
          instance: {
            prompt:
              'Rewrite $a^{-3}$ without a negative exponent. Use the form "1/a^k".',
            answer: '1/a^3',
            answerType: 'polynomial',
            hint: '$a^{-n} = \\dfrac{1}{a^n}$.',
            solution: [
              '$a^{-3} = \\dfrac{1}{a^3}$.',
            ],
          },
        },
      ],
    },

    {
      id: 'exponential-applications',
      heading: 'Initial value, growth rate & long-run',
      summary: 'Reading real-world meaning from exponential parameters.',
      body: `For a model $y = a \\cdot b^{n(x+k)} + c$ with $b > 1$ (growth):

- **Initial value** ($x = 0$): $y = a \\cdot b^{n k} + c$. If $k = 0$ the initial value is just $a + c$.
- **Growth factor** per unit step: $b^n$ — the multiplier when $x$ increases by $1$. E.g. $b = 1.05$, $n = 1$ means $5\\%$ per step.
- **Doubling time**: solve $b^{n t_2} = 2$, giving $t_2 = \\dfrac{\\ln 2}{n \\ln b}$.
- **Long-run value** as $x \\to \\infty$: $\\infty$ (the curve shoots away to infinity).

For $0 < b < 1$ (decay):
- **Initial value**: same form as above.
- **Decay factor** per unit step: $b^n$ (less than $1$).
- **Half-life**: solve $b^{n t_{1/2}} = \\tfrac12$, giving $t_{1/2} = \\dfrac{\\ln(1/2)}{n \\ln b} = -\\dfrac{\\ln 2}{n \\ln b}$.
- **Long-run value** as $x \\to \\infty$: the asymptote $c$.`,
      examples: [
        {
          id: 'ex-half-life',
          statement:
            'A radioactive sample obeys $N(t) = 100 \\cdot 0.5^{t / 8}$ grams. Find the half-life.',
          steps: [
            'The exponent is $t / 8$.',
            'For $N$ to halve, the factor $0.5^{t/8}$ must equal $\\tfrac12 = 0.5^1$.',
            'So $t / 8 = 1$, giving $t = 8$.',
            'Half-life is $8$ units.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-initial-value',
          difficulty: 'intro',
          build: (seed) => {
            const a = (seed % 4) + 2 // 2..5
            const c = ((Math.floor(seed / 4) % 4) + 1) * 5 // 5,10,15,20
            const cPart = c >= 0 ? `+ ${c}` : `- ${Math.abs(c)}`
            return {
              prompt: `For $y = ${a} \\cdot 2^x ${cPart}$, state the initial value $y(0)$ as a number.`,
              answer: String(a + c),
              answerType: 'numeric',
              hint: 'Set $x = 0$.',
              solution: [
                `$y(0) = ${a} \\cdot 2^0 ${c >= 0 ? '+ ' + c : '- ' + Math.abs(c)}$.`,
                `$2^0 = 1$, so $y(0) = ${a} ${c >= 0 ? '+ ' + c : '- ' + Math.abs(c)} = ${a + c}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-doubling-time',
          difficulty: 'challenge',
          build: (seed) => {
            // y = 2^(x/n). doubling time = n.
            const n = (seed % 4) + 2 // 2..5
            return {
              prompt: `A quantity obeys $y = 2^{x/${n}}$ (and $y > 0$). Find the doubling time — the time for $y$ to double. State as an integer.`,
              answer: String(n),
              answerType: 'numeric',
              hint: 'Set $y$ equal to $2y_0$, then solve for the increment in $x$.',
              solution: [
                `Doubling time: solve $2^{t/${n}} = 2$, so $t/${n} = 1$, giving $t = ${n}$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
