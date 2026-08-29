# 49. Group Anagrams

leetcode | medium | hash-map, strings

## Task

Group strings that are anagrams of each other.

## Key insight

Give every string a canonical KEY that anagrams share, then bucket by it.
Sorting the characters is the obvious key; a 26-length count vector is
the O(n) alternative that avoids the log factor.

## Invariant

Two strings land in the same bucket iff they have identical character
multisets.

## Complexity

sorted key O(n * k log k)   count key O(n * k)   space O(n * k)

## Pitfall

Choosing the key IS the problem. Everything else is a hash map.

For the count-vector key you need something hashable — a `string` of 26
counts, or an `array<int,26>` with a custom hash. Counts above 9 make a
naive digit concatenation ambiguous, so use a separator or fixed-width
encoding.

## Status

NOT SOLVED. This was a scaffold in the Kotlin lab with a `TODO` body —
it was never implemented. Nothing to compare against; solve it fresh.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:src/main/kotlin/algorithms/problems/medium/group_anagrams/GroupAnagrams.kt
