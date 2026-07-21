// Deterministic seeded RNG so parameterised questions are reproducible and a
// "new question" button just advances the seed. No Date.now / Math.random in
// content code, keeping instances pure functions of their seed.

/** mulberry32: tiny, fast, good-enough PRNG seeded by a 32-bit integer. */
export function makeRng(seed: number) {
  let a = seed >>> 0
  return function next(): number {
    a |= 0
    a = (a + 0x6d2b79f5) | 0
    let t = Math.imul(a ^ (a >>> 15), 1 | a)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

export interface Rng {
  /** Float in [0, 1). */
  next: () => number
  /** Integer in [min, max] inclusive. */
  int: (min: number, max: number) => number
  /** Integer in [min, max] excluding 0. */
  nonZeroInt: (min: number, max: number) => number
  /** Pick one element of an array. */
  pick: <T>(items: readonly T[]) => T
  /** ±1 at random. */
  sign: () => number
}

export function makeSeededRng(seed: number): Rng {
  const r = makeRng(seed)
  const int = (min: number, max: number) => min + Math.floor(r() * (max - min + 1))
  const nonZeroInt = (min: number, max: number) => {
    let v = 0
    // Guaranteed to terminate quickly; range always includes non-zero values in practice.
    do {
      v = int(min, max)
    } while (v === 0)
    return v
  }
  return {
    next: r,
    int,
    nonZeroInt,
    pick: (items) => items[Math.floor(r() * items.length)],
    sign: () => (r() < 0.5 ? -1 : 1),
  }
}
