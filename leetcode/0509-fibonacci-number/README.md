# 509. Fibonacci Number

leetcode | easy | dynamic-programming

## Task

The nth Fibonacci number.

## Key insight

Iterate with two rolling variables. Naive recursion is O(2^n) because it
recomputes the same subtrees exponentially many times.

## Invariant

(a, b) holds (F(i-1), F(i)) at every step.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Go version memoised into a package-level `var memo` — GLOBAL MUTABLE
STATE that persists across calls and across test cases. It happens to be
safe because Fibonacci is a pure function of n, but it is a habit that
produces wrong answers the moment the cached data depends on the input,
and it is not thread-safe. Keep the memo local, or better, drop it for
the two-variable loop.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/509-fibonacci-number.go
