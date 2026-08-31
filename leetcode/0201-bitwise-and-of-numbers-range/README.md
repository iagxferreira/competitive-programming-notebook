# 201. Bitwise AND of Numbers Range

leetcode | medium | bits, math

## Task

Bitwise AND of every integer in [left, right].

## Key insight

The answer is the common binary PREFIX of left and right,
zero-padded. Any bit that differs anywhere in the range must flip somewhere
inside it, and a bit that flips is ANDed to zero. So shift both right until
they agree, then shift back.

## Invariant

After k shifts, the surviving bits are those left and right agree on.

## Complexity

time O(log n)   space O(1)

## Pitfall

Looping from left to right and ANDing is O(range) and times out
- the range can be ~2^31. Brian Kernighan's `right & (right - 1)` in a loop
is the other clean solution; both beat iterating.

## Review

last: never   confidence: 0/5
