# 2089. Find Target Indices After Sorting Array

leetcode | easy | sorting, binary search

## Task

Return the indices where `target` appears after sorting `nums` in
non-decreasing order.

## Key insight

After sorting, all values smaller than `target` come first, followed by
all occurrences of `target`. Count both in one pass: the target indices are
`less, less + 1, ..., less + equal - 1`.

## Invariant

`less` is the starting index of the target block in the sorted array;
`equal` is its length.

## Complexity

time O(n)   space O(k) for the returned indices

## Pitfall

The problem asks for indices in the sorted array, not the original
positions. Sorting the input is unnecessary: only the counts of smaller
values and equal values are needed.

## Status

SOLVED. Count values below and equal to `target`; emit the consecutive
indices beginning at the count of smaller values.

## Review

last: never   confidence: 0/5
