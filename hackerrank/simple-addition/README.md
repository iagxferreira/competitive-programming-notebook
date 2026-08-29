# Simple Addition

hackerrank | trivial | warmup

## Task

Return the sum of two integers.

## Key insight

None. This is a "does your submission harness work" problem.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

If the operands can reach the `int` limit, the sum overflows before it
is ever returned. Widen to `long long` at the parameter, not at the
return.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/hackerrank/sum.kt
