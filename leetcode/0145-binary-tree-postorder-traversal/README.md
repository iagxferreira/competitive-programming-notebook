# 145. Binary Tree Postorder Traversal

leetcode | easy | trees, dfs, stack

## Task

Return the postorder traversal of a binary tree's node values: **left,
right, node**.

`[1,null,2,3]` gives `[3,2,1]`. The empty tree gives `[]`.

`0 <= nodes <= 100`   `-100 <= Node.val <= 100`

Follow up: the recursive solution is trivial — do it iteratively.

## Key insight

Solved with the reverse trick: run the preorder walk mirrored - visit,
then go **right** first - which produces node, right, left. Reverse that
and you have left, right, node, which is postorder.

It dodges the real difficulty rather than confronting it, and that is the
point: no second stack, no visited flags, no revisit bookkeeping.

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

Before the reverse, `result` holds a node-right-left walk, which is the
exact mirror of preorder. Reversing a sequence mirrors it back, giving
left-right-node.

## Complexity

time O(n), including the O(n) reverse   space O(h) for the stack

## Pitfall

The difficulty named in the scaffold - a node cannot be emitted until
both subtrees are done - was resolved by not emitting in postorder at
all. Build the mirror order, where every node *can* be emitted on sight,
and reverse at the end.

Worth knowing the cost of that choice: it needs the whole result in
memory before it produces anything, so it cannot stream. The honest
single-stack version, which tracks the last node visited and only pops a
node once its right subtree is finished, does stream. Write that one too
at some point - it is the version that actually confronts the problem.

Watch the mirror carefully: descending must be `current.right` and the
pop step must be `current.left`. Getting those the usual way round gives
you a reversed *preorder*, which is not postorder and looks plausible on
a symmetric tree.

## Review

last: 2026-09-01   confidence: ?/5   (set your own)

## Origin

New problem - not in the legacy archive. Added on request. Completes the
traversal trio with 0094 and 0144.
