# 108. Convert Sorted Array to Binary Search Tree

leetcode | easy | trees, divide-and-conquer

## Task

Build a height-balanced BST from a sorted array.

## Key insight

The middle element becomes the root; recurse on the halves. Choosing the
midpoint is what guarantees balance, and the sorted order is what
guarantees the BST property.

## Invariant

buildTree(lo, hi) returns a balanced BST over exactly nums[lo..hi].

## Complexity

time O(n)   space O(log n) recursion

## Pitfall

Base case is `lo > hi` returning null, which handles both the empty array
and the bottom of every branch. Your Go version has this right.

`(lo + hi) / 2` can overflow for large indices; `lo + (hi - lo) / 2` is
the habit worth building, even though n is small here.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/108-sorted-array-to-bst.go
