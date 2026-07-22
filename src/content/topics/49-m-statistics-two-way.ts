import type { Topic } from '../types'

// Foundation (Year 10) · Strand: Statistics · VC2M10ST03.
// Construct two-way tables and discuss possible relationship between
// categorical variables.

export const statisticsTwoWay: Topic = {
  id: 'm10-statistics-two-way',
  unit: 10,
  order: 27,
  title: 'Two-way tables & categorical variables',
  blurb:
    'Tabulate two categorical variables side-by-side, read row/column percentages, and spot association.',
  dotPoints: ['m10-st-3'],

  lessons: [
    {
      id: 'two-way',
      heading: 'Reading and building two-way tables',
      summary: 'Rows × columns; percentages along a row or column reveal association.',
      body: `A **two-way table** cross-tabulates two categorical variables. Rows = one variable, columns = the other, cells = counts.

### How to read
- **Joint count**: the number in a specific row + column.
- **Row total** / **column total**: sum across a row / down a column.
- **Grand total**: sum of every cell.

### Percentages — your key tool
- **Row percentage** = (cell) / (row total). Tells you the breakdown **within that row**.
- **Column percentage** = (cell) / (column total). Tells you the breakdown **within that column**.

### Spotting association
- If the row percentages are **roughly the same** across all rows → no association between the variables.
- If the row percentages **vary noticeably** between rows → there is an association (the variables are related).`,
      examples: [
        {
          id: 'ex-twoway-build',
          statement:
            "A school surveys $100$ students. $40$ play sport; of those, $30$ are happy with the canteen. Of the $60$ non-sport students, $20$ are happy. Build a two-way table.",
          steps: [
            '|              | Happy | Not happy | Total |',
            '|--------------|-------|-----------|-------|',
            '| Sport        |   30  |    10     |   40  |',
            '| No sport     |   20  |    40     |   60  |',
            '| Total        |   50  |    50     |  100  |',
          ],
        },
        {
          id: 'ex-row-pct',
          statement:
            "From the table above, what percentage of **sport-playing** students are happy? (As a percentage, e.g. \"75%\".)",
          steps: [
            'Row total for sport: $40$.',
            "Happy sport: $30$. Percentage: $30/40 = 0.75 = 75\\%$.",
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-row-pct',
          difficulty: 'intro',
          instance: {
            prompt:
              "In a survey, $50$ of $100$ boys like maths, and $30$ of $100$ girls like maths. What percentage of **girls** like maths? (Number, no \"%\".)",
            answer: '30',
            answerType: 'numeric',
            hint: 'Girls: $30$ of $100$ like maths.',
            solution: [
              '$30/100 = 30\\%$.',
            ],
          },
        },
        {
          kind: 'curated',
          id: 'c-association',
          difficulty: 'core',
          instance: {
            prompt:
              "In a $2 \\times 2$ table, if row percentages are exactly equal across all rows, the variables are: \"associated\" or \"independent\"?",
            answer: 'independent',
            answerType: 'exact',
            hint: "Equal row percentages = knowing the row doesn't change the column distribution.",
            solution: [
              'No association — the variables appear independent.',
            ],
          },
        },
      ],
    },
  ],
}