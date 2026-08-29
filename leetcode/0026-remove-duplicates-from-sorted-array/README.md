# 26. Remove Duplicates from Sorted Array

leetcode | easy | two-pointers

## Task

Remove duplicates in place from a sorted array; return the new length.

## Key insight

Read and write pointers. Because the array is sorted, duplicates are
adjacent — a new distinct value is simply one that differs from the last
one written.

## Invariant

nums[0..left] holds the distinct values seen so far, in order.

## Complexity

time O(n)   space O(1)

## Pitfall

Return `left + 1`, not `left` — the pointer is an index, the answer is a
count. Guard the empty array, since left starts at 0 assuming one
element exists. Your Go version does both.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/26-remove-duplicates.go
