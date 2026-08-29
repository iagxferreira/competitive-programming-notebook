# 3760. Count Distinct Characters

leetcode | easy | hash-set

## Task

Number of distinct characters in the string.

## Key insight

A set, or for a known alphabet a bitmask: set bit `c - 'a'` and popcount
at the end.

## Invariant

None.

## Complexity

time O(n)   space O(1) for a bounded alphabet

## Pitfall

Your Go version used `map[rune]struct{}` — the idiomatic zero-byte set.
The C++ equivalent is `unordered_set`, but for lowercase letters a
32-bit mask with `__builtin_popcount` is dramatically faster and is the
form worth internalising for contests.

Verify the problem number against the archive filename before trusting
this card's title.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3760-max-distinct.go
