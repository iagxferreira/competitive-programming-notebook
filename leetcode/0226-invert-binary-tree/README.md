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

Java has no tuple assignment at all, so you must write two statements —
and the naive pair is WRONG:

    root.left = invertTree(root.right);
    root.right = invertTree(root.left);   // reads the NEW left

The second line sees the value just assigned. Save one child in a
temporary first, or swap the two references and then recurse.

## Review

last: 2026-08-29   confidence: ?/5   (post-order swap — set your own confidence)

## Origin

git show legacy-archive:legacy/go/leetcode/226-invert-binary-tree.go
