# 315. Count of Smaller Numbers After Self

leetcode | hard | fenwick-tree, merge-sort, divide-and-conquer

## Task

For each element, how many elements to its right are smaller.

## Key insight

This is inversion counting per index. Two standard routes.
Merge sort: while merging, whenever you take from the right half, every
element still waiting in the left half is inverted with it. Fenwick tree:
walk right to left, query the count of values already seen below this one,
then insert.

## Invariant

Fenwick route: the tree holds the frequency of every value
strictly to the right of the current index. Merge route: both halves are
sorted, so a single comparison settles a whole block at once.

## Complexity

time O(n log n)   space O(n)

## Pitfall

Values can be negative and large, so you must coordinate-
compress before indexing a Fenwick tree - sort the distinct values and map
each to its rank. Skipping that step is the usual failure. In the merge
version, sort INDICES rather than values or you lose track of which
original position each count belongs to.

## Review

last: never   confidence: 0/5
