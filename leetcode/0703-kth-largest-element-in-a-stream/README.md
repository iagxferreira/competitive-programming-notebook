# 703. Kth Largest Element in a Stream

leetcode | easy | heap, design

## Task

Report the kth largest value seen so far, after each insertion.

## Key insight

Keep a MIN-heap of size exactly k. Its root is then the kth
largest, and anything smaller than the root can be discarded on arrival.
The counter-intuitive part - a min-heap to answer a "largest" question - is
the whole lesson.

## Invariant

The heap holds the k largest values seen so far; its root is the answer.

## Complexity

time O(log k) per add   space O(k)

## Pitfall

Sorting on every add is O(n log n) per call and the point of
the problem is to avoid it. Trim the heap AFTER offering, not before, or
the very first k inserts behave differently from the rest.

## Review

last: never   confidence: 0/5
