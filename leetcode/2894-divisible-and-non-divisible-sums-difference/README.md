# 2894. Divisible and Non-Divisible Sums Difference

leetcode | easy | math

## Task

Sum of 1..n not divisible by m, minus the sum of those that are.

## Key insight

One pass, adding or subtracting per element. The closed form uses
`n(n+1)/2` for the total and `m * k(k+1)/2` with `k = n/m` for the
divisible part, giving O(1).

## Invariant

None.

## Complexity

loop O(n)   closed form O(1)   space O(1)

## Pitfall

Nothing subtle at these bounds. If n were large, `n(n+1)/2` would need
`long long` — divide by 2 after multiplying, and note that n(n+1) is
always even so no precision is lost.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2894-sum-difference.go
