# 1470. Shuffle the Array

leetcode | easy | arrays

## Task

Given [x1..xn, y1..yn], return [x1, y1, x2, y2, ...].

## Key insight

Index arithmetic: element i pairs with element i + n.

## Invariant

None.

## Complexity

time O(n)   space O(n) for the output

## Pitfall

Nothing subtle. `reserve(2 * n)` to avoid reallocation.

The in-place O(1)-space variant exists and uses the same
encode-two-values-in-one-slot trick as problem 1920, if you want the
harder version.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/1470.shuffle-array.py
