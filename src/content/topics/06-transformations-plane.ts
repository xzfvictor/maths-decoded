import type { Topic } from '../types'
import { signed } from '../../exercises/format'

// Unit 1 · Topic 6 — Transformations of the plane, and using parameters to
// represent families of functions / find rules from given information.

export const transformationsPlane: Topic = {
  id: 'transformations-plane',
  unit: 1,
  order: 6,
  title: 'Transformations of the plane',
  blurb:
    'Dilations, reflections and translations applied to basic graphs, using parameters to describe families of functions, and finding a rule from given information.',
  dotPoints: ['u1-al-4', 'u1-al-5'],

  lessons: [
    {
      id: 'translations',
      heading: 'Translations',
      summary: 'Shifting a graph horizontally and vertically, and the horizontal sign flip.',
      body: `A **translation** slides a graph without changing its shape or orientation. Starting from $y = f(x)$:

- $y = f(x) + c$ shifts the graph **up** by $c$ (down if $c < 0$).
- $y = f(x - h)$ shifts the graph **right** by $h$ (left if $h < 0$).

### The horizontal sign flip
Horizontal shifts feel backwards: replacing $x$ with $x - h$ moves the graph **right**, and $x + h$ moves it **left**. Think "what value of $x$ makes the bracket zero?" — for $f(x - 3)$ the graph's features occur $3$ units later, i.e. shifted right.

### Effect on points
A translation of "right $h$, up $c$" sends each point $(x, y) \\mapsto (x + h,\\ y + c)$.`,
      examples: [
        {
          id: 'ex-translate-point',
          statement:
            'The point $(2, 5)$ is on $y = f(x)$. Where does it move on $y = f(x - 3) + 1$?',
          steps: [
            'The rule $f(x - 3) + 1$ shifts the graph right $3$ and up $1$.',
            'Apply to the point: $(2, 5) \\mapsto (2 + 3,\\ 5 + 1)$.',
            'The image is $(5, 6)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-translate-point',
          difficulty: 'core',
          build: (seed) => {
            const x = ((seed % 7) - 3) // -3..3
            const y = ((Math.floor(seed / 7) % 7) - 3)
            const h = ((Math.floor(seed / 49) % 5) - 2) || 2 // right shift
            const c = ((Math.floor(seed / 5) % 5) - 2) || 1 // up shift
            return {
              prompt: `The point $(${x}, ${y})$ lies on $y = f(x)$. Find its image on $y = f(x ${signed(-h)}) ${signed(c)}$ as $(p, q)$.`,
              answer: `(${x + h},${y + c})`,
              answerType: 'exact',
              hint: `$f(x - h) + c$ shifts right by $h$ and up by $c$.`,
              solution: [
                `The graph is shifted right $${h}$ and up $${c}$.`,
                `$(${x}, ${y}) \\mapsto (${x} + ${h},\\ ${y} + ${c}) = (${x + h}, ${y + c})$.`,
              ],
            }
          },
        },
      ],
    },

    {
      id: 'dilations-reflections',
      heading: 'Dilations & reflections',
      summary: 'Stretching from an axis, and flipping in an axis.',
      body: `### Dilations (stretches)
A **dilation** scales distances from an axis.
- $y = a\\,f(x)$ is a dilation by factor $a$ **from the $x$-axis** (parallel to the $y$-axis): each $y$-coordinate is multiplied by $a$. $(x, y) \\mapsto (x, ay)$.
- $y = f(nx)$ is a dilation by factor $\\dfrac{1}{n}$ **from the $y$-axis** (parallel to the $x$-axis): each $x$-coordinate is divided by $n$. $(x, y) \\mapsto (\\tfrac{x}{n}, y)$.

The second one is counter-intuitive: $f(2x)$ **compresses** horizontally by a factor of $2$.

### Reflections
- $y = -f(x)$ reflects in the **$x$-axis** (flips top-to-bottom): $(x, y) \\mapsto (x, -y)$.
- $y = f(-x)$ reflects in the **$y$-axis** (flips left-to-right): $(x, y) \\mapsto (-x, y)$.

### Order matters
When several transformations combine in $a\\,f(n(x + b)) + c$, apply dilations/reflections **before** translations to track a point correctly.`,
      examples: [
        {
          id: 'ex-dilation-point',
          statement: 'Under $y = 3f(x)$, where does $(4, -2)$ move?',
          steps: [
            '$y = 3f(x)$ is a dilation of factor $3$ from the $x$-axis: multiply the $y$-coordinate by $3$.',
            '$(4, -2) \\mapsto (4,\\ 3 \\times -2)$.',
            'The image is $(4, -6)$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-dilate-point',
          difficulty: 'core',
          build: (seed) => {
            const x = ((seed % 5) - 2) || 1
            const y = ((Math.floor(seed / 5) % 5) - 2) || 1
            const a = (seed % 3) + 2 // 2..4
            return {
              prompt: `Under the dilation $y = ${a}f(x)$, find the image of $(${x}, ${y})$ as $(p, q)$.`,
              answer: `(${x},${a * y})`,
              answerType: 'exact',
              hint: 'Dilation by $a$ from the $x$-axis multiplies the $y$-coordinate by $a$.',
              solution: [
                `The $x$-coordinate is unchanged; the $y$-coordinate is multiplied by $${a}$.`,
                `$(${x}, ${y}) \\mapsto (${x},\\ ${a} \\times ${y}) = (${x}, ${a * y})$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-reflect-axis',
          difficulty: 'intro',
          instance: {
            prompt:
              'Which transformation does $y = f(-x)$ represent? Answer "reflection in the x-axis" or "reflection in the y-axis".',
            answer: 'reflection in the y-axis',
            answerType: 'exact',
            hint: 'Replacing $x$ with $-x$ swaps left and right.',
            solution: [
              'Replacing $x$ by $-x$ sends $(x, y)$ to $(-x, y)$.',
              'That is a reflection in the $y$-axis.',
            ],
          },
        },
      ],
    },

    {
      id: 'families-rules',
      heading: 'Families of functions & finding rules',
      summary: 'Parameters describe families; given information pins down the rule.',
      body: `A **parameter** is a letter standing for a constant that can vary, describing a whole **family** of functions at once.

- $y = mx + c$ is the family of all straight lines; choosing $m$ and $c$ selects one.
- $y = a(x - h)^2 + k$ is the family of all parabolas.

### Finding a specific rule
To pin down the parameters you need as many independent pieces of information as there are unknowns. Each known point or feature gives one equation.

**Strategy**
1. Write the general form for the family.
2. Substitute each given fact (a point, an intercept, a turning point) to get equations.
3. Solve for the parameters.

### Example set-up
"A parabola has turning point $(2, -1)$ and passes through $(0, 7)$." Use $y = a(x - 2)^2 - 1$ (turning-point form encodes the vertex), then substitute $(0, 7)$ to find $a$.`,
      examples: [
        {
          id: 'ex-find-parabola',
          statement:
            'Find the rule of the parabola with turning point $(2, -1)$ passing through $(0, 7)$.',
          steps: [
            'Turning-point form: $y = a(x - 2)^2 - 1$.',
            'Substitute $(0, 7)$: $7 = a(0 - 2)^2 - 1 = 4a - 1$.',
            'Solve: $4a = 8$, so $a = 2$.',
            'The rule is $y = 2(x - 2)^2 - 1$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-find-a',
          difficulty: 'core',
          build: (seed) => {
            const h = ((seed % 5) - 2) || 2 // -2..2 vertex x, avoid 0
            const k = ((Math.floor(seed / 5) % 5) - 2) || -2 // vertex y, avoid 0
            const a = (seed % 3) + 1 // 1..3
            // passes through (h+1, k + a*1) -> choose point x0 = h + 2 to make it non-trivial
            const x0 = h + 2
            const y0 = a * (x0 - h) * (x0 - h) + k // = 4a + k
            return {
              prompt: `A parabola has turning point $(${h}, ${k})$ and passes through $(${x0}, ${y0})$. Find the dilation factor $a$ in $y = a(x ${signed(-h)})^2 ${signed(k)}$.`,
              answer: String(a),
              answerType: 'numeric',
              hint: 'Substitute the given point into $y = a(x - h)^2 + k$ and solve for $a$.',
              solution: [
                `Substitute $(${x0}, ${y0})$: $${y0} = a(${x0} ${signed(-h)})^2 ${signed(k)}$.`,
                `$${y0} = a(${x0 - h})^2 ${signed(k)} = ${(x0 - h) * (x0 - h)}a ${signed(k)}$.`,
                `Solve: $${(x0 - h) * (x0 - h)}a = ${y0 - k}$, so $a = ${a}$.`,
              ],
            }
          },
        },
        {
          kind: 'curated',
          id: 'c-line-through-points',
          difficulty: 'core',
          instance: {
            prompt:
              'A line $y = mx + c$ passes through $(0, 3)$ and $(2, 11)$. Find $m$.',
            answer: '4',
            answerType: 'numeric',
            hint: 'The gradient is the rise over the run between the two points.',
            solution: [
              '$m = \\dfrac{11 - 3}{2 - 0} = \\dfrac{8}{2} = 4$.',
              '(And $c = 3$ from the point $(0, 3)$, giving $y = 4x + 3$.)',
            ],
          },
        },
      ],
    },
  ],
}
