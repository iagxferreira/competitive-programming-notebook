# 4. Median of Two Sorted Arrays

leetcode | hard | binary-search

## Task

Median of two sorted arrays, required in O(log(n+m)).

## Key insight

Binary search the *partition*, not the value. Choose how many elements of
nums1 fall left of the cut; that fixes the count from nums2. The cut is
correct when `maxLeft1 <= minRight2 && maxLeft2 <= minRight1`.

## Invariant

Both sides of the cut always hold (n+m+1)/2 elements, so once the
cross-conditions hold the median is at the boundary.

## Complexity

target time O(log min(n, m))   space O(1)

## Pitfall

Your Go version concatenated and sorted — O((n+m) log(n+m)). It is
accepted, but it ignores the only reason this problem is Hard. This is
the one in the set most worth redoing properly.

Binary search over the shorter array or the index maths goes out of
range. Use sentinels of ±infinity for the empty-side cases.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/4-median-of-two-arrays.go
