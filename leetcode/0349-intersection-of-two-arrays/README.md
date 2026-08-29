# 349. Intersection of Two Arrays

leetcode | easy | hash-set

## Task

The unique values present in both arrays.

## Key insight

Put nums1 in a set, scan nums2, and erase on each hit so the same value
cannot be reported twice.

## Invariant

The set holds the values of nums1 not yet emitted.

## Complexity

time O(n + m)   space O(n)

## Pitfall

The result must be de-duplicated. Your Go version handles it by deleting
the key on first match — a neat way to get uniqueness without a second
set.

If both inputs were sorted, two pointers would give O(1) extra space.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/349-intersection-of-two-arrays.go
