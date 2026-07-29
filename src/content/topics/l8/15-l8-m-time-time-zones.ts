import type { Topic } from '../../types'

// Foundation (Year 8) · Strand: Measurement · l8-m-4 (VC2M8M04).
// Solve problems involving time and duration, including using 12- and
// 24-hour time across multiple time zones.

export const l8MTimeTimeZones: Topic = {
  id: 'l8-m-time-time-zones',
  unit: 8,
  order: 15,
  title: 'Time and time zones',
  blurb:
    'Solve problems involving time and duration using 12- and 24-hour time across multiple time zones, and interpret the time-zone language used in everyday life.',
  dotPoints: ['l8-m-4'],

  lessons: [
    {
      id: 'time-zones',
      heading: 'Time zones and the international date line',
      summary: 'Add or subtract the hour difference between zones; cross the date line and add or subtract a day.',
      body: `The world is split into **time zones**. Within a zone, everyone agrees on the same clock time. Neighbouring zones usually differ by **one hour**.

### UTC offsets
A zone's offset tells you how many hours it is ahead of (positive) or behind (negative) UTC.
- Australia (Eastern, VIC): UTC +10 in winter, UTC +11 with daylight saving.
- UK (London): UTC +0 in winter, UTC +1 with daylight saving.
- USA (New York): UTC −5 in winter, UTC −4 with daylight saving.

### Converting between zones
To convert from zone A to zone B:
$$\\text{time in B} = \\text{time in A} + (\\text{offset of B} - \\text{offset of A}).$$
If the answer is $24$ or more, **subtract $24$ and add a day**. If it is negative, **add $24$ and go back a day**.

### The international date line
The IDL runs through the Pacific. Cross it heading **west** (from e.g. Australia to the Americas) and you **add a day** (because you are catching up to the calendar). Cross it heading **east** and you **subtract a day**.

### Common everyday language
- "AEST" = Australian Eastern Standard Time (UTC +10).
- "AEDT" = Australian Eastern Daylight Time (UTC +11).
- "GMT" / "UTC" — the reference point at $0°$ longitude.
- "AM" runs from 12:00 midnight to 12:00 noon; "PM" runs from 12:00 noon to 12:00 midnight.`,
      examples: [
        {
          id: 'ex-east-west',
          statement:
            'It is 9:00 am in Sydney (UTC +10). What time is it in London (UTC +0)?',
          steps: [
            'Difference: $0 - 10 = -10$ hours.',
            '$9{:}00 - 10\\text{ h} = $ previous day, $23{:}00$ (11 pm).',
            'Answer: 11:00 pm the previous day in London.',
          ],
        },
        {
          id: 'ex-day-rollover',
          statement:
            'It is 14:00 in Tokyo (UTC +9). A flight leaves for Sydney (UTC +10) immediately. What time does it arrive, given the flight takes $8$ hours?',
          steps: [
            'Take-off time in Sydney: $14{:}00 + (10 - 9) = 15{:}00$ (3 pm Sydney time).',
            'Add flight time: $15{:}00 + 8\\text{ h} = 23{:}00$ (11 pm) the same day.',
          ],
        },
        {
          id: 'ex-date-line',
          statement:
            'A ship crosses the international date line at 12:00 noon, going east. The clocks are unchanged but the day becomes the day before. What day and time is it now?',
          steps: [
            'Crossing east: subtract a day, so the clock stays at 12:00 noon.',
            'But the date has gone back by one calendar day.',
            'Answer: 12:00 noon, but it is now the previous calendar day.',
          ],
        },
      ],
      exercises: [
        {
          kind: 'curated',
          id: 'c-tz-ahead',
          difficulty: 'intro',
          instance: {
            prompt:
              'It is 8:00 am in Los Angeles (UTC −8). What time is it in Melbourne (UTC +10)? (Answer as the hour difference — how many hours ahead is Melbourne?)',
            answer: '18',
            answerType: 'numeric',
            hint: 'Difference in offsets $= 10 - (-8) = 18$ hours.',
            solution: [
              'Melbourne is $10 - (-8) = 18$ hours ahead.',
              'So it is $8{:}00 + 18 = 26{:}00$, which is $2{:}00$ am the next day in Melbourne.',
              'The hour difference is $18$ hours ahead.',
            ],
          },
        },
      ],
    },
  ],
}