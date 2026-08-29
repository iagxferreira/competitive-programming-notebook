# 3512. Minimum Operations to Make Array Sum Divisible by K

leetcode | easy | math

## Task

Each operation decrements an element by 1. Minimum operations to make the
sum divisible by k.

## Key insight

Only the total matters. Removing `sum % k` from the total is both
necessary and achievable one unit at a time, so the answer is `sum % k`.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

Accumulate in `long` — n elements near the int limit overflow a 32-bit
sum before you ever take the modulus, and Java wraps silently rather
than trapping, so the result is plausible-looking garbage.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3512-min-operations.go
