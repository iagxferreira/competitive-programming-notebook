# Repeated String

hackerrank | easy | math, counting, overflow

## Task

An infinite repetition of a string, truncated to n characters. How many
`a` are in it?

## Key insight

Count the `a` in one copy, multiply by the number of whole copies
(`n / len`), then add the count in the leading `n % len` characters of a
partial copy. No string is ever built.

## Invariant

None.

## Complexity

time O(len)   space O(1)

## Pitfall

n goes up to 1e12, so the answer and every intermediate MUST be `long` -
an int overflows silently. Actually constructing the repeated string is an
instant out-of-memory, and the whole reason the problem exists.

## Review

last: never   confidence: 0/5
