# 1046. Last Stone Weight

leetcode | easy | heap

## Task

Repeatedly smash the two heaviest stones; equal weights destroy
both, otherwise the difference goes back. Return what is left, or 0.

## Key insight

A pure simulation whose only requirement is "give me the
largest, repeatedly, while I keep inserting". That is a max-heap:
`new PriorityQueue<>(Comparator.reverseOrder())`.

## Invariant

The heap always holds every stone not yet destroyed.

## Complexity

time O(n log n)   space O(n)

## Pitfall

PriorityQueue is a MIN-heap by default in Java, the opposite of
C++. Forgetting the comparator gives a plausible-looking wrong answer
rather than a crash. Do not write `(a, b) -> b - a` as the comparator
reflex either - it overflows on extreme values.

## Review

last: never   confidence: 0/5
