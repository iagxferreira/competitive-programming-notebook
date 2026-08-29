# 3190. Find Minimum Operations to Make All Elements Divisible by Three

leetcode | easy | math

## Task

Each operation changes an element by 1. Minimum operations to make every
element divisible by 3.

## Key insight

Any element with a non-zero remainder mod 3 is exactly one step from a
multiple: remainder 1 goes down, remainder 2 goes up. So the answer is
just the count of non-multiples.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

The insight is that remainder 2 costs 1, not 2 — you may move in either
direction. Assuming you can only add turns this into a wrong, larger
answer.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3190-minimum-operations.go
