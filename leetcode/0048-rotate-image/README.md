# 48. Rotate Image

leetcode | medium | matrix

## Task

Rotate an n x n matrix 90 degrees clockwise, in place.

## Key insight

Clockwise rotation = transpose, then reverse each row. Two simple passes
replace one very error-prone index formula.

## Invariant

Transpose swaps only j > i, so each pair is exchanged exactly once.

## Complexity

time O(n^2)   space O(1)

## Pitfall

Your Go version FUSED the two passes — it transposes row i and reverses
row i in the same iteration. That is actually correct, because row i is
never revisited once the outer loop passes it. But it is delicate: the
correctness depends on the `j = i` lower bound and on rows below i still
being untransposed when read. Write it as two separate loops. The fused
version is the kind of cleverness that breaks silently when edited.

Transposing over the full range instead of `j >= i` swaps every pair
twice and returns the original matrix.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/48-rotate-image.go
