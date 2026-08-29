# 136. Single Number

leetcode | easy | bit-manipulation

## Task

Every element appears twice except one. Find it, in O(n) time and O(1)
space.

## Key insight

XOR. `x ^ x == 0` and `x ^ 0 == x`, and XOR is commutative and
associative — so XORing everything cancels every pair regardless of
order, leaving the loner.

## Invariant

The accumulator holds the XOR of everything seen; paired values have
already annihilated.

## Complexity

time O(n)   space O(1)

## Pitfall

None in the code — it is four lines. The pitfall is not KNOWING the
trick. A hash map also works but violates the O(1) space requirement,
which is the only reason this problem exists.

Seed the accumulator at 0, the XOR identity.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/136-single-number.go
