# 21. Merge Two Sorted Lists

leetcode | easy | linked-list

## Task

Merge two sorted lists into one sorted list by splicing nodes.

## Key insight

Repeatedly take the smaller head. Because both inputs are sorted, the
smaller of the two heads is the global minimum of what remains.

## Invariant

Everything already appended is sorted and <= both remaining heads.

## Complexity

time O(n + m)   space O(1) iterative, O(n + m) recursive

## Pitfall

Your Go version is recursive, which is elegant but O(n+m) stack — a
stack overflow risk on long lists. The iterative version with a dummy
head is O(1) space and is the one to write. Java's default stack
overflows around depth 10^4, well under this problem's 200-node limit,
but the habit matters for the deep-recursion problems later.

Do not forget to attach the non-empty remainder at the end.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/21-merge-two-sorted-lists.go
