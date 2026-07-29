import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Probability · l8-p-1 (VC2M8P01).
// Recognise that complementary events have a combined probability of one;
// use this relationship to calculate probabilities in applied contexts.

export const l8PComplementaryEvents: Topic = {
  id: 'l8-p-complementary-events',
  unit: 8,
  order: 27,
  title: 'Complementary events',
  blurb:
    'Recognise that complementary events have a combined probability of one, and use this relationship to calculate probabilities in applied contexts.',
  dotPoints: ['l8-p-1'],
  lessons: [
    {
      id: 'what-is-complement',
      heading: 'What is a complementary event?',
      summary:
        'The complement of an event is everything that is NOT the event. Their probabilities always sum to 1.',
      body: `Two events are **complementary** if one is exactly the opposite of the other: one happens **or** the other happens, and they cannot both happen at the same time.

### Notation
If $A$ is an event, then $A'$ (or "not $A$") is its **complement** — every outcome in which $A$ does **not** happen.

### The complement rule
The two complementary events together cover **every** possible outcome, so their probabilities add up to $1$:

$$\\Pr(A) + \\Pr(A') = 1.$$

This lets you find one from the other:

$$\\Pr(A') = 1 - \\Pr(A).$$

### Examples of complementary pairs
- Rolling a $6$ vs. rolling **not** a $6$.
- Drawing a red card vs. drawing a **black** card.
- It rains tomorrow vs. it does **not** rain tomorrow.
- A baby is a girl vs. a baby is a **boy** (assuming no other options).

### Why it is so useful
Sometimes it is **much easier** to find the probability of the complement than of the event itself.
- "At least one head in three tosses" → easier to compute the complement "no heads at all".
- "No defects in a batch of $100$" → easier to compute "at least one defect".

> [!warning] Watch out
> "Complementary" is **not** the same as "mutually exclusive". Two complementary events are mutually exclusive (they cannot both happen), but two mutually exclusive events are not necessarily complementary (a third option may exist). For example, "rolled a 1" and "rolled a 2" are mutually exclusive but **not** complementary — there are four other faces.`,
      examples: [
        {
          id: 'ex-basic',
          statement:
            'The probability a bus is late is $0.3$. What is the probability it is on time?',
          steps: [
            '"Late" and "on time" are complementary events.',
            '$\\Pr(\\text{on time}) = 1 - \\Pr(\\text{late}) = 1 - 0.3 = 0.7$.',
          ],
        },
        {
          id: 'ex-not-six',
          statement:
            'A fair die is rolled. Find $\\Pr(\\text{not a 6})$.',
          steps: [
            '$\\Pr(6) = 1/6$.',
            '$\\Pr(\\text{not 6}) = 1 - 1/6 = 5/6$.',
          ],
        },
        {
          id: 'ex-not-equal',
          statement:
            'A bag has $3$ red and $2$ blue balls. Find $\\Pr(\\text{not red})$ when one ball is drawn.',
          steps: [
            '$\\Pr(\\text{red}) = 3/5$.',
            '$\\Pr(\\text{not red}) = 1 - 3/5 = 2/5$.',
            '(This is the same as $\\Pr(\\text{blue}) = 2/5$ — sanity check.)',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-basic',
          difficulty: 'intro',
          instance: {
            prompt:
              'The probability it rains tomorrow is $0.4$. What is the probability it does not rain? Answer as a decimal.',
            answer: '0.6',
            answerType: 'numeric',
            hint: 'Raining and not raining are complementary — probabilities sum to $1$.',
            solution: [
              '$\\Pr(\\text{not rain}) = 1 - 0.4 = 0.6$.',
            ],
          },
        },
      ],
    },
    {
      id: 'using-the-complement',
      heading: 'Using the complement to solve problems',
      summary:
        'When "at least one" or "all" make a direct calculation messy, compute the complement instead.',
      body: `The complement rule is most powerful when computing the event directly requires many cases, but the complement has **one** case.

### "At least one" → use "none"
"At least one success" means one, two, three ... successes. Its complement is "**no** successes" — usually one case.

### "All" → use "at least one fails"
"All items pass" means every one passes. Its complement is "**at least one fails**" — usually easier with inclusion-exclusion or a chain of multiplications.

### Recipe
1. Identify the event $A$ you want.
2. Find its complement $A'$ — the "easy" case.
3. Compute $\\Pr(A')$.
4. Then $\\Pr(A) = 1 - \\Pr(A')$.

### Examples in context
- "At least one head in two coin tosses" → easier to compute "no heads" = $TT = 1/4$, then $1 - 1/4 = 3/4$.
- "At least one six when rolling two dice" → complement "no sixes" = $(5/6)^2$, then $1 - 25/36 = 11/36$.
- "It rains at least one day in a $7$-day forecast" → complement "no rain all week" is one easy multiplication.`,
      examples: [
        {
          id: 'ex-at-least-one',
          statement:
            'A coin is tossed $3$ times. Find $\\Pr(\\text{at least one H})$.',
          steps: [
            'Direct: list all patterns with at least one H — many cases.',
            'Complement: **no** H at all $= TTT$.',
            '$\\Pr(TTT) = (1/2)^3 = 1/8$.',
            '$\\Pr(\\text{at least one H}) = 1 - 1/8 = 7/8$.',
          ],
        },
        {
          id: 'ex-two-dice',
          statement:
            'Two fair dice are rolled. Find $\\Pr(\\text{at least one 6})$.',
          steps: [
            'Complement: no $6$ on either die.',
            '$\\Pr(\\text{no 6}) = (5/6) \\cdot (5/6) = 25/36$.',
            '$\\Pr(\\text{at least one 6}) = 1 - 25/36 = 11/36$.',
          ],
        },
        {
          id: 'ex-rain',
          statement:
            'The probability it rains on any given day is $0.2$, independently. What is the probability it rains at least once in a $3$-day weekend?',
          steps: [
            'Complement: no rain on any of the $3$ days.',
            '$\\Pr(\\text{no rain in 3 days}) = 0.8^3 = 0.512$.',
            '$\\Pr(\\text{rains at least once}) = 1 - 0.512 = 0.488$.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-at-least-one',
          difficulty: 'intro',
          instance: {
            prompt:
              'Two fair dice are rolled. Find $\\Pr(\\text{at least one 6})$ as a fraction in lowest terms.',
            answer: '11/36',
            answerType: 'numeric',
            hint: 'Use the complement: $\\Pr(\\text{no 6}) = (5/6)(5/6)$.',
            solution: [
              '$\\Pr(\\text{no 6 on either die}) = (5/6) \\cdot (5/6) = 25/36$.',
              '$\\Pr(\\text{at least one 6}) = 1 - 25/36 = 11/36$.',
            ],
          },
        },
      ],
    },
  ],
}