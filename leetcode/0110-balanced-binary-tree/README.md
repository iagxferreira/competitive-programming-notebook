# 110. Balanced Binary Tree

leetcode | easy | trees, dfs

## Task

Is every node's two subtree heights within 1 of each other?

## Key insight

Return height and balance TOGETHER from one traversal. Computing height
separately at each node re-walks the same subtrees and costs O(n^2).

## Invariant

Each call returns the true height of its subtree plus whether everything
below is balanced.

## Complexity

time O(n)   space O(h)

## Pitfall

The naive `isBalanced(node) = |h(l) - h(r)| <= 1 && isBalanced(l) &&
isBalanced(r)` is O(n log n) at best and O(n^2) on a skewed tree. Your
Python version correctly bundles both results into one return.

In C++ return a `pair<bool, int>`, or use -1 as a sentinel height meaning
"already unbalanced" and short-circuit on it.

Balance is required at EVERY node, not just the root.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/110.balanced-binary-tree.py
