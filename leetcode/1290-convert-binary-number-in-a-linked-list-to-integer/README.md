# 1290. Convert Binary Number in a Linked List to Integer

leetcode | easy | linked-list, bit-manipulation

## Task

The list holds bits, most significant first. Return the value.

## Key insight

`result = (result << 1) | bit`. Shifting left makes room for the incoming
bit, so a single forward pass works — no need to know the length first.

## Invariant

result holds the value of the prefix consumed so far.

## Complexity

time O(n)   space O(1)

## Pitfall

Since the bits arrive most-significant-first, the shift-then-or order is
what makes one pass sufficient. Reverse the order and you would need the
length up front.

`result * 2 + bit` is identical and arguably clearer.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/1290-convert-binary-from-list.go
