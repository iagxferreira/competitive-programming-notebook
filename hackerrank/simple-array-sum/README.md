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
no seed. `std::accumulate(all(v), 0LL)` takes an explicit initial value
and handles empty naturally — and the `0LL` also prevents the sum from
overflowing `int`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/hackerrank/array-sum.kt
