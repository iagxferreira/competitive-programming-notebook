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

Solved 2026-09-01 with the iterative stack version directly, skipping
the recursion. No wrong turn - correct first time, and verified against a
recursive reference.

All three of your traversals share one skeleton, which is worth noticing
and keeping:

```
while (current != null || !stack.isEmpty())
    if (current != null)  push, step one way
    else                  pop, step the other way
```

- **inorder** - step left on the way down, visit on the pop, then right
- **preorder** - same walk, visit moved to the push instead of the pop
- **postorder** - mirror it (down the RIGHT), visit on the push, then
  reverse the whole result at the end

One loop, three orders, differing only in where `visit` sits and which
child you descend to.

## Review

last: 2026-09-01   confidence: ?/5   (set your own)
