# 111. Minimum Depth of Binary Tree

leetcode | easy | trees, bfs

## Task

Number of nodes on the shortest root-to-LEAF path.

## Key insight

BFS returns the moment it dequeues a leaf, because the first leaf reached
is necessarily at minimum depth. DFS must explore everything.

## Invariant

BFS visits nodes in non-decreasing depth order.

## Complexity

DFS O(n)   BFS O(n) worst case but exits early   space O(h) / O(width)

## Pitfall

This is NOT the mirror of problem 104. `1 + min(left, right)` is wrong
for a node with one child: the null side reports 0 and you get a path
that stops at a non-leaf. A leaf is a node with BOTH children null —
your Go version tests exactly that, which is why it is correct.

Since you already have the DFS, write the BFS version here for the early
exit.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/111-min-depth-bst.go
