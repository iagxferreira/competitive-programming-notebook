# 2325. Decode the Message

leetcode | easy | hash-map, strings

## Task

The first appearance order of letters in `key` defines a substitution
cipher onto a, b, c... Decode `message`. Spaces map to spaces.

## Key insight

One pass over key building the table, ignoring repeats and spaces; one
pass over message applying it.

## Invariant

Each distinct letter of key is assigned exactly once, in first-appearance
order.

## Complexity

time O(n + m)   space O(1) — 26 entries

## Pitfall

The "only on first appearance" rule is the whole problem. Your Go version
tests `rainbowTable[char] == 0`, relying on Go's zero value for a missing
key. Java's `map.get(k)` returns `null` for a missing key rather than
inserting, so the map does not grow — but assigning that to a primitive
`char` or `int` throws a NullPointerException on unboxing. Use
`containsKey`, or `getOrDefault(k, (char) 0)`.

Simpler still: a `char[26]` indexed by `c - 'a'`, which sidesteps boxing
and null entirely.

Skip spaces when assigning letters but preserve them when decoding.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2325-decode-message.go
