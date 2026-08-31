# 739. Daily Temperatures

leetcode | medium | monotonic-stack

## Task

For each day, how many days until a warmer one; 0 if none.

## Key insight

Monotonic stack of INDICES whose answer is still unknown, kept
in decreasing temperature order. A warmer day resolves everything on top
that is colder than it, and the distance is the index difference.

## Invariant

Temperatures at the stacked indices are non-increasing from
bottom to top. Anything still on the stack at the end has no warmer day,
which is why the array is pre-filled with 0.

## Complexity

time O(n)   space O(n)

## Pitfall

Stacking temperatures instead of indices. You need the index to
compute the gap, and recovering it afterwards is not possible when values
repeat. Use ArrayDeque, not Stack.

## Review

last: never   confidence: 0/5
