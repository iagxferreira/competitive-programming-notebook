# 3202. Find the Maximum Length of Valid Subsequence II

leetcode | medium | dynamic-programming

## Task

Longest subsequence where every adjacent pair has the same
`(a + b) % k`.

## Key insight

Fix the target sum-mod t, then run a DP over remainders: for each num
with `r = num % k`, the element that must precede it has remainder
`(t - r + k) % k`. So `dp[r] = dp[(t - r + k) % k] + 1`. Repeat for all k
choices of t.

## Invariant

For a fixed t, dp[r] is the longest valid subsequence ending in an
element with remainder r.

## Complexity

time O(n * k)   space O(k)

## Pitfall

`(t - r + k) % k` — the `+ k` is mandatory. In C++ `%` on a negative
left operand yields a negative result, so omitting it indexes the array
out of bounds. This is a real difference from Python's `%`, and one of
the top sources of C++-specific bugs in modular problems.

Reset the dp array for each t.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3202-maximum-length-subsequence-ii.go
