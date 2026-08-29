# 19. Remove Nth Node From End of List

leetcode | medium | linked-list, two-pointers

## Task

Remove the nth node from the end and return the head.

## Key insight

One pass with two pointers: advance `fast` n steps first, then move both
until fast hits the end. `slow` now sits on the node before the target,
because the gap between them never changes.

## Invariant

fast is always exactly n nodes ahead of slow.

## Complexity

time O(n)   space O(1)

## Pitfall

Removing the head is the edge case — a dummy node before the head makes
it disappear entirely. Your Go version instead counted the length and
special-cased `n == length`, which works but needs two passes and an
explicit branch.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/19-remove-nth-list.go
