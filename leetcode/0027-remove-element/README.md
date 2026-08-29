# 27. Remove Element

leetcode | easy | two-pointers

## Task

Remove all occurrences of val in place; return the new length. Order of
the remaining elements does not matter.

## Key insight

A write pointer. Copy every element that is not val to the front. What
lies beyond the write pointer is explicitly allowed to be garbage.

## Invariant

nums[0..aux) contains exactly the kept elements.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Go version swapped rather than assigned. Swapping is harmless but
unnecessary — the tail is unspecified, so a plain overwrite is enough and
clearer.

Since order is free, the alternative is to swap the last element into any
hit, which is faster when matches are rare.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/27-remove-element.go
