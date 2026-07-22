import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Probability · VC2M10P01.
// Use the language of "if … then …", "given", "of" and "knowing that" to
// investigate conditional statements and identify common mistakes in
// interpreting such language, and involving conditional probability;
// design and conduct simulations using digital tools to model conditional
// probability and interpret results.

export const probabilityConditional: Topic = {
  id: 'm10-probability-conditional',
  unit: 10,
  order: 6,
  title: 'Conditional probability & simulation',
  blurb:
    'Read conditional language carefully, set up two-way tables / tree diagrams, and use simulation to estimate conditional probabilities.',
  dotPoints: ['m10-p-1'],

  lessons: [
    {
      id: 'conditional-language',
      heading: 'Reading conditional language',
      summary: 'Spot the difference between "given" and "of" — they swap the conditional direction.',
      body: `Conditional language is everywhere in probability, but two common phrases have **opposite** directions:

### "$\\Pr(A \\mid B)$" vs "$\\Pr(B \\mid A)$"
- **$\\Pr(A \\text{ given } B)$**: $B$ has happened, what's the chance of $A$ next? *Reduce the sample space to $B$.*
- **$\\Pr(A \\text{ of } B)$**: of all the $A$s, what fraction were $B$? *Restrict to $A$ first.*

The famous medical-test fallacy swaps these: a test that's 99% accurate still gives a high *false-positive* rate when the disease is rare.

### Two-way tables & Venn diagrams
The cleanest way to compute conditional probabilities is to draw them as a grid:

|              | $B$        | not $B$    | Total |
|--------------|-----------|-----------|-------|
| $A$          | $a$       | $b$       | $a + b$ |
| not $A$      | $c$       | $d$       | $c + d$ |
| **Total**    | $a + c$   | $b + d$   | $n$    |

Then $\\Pr(A \\mid B) = \\dfrac{a}{a + c}$ and $\\Pr(B \\mid A) = \\dfrac{a}{a + b}$.

### Common mistakes to watch for
- Swapping the condition (most common).
- Confusing "of" with "given" — they reverse the fraction.
- Forgetting the sample space shrinks when you condition (you only look inside the column / row).`,
      examples: [
        {
          id: 'ex-two-way',
          statement:
            'In a class, $20$ students play sport and music, $10$ play sport only, $5$ play music only, $15$ play neither. Find $\\Pr(\\text{sport} \\mid \\text{music})$.',
          steps: [
            'Two-way table — fill the music column: yes music $= 20 + 5 = 25$, of which sport $= 20$.',
            '$\\Pr(\\text{sport} \\mid \\text{music}) = \\dfrac{20}{25} = 0.8$.',
          ],
        },
        {
          id: 'ex-swap-fallacy',
          statement:
            'A disease affects $1$ in $1000$ people. A test is $99\\%$ accurate. Out of $100\\,000$ people, how many false positives do you expect?',
          steps: [
            'Real positives: $100$ people. True positives: about $99$ (test catches $99\\%$).',
            'Healthy people: $99\\,900$. False positives: $1\\%$ of them $= 999$ people.',
            'So a positive test is **only ~9% likely to indicate real disease** ($99 / (99 + 999)$).',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-pr-given',
          difficulty: 'core',
          instance: {
            prompt:
              'Two cards are drawn without replacement. Given the first card is a King, what is $\\Pr(\\text{second card is a King})$ as a fraction in simplest form?',
            answer: '3/51',
            answerType: 'numeric',
            hint: 'After one King is gone, $3$ Kings remain among $51$ cards.',
            solution: [
              'After drawing a King, $3$ Kings remain in $51$ cards.',
              '$\\Pr = \\dfrac{3}{51} = \\dfrac{1}{17}$.',
              "Don't forget to simplify: $3/51 = 1/17$.",
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-pr-of',
          difficulty: 'intro',
          instance: {
            prompt:
              'A bag has $3$ red and $7$ blue balls. One ball is drawn. State $\\Pr(\\text{red of the draw})$ — but use the correct conditional phrasing. (Answer as a decimal.)',
            answer: '0.3',
            answerType: 'numeric',
            hint: 'Of all the draws, what fraction were red?',
            solution: [
              'Of every draw, the red draws are $3$ out of $10$, so $\\Pr(\\text{red of the draw}) = 0.3$.',
            ],
          },
        },
      ],
    },
  ],
}