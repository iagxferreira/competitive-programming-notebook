# 1004. Max Consecutive Ones III

leetcode | medium | sliding-window

## Task

Longest run of 1s obtainable by flipping at most k zeroes.

## Key insight

Restate it: the longest window containing at most k zeroes.
Once stated that way it is the standard grow-right, shrink-while-invalid
window and the flipping never has to be simulated.

## Invariant

The window always holds at most k zeroes after the shrink loop.

## Complexity

time O(n)   space O(1)

## Pitfall

Shrinking with an `if` instead of a `while` works here only
because the right edge advances one at a time - it is a coincidence, not a
rule, and copying that habit into a window that can jump breaks it. Write
the `while`.

## Review

last: never   confidence: 0/5
