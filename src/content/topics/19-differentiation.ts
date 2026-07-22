import type { Topic } from '../types'
import { signed } from '../../exercises/format'

// Unit 2 · Topic 8 — Derivative as gradient / rate; differentiation rules for
// polynomial functions and applications (stationary points, maxima/minima,
// points of inflection, motion graphs, max/min problems).

export const differentiationTopic: Topic = {
  id: 'differentiation',
  unit: 2,
  order: 8,
  title: 'Differentiation rules & applications',
  blurb:
    'Derivative as gradient and rate of change; differentiation of polynomial functions by rule; applications to stationary points, motion, and max/min problems.',
  dotPoints: ['u2-ca-3', 'u2-ca-4', 'u2-ca-5'],

  lessons: [
    {
      id: 'derivative-interpretations',
      heading: 'Three faces of the derivative',
      summary: 'Slope, gradient function, and rate of change — all the same thing.',
      body: `The derivative $f'(x)$ has three equivalent meanings:

1. **Geometric**: the **gradient of the tangent** to $y = f(x)$ at the point $x$.
2. **Symbolic**: the **gradient function** — the function mapping each $x$ to the tangent gradient there.
3. **Physical**: the **instantaneous rate of change** of $y$ with respect to $x$.

### Relationship to the original graph
Where $f$ is **rising**, $f' > 0$.
Where $f$ is **falling**, $f' < 0$.
Where $f$ has a **horizontal tangent** (turning point or point of inflection), $f' = 0$.
Where $f'$ is **largest** (most positive), $f$ is **steepest uphill**.

### When the derivative does not exist
- Vertical tangent (e.g. $y = \\sqrt[3]{x}$ at $x = 0$).
- Corner (e.g. $|x|$ at $x = 0$).
- Jump in the original function.`,
      examples: [
        {
          id: 'ex-derivative-gives-slope',
          statement:
            "If $f'(3) = 4$, what is the slope of the tangent to $y = f(x)$ at $x = 3$?",
          steps: [
            'The derivative is the slope of the tangent by definition.',
            'So the slope is $4$.',
          ],
        },
        {
          id: 'ex-three-views',
          statement:
            'A ball\'s height $h(t)$ (m, t in s) has $h\\prime(2) = 3$. Interpret this geometrically, symbolically and physically.',
          steps: [
            'Geometric: the tangent at $t = 2$ has slope $3$.',
            'Symbolic: $h\\prime$ takes the value $3$ at $t = 2$.',
            'Physical: at $t = 2$, the ball is rising at $3$ m/s.',
          ],
        },
        {
          id: 'ex-zero-derivative',
          statement:
            'If $f\\prime(2) = 0$, what does that tell you about the graph at $x = 2$?',
          steps: [
            'The tangent at $x = 2$ is horizontal.',
            'That is a stationary point (turning point or horizontal point of inflection).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-sign-reading',
          difficulty: 'intro',
          instance: {
            prompt:
              'If $f\\prime(2) < 0$, what is $f$ doing at $x = 2$? (Answer "increasing" or "decreasing".)',
            answer: 'decreasing',
            answerType: 'exact',
            hint: '$f\\prime > 0$ means rising; $f\\prime < 0$ means falling.',
            solution: [
              'A negative derivative at $x = 2$ means the tangent slopes downwards.',
              'So $f$ is decreasing there.',
            ],
          },
        },
        {
          kind: 'param',
          id: 'p-stationary-meaning',
          difficulty: 'core',
          build: (seed: number) => {
            const descs = [
              'a local maximum',
              'a local minimum',
              'a point of inflection with horizontal tangent',
            ]
            // Cycle through types
            const kind = descs[seed % descs.length]
            return {
              prompt: `At $x = a$, $f\\prime(a) = 0$ and the behaviour around that point means the graph has ${kind}. What does the derivative being zero tell you, alone? (Answer "horizontal tangent", "vertical tangent", or "the function is undefined".)`,
              answer: 'horizontal tangent',
              answerType: 'exact',
              hint: 'A zero slope at a single point means the tangent is flat there.',
              solution: [
                'A derivative of zero means the tangent has slope $0$ — a horizontal tangent.',
                'Distinguishing between a local max, local min, and an inflection point needs more information (the second derivative or values nearby).',
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-f-prime-physical',
          difficulty: 'core',
          instance: {
            prompt:
              'A water tank\'s depth $D(t)$ (m, t in hours) satisfies $D\\prime(0) = 0.05$. What does this mean physically? Answer in a sentence.',
            answer: 'depth rising at 0.05 m/hr',
            answerType: 'exact',
            hint: 'The derivative is an instantaneous rate of change.',
            solution: [
              'At $t = 0$, the depth is rising at $0.05$ metres per hour.',
            ],
          },
        },
      ],
    },

    {
      id: 'poly-derivative',
      heading: 'Polynomials: differentiation by rule',
      summary: 'Power rule term-by-term, plus constant and sum/difference rules.',
      body: `For a polynomial, the derivative is found term-by-term. The key rule is the **power rule**:
$$\\dfrac{d}{dx}\\!\\left[x^n\\right] = n x^{n - 1}, \\quad \\text{for any real } n.$$

### Working rules
- **Constant**: $\\dfrac{d}{dx}(c) = 0$.
- **Multiple of $f$**: $\\dfrac{d}{dx}(k f) = k f'$.
- **Sum**: $(f + g)' = f' + g'$.
- **Difference**: $(f - g)' = f' - g'$.
- **Powers of $x$**: $\\dfrac{d}{dx}(x^n) = n x^{n - 1}$.

### Worked example
$f(x) = 3x^4 - 2x^3 + 5x - 7$.
Term-by-term:
$\\dfrac{d}{dx}(3x^4) = 12x^3$, $\\dfrac{d}{dx}(-2x^3) = -6x^2$, $\\dfrac{d}{dx}(5x) = 5$, $\\dfrac{d}{dx}(-7) = 0$.
So $f'(x) = 12x^3 - 6x^2 + 5$.

### A property: degree drops by 1
A polynomial of degree $n$ always has a derivative of degree $n - 1$ (when $n \\ge 1$).`,
      examples: [
        {
          id: 'ex-power-rule',
          statement: "Differentiate $f(x) = 5x^3 - x + 4$.",
          steps: [
            '$\\dfrac{d}{dx}(5x^3) = 15x^2$.',
            '$\\dfrac{d}{dx}(-x) = -1$.',
            '$\\dfrac{d}{dx}(4) = 0$.',
            '$f\\prime(x) = 15x^2 - 1$.',
          ],
        },
        {
          id: 'ex-quadratic-derivative',
          statement: "Differentiate $f(x) = 3x^2 - 6x + 1$.",
          steps: [
            '$\\dfrac{d}{dx}(3x^2) = 6x$.',
            '$\\dfrac{d}{dx}(-6x) = -6$.',
            '$\\dfrac{d}{dx}(1) = 0$.',
            '$f\\prime(x) = 6x - 6$.',
          ],
        },
        {
          id: 'ex-quartic-derivative',
          statement: "Differentiate $f(x) = x^4$.",
          steps: [
            'Power rule: $\\dfrac{d}{dx}(x^4) = 4x^3$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-power-rule',
          difficulty: 'intro',
          build: (seed: number) => {
            // d/dx (a*x^n) = a*n*x^(n-1). Choose a in [2..5], n in [3..5]
            const a = (seed % 4) + 2 // 2..5
            const n = ((Math.floor(seed / 4)) % 3) + 3 // 3..5
            const newA = a * n
            const newN = n - 1
            const coeffStr = newA === 1 ? '' : `${newA}`
            const xStr = newN === 1 ? 'x' : `x^${newN}`
            return {
              prompt: `Differentiate $y = ${a}x^${n}$.`,
              answer: `${coeffStr}${xStr}`,
              answerType: 'polynomial',
              hint: 'Power rule: $\\frac{d}{dx}(a x^n) = a \\cdot n \\cdot x^{n-1}$.',
              solution: [
                `$\\dfrac{d}{dx}(${a}x^${n}) = ${a} \\cdot ${n} \\cdot x^${n - 1} = ${newA}x^${n - 1}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-derivative-constant',
          difficulty: 'intro',
          instance: {
            prompt:
              'What is the derivative of $f(x) = 7$?',
            answer: '0',
            answerType: 'numeric',
            hint: 'A constant never changes.',
            solution: [
              '$\\dfrac{d}{dx}(7) = 0$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-derivative-cubic',
          difficulty: 'core',
          instance: {
            prompt:
              'Differentiate $f(x) = x^3$. Type the result.',
            answer: '3x^2',
            answerType: 'polynomial',
            hint: 'Power rule: bring down the $3$, drop the exponent to $2$.',
            solution: [
              '$\\dfrac{d}{dx}(x^3) = 3x^2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'stationary-points',
      heading: 'Stationary points & the second derivative',
      summary: 'f′=0 to find candidates; f″ to classify them; inflections.',
      body: `A **stationary point** of $f$ is where $f'(x) = 0$. Stationary points come in three flavours: local **maximum**, local **minimum**, and **horizontal point of inflection**.

### Finding candidates
1. Differentiate to find $f'(x)$.
2. Solve $f'(x) = 0$ for $x$ — these $x$-values are your candidates.

### Classifying with the second derivative
Differentiate again to get the **second derivative** $f''(x)$. For each candidate $x = c$:

- $f''(c) < 0 \\Rightarrow$ **local maximum** (graph is curving $\\frown$).
- $f''(c) > 0 \\Rightarrow$ **local minimum** (graph is curving $\\smile$).
- $f''(c) = 0 \\Rightarrow$ **inconclusive** — could be a point of inflection; check $f'''(c)$.

### Point of inflection (without horizontal tangent)
$f''(x) = 0$ **and** $f''$ changes sign — the curvature changes from concave up to concave down (or vice versa). It's a feature of the curve's shape rather than a stationary point in the usual sense.`,
      examples: [
        {
          id: 'ex-stationary',
          statement:
            "Find and classify the stationary point of $f(x) = x^2 - 4x$. State the $x$-value.",
          steps: [
            "$f'(x) = 2x - 4$.",
            '$f\\prime(x) = 0 \\Rightarrow x = 2$.',
            "$f''(x) = 2 > 0$, so it's a local minimum.",
          ],
        },
        {
          id: 'ex-cubic-stationary',
          statement:
            'Find the stationary points of $f(x) = x^3 - 3x$.',
          steps: [
            "$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x - 1)(x + 1)$.",
            "Stationary points at $x = 1$ and $x = -1$.",
            '$f\\prime\\prime(1) = 6 > 0$, so $x = 1$ is a local minimum.',
            '$f\\prime\\prime(-1) = -6 < 0$, so $x = -1$ is a local maximum.',
          ],
        },
        {
          id: 'ex-second-derivative-test',
          statement:
            'When is the second-derivative test inconclusive? Give one reason.',
          steps: [
            'When $f\\prime\\prime(c) = 0$ — the second derivative alone cannot classify the point.',
            'Need to look at $f\\prime$ sign change (max/min) or higher derivatives (inflection).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-stationary-x',
          difficulty: 'core',
          build: (seed: number) => {
            // f(x) = x^2 - 2 a x  => f'(x) = 2 x - 2 a ; f'(x)=0 at x=a.
            const a = ((seed % 5) + 1) // 1..5
            return {
              prompt: `Find the $x$-value of the stationary point of $f(x) = x^2 - ${2 * a}x$.`,
              answer: String(a),
              answerType: 'numeric',
              hint: "Set $f\\prime(x) = 2x - ${2 * a}$ to zero and solve.",
              solution: [
                `$f\\prime(x) = 2x - ${2 * a}$.`,
                `Set $f\\prime(x) = 0$: $2x = ${2 * a}$, so $x = ${a}$.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-classify',
          difficulty: 'core',
          build: (seed: number) => {
            // f(x) = -x^2 + 2 b x => max at x = b
            // f(x) = x^2 - 2 c x => min at x = c
            const useMax = seed % 2 === 0
            const c = ((Math.floor(seed / 2)) % 5) + 1
            const kind = useMax ? 'local maximum' : 'local minimum'
            return {
              prompt: `Given $f(x) = ${useMax ? '-' : ''}x^2 ${signed(2 * (useMax ? c : -c))}$, classify the stationary point. Answer "local maximum" or "local minimum".`,
              answer: kind,
              answerType: 'exact',
              hint: 'A negative coefficient on $x^2$ gives a downward parabola (max); positive gives min.',
              solution: [
                `The leading coefficient is ${useMax ? 'negative' : 'positive'}, so the parabola opens ${useMax ? 'downwards' : 'upwards'}.`,
                `The stationary point is a ${kind}.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-second-derivative-sign',
          difficulty: 'core',
          instance: {
            prompt:
              'At a stationary point, $f\\prime\\prime(c) > 0$. What kind of point is it? Answer "local maximum", "local minimum", or "point of inflection".',
            answer: 'local minimum',
            answerType: 'exact',
            hint: 'Positive second derivative means concave up.',
            solution: [
              'Concave up at the stationary point → local minimum.',
            ],
          },
        },
      ],
    },

    {
      id: 'max-min-problems',
      heading: 'Maximum & minimum problems',
      summary: 'Build the model, find the stationary point, confirm it lies in the domain.',
      body: `Many applied problems ask for the **maximum or minimum value** of a quantity described by a formula on a specific **modelling domain**. The recipe:

### Recipe
1. **Build the formula** for the quantity to optimise, in terms of one variable.
2. **Identify the domain** — what's physically allowed for that variable?
3. **Differentiate** and set the derivative to zero.
4. **Check both** the stationary point and the **endpoints** of the domain — the global max/min can be at either place.
5. **Justify**: if there's one stationary point in the interior and the function blows up at both endpoints (e.g. very large $|x|$), the stationary point is the global extremum.

### Endpoints matter
A polynomial can have its maximum/minimum at the boundary of the domain, not necessarily where the derivative is zero. Always check the endpoints of a closed interval.`,
      examples: [
        {
          id: 'ex-fence',
          statement:
            'A rectangular paddock uses 200 m of fencing along three sides (one side is a river). Find the maximum area.',
          steps: [
            'Two widths + one length = $200$. If width $= x$ and length $= L$: $2x + L = 200$, so $L = 200 - 2x$.',
            'Area $A = x L = x(200 - 2x) = 200x - 2x^2$.',
            '$A\\prime(x) = 200 - 4x = 0 \\Rightarrow x = 50$.',
            'Substitute back: $L = 200 - 100 = 100$.',
            'Maximum area $= 50 \\cdot 100 = 5000$ m².',
          ],
        },
        {
          id: 'ex-min-perimeter',
          statement:
            'A rectangular field has area $100$ m². Minimise the perimeter if the side parallel to a wall needs no fence.',
          steps: [
            'Let width $= x$, length $= L$, with $xL = 100 \\Rightarrow L = 100/x$.',
            'Paddock fencing (three sides) $= 2x + L = 2x + 100/x$.',
            'Differentiate: $P\\prime(x) = 2 - 100/x^2 = 0 \\Rightarrow x^2 = 50$, $x = \\sqrt{50}$.',
            'Then $L = 100/\\sqrt{50} = \\sqrt{50} \\cdot 2$. So square side: $L = 2x$ (twice the width).',
          ],
        },
        {
          id: 'ex-endpoints-matter',
          statement:
            'Why check endpoints when finding a global max/min?',
          steps: [
            'A stationary point might be a local, not global, extremum.',
            'The true max/min can occur at a domain endpoint.',
            'Compare $f$ at every stationary point AND every endpoint.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-paddock',
          difficulty: 'challenge',
          build: (seed: number) => {
            // Open-top box.  Volume = V = L W H, with L,W material from a fixed L,W sheet.
            // Simpler: rectangular strip problem — perimeter problem.
            // P = 2L + W, A = L*W.
            // Maximise area given P=2L+W=p for fixed p.
            // A = L(p - 2L) = pL - 2L^2. Maximised at L = p/4, gives max area = p^2/8.
            const p = (seed % 3 + 1) * 40 // 40, 80, 120
            const L = p / 4
            const W = p - 2 * L
            const area = L * W
            return {
              prompt: `A rectangle has perimeter ${p} m, and one side is fixed (a wall). Let the perpendicular side have length $L$ and the side parallel to the wall have length $W = ${p} - 2L$. Area is $A = L \\cdot W = L(${p} - 2L)$. Find the maximum area, in m².`,
              answer: String(area),
              answerType: 'numeric',
              hint: "Maximise $A = ${p}L - 2L^2$. Set $A'(L) = 0$ and solve.",
              solution: [
                `$A = ${p}L - 2L^2$.`,
                `$A'(L) = ${p} - 4L = 0 \\Rightarrow L = ${L}$.`,
                `$W = ${p} - 2 \\cdot ${L} = ${W}$.`,
                `Max area $= ${L} \\cdot ${W} = ${area}$ m².`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-check-endpoints',
          difficulty: 'intro',
          instance: {
            prompt:
              'When finding the maximum of $f$ on a closed interval $[a, b]$, you should compare $f$ at stationary points and at the endpoints. True or false? Answer "true" or "false".',
            answer: 'true',
            answerType: 'exact',
            hint: 'A global max can occur at an endpoint.',
            solution: [
              'True — the max can be at a stationary point or an endpoint, and you must check both.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-paddock-quick',
          difficulty: 'core',
          instance: {
            prompt:
              'A rectangular paddock with 3 sides uses 60 m of fencing. The area is maximised when the length parallel to the wall is (in m):',
            answer: '30',
            answerType: 'numeric',
            hint: 'Optimal: $L = 2x$ where $2x + L = 60$.',
            solution: [
              'Optimum is at $L = 2x$, so $2x + 2x = 60 \\Rightarrow x = 15, L = 30$.',
            ],
          },
        },
      ],
    },

    {
      id: 'motion-graphs',
      heading: 'Motion graphs & calculus',
      summary: 'Reading velocity from s-t, and acceleration from v-t.',
      body: `For motion along a line with displacement $s$ as a function of time $t$:

- **Velocity** $v(t) = s'(t)$ — the gradient of the displacement graph.
- **Acceleration** $a(t) = v'(t) = s''(t)$ — the gradient of the velocity graph.

### Reading from graphs
- On an **s–t** graph: steepness means speed. Flat sections mean stationary.
- On a **v–t** graph: the height of the graph is the speed; the gradient of the graph is the acceleration.
- A horizontal v–t line means **constant velocity** ($a = 0$).
- A v–t line through zero means **changing direction** at that instant.

### Turning points on the s–t graph
$s'(t) = 0$ gives moments where the object is instantaneously stationary — turning points on the displacement graph.`,
      examples: [
        {
          id: 'ex-velocity-from-s',
          statement:
            "The displacement of a particle is $s(t) = t^3 - 3t$ metres, $t$ in seconds. Find the velocity at $t = 2$.",
          steps: [
            "$s'(t) = 3t^2 - 3$.",
            '$v(2) = 3(4) - 3 = 9$ m/s.',
          ],
        },
        {
          id: 'ex-accel',
          statement:
            "For $s(t) = 4t^2 + t$, find the acceleration at $t = 3$.",
          steps: [
            "$v(t) = s'(t) = 8t + 1$.",
            "$a(t) = v'(t) = 8$.",
            "Acceleration is constant $8$ m/s².",
          ],
        },
        {
          id: 'ex-direction-change',
          statement:
            "Find when the direction of motion changes for $s(t) = t^2 - 4t + 1$.",
          steps: [
            "$v(t) = 2t - 4 = 0 \\Rightarrow t = 2$.",
            "At $t = 2$, velocity is zero — direction reverses.",
            "This is a turning point on the displacement graph.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-velocity',
          difficulty: 'core',
          build: (seed: number) => {
            // s(t) = a*t^2 + b (or similar). Pick something that makes v(t0) clean.
            const a = (seed % 3) + 2 // 2..4
            const t0 = (Math.floor(seed / 3) % 4) + 1 // 1..4
            // s(t) = a t^2 ; v(t) = 2 a t ; v(t0) = 2 a t0
            const v = 2 * a * t0
            return {
              prompt: `For motion with $s(t) = ${a}t^2$ metres, $t$ in seconds, find the velocity at $t = ${t0}$.`,
              answer: String(v),
              answerType: 'numeric',
              hint: 'Velocity is $v(t) = s\\prime(t)$.',
              solution: [
                `$v(t) = \\dfrac{d}{dt}(${a}t^2) = ${2 * a}t$.`,
                `$v(${t0}) = ${2 * a} \\cdot ${t0} = ${v}$ m/s.`,
              ],
            }
          },
        },
        {
          kind: 'param',
          id: 'p-stationary-s',
          difficulty: 'core',
          build: (seed: number) => {
            // s(t) = t^2 - 2 a t => v(t) = 2t - 2 a ; stationary at t = a
            const a = ((seed % 5)) + 1 // 1..5
            return {
              prompt: `For motion with $s(t) = t^2 - ${2 * a}t$, find the smallest positive $t$ at which the object is instantaneously stationary.`,
              answer: String(a),
              answerType: 'numeric',
              hint: "Set $v(t) = s'(t) = 0$ and solve.",
              solution: [
                `$v(t) = 2t - ${2 * a}$.`,
                `Set $v(t) = 0$: $2t = ${2 * a}$, so $t = ${a}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-direction-reversal',
          difficulty: 'core',
          instance: {
            prompt:
              'An object has $s(t) = t^3 - 12t$. At what $t$ does it change direction?',
            answer: '2',
            answerType: 'numeric',
            hint: 'Direction changes when $v(t) = s\\prime(t) = 0$.',
            solution: [
              '$v(t) = 3t^2 - 12 = 0 \\Rightarrow t^2 = 4 \\Rightarrow t = 2$.',
            ],
          },
        },
      ],
    },

    {
      id: 'inflection',
      heading: 'Points of inflection',
      summary: 'Where the curvature flips — f″(c) = 0 and f″ changes sign.',
      body: `A **point of inflection** on the graph of $f$ is a point at which the graph changes its **curvature** — concave-up becomes concave-down, or vice versa.

### Locating inflections
1. Differentiate twice to get $f''(x)$.
2. Solve $f''(x) = 0$ — these are your candidates.
3. **Test sign change** of $f''$ on either side of each candidate. The curvature must change sign.
4. (Optional with the second derivative test for stationary points.) A **point of inflection with horizontal tangent** also satisfies $f'(c) = 0$ **and** $f''(c) = 0$.

### Why it matters
Inflections are where the **rate of change is itself changing in nature** — the rate was accelerating (in the sense of how fast it was changing) until this moment, and then starts decelerating (or vice versa). For example, a graph of population growth often has an inflection at the moment growth is fastest.`,
      examples: [
        {
          id: 'ex-inflection',
          statement:
            "Locate the point of inflection of $f(x) = x^3$. State its $x$-value.",
          steps: [
            "$f'(x) = 3x^2$. $f''(x) = 6x$.",
            '$f\\prime\\prime(x) = 0 \\Rightarrow x = 0$.',
            '$f\\prime\\prime(x) < 0$ for $x < 0$ and $f\\prime\\prime(x) > 0$ for $x > 0$ — curvature changes sign.',
            'Point of inflection at $x = 0$.',
          ],
        },
        {
          id: 'ex-quartic-inflection',
          statement:
            "Locate any inflection points of $f(x) = x^4 - 6x^2$.",
          steps: [
            "$f'(x) = 4x^3 - 12x$, $f''(x) = 12x^2 - 12 = 12(x^2 - 1)$.",
            "$f''(x) = 0 \\Rightarrow x = \\pm 1$.",
            "Sign of $f''$: positive for $|x| > 1$, negative for $|x| < 1$ — changes at both, so both are inflection points.",
          ],
        },
        {
          id: 'ex-inflection-not-stationary',
          statement:
            'Is a point of inflection always a stationary point? Give a one-sentence reason.',
          steps: [
            'No — a point of inflection needs $f\\prime\\prime = 0$ and a sign change of $f\\prime\\prime$, but $f\\prime$ need not be $0$.',
            'E.g. $y = x^3 + x$ has $f\\prime\\prime(0) = 0$ and is an inflection at $0$, but $f\\prime(0) = 1 \\ne 0$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-inflection-cubic',
          difficulty: 'core',
          build: (seed: number) => {
            // f(x) = a x^3 + b ; inflection at x = 0 (always).
            // To make it non-trivial: f(x) = (x - a)^3 + c, inflection at x = a.
            const a = ((seed % 5) - 2) || 2 // -2..2 (skip 0)
            return {
              prompt: `Locate the point of inflection of $f(x) = (x ${signed(-a)})^3$. State its $x$-value.`,
              answer: String(a),
              answerType: 'numeric',
              hint: "$f''(x) = 6(x - a). Set this to zero.",
              solution: [
                `Expanding $f$ gives a cubic with the same shape as $x^3$ shifted horizontally by $a$.`,
                `The inflection is at $x = ${a}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-quartic-inflection-x',
          difficulty: 'core',
          instance: {
            prompt:
              'For $f(x) = x^4 - 6x^2$, state the smallest positive $x$-value of an inflection point.',
            answer: '1',
            answerType: 'numeric',
            hint: '$f\\prime\\prime(x) = 12x^2 - 12 = 12(x - 1)(x + 1)$.',
            solution: [
              '$f\\prime\\prime(x) = 0 \\Rightarrow x = \\pm 1$.',
              'Smallest positive is $1$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-inflection-conditions',
          difficulty: 'core',
          instance: {
            prompt:
              'A point of inflection requires $f\\prime\\prime = 0$ **and** what else?',
            answer: 'f sign changes',
            answerType: 'exact',
            hint: 'The curvature has to flip.',
            solution: [
              '$f\\prime\\prime$ must change sign at the candidate — the curvature must flip.',
            ],
          },
        },
      ],
    },
  ],
}
