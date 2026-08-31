# Grading Students

hackerrank | easy | arrays, arithmetic

## Task

Round a grade up to the next multiple of 5 when that multiple is less
than 3 away, but never round anything below 38.

## Key insight

`next = ((g / 5) + 1) * 5`; round up if `g >= 38 && next - g < 3`.
Integer division does the flooring for you.

## Invariant

None.

## Complexity

time O(n)   space O(n)

## Pitfall

The `< 3` is strict and the `>= 38` guard comes first. A grade of exactly
38 rounds to 40; 37 does not round at all even though it is 3 away. Both
boundaries are tested.

## Review

last: never   confidence: 0/5
