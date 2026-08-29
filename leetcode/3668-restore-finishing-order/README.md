# 3668. Restore Finishing Order

leetcode | easy | hash-set, arrays

## Task

Keep only the elements of `order` that appear in `friends`, preserving
order.

## Key insight

A filter. Membership must be O(1), so put `friends` into a set (or a
boolean array, since the values are small and bounded) before scanning.

## Invariant

Output preserves the relative order of `order`.

## Complexity

time O(n + m)   space O(m)

## Pitfall

Your Python version wrote `participant in friends` where `friends` is a
LIST — that is a linear scan per element, making the whole thing O(n*m).
It passes at these constraints and is quietly quadratic. Converting to a
set first is a one-word change in Python and the difference between
passing and TLE at larger bounds.

In C++ use `vector<bool>` indexed by value; it beats `unordered_set` when
the value range is small.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/3668.finish-order.py
