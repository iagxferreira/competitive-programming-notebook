# 1. Two Sum

leetcode | easy | hash-map

## Task

Return indices of the two numbers summing to target. Exactly one answer
exists; you may not reuse an element.

## Key insight

Instead of searching for a partner, remember what you have seen. For each
x, the partner you need is `target - x` — a lookup, not a scan.

## Invariant

The map holds value -> index for every element strictly left of i. So a
hit is always a distinct earlier element, which is what makes reuse
impossible by construction.

## Complexity

time O(n)   space O(n)

## Pitfall

Your Go version was the O(n^2) double loop. It passes, but this problem
exists to teach the trade of space for time — redo it with the map.

Check the map BEFORE inserting x, otherwise `target == 2*x` matches the
element against itself.

## Review

last: 2026-08-28   confidence: ?/5   (solved in C++, ported to Java)

## Origin

git show legacy-archive:legacy/go/leetcode/1-two-sum.go
git show legacy-archive:legacy/python/leetcode/1.two-sum.py

Full study essay from the Kotlin lab (~300 lines):

    git show legacy-archive:problems/easy/two-sum/README.md
