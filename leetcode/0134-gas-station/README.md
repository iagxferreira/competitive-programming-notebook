# 134. Gas Station

leetcode | medium | greedy

## Task

Index to start from to complete the circuit, or -1. The answer is unique.

## Key insight

Two facts collapse the O(n^2) simulation to one pass. The trip
is possible exactly when total gas >= total cost. And if you run dry going
from i to j, no station between them works either, so restart at j + 1.

## Invariant

`tank` is the fuel accumulated since `start`; it is never
allowed to go negative without moving `start` past the failure point.

## Complexity

time O(n)   space O(1)

## Pitfall

Returning the candidate start without checking the global
total. The running reset alone will happily return an index on a circuit
that cannot be completed at all.

## Review

last: never   confidence: 0/5
