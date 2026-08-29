# Compare the Triplets

hackerrank | easy | arrays

## Task

Two triplets a and b. For each of the 3 positions, the larger value earns
its owner a point; ties award nothing. Return {aPoints, bPoints}.

## Key insight

Independent per-position comparison. There is no interaction between
positions, so a single pass with two counters is enough.

## Invariant

points[0] + points[1] + ties == number of positions examined so far.

## Complexity

time O(1)   space O(1)

## Pitfall

The three-way comparison needs all three branches. Writing it as
`if (a > b) ... else ...` silently gives b a point on every tie.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/hackerrank/compare-triplets.kt
