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

Three notes on the solution as written, none of them bugs:

`containsKey` then `put` then `get` hashes the key three times per word.
`seen.computeIfAbsent(sorted, k -> new ArrayList<>()).add(s)` does it
once, and is the idiom to reach for every time you build a map of lists.

The `strs == null` guard is dead — the constraints promise
`1 <= strs.length`. The `length == 0` half is also unreachable, though it
would be correct if it were.

`new ArrayList<>(seen.values())` returns groups in `HashMap` iteration
order, which is unspecified. The judge accepts any order here, so this is
fine — just do not build anything on top of it that assumes an order.

## Status

Solved fresh on 2026-08-31, with the sorted-characters key. There is no
prior attempt to diff against: the Kotlin original was a `TODO` scaffold,
so the Origin command below returns an empty body.

## Review

last: 2026-08-31   confidence: ?/5   (set your own)

## Origin

git show legacy-archive:src/main/kotlin/algorithms/problems/medium/group_anagrams/GroupAnagrams.kt
