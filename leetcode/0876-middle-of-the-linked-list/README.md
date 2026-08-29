# 876. Middle of the Linked List

leetcode | easy | linked-list, two-pointers

## Task

Return the middle node; for even length, the second of the two middles.

## Key insight

Same tortoise-and-hare as 141. When fast reaches the end, slow is at the
midpoint — because it has moved exactly half as far.

## Invariant

slow has taken exactly half as many steps as fast.

## Complexity

time O(n)   space O(1)

## Pitfall

The loop condition selects WHICH middle you get on even-length lists.
`while (fast != null && fast.next != null)` returns the second middle,
which is what this problem wants. `while (fast.next != null &&
fast.next.next != null)` returns the first — that variant is what you
need for splitting a list in merge sort.

Knowing which condition gives which is worth more than the problem
itself.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/876.middle-node.py
