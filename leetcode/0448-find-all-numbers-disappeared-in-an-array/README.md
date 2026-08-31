# 448. Find All Numbers Disappeared in an Array

leetcode | Easy | array, hash-table

## Task

Given an array `nums` of `n` integers where `nums[i]` is in the range
`[1, n]`, return an array of all the integers in the range `[1, n]` that
do not appear in `nums`.

`n == nums.length`   `1 <= n <= 10^5`   `1 <= nums[i] <= n`

Follow up: could you do it without extra space and in O(n) runtime? The
returned list does not count as extra space.

## Key insight

Two passes, opposite directions. First put the values into a set, then
walk the candidates `1..n` and report the ones the set does not hold. The
set answers membership in O(1), so the second pass is linear instead of a
scan per candidate.

## Invariant

`present` holds exactly the distinct values of `nums`, and `answer` holds
every candidate below `i` that is not among them - already in ascending
order, so no sort at the end.

## Complexity

time O(n)   space O(n)

## Pitfall

Enumerate the candidates, not the entries. Asking whether `nums[i]` is in
a set built from `nums` is true by construction and can never produce an
answer - the things that might be missing are the numbers `1..n`.

The second loop runs over values, so it is `1..n` inclusive, not the
`0..n-1` of an index loop.

`Arrays.asList(nums)` on an `int[]` does not build a list of numbers.
`asList` is generic varargs and `int` is not a reference type, so the
whole array binds as a single element: a `List<int[]>` of size one. It
compiles, `contains` boxes to `Integer`, and every lookup is false.

## Review

last: 2026-08-31   confidence: ?/5   (set your own)

## Origin

New problem - not in the legacy archive. Added from the pattern study
list.
