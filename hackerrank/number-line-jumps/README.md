# Number Line Jumps

hackerrank | easy | math, modular-arithmetic

## Task

Two kangaroos start at x1 and x2 and jump v1 and v2 each step. Will they
ever land on the same spot at the same time?

## Key insight

Solve `x1 + n*v1 == x2 + n*v2` for a non-negative integer n:
`n = (x2 - x1) / (v1 - v2)`. The answer is YES exactly when the division is
exact and n is non-negative.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Division by zero when `v1 == v2` - handle that case separately (YES only
if they already start together, which the constraints exclude). Simulating
the jumps in a loop also passes here, but the closed form is the point:
recognising a linear Diophantine condition.

## Review

last: never   confidence: 0/5
