# 94. Binary Tree Inorder Traversal

leetcode | easy | trees, dfs

## Task

Return the inorder traversal of a binary tree.

## Key insight

Left, node, right. Recursion is three lines; the follow-up asks for the
iterative form, which needs an explicit stack: push all the way left,
pop and visit, then move to the right child.

## Invariant

Iterative version: the stack holds the ancestors whose values have not
been emitted yet.

## Complexity

time O(n)   space O(h), h = height

## Pitfall

Your Go version passes the accumulator by value and reassigns it
(`arr = inOrder(...)`), which works because it returns the slice — but in
C++ pass the vector by reference or you copy the whole thing at every
node, turning O(n) into O(n^2).

Do the iterative version too; it is the one interviews actually ask for.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/94-binary-tree-inorder-traversal.go
