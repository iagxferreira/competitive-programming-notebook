# 101. Symmetric Tree

leetcode | easy | trees, dfs

## Task

Is the tree a mirror of itself?

## Key insight

Compare two nodes at mirrored positions: `left->left` against
`right->right`, and `left->right` against `right->left`. This is
problem 100 with one of the child pairings crossed.

## Invariant

Every popped pair occupies mirrored positions in the tree.

## Complexity

time O(n)   space O(h)

## Pitfall

The crossed pairing is the whole problem. Comparing left-with-left
straight down just tests the tree against itself and returns true always.

Your Python version pushes `root.right, root.left` without a null check
on root — it dereferences immediately. Guard the empty tree.

Order matters when pushing pairs onto an explicit stack: push and pop
consistently or the pairings desynchronise.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/101.symmetric-tree.py
