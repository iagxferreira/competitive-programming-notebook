# 226. Invert Binary Tree

leetcode | easy | trees, dfs

## Task

Mirror a binary tree.

## Key insight

Swap the children at every node and recurse. Three lines.

## Invariant

After the call on a node, the subtree rooted there is fully mirrored.

## Complexity

time O(n)   space O(h)

## Pitfall

Your Go version wrote `root.Left, root.Right = invertTree(root.Right),
invertTree(root.Left)` — Go's tuple assignment evaluates the right side
completely before assigning, so this is safe there.

C++ has NO such guarantee for a comma-separated assignment. You must save
one pointer in a temporary, or call `std::swap` first and then recurse.
Translating this line literally is a genuine bug.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/226-invert-binary-tree.go
