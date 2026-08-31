# 179. Largest Number

leetcode | medium | sorting, comparator, greedy

## Task

Arrange the numbers to form the largest possible concatenation.

## Key insight

Sort with a custom comparator: a before b iff `a+b` > `b+a` as
strings. Comparing the concatenations directly is what makes 3 beat 30,
which no numeric or lexicographic ordering does.

## Invariant

That comparator is a strict weak ordering - it is transitive,
which is not obvious and is why this problem is worth doing. If it were
not, Java's TimSort would throw "Comparison method violates its general
contract".

## Complexity

time O(n log n * k)   space O(n)

## Pitfall

All-zero input gives "000" instead of "0" - check for a leading
zero at the end. Note also that you must box to String[] or Integer[] to
sort with a comparator at all; there is no comparator overload for
int[].

## Review

last: never   confidence: 0/5
