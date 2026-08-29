# 2. Add Two Numbers

leetcode | medium | linked-list, math

## Task

Two numbers stored as reversed digit lists. Return their sum in the same
form.

## Key insight

Reversed storage means the head is the ones place — you traverse in the
exact order schoolbook addition wants. No reversal needed.

## Invariant

At each step carry is 0 or 1, and the output list holds the correct
digits for every place value already consumed.

## Complexity

time O(max(n, m))   space O(max(n, m)) for the output

## Pitfall

The loop condition must be `l1 != null || l2 != null || carry != 0`.
Dropping the carry test
loses the final digit of 5 + 5. Your Go version got this right.

That file also defines an unused `reverse` helper — leftover from a first
attempt. Do not port it.

A dummy head node removes the "is this the first node" branch you wrote.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2-sum-two-numbers.go
