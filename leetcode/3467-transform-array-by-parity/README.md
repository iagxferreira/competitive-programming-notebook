# 3467. Transform Array by Parity

leetcode | easy | counting, sorting

## Task

Replace evens with 0 and odds with 1, then sort ascending.

## Key insight

Sorting a binary array is just counting. Count the evens, then write that
many 0s followed by 1s. O(n) instead of O(n log n).

## Invariant

None.

## Complexity

counting O(n)   sorting O(n log n)   space O(1)

## Pitfall

Your Python version mapped then called `.sort()`. Correct, but the sort
is unnecessary work on a two-valued array — this is counting sort's
simplest case and worth recognising as such.

In C++, `%` on a negative number yields a negative remainder, so
`n % 2 == 1` is FALSE for negative odd values. Use `n % 2 != 0`, or
better `n & 1`. This is a real difference from Python, where `-3 % 2`
is 1.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/3467.transform-by-parity.py
