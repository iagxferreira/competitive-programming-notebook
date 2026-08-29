# 88. Merge Sorted Array

leetcode | easy | two-pointers

## Task

Merge nums2 into nums1 in place. nums1 has exactly n spare slots at the
end.

## Key insight

Merge from the BACK. Filling forwards would overwrite unread elements of
nums1; filling backwards writes only into space that is already spare or
already consumed.

## Invariant

The write index m+n-1 is always strictly greater than both read indices,
so a write can never clobber a value still needed.

## Complexity

time O(n + m)   space O(1)

## Pitfall

When nums1 runs out (m == 0) the rest of nums2 must still be copied; when
nums2 runs out the remaining nums1 elements are already in place and need
no work. Your Go version's `m != 0 &&` guard covers the first case
correctly.

Backwards is the entire lesson. Forwards needs a temporary buffer.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/88-merge-sorted-array.go
