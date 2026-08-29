# 12. Integer to Roman

leetcode | medium | math, greedy

## Task

Convert 1..3999 to a Roman numeral.

## Key insight

Two equivalent approaches. Your Go version used the lookup-table trick:
because the input is bounded at 3999, precompute the numeral for each
digit at each place value and concatenate four table hits. O(1), no loop.

The general alternative is greedy: walk value/symbol pairs (including the
subtractive 900/400/90/40/9/4) largest first, emitting while it fits.

## Invariant

Greedy version: after handling value v, the remainder is strictly less
than v.

## Complexity

time O(1) either way   space O(1)

## Pitfall

The subtractive forms (IV, IX, XL, XC, CD, CM) are the whole problem.
Table lookup encodes them implicitly, which is why it is hard to get
wrong — and also why it teaches you less. Redo it greedily.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/12-integer-to-roman.go
