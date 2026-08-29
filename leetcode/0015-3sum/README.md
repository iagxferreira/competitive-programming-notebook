# 15. 3Sum

leetcode | medium | two-pointers, sorting

## Task

All unique triplets summing to zero.

## Key insight

Sort, then fix nums[i] and solve Two Sum II on the suffix with two
pointers. Sorting is what makes both the two-pointer scan and the
duplicate skipping possible.

## Invariant

nums is sorted; for a fixed i, left and right converge and
`sum < target` implies only `left++` can help.

## Complexity

time O(n^2)   space O(1) excluding output

## Pitfall

Duplicates must be skipped at ALL THREE positions: for i before the inner
loop, and for left and right after recording a hit. Your Go version does
all three correctly — that is the part worth re-deriving rather than
re-reading.

You can break early once nums[i] > 0: no three non-negative numbers sum
to zero unless all are zero.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/15-three-sum.go
