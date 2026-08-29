# 3110. Score of a String

leetcode | easy | strings

## Task

Sum of absolute differences between adjacent characters' ASCII values.

## Key insight

One pass over adjacent pairs.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Go version routed this through `float64` and `math.Abs`, then cast
back to int. Character codes are integers — use `abs(s[i] - s[i+1])` on
ints. Floating point here is a pointless precision risk and slower.

Loop to `n - 1`, and guard n == 0 since `n - 1` on an unsigned size wraps.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3110-score-of-string.go
