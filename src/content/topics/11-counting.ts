import type { Topic } from '../types'

// Fully authored exemplar topic (Unit 1). Counting techniques, split into lessons.

function factorial(n: number): number {
  let r = 1
  for (let i = 2; i <= n; i++) r *= i
  return r
}
function nCr(n: number, r: number): number {
  if (r < 0 || r > n) return 0
  return factorial(n) / (factorial(r) * factorial(n - r))
}
function gcd(x: number, y: number): number {
  return y === 0 ? x : gcd(y, x % y)
}

export const countingTechniques: Topic = {
  id: 'counting',
  unit: 1,
  order: 11,
  title: 'Counting techniques',
  blurb:
    'Addition and multiplication principles, arrangements, combinations (nCr), and applying counting to probability.',
  dotPoints: ['u1-pr-3', 'u1-pr-4'],

  lessons: [
    // ------------------------------------------------------------------ lesson 1
    {
      id: 'principles',
      heading: 'Addition and multiplication principles',
      summary: 'The "and" rule vs the "or" rule for counting.',
      body: `Counting problems ask "in how many ways can this happen?" Two principles do most of the work.

### Multiplication principle
If a task is made of a sequence of stages, and stage 1 can be done in $n_1$ ways, stage 2 in $n_2$ ways, and so on, then the whole task can be done in
$$n_1 \\times n_2 \\times \\cdots \\times n_k$$
ways. Use it when you make a choice **and then** another choice ("this **and** that").

### Addition principle
If a task can be done by one of several **mutually exclusive** methods — $n_1$ ways using method A **or** $n_2$ ways using method B (with no overlap) — then the number of ways is
$$n_1 + n_2 + \\cdots$$
Use it for "this **or** that" where the options don't overlap.`,
      examples: [
        {
          id: 'ex-mult-principle',
          statement:
            'A cafe offers 3 breads, 4 fillings and 2 sauces. How many different sandwiches (one of each) are possible?',
          steps: [
            'Choosing a sandwich is a sequence of three independent choices, so use the multiplication principle.',
            'Bread AND filling AND sauce: $3 \\times 4 \\times 2$.',
            'That gives $24$ possible sandwiches.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-mult-principle',
          difficulty: 'intro',
          build: (seed) => {
            const a = (seed % 4) + 2 // 2..5
            const b = (Math.floor(seed / 4) % 4) + 2
            const c = (Math.floor(seed / 16) % 3) + 2
            return {
              prompt: `A meal has ${a} choices of entree, ${b} choices of main and ${c} choices of dessert. How many different three-course meals are possible?`,
              answer: String(a * b * c),
              answerType: 'numeric',
              hint: 'One choice for each course — multiply the options.',
              solution: [
                'Entree AND main AND dessert, so use the multiplication principle.',
                `$${a} \\times ${b} \\times ${c} = ${a * b * c}$.`,
              ],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 2
    {
      id: 'arrangements',
      heading: 'Arrangements (order matters)',
      summary: 'Permutations: n! and ⁿPr when order counts.',
      body: `An **arrangement** (or permutation) counts orderings, where a different order counts as a different outcome.

- The number of ways to arrange $n$ distinct objects in a row is $n! = n \\times (n-1) \\times \\cdots \\times 2 \\times 1$.
- The number of ways to arrange $r$ objects chosen from $n$ distinct objects is
$$^nP_r = \\frac{n!}{(n-r)!}.$$

By convention $0! = 1$. Arrangements answer questions like "how many ways can 4 people line up?" ($4! = 24$).`,
      examples: [
        {
          id: 'ex-arrange',
          statement: 'In how many ways can 5 different books be arranged on a shelf?',
          steps: [
            'Order matters, and we use all 5 books, so this is $5!$.',
            '$5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-arrange-n',
          difficulty: 'intro',
          build: (seed) => {
            const n = (seed % 4) + 3 // 3..6
            return {
              prompt: `In how many ways can ${n} different people line up in a row?`,
              answer: String(factorial(n)),
              answerType: 'numeric',
              hint: 'All $n$ people, order matters — that is $n!$.',
              solution: [`Arrange all ${n}: $${n}! = ${factorial(n)}$.`],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 3
    {
      id: 'combinations',
      heading: 'Combinations (order does not matter)',
      summary: 'Selections and ⁿCr, and when to use it instead of an arrangement.',
      body: `A **combination** counts **selections**, where the order of the chosen items does not matter. The number of ways to choose $r$ objects from $n$ distinct objects is
$$^nC_r = \\binom{n}{r} = \\frac{n!}{r!\\,(n-r)!}.$$

The extra $r!$ in the denominator (compared with $^nP_r$) removes the duplicate orderings of the same selection. Key facts:

- $\\binom{n}{0} = \\binom{n}{n} = 1$ — one way to choose none, one way to choose all.
- $\\binom{n}{r} = \\binom{n}{n-r}$ — choosing which $r$ to include is the same as choosing which $n-r$ to leave out.

**Rule of thumb:** if rearranging the chosen items gives a genuinely different outcome, use an arrangement; if not, use a combination. "Choose a committee of 3" is a combination; "elect a president, secretary and treasurer" is an arrangement.`,
      examples: [
        {
          id: 'ex-combination',
          statement: 'In how many ways can a committee of 3 be chosen from 7 people?',
          steps: [
            'Order does not matter for a committee, so this is a combination.',
            'Compute $\\binom{7}{3} = \\dfrac{7!}{3!\\,4!}$.',
            '$= \\dfrac{7 \\times 6 \\times 5}{3 \\times 2 \\times 1} = \\dfrac{210}{6} = 35$.',
            'There are $35$ possible committees.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-order-matters',
          difficulty: 'intro',
          instance: {
            prompt:
              'Electing a president, secretary and treasurer from a club: is this a combination or an arrangement? (Answer "combination" or "arrangement")',
            answer: 'arrangement',
            answerType: 'exact',
            hint: 'Does swapping who holds which role change the outcome?',
            solution: [
              'The three roles are distinct, so president–secretary–treasurer differs from secretary–president–treasurer.',
              'Because order (which role) matters, this is an arrangement (permutation), not a combination.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-ncr-symmetry',
          difficulty: 'core',
          instance: {
            prompt: 'Using $\\binom{n}{r} = \\binom{n}{n-r}$, evaluate $\\binom{10}{8}$.',
            answer: '45',
            answerType: 'numeric',
            hint: '$\\binom{10}{8} = \\binom{10}{2}$, which is easier to compute.',
            solution: ['$\\binom{10}{8} = \\binom{10}{2} = \\dfrac{10 \\times 9}{2 \\times 1} = 45$.'],
          },
        },
        {
          kind: 'param',
          id: 'p-choose-committee',
          difficulty: 'core',
          build: (seed) => {
            const n = (seed % 6) + 5 // 5..10
            const r = (Math.floor(seed / 6) % 3) + 2 // 2..4
            const val = nCr(n, r)
            return {
              prompt: `In how many ways can a group of ${r} be chosen from ${n} people?`,
              answer: String(val),
              answerType: 'numeric',
              hint: 'A group has no order, so use $\\binom{n}{r} = \\dfrac{n!}{r!(n-r)!}$.',
              solution: [
                `Order does not matter, so compute $\\binom{${n}}{${r}}$.`,
                `$\\binom{${n}}{${r}} = \\dfrac{${n}!}{${r}!\\,${n - r}!} = ${val}$.`,
              ],
            }
          },
        },
      ],
    },

    // ------------------------------------------------------------------ lesson 4
    {
      id: 'to-probability',
      heading: 'Applying counting to probability',
      summary: 'Favourable ÷ total, using combinations for selections.',
      body: `For an experiment where every outcome is **equally likely**,
$$\\Pr(\\text{event}) = \\frac{\\text{number of favourable outcomes}}{\\text{total number of outcomes}}.$$

Counting techniques let you compute the numerator and denominator when listing them all would be impractical. A common pattern for "selecting without regard to order" uses combinations on the top (ways to pick the favourable items) and bottom (ways to pick any group of that size).

For example, the probability of drawing 2 red counters from a bag of reds and blues uses $\\binom{\\text{reds}}{2}$ on top and $\\binom{\\text{total}}{2}$ on the bottom.`,
      examples: [
        {
          id: 'ex-prob-with-counting',
          statement:
            'A bag has 5 red and 3 blue counters. Two are drawn at random without replacement. Find the probability both are red.',
          steps: [
            'Total ways to choose any 2 of the 8 counters: $\\binom{8}{2} = 28$.',
            'Ways to choose 2 of the 5 red counters: $\\binom{5}{2} = 10$.',
            'Since all selections are equally likely, $\\Pr(\\text{both red}) = \\dfrac{10}{28} = \\dfrac{5}{14}$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'param',
          id: 'p-prob-all-red',
          difficulty: 'challenge',
          build: (seed) => {
            const red = (seed % 4) + 3 // 3..6
            const blue = (Math.floor(seed / 4) % 3) + 2 // 2..4
            const total = red + blue
            const favourable = nCr(red, 2)
            const all = nCr(total, 2)
            const g = gcd(favourable, all)
            return {
              prompt: `A bag has ${red} red and ${blue} blue counters. Two are drawn at random without replacement. Find the probability both are red. Give your answer as a fraction $a/b$ in simplest form.`,
              answer: `${favourable / g}/${all / g}`,
              answerType: 'exact',
              hint: 'Favourable = ways to pick 2 reds; total = ways to pick any 2. Use combinations.',
              solution: [
                `Total ways to choose 2 of ${total}: $\\binom{${total}}{2} = ${all}$.`,
                `Ways to choose 2 of the ${red} red: $\\binom{${red}}{2} = ${favourable}$.`,
                `$\\Pr(\\text{both red}) = \\dfrac{${favourable}}{${all}} = \\dfrac{${favourable / g}}{${all / g}}$.`,
              ],
            }
          },
        },
      ],
    },
  ],
}
