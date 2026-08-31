# 45. Jump Game II

leetcode | medium | greedy, bfs

## Task

Fewest jumps to reach the last index. Reaching it is guaranteed.

## Key insight

This is breadth-first search over ranges without a queue.
Everything reachable in one jump is a level; the furthest reach of that
whole level is the next boundary. Sweep once, incrementing the count each
time you step past the current boundary.

## Invariant

`currentEnd` is the last index reachable in `jumps` jumps and
`farthest` is the furthest index reachable in `jumps + 1`. Both only ever
increase.

## Complexity

time O(n)   space O(1)

## Pitfall

Looping to n - 1 inclusive counts one jump too many: arriving
at the last index is the goal, not a place you jump from. Stop the loop at
n - 2.

## Review

last: never   confidence: 0/5
