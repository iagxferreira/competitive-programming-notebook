# 24. Swap Nodes in Pairs

leetcode | medium | linked-list

## Task

Swap every two adjacent nodes. Values may not be modified — relink.

## Key insight

A dummy head removes the special case for the first pair. Per pair you
need three relinks and a saved pointer to the start of the NEXT pair
before you destroy the links.

## Invariant

`prev` always points at the last node of the already-swapped prefix.

## Complexity

time O(n)   space O(1)

## Pitfall

Save `current->next->next` FIRST. Every other order strands the rest of
the list.

The loop guard must be `current && current->next` — an odd trailing node
is left in place, and testing only `current` dereferences null.

Return `dummy->next`, not head: head is the second node after the first
swap. Your Python version gets all of this right.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/24.swap-pairs.py
