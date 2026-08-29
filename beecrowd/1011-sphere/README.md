# 1011. Sphere

beecrowd | trivial | io, floating-point

## Task

Read radius R. Print `VOLUME = ` followed by (4/3) * pi * R^3,
3 decimals.

## Key insight

Write the fraction as `4.0 / 3.0`. In Java `4 / 3` is integer division
and evaluates to 1, quietly producing a 25% error.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

That integer-division trap is the entire point of this problem, and it
is the single most common way to lose a contest problem to a one-token
mistake. Again use pi = 3.14159 as specified.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1011.kt
