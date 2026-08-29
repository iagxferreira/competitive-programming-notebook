# 704. Binary Search

leetcode | easy | binary-search

## Task

Index of target in a sorted array, or -1.

## Key insight

Halve the search range each step by comparing against the midpoint. The
canonical implementation of the most important primitive in the toolkit.

## Invariant

If target is present, it lies within [lo, hi] at every step.

## Complexity

time O(log n)   space O(1) iterative, O(log n) recursive

## Pitfall

`(lo + hi) / 2` overflows when both are large. Always write
`lo + (hi - lo) / 2` — build the habit here where it is harmless.

Write it ITERATIVELY. Your Go version recurses, which costs stack for no
benefit and is harder to adapt into the lower-bound variant you actually
need in contests.

Get the boundary discipline right: with `hi = n - 1`, the loop is
`lo <= hi` and the update is `hi = mid - 1`. Mixing that with the
`hi = n` convention is the most common way to write an infinite loop.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/704-binary-search.go
