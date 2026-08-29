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

`HashSet<Integer>` is the direct translation, but note it boxes every
element — for a tight time limit a `long`-encoded open-addressing set or
a sort is measurably faster.

If you take the sort route, remember `Arrays.sort(int[])` is dual-pivot
quicksort with adversarial O(n^2) cases that get hacked on Codeforces.
Shuffle first, or sort a boxed `Integer[]` which uses TimSort.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/217-contains-duplicate.go

Full study essay from the Kotlin lab (~300 lines):

    git show legacy-archive:problems/easy/contains-duplicate/README.md
