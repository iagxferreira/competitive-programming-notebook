# 1036. Bhaskara's Formula

beecrowd | easy | math, floating-point, edge-cases

## Task

Read A, B and C and print the two roots of the quadratic with five
decimals, or the impossibility message when there are none.

## Key insight

Compute the discriminant first and branch on it. Two separate failure
conditions collapse into the same message: a negative discriminant, and
A == 0 which is not a quadratic at all.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Forgetting the `A == 0` case - it divides by zero and prints `Infinity`
or `NaN` rather than the expected message. Check `delta < 0 || A == 0`
before computing anything. And `Locale.US` for the five decimals.

## Review

last: never   confidence: 0/5
