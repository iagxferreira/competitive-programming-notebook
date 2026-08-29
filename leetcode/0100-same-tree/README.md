# 100. Same Tree

leetcode | easy | trees, dfs

## Task

Are two binary trees identical in structure and values?

## Key insight

Three base cases then recurse: both null (equal), exactly one null
(unequal), values differ (unequal). Otherwise both subtrees must match.

## Invariant

The recursion compares nodes at identical positions in both trees.

## Complexity

time O(n)   space O(h)

## Pitfall

The order of the null checks matters. `both null` must be tested before
`one null`, or two empty trees are reported unequal. Your Go version has
them in the right order.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/100-same-tree.go
git show legacy-archive:legacy/python/leetcode/100.same-tree.py
