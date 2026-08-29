# 1367. Linked List in Binary Tree

leetcode | medium | trees, linked-list, dfs

## Task

Does the linked list appear as a downward path in the tree?

## Key insight

Two nested recursions. The outer one tries every tree node as a possible
starting point; the inner one checks whether the list matches going
strictly downward from there. This is the tree analogue of naive
substring search.

## Invariant

checkPath(head, node) is true iff the remaining list matches some
downward path starting at node.

## Complexity

time O(n * min(len, height))   space O(height)

## Pitfall

The base cases must be ordered: list exhausted means SUCCESS, and it must
be tested before the null-tree check. Reversing them reports failure on a
complete match that ends exactly at a leaf. Your Python version has the
order right.

A match must be contiguous and downward — you cannot restart mid-path,
which is why the outer traversal is needed at all.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/1367.linked-list-in-binary-tree.py
