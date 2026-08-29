# Simple Array Sum

hackerrank | easy | arrays

## Task

Return the sum of all elements of an integer array.

## Key insight

A fold. Every "reduce the array to one value" problem is this shape with
a different binary operator.

## Invariant

After processing index i, the accumulator holds the sum of [0..i].

## Complexity

time O(n)   space O(1)

## Pitfall

Your Kotlin used `reduce`, which throws on an empty list because it has
no seed. In Java either loop with `long sum = 0`, or
`Arrays.stream(a).asLongStream().sum()` — the `asLongStream` is what
stops the total overflowing `int`. Plain `Arrays.stream(a).sum()`
returns an int and wraps.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/hackerrank/array-sum.kt
