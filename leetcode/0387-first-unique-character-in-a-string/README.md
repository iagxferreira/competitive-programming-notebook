# 387. First Unique Character in a String

leetcode | easy | counting, strings

## Task

Index of the first non-repeating character, or -1.

## Key insight

Two passes. Count every character, then rescan in order and return the
first with count 1. One pass cannot work — uniqueness is not knowable
until the whole string has been read.

## Invariant

After pass one, counts are final; pass two preserves original order.

## Complexity

time O(n)   space O(1) for a 26-entry array

## Pitfall

The second pass must walk the STRING, not the map — a hash map has no
meaningful order, so iterating it returns an arbitrary unique character
rather than the first one.

Your Go version ranges over the string with `for index, char := range s`,
which yields BYTE offsets for multi-byte runes. Irrelevant for ASCII
input, but the same habit breaks on UTF-8.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/387-first-uniq-char.go
