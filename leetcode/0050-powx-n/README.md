# 50. Pow(x, n)

leetcode | medium | math, fast-exponentiation, recursion

## Task

Compute x^n for a possibly negative n.

## Key insight

Exponentiation by squaring: x^n is (x^(n/2))^2 for even n, and
x * x^(n-1) for odd n. That halves the exponent each step instead of
multiplying one factor at a time, so O(log n) rather than O(n). The same
routine, taken mod p, is modPow - the workhorse of contest number theory.

## Invariant

result * base^exponent is constant across every loop iteration.

## Complexity

time O(log n)   space O(1) iteratively

## Pitfall

`n = Integer.MIN_VALUE`. Negating it overflows back to itself,
so `x^(-n)` silently computes the wrong thing. Widen to long before
negating. This is the entire reason the problem is rated medium.

## Review

last: never   confidence: 0/5
