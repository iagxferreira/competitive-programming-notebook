# 98. Validate Binary Search Tree

leetcode | medium | trees, dfs

## Task

Is the binary tree a valid BST?

## Key insight

A tree is a BST exactly when its inorder traversal is strictly
increasing. Your Go version used that directly. The alternative is to
push (min, max) bounds down the recursion, tightening one side at each
step.

## Invariant

Bounds version: every node must lie strictly inside the open interval
inherited from its ancestors.

## Complexity

time O(n)   space O(h), or O(n) if you materialise the traversal

## Pitfall

The classic wrong answer compares each node only against its immediate
children. That accepts trees where a deep left-subtree node exceeds a
distant ancestor — the constraint is global, not local.

Strictly increasing: equal adjacent values are invalid. Your `>=` test is
correct.

Bounds must be `long` (or nullable `Integer`), since a node may
legitimately hold `Integer.MIN_VALUE` or `MAX_VALUE` — seeding the
recursion with those as sentinels then rejects a valid tree.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/98-valid-bst.go
git show legacy-archive:legacy/python/leetcode/98.valid-bst.py
