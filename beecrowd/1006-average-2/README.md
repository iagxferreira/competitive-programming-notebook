# 1006. Average 2

beecrowd | trivial | io, floating-point

## Task

Read three reals. Print `MEDIA = ` followed by
(A*2 + B*3 + C*5) / 10, to 1 decimal place.

## Key insight

Weights 2/3/5 sum to 10. Same structure as 1005, different constants and
a different precision.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

One decimal place, not five. Each problem in this run changes the
precision on purpose to catch copy-paste.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1006.kt
