# 144. Binary Tree Preorder Traversal

leetcode | easy | trees, dfs, stack

## Task

Return the preorder traversal of a binary tree's node values: **node,
left, right**.

`[1,null,2,3]` gives `[1,2,3]`. The empty tree gives `[]`.

`0 <= nodes <= 100`   `-100 <= Node.val <= 100`

Follow up: the recursive solution is trivial — do it iteratively.

## Key insight

Solved iteratively, straight past the recursion.

Rather than the usual push-root-then-push-right-then-left version, this
reuses the inorder skeleton and just moves the visit: emit the node when
you *push* it on the way down, instead of when you pop it. Node before
children is exactly what preorder means, so moving one line is the whole
change.

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

## Invariant

The stack holds the ancestors of `current` whose right subtrees have not
been walked yet. Every node has been emitted by the time it is popped.

## Complexity

time O(n)   space O(h) for the stack, h = height

## Pitfall

No wrong turn here - the root-with-both-children case, which is what
separates a correct stack version from one that emits children in the
wrong order, was right first time. Verified against a recursive
reference.

The one thing to watch in the more common formulation (push the root,
then pop and push right then left) is that a stack reverses you, so the
children go on in reverse. This version sidesteps that entirely by never
pushing both children.

`ArrayDeque` is the right stack here. Never `java.util.Stack` - it is
synchronised and extends `Vector`.

## Review

last: 2026-09-01   confidence: ?/5   (set your own)

## Origin

New problem - not in the legacy archive. Added on request. Completes the
traversal trio with 0094 and 0145.
