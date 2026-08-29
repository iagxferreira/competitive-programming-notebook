# 167. Two Sum II - Input Array Is Sorted

leetcode | medium | two-pointers

## Task

Sorted array, find the two values summing to target. Return 1-indexed
positions. O(1) extra space.

## Key insight

Two pointers from both ends. If the sum is too small only `left++` can
increase it; if too large only `right--` can decrease it. Sortedness
turns the hash map of problem 1 into a constant-space scan.

## Invariant

The answer pair, if it exists, always lies within [left, right].

## Complexity

time O(n)   space O(1)

## Pitfall

The indices are ONE-BASED. Returning 0-based is the most common wrong
answer here.

The O(1) space requirement is what rules out reusing the problem-1 hash
map. Understanding why each pointer move is safe — that you discard only
pairs that cannot be the answer — is the reusable part, and it is the
same argument underpinning 3Sum and container-with-most-water.

## Status

NOT SOLVED. Kotlin lab scaffold with a `TODO` body.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:src/main/kotlin/algorithms/problems/medium/two_sum_ii/TwoSumIi.kt
