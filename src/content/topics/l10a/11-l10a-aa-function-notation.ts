import type { Topic } from '../../types'

// Foundation (Year 10A) · Strand: Algebra · l10a-aa-8 (VC2M10AA08).
// Use function notation to describe the relationship between dependent
// and independent variables in modelling contexts.

export const l10aAaFunctionNotation: Topic = {
  id: 'l10a-aa-function-notation',
  unit: '10A',
  order: 11,
  title: 'Function notation in modelling',
  blurb:
    'Use function notation to describe the relationship between dependent and independent variables in modelling contexts.',
  dotPoints: ['l10a-aa-8'],

  lessons: [
    {
      id: 'function-notation-basics',
      heading: 'Function notation: f(x)',
      summary: 'f(x) is the value of function f at input x — readable shorthand for "y" in y = f(x).',
      body: `Instead of writing "the value of $y$ when $x = 2$" in a model, maths uses shorthand: $f(2)$.

### Reading function notation
$f(x)$ means **the output of function $f$ at input $x$**. If the rule is $f(x) = 3x + 1$:
- $f(2) = 3 \\cdot 2 + 1 = 7$ — read as "$f$ of $2$ equals $7$".
- $f(-1) = 3 \\cdot (-1) + 1 = -2$.
- $f(0) = 1$ (the $y$-intercept).

### Why it matters for modelling
A model names the relationship, then asks **"what is $f$ at this input?"** instead of substituting a single $x$-value.

### Common conventions
- $f$ is the most common function name.
- $g, h, V, A, P$ are also used, often picked to hint at the quantity.
- The **input** variable does not have to be $x$ — it can be $t$ (time), $A$ (amplitude), $r$ (radius). Whatever makes the model clear.`,
      examples: [
        {
          id: 'ex-eval',
          statement: 'For $f(x) = 3x + 5$, find $f(4)$.',
          steps: [
            'Substitute $x = 4$.',
            '$f(4) = 3 \\cdot 4 + 5 = 17$.',
          ],
        },
        {
          id: 'ex-multi-fns',
          statement:
            'For $g(t) = 10 - 2t$, find $g(3)$.',
          steps: [
            'Substitute $t = 3$.',
            '$g(3) = 10 - 6 = 4$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-eval',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $f(x) = 2x - 7$, find $f(5)$. State the integer answer.',
            answer: '3',
            answerType: 'numeric',
            hint: 'Substitute $x = 5$.',
            solution: [
              '$f(5) = 2 \\cdot 5 - 7 = 10 - 7 = 3$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-time',
          difficulty: 'core',
          instance: {
            prompt:
              "For the model $h(t) = 30 - 5t$, find $h(4)$.",
            answer: '10',
            answerType: 'numeric',
            hint: 'Substitute $t = 4$.',
            solution: [
              '$h(4) = 30 - 5 \\cdot 4 = 30 - 20 = 10$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-solve',
          difficulty: 'challenge',
          instance: {
            prompt:
              'For $f(x) = 4x + 1$, find $x$ such that $f(x) = 21$. State the integer.',
            answer: '5',
            answerType: 'numeric',
            hint: 'Solve $4x + 1 = 21$.',
            solution: [
              '$4x = 20 \\Rightarrow x = 5$. So $f(5) = 21$.',
            ],
          },
        },
      ],
    },

    {
      id: 'modelling-with-notation',
      heading: 'Building models in function notation',
      summary: 'Pick variable names that match the context (V for volume, P for population), then state the model as V(t) = …',
      body: `In a **modelling context**, function notation lets the variable name hint at the quantity being modelled.

### Examples of contextual function names
- $V(r) = \\tfrac{4}{3} \\pi r^3$ — volume of a sphere of radius $r$.
- $A(w) = w(\\ell - 2w)$ — area of a path of width $w$ inside a fixed region.
- $P(t) = 100 \\cdot (1.05)^t$ — population after $t$ years at $5\\%$ growth.
- $C(n) = 5n + 20$ — cost in dollars for $n$ hours of work.

### Recipe for building a model
1. **Identify the input** (independent variable) and give it a meaningful letter.
2. **Identify the output** (dependent variable) and write it as a function of the input.
3. **Translate** the relationship into a formula.
4. **Evaluate** at chosen inputs to answer the modelled questions.

### Key feature: dependent vs independent
The input is the **independent** variable. The output is the **dependent** variable — its value depends on the input. In $P(t) = 100 \\cdot 1.05^t$, $t$ is independent, $P$ is dependent.`,
      examples: [
        {
          id: 'ex-volume',
          statement:
            'A spherical balloon has volume $V(r) = \\tfrac{4}{3} \\pi r^3$ in cm³. Find the volume when $r = 3$. Use $\\pi \\approx 3.14$.',
          steps: [
            'Substitute $r = 3$.',
            '$V(3) = \\tfrac{4}{3} \\cdot 3.14 \\cdot 27 = 4 \\cdot 3.14 \\cdot 9 = 113.04$ cm³.',
          ],
        },
        {
          id: 'ex-pop',
          statement:
            'A city has population $P(t) = 25000 \\cdot (1.03)^t$. Find $P(10)$ rounded to the nearest 100.',
          steps: [
            'Substitute $t = 10$: $P(10) = 25000 \\cdot (1.03)^{10}$.',
            '$1.03^{10} \\approx 1.3439$. So $P(10) \\approx 33598$, rounded to nearest $100$ is $33600$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-volume',
          difficulty: 'intro',
          instance: {
            prompt:
              'For $V(r) = \\tfrac{4}{3} \\pi r^3$, find $V(6)$ with $\\pi = 3.14$. Round to the nearest integer.',
            answer: '904',
            answerType: 'numeric',
            hint: '$\\tfrac{4}{3} \\cdot 3.14 \\cdot 6^3 = \\tfrac{4}{3} \\cdot 3.14 \\cdot 216$.',
            solution: [
              '$V(6) = \\tfrac{4}{3} \\cdot 3.14 \\cdot 216 = 904.32$; nearest integer $= 904$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-cost',
          difficulty: 'core',
          instance: {
            prompt:
              'A taxi fare is $C(d) = 3 + 2.50d$ dollars for $d$ km travelled. Find $C(8)$.',
            answer: '23',
            answerType: 'numeric',
            hint: 'Substitute $d = 8$.',
            solution: [
              '$C(8) = 3 + 2.5 \\cdot 8 = 3 + 20 = 23$ dollars.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-compound',
          difficulty: 'challenge',
          instance: {
            prompt:
              'A principal of $\\$500$ earns interest so that $A(t) = 500 \\cdot (1.04)^t$ in dollars. Find $A(3)$ rounded to the nearest dollar.',
            answer: '562',
            answerType: 'numeric',
            hint: '$500 \\cdot 1.04^3$.',
            solution: [
              '$1.04^3 = 1.124864$. So $A(3) \\approx 562.43$, rounded to $562$.',
            ],
          },
        },
      ],
    },
  ],
}
