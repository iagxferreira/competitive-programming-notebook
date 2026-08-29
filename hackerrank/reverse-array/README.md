# Arrays - DS (Reverse Array)

hackerrank | easy | arrays

## Task

Return the input array in reverse order.

## Key insight

Either walk the source backwards into a new array, or swap ends inward
in place. The in-place version needs no extra allocation.

## Invariant

In-place version: after k swaps, the outermost k elements on each side
are in final position.

## Complexity

time O(n)   space O(1) in place, O(n) if copying

## Pitfall

The two-pointer loop stops at `l < r`, not `l <= r`. With `<=` the middle
element of an odd-length array is swapped with itself — harmless here,
but the same off-by-one corrupts data in other two-pointer problems.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/hackerrank/reverse-array.kt
