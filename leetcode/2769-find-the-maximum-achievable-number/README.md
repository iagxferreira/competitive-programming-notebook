# 2769. Find the Maximum Achievable Number

leetcode | easy | math

## Task

x and num can each move by 1 per operation, at most t operations. Largest
x that can meet num.

## Key insight

Each operation closes the gap by 2 — decrement x, increment num. So the
answer is `num + 2 * t`. Closed form, no loop.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

None. The only trap is simulating the operations instead of noticing the
gap closes by 2 each time.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2769-maximum-achievable.go
