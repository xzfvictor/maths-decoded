// Core content model for the app. Topics are authored as plain data so the whole
// site is static and the coverage checker can reason about it.

export type Unit = 1 | 2 | 10

/**
 * A lesson (sub-topic) — the unit of a single study session. Holds its own theory,
 * worked examples and exercises so a student can learn and practise one idea at a time.
 * `body` is lightweight markdown with `$...$` / `$$...$$` TeX.
 */
export interface Lesson {
  /** Stable id within a topic, used for routing and progress tracking. */
  id: string
  heading: string
  /** One-line description shown on the topic overview card. */
  summary?: string
  body: string
  examples: WorkedExample[]
  exercises: Exercise[]
}

/** A fully worked example: statement plus ordered solution steps. */
export interface WorkedExample {
  id: string
  statement: string
  /** Each step is markdown+TeX; rendered as an ordered, revealable list. */
  steps: string[]
}

/** The result of instantiating any exercise — what the UI actually renders. */
export interface ExerciseInstance {
  /** Question text (markdown + TeX). */
  prompt: string
  /** Canonical correct answer used by the checker. */
  answer: string
  /** How to compare the student's response to `answer`. */
  answerType: AnswerType
  /** Ordered worked-solution steps, revealed after answering. */
  solution: string[]
  /** Optional hint shown before revealing the full solution. */
  hint?: string
  /** Optional multiple-choice options; when present the UI shows choices. */
  choices?: string[]
}

export type AnswerType =
  | 'exact' // normalised string equality (case/space-insensitive)
  | 'numeric' // parse to number, compare within tolerance
  | 'polynomial' // normalise polynomial form before comparing
  | 'set' // comma/`,`-separated set of values, order-independent

/** A hand-written question with a fixed statement and solution. */
export interface CuratedExercise {
  kind: 'curated'
  id: string
  difficulty: Difficulty
  instance: ExerciseInstance
}

/** A parameterised question: `build(seed)` returns a concrete instance. */
export interface ParamExercise {
  kind: 'param'
  id: string
  difficulty: Difficulty
  build: (seed: number) => ExerciseInstance
}

export type Exercise = CuratedExercise | ParamExercise
export type Difficulty = 'intro' | 'core' | 'challenge'

export interface Topic {
  /** kebab id, also the route param. */
  id: string
  unit: Unit
  /** 1-based order within the unit for the sidebar. */
  order: number
  title: string
  /** One-sentence description for the topic card. */
  blurb: string
  /** VCAA dot-point ids this topic covers (see coverage.ts). */
  dotPoints: string[]
  /** The sub-topics that make up this topic; each is a single study session. */
  lessons: Lesson[]
}
