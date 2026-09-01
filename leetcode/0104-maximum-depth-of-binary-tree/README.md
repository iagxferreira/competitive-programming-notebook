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

Solved 2026-09-01 with the return-value form, as recommended. Nothing
shared, nothing threaded through.

The one risk that remains is stack depth. The constraints allow 10^4
nodes, and a degenerate chain makes the recursion exactly that deep.
Measured rather than assumed: 10^4-node left and right chains both
complete on the default stack, and so do 5×10³. Do not read that as
general permission — the frames here are tiny (three locals, no
allocation). The repo template runs work on a 256MB-stack thread for
exactly this reason, and a heavier frame or a deeper input tips it.

## Review

last: 2026-09-01   confidence: ?/5   (set your own)

## Origin

git show legacy-archive:legacy/go/leetcode/104-maximum-depth-bst.go
