# 938. Range Sum of BST

leetcode | easy | trees, dfs, binary-search

## Task

Sum of all node values in [low, high].

## Key insight

Prune using the BST ordering. If `node->val <= low` the entire left
subtree is below the range and can be skipped; if `node->val >= high` the
right subtree is above it. This is what makes the traversal better than
visiting every node.

## Invariant

Any subtree entered still overlaps the range.

## Complexity

time O(n) worst case, much less with pruning   space O(h)

## Pitfall

The pruning comparisons must be strict in the right direction:
`if (val > low) recurse left` and `if (val < high) recurse right`. Using
`>=` / `<=` there still gives the right sum but wastes the pruning; using
them in the inclusion test would double-count boundary values. Your
Python version separates the two tests correctly.

Bounds are inclusive on both ends.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/938.range-sum-bst.py
