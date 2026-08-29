# 1005. Average 1

beecrowd | trivial | io, floating-point

## Task

Read two reals A and B. Print `MEDIA = ` followed by the weighted
average (A*3.5 + B*7.5) / 11, to 5 decimal places.

## Key insight

The weights sum to 11, which is the divisor. That is what makes it a
weighted *average* rather than just a weighted sum.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Divide in floating point. If both weights and the divisor were integers
you would get truncation — here 3.5/7.5 force promotion, but do not rely
on that habit. `printf("MEDIA = %.5f\n", avg)`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1005.kt
