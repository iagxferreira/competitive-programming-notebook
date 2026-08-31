# 1019. Time Conversion

beecrowd | trivial | io, math

## Task

Read a duration in seconds and print it as hours, minutes and seconds
separated by colons.

## Key insight

`h = s / 3600`, `m = (s % 3600) / 60`, `sec = s % 60`. Three integer
divisions and nothing else.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

This problem does NOT zero-pad, unlike most time formatting - check the
statement before reaching for `%02d`. Chaining the remainders wrongly
(`s / 60 % 60` versus `s % 3600 / 60`) gives the same answer here but
diverges elsewhere; write the one you can justify.

## Review

last: never   confidence: 0/5
