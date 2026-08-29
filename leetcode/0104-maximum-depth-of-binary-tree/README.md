# 104. Maximum Depth of Binary Tree

leetcode | easy | trees, dfs

## Task

Number of nodes on the longest root-to-leaf path.

## Key insight

`depth(node) = 1 + max(depth(left), depth(right))`, with depth(null) = 0.
The recursion returns the answer directly — no accumulator needed.

## Invariant

Each call returns the height of the subtree rooted at that node.

## Complexity

time O(n)   space O(h)

## Pitfall

Your Go version threaded a `*int` maximum through the traversal. That
works, but the pure return-value formulation is shorter and has no shared
mutable state. Prefer it — and note the same file names its helper
`inOrderTraversal` even though it is a preorder walk.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/104-maximum-depth-bst.go
