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
The Java equivalent is `HashSet<Character>`, but for lowercase letters an
`int` bitmask with `Integer.bitCount(mask)` is dramatically faster and
is the form worth internalising for contests: set bit `c - 'a'`, then
count bits once at the end.

Verify the problem number against the archive filename before trusting
this card's title.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3760-max-distinct.go
