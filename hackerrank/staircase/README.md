# Staircase

hackerrank | easy | strings

## Task

Print a right-aligned staircase of height n built from `#`, where row i
(1-indexed) has i hashes padded by n-i leading spaces.

## Key insight

Row i is `string(n - i, ' ') + string(i, '#')`. Constructing each row
directly beats printing character by character.

## Invariant

Every row has exactly n characters, so the right edge stays flush.

## Complexity

time O(n^2)   space O(n) per row

## Pitfall

No trailing spaces after the hashes — the staircase is right-aligned, so
padding goes on the left only. Your Go version wrote
`for s := n - 1; s >= i; s--`, an easy place to be off by one; the Rust
version's `n - i - 1` on a 0-indexed loop is the same count expressed
more clearly.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/rust/hackerrank/staircase.rs
git show legacy-archive:legacy/go/hackerrank/staircase.go
