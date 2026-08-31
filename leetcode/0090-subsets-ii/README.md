# 90. Subsets II

leetcode | medium | backtracking, deduplication

## Task

All distinct subsets of an array that may contain duplicates.

## Key insight

Sort first, then at each recursion level skip a candidate equal
to the previous one at the SAME level. That kills duplicate branches at
the source, which is far better than generating everything and pushing it
through a HashSet.

## Invariant

Within one call, each distinct value is chosen at most once
as the next element, so no two branches ever produce the same subset.

## Complexity

time O(n * 2^n)   space O(n) recursion

## Pitfall

The skip condition is `i > start && nums[i] == nums[i-1]`, not
`i > 0`. Using `i > 0` also skips the legitimate case where the duplicate
is being taken as part of the same run - it silently drops valid subsets
like [2,2].

## Review

last: never   confidence: 0/5
