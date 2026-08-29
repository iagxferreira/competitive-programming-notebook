# 35. Search Insert Position

leetcode | easy | binary-search

## Task

Index of target in a sorted array, or the index where it would be
inserted. Required in O(log n).

## Key insight

Binary search for the lower bound: the first index whose value is >=
target. That single formulation answers both the "found" and "would
insert" cases with no special casing.

## Invariant

The answer always lies in [lo, hi]. Every step halves that range.

## Complexity

required time O(log n)   space O(1)

## Pitfall

Your Go version was a LINEAR scan. It is accepted, but the problem
explicitly demands O(log n) — this one is worth redoing for real, since
lower-bound binary search is the single most reused primitive in
competitive programming.

Use `lo < hi` with `hi = n` (not `n - 1`), so the insert-at-end case
falls out naturally.

Java's `Arrays.binarySearch` does exist, but it returns
`-(insertion point) - 1` when the target is absent, so you would write
`int i = Arrays.binarySearch(nums, target); return i < 0 ? -i - 1 : i;`.
That encoding is worth memorising — it is exactly this problem's answer
and it comes up constantly. But write the loop by hand here; lower-bound
binary search is the primitive you need to own outright.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/35-search-insert.go
