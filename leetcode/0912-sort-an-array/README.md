# 912. Sort an Array

leetcode | medium | sorting, divide-and-conquer, heap

## Task

Sort an array without using the built-in sort.

## Key insight

The place to actually write merge sort, heap sort and a
three-way quicksort in Java rather than describing them. Merge sort is the
divide-and-conquer template you reuse for 315; the three-way partition is
what keeps quicksort alive on arrays full of duplicates.

## Invariant

Merge: both halves are sorted before merging. Quick: after
partitioning, the pivot is in its final position.

## Complexity

time O(n log n)   space O(n) for merge, O(log n) for quick

## Pitfall

This problem has anti-quicksort test cases specifically to
punish a naive last-element pivot with O(n^2). That is exactly the
`Arrays.sort(int[])` hackability the repo template warns about, in a form
you can feel. Shuffle first, pick a random or median-of-three pivot, or
use merge sort.

## Review

last: never   confidence: 0/5
