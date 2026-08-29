# 141. Linked List Cycle

leetcode | easy | linked-list, two-pointers

## Task

Does the list contain a cycle? O(1) space.

## Key insight

Floyd's tortoise and hare. Slow moves one, fast moves two. If a cycle
exists the gap between them shrinks by exactly one per step, so fast
cannot jump over slow — they must meet. Without a cycle, fast reaches
null.

## Invariant

Inside a cycle, the distance from fast to slow decreases by 1 each step,
so it reaches 0.

## Complexity

time O(n)   space O(1)

## Pitfall

Guard BOTH `fast` and `fast->next` before the double advance, or you
dereference null on an even-length acyclic list.

A hash set of visited nodes also works but uses O(n) space, which the
problem's follow-up rules out.

Compare pointers, not values — duplicate values are not a cycle.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/141.cicled-list.py
