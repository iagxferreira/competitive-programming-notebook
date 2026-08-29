# 217. Contains Duplicate

leetcode | easy | hash-set

## Task

Does the array contain any value twice?

## Key insight

A set answers "have I seen this" in O(1). Check membership before
inserting and return on the first hit.

## Invariant

The set holds exactly the values at indices strictly before i.

## Complexity

time O(n)   space O(n)

## Pitfall

Return early. Building the whole set and comparing sizes at the end also
works but does needless work on the common case.

`unordered_set` is the direct translation, but sorting and scanning for
adjacent equals is O(n log n) time with O(1) space — know which trade you
are making rather than reaching for the map reflexively.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/217-contains-duplicate.go

Full study essay from the Kotlin lab (~300 lines):

    git show legacy-archive:problems/easy/contains-duplicate/README.md
