# 567. Permutation in String

leetcode | medium | sliding-window, counting

## Task

Does s2 contain any permutation of s1 as a substring?

## Key insight

A permutation is a multiset, so this is a fixed-size window of
length s1.length() and a character-count comparison. Keep a running count
of how many of the 26 letters currently match rather than re-comparing the
arrays each step.

## Invariant

The window is always exactly s1.length() wide once it has
filled, and `matches` equals the number of letters whose counts agree.

## Complexity

time O(n)   space O(1), 26 slots

## Pitfall

Updating `matches` after mutating the count but forgetting the
before-state: a count going from equal to unequal must decrement, and the
reverse must increment. Check both transitions on entry AND on exit or the
counter drifts.

## Review

last: never   confidence: 0/5
