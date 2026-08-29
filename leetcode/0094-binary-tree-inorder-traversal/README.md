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
(`arr = inOrder(...)`), which works because it returns the slice. In Java
this concern disappears: a `List` parameter is already a reference, so
passing it down and calling `add` mutates the one list. Just do not
reassign the parameter and expect the caller to see it.

Do the iterative version too; it is the one interviews actually ask for.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/94-binary-tree-inorder-traversal.go
