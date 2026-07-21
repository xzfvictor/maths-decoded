import type { Topic } from '../types'

// Unit 2 · Topic 2 — Symmetry, periodicity and complementary relations for sin,
// cos and tan; transformations of the form y = a f(n(x+b)) + c; small-angle
// behaviour; applications to modelling (amplitude, period, mean value).

export const periodicProperties: Topic = {
  id: 'periodic-properties',
  unit: 2,
  order: 2,
  title: 'Periodicity, symmetry & transformed circular functions',
  blurb:
    'Symmetry and periodicity of sin/cos/tan, complementary relations, the small-angle identity sin x ≈ x, transformed graphs y = a f(n(x+b)) + c, and modelling with amplitude, period and mean value.',
  dotPoints: ['u2-fr-2', 'u2-fr-4', 'u2-fr-5', 'u2-fr-6'],

  lessons: [
    {
      id: 'periodicity',
      heading: 'Periodicity of sin, cos & tan',
      summary: 'How often the graph repeats, and the period of each function.',
      body: `A function $f$ is **periodic** with period $T$ if $f(x + T) = f(x)$ for every $x$ (with $T > 0$ the smallest such value).

### Period of each function
- $\\sin(x + 2\\pi) = \\sin x$, so $\\sin$ has period $2\\pi$.
- $\\cos(x + 2\\pi) = \\cos x$, so $\\cos$ has period $2\\pi$.
- $\\tan(x + \\pi) = \\tan x$, so $\\tan$ has period $\\pi$ (one short because of the asymptotes — the loop on the unit circle returns after half a turn).

### Co-periodic identities (shift by one period)
- $\\sin(x + \\pi) = -\\sin x$
- $\\cos(x + \\pi) = -\\cos x$
- $\\tan(x + \\pi) = \\tan x$

### Negative-angle identities (turn-symmetry)
- $\\sin(-x) = -\\sin x$ — $\\sin$ is **odd** (symmetric about the origin).
- $\\cos(-x) = \\cos x$ — $\\cos$ is **even** (symmetric about the $y$-axis).
- $\\tan(-x) = -\\tan x$ — $\\tan$ is **odd**.`,
      examples: [
        {
          id: 'ex-period',
          statement:
            'Use the period of $\\sin$ to write $\\sin(\\theta + 4\\pi)$ in terms of $\\sin\\theta$.',
          steps: [
            'Period of $\\sin$ is $2\\pi$, so $\\sin(\\theta + 2\\pi) = \\sin\\theta$.',
            '$4\\pi$ is two full periods, so $\\sin(\\theta + 4\\pi) = \\sin\\theta$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-period-fn',
          difficulty: 'intro',
          build: (seed) => {
            const fns = [
              { name: '\\sin', period: '2pi' },
              { name: '\\cos', period: '2pi' },
              { name: '\\tan', period: 'pi' },
            ]
            const f = fns[seed % fns.length]
            return {
              prompt: `What is the period of $f(\\theta) = ${f.name}\\theta$? Give your answer as a multiple of $\\pi$: e.g. for $2\\pi$ write "2pi" and for $\\pi$ write "pi".`,
              answer: f.period,
              answerType: 'exact',
              hint: 'How far do you have to travel along the unit circle before the function repeats?',
              solution: [
                `The period of ${f.name} is ${f.period}.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-co-periodic-value',
          difficulty: 'core',
          build: (seed) => {
            // Use the co-periodic identity sin(x + pi) = -sin x.
            // Ask: what is sin(theta + pi) if sin(theta) = v, where v is a simple fraction.
            const fns = [
              { sym: '\\sin', sign: '-', value: '0.5' },
              { sym: '\\cos', sign: '-', value: '0.5' },
              { sym: '\\sin', sign: '-', value: '0.6' },
            ]
            const it = fns[seed % fns.length]
            return {
              prompt: `If $${it.sym}\\theta = ${it.value}$, find $${it.sym}(\\theta + \\pi)$. (Answer as a signed decimal number, e.g. "-0.5".)`,
              answer: it.sign + it.value,
              answerType: 'numeric',
              hint: `Use the co-periodic identity $${it.sym}(x + \\pi) = -${it.sym} x$.`,
              solution: [
                `$${it.sym}(\\theta + \\pi) = -${it.sym}\\theta = ${it.sign}${it.value}$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'symmetry',
      heading: 'Symmetry & complementary relations',
      summary: 'Even/odd, supplementary, and complementary-angle identities.',
      body: `The unit-circle symmetries give a small toolkit of identities.

### Even / odd (negative-angle)
- $\\cos(-x) = \\cos x$ (even)
- $\\sin(-x) = -\\sin x$ (odd)
- $\\tan(-x) = -\\tan x$ (odd)

### Supplementary angles ($x$ and $\\pi - x$)
- $\\sin(\\pi - x) = \\sin x$
- $\\cos(\\pi - x) = -\\cos x$
- $\\tan(\\pi - x) = -\\tan x$

### Complementary angles ($x$ and $\\dfrac{\\pi}{2} - x$)
- $\\sin\\left(\\dfrac{\\pi}{2} - x\\right) = \\cos x$
- $\\cos\\left(\\dfrac{\\pi}{2} - x\\right) = \\sin x$
- $\\tan\\left(\\dfrac{\\pi}{2} - x\\right) = \\cot x = \\dfrac{1}{\\tan x}$ (where $\\tan x \\ne 0$).

These identities let you recognise familiar values inside a less-familiar angle.`,
      examples: [
        {
          id: 'ex-comp',
          statement:
            'Find $\\sin\\dfrac{2\\pi}{3}$ using the supplementary identity and the fact that $\\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$.',
          steps: [
            '$\\dfrac{2\\pi}{3} = \\pi - \\dfrac{\\pi}{3}$.',
            '$\\sin\\left(\\pi - \\dfrac{\\pi}{3}\\right) = \\sin\\dfrac{\\pi}{3} = \\dfrac{\\sqrt{3}}{2}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-even-odd',
          difficulty: 'core',
          build: (seed) => {
            const items = [
              { fn: '\\sin', kind: 'odd' },
              { fn: '\\cos', kind: 'even' },
              { fn: '\\tan', kind: 'odd' },
            ]
            const it = items[seed % items.length]
            const hint =
              it.fn === '\\cos'
                ? 'Check $\\cos(-\\theta) = \\cos\\theta$ vs $\\cos(-\\theta) = -\\cos\\theta$.'
                : `Check whether $${it.fn}(-\\theta) = ${it.fn}\\theta$ or $${it.fn}(-\\theta) = -${it.fn}\\theta$.`
            return {
              prompt: `Is $f(x) = ${it.fn}(x)$ even, odd or neither? Answer "even" or "odd".`,
              answer: it.kind,
              answerType: 'exact',
              hint,
              solution: [
                `${it.fn.charAt(0).toUpperCase() + it.fn.slice(1)} is ${it.kind} because $${it.fn}(-\\theta) = ${it.kind === 'even' ? '' : '-'}${it.fn}\\theta$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-supplementary-sign',
          difficulty: 'core',
          build: (seed) => {
            const cases = [
              { ang: '2π/3', sym: 'sin', sign: 'positive', val: 'sqrt(3)/2' },
              { ang: '3π/4', sym: 'cos', sign: 'negative', val: '-sqrt(2)/2' },
              { ang: '5π/6', sym: 'sin', sign: 'positive', val: '1/2' },
            ]
            const it = cases[seed % cases.length]
            return {
              prompt: `State the sign of $${it.sym}\\dfrac{${it.ang}}$ (a supplementary-angle case). Answer "positive" or "negative".`,
              answer: it.sign,
              answerType: 'exact',
              hint: `Apply the supplementary identity for $${it.sym}$.`,
              solution: [
                `Supplementary angle $\\pi - x$ lies in quadrant II where $${it.sym}$ is ${it.sym === 'sin' ? 'positive' : 'negative'}.`,
                `So $${it.sym}\\dfrac{${it.ang}}$ is ${it.sign}.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'small-angle',
      heading: 'The small-angle approximation',
      summary: 'sin x ≈ x for x near 0, and how to read it from the graph.',
      body: `For very small angles $x$ (in radians), the chord and the arc of the unit circle are nearly the same length. The $y$-coordinate at angle $x$ — which is $\\sin x$ — is very close to $x$ itself:
$$\\sin x \\approx x \\quad \\text{when } x \\text{ is small (in radians)}.$$

### Reading the graph near 0
Plot $y = \\sin x$ and $y = x$ near the origin. Both pass through $(0, 0)$ and have slope $1$ there. For small $|x|$ the two graphs are visually indistinguishable; as $|x|$ grows, $\\sin x$ starts to bend away from the line $y = x$.

### Approximation vs. equality
- $\\sin(0.1) \\approx 0.0998$ — very close to $0.1$.
- $\\sin(0.5) \\approx 0.479$ — already drifting below $0.5$.
- $\\sin(1) \\approx 0.841$ — the difference is no longer small.

Use the approximation when $x$ is small enough that the gap is negligible **for the problem at hand**.`,
      examples: [
        {
          id: 'ex-small-angle',
          statement:
            'A pendulum swings through a small angle. Estimate $\\sin(0.03)$ using the small-angle approximation.',
          steps: [
            '$0.03$ radians is small (about $1.7°$).',
            '$\\sin(0.03) \\approx 0.03$.',
            'Compare with the true value $\\sin(0.03) \\approx 0.0299955$ — extremely close.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-small-angle',
          difficulty: 'intro',
          build: (seed) => {
            const choices = [0.01, 0.02, 0.05, 0.1, 0.15, 0.2]
            const x = choices[seed % choices.length]
            return {
              prompt: `Use the small-angle approximation $\\sin x \\approx x$ to estimate $\\sin(${x})$ as a decimal.`,
              answer: String(x),
              answerType: 'numeric',
              hint: 'With $x$ small (in radians), $\\sin x \\approx x$.',
              solution: [
                `$${x}$ radians is small, so $\\sin(${x}) \\approx ${x}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-validity',
          difficulty: 'core',
          instance: {
            prompt:
              'Is the approximation $\\sin x \\approx x$ more accurate for $x = 0.05$ or for $x = 1.5$? (Answer with the decimal.)',
            answer: '0.05',
            answerType: 'exact',
            hint: 'The smaller $|x|$, the closer $\\sin x$ is to $x$.',
            solution: [
              '$|x|$ matters — smaller is better.',
              '$0.05 \\ll 1.5$, so $\\sin(0.05) \\approx 0.05$ is far more accurate than $\\sin(1.5) \\approx 1.5$.',
            ],
          },
        },
      ],
    },

    {
      id: 'transformations',
      heading: 'Graphs of $y = a\\,f\\bigl(n(x + b)\\bigr) + c$',
      summary: 'How the parameters change amplitude, period, phase and mean value.',
      body: `The general form for a transformed sine, cosine or tangent is
$$y = a\\,f\\bigl(n(x + b)\\bigr) + c,$$
where $f$ is one of $\\sin, \\cos, \\tan$. Each parameter changes the graph in a specific way.

### What each parameter does (starting from $y = f(x)$)
- $a$: a **dilation from the $x$-axis** by factor $|a|$. For trig, $|a|$ is the **amplitude**. A sign flip in $a$ reflects in the $x$-axis.
- $n$: a **horizontal dilation** by factor $\\tfrac{1}{|n|}$ — the **period** becomes $\\dfrac{\\text{period of }f}{|n|}$. For $y = \\sin(nx)$ the period is $\\tfrac{2\\pi}{|n|}$.
- $b$ (inside the bracket $x + b$): a **horizontal translation** by $-b$. **Watch the sign**: $y = \\sin(x + b)$ shifts the graph **left** by $b$.
- $c$: a **vertical translation** by $c$. For sine/cosine, $c$ is the **mean value** (the centre line the wave oscillates around).

### Putting it together
For $y = 3\\sin\\bigl(2(x + \\tfrac{\\pi}{4})\\bigr) + 1$:
- amplitude $3$, period $\\pi$, shifted left $\\tfrac{\\pi}{4}$, mean value $1$.`,
      examples: [
        {
          id: 'ex-amplitude',
          statement:
            'For $y = 4\\sin(2x) - 1$, state the amplitude, period and mean value.',
          steps: [
            'Amplitude $= |a| = 4$.',
            'Period $= \\dfrac{2\\pi}{|n|} = \\dfrac{2\\pi}{2} = \\pi$.',
            'Mean value $= c = -1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-period',
          difficulty: 'core',
          build: (seed) => {
            // period of sin(nx) = 2π/n, period of tan(nx) = π/n.
            // Pick n ∈ {2, 3, 4} and function so the period is a clean fraction of π.
            const nTable = [2, 3, 4]
            const n = nTable[seed % nTable.length]
            const isTan = seed % 2 === 1
            // Coefficient of pi in period = (isTan ? 1 : 2) / n, written as reduced fraction.
            const g = (a: number, b: number): number => (b ? g(b, a % b) : a)
            const numBase = isTan ? 1 : 2
            const k = g(numBase, n)
            const num = numBase / k
            const den = n / k
            const fn = isTan ? '\\tan' : '\\sin'
            // Build the answer string — student types "n/dpi" or "kpi" depending on simplest form.
            const answerString =
              den === 1 ? `${num}pi` : `${num}/${den}pi`
            const answerTex =
              den === 1 ? `${num}\\pi` : `\\dfrac{${num === 1 ? '' : `${num}`}\\pi}{${den}}`
            return {
              prompt: `Find the period of $y = ${fn}(${n}x)$. Give your answer as a coefficient of $\\pi$: e.g. for $2\\pi$ write "2pi", for $\\tfrac{\\pi}{3}$ write "1/3pi".`,
              answer: answerString,
              answerType: 'exact',
              hint: isTan
                ? 'Period of $\\tan$ is $\\dfrac{\\pi}{|n|}$.'
                : 'Period of $\\sin$ is $\\dfrac{2\\pi}{|n|}$.',
              solution: [
                `Period = ${isTan ? `$\\dfrac{\\pi}{|${n}|}$` : `$\\dfrac{2\\pi}{|${n}|}$`} = $${answerTex}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-amplitude',
          difficulty: 'core',
          build: (seed) => {
            const a = (seed % 4) + 2 // 2..5
            return {
              prompt: `For $y = ${a}\\sin(2x) - 1$, state the amplitude as a positive integer.`,
              answer: String(a),
              answerType: 'numeric',
              hint: 'Amplitude is $|a|$, the absolute value of the coefficient of $\\sin$.',
              solution: [
                `The coefficient of $\\sin$ is $|${a}| = ${a}$.`,
                `Amplitude $= ${a}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-mean-value',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $y = 2\\sin(3x) - 5$, what is the mean value (centre of oscillation)?',
            answer: '-5',
            answerType: 'numeric',
            hint: 'The mean value is $c$, the constant term in $a\\sin(nx) + c$.',
            solution: [
              'In $y = a\\sin(nx) + c$, the mean value is $c$.',
              'Here $c = -5$, so the mean value is $-5$.',
            ],
          },
        },
      ],
    },

    {
      id: 'modelling',
      heading: 'Modelling with sine & cosine',
      summary: 'Reading period, amplitude and mean value from a model.',
      body: `Sine and cosine model any quantity that oscillates — tides, sound waves, pistons, daily temperature. The rule
$$y = a\\sin\\bigl(n(x + b)\\bigr) + c$$
encodes everything we need to describe the motion.

### Real-world interpretations
- **Amplitude** $|a|$ — the size of the swing (how far the tide rises and falls).
- **Period** $\\dfrac{2\\pi}{|n|}$ — how long one cycle takes (e.g. a $12$-hour tide cycle).
- **Mean value** $c$ — the centre line (e.g. mean sea level, mean daily temperature).
- **Phase** $b$ — when the cycle starts. "$b = 2$" may mean a $2$-hour delay before the first maximum.

### Example decoding
"The depth of water in a harbour is $d(t) = 1.5\\sin\\bigl(\\tfrac{\\pi}{6}(t - 2)\\bigr) + 5$ metres, $t$ in hours."
- Amplitude $1.5$, so depth varies $\\pm 1.5$ m.
- Period $\\dfrac{2\\pi}{\\pi/6} = 12$ hours.
- Mean depth $5$ m.
- High tide at $t = 2 + 3 = 5$ hours (a quarter-period after $t = 2$).`,
      examples: [
        {
          id: 'ex-decode',
          statement:
            'A daily temperature (°C) is modelled by $T = 5\\cos\\bigl(\\tfrac{\\pi}{12}(t - 14)\\bigr) + 18$ with $t$ in hours past midnight. What is the maximum temperature?',
          steps: [
            'Amplitude is $5$, mean value $18$.',
            'Maximum temperature is the mean plus the amplitude: $18 + 5 = 23$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-model-max',
          difficulty: 'core',
          build: (seed) => {
            const a = (seed % 3) + 2 // 2..4
            const c = ((Math.floor(seed / 3) % 5) + 10) // 10..14
            return {
              prompt: `A quantity obeys $y = ${a}\\sin(x) + ${c}$. Find its maximum value (amplitude + mean value).`,
              answer: String(c + a),
              answerType: 'numeric',
              hint: 'Maximum of $a\\sin(x) + c$ is $a + c$ (for $a > 0$).',
              solution: [
                `Amplitude is $|${a}| = ${a}$, mean value is $${c}$.`,
                `Maximum $= ${c} + ${a} = ${c + a}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-model-min',
          difficulty: 'core',
          instance: {
            prompt:
              'A quantity obeys $y = 3\\sin(x) + 7$. Find its minimum value.',
            answer: '4',
            answerType: 'numeric',
            hint: 'Minimum of $a\\sin(x) + c$ is $c - a$ (for $a > 0$).',
            solution: [
              '$|a| = 3$, mean value $7$.',
              'Minimum $= 7 - 3 = 4$.',
            ],
          },
        },
      ],
    },
  ],
}
