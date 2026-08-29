# 1038. Binary Search Tree to Greater Sum Tree

leetcode | medium | trees, dfs

## Task

Replace each node's value with the sum of all values greater than or
equal to it.

## Key insight

REVERSE inorder — right, node, left — visits values in descending order.
Carry a running total; each node's new value is that total after adding
its own.

## Invariant

The accumulator holds the sum of every value strictly greater than the
node about to be visited.

## Complexity

time O(n)   space O(h)

## Pitfall

The direction is everything. Ordinary inorder ascends and gives you the
sum of SMALLER values instead.

Your Python version threads the accumulator through return values, which
is correct but genuinely hard to read — `node.val += dfs(node.right,
count)` mutates and returns in the same expression. Java has no
by-reference ints, so carry the running total as a FIELD on the solution
class (or a one-element `int[]`); that is far clearer than threading it
through return values.

Be aware a field persists between calls if the judge reuses the
instance — reset it at the top of the public method.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/1038.bst-to-gst.py
