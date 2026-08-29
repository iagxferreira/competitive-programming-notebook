# 160. Intersection of Two Linked Lists

leetcode | easy | linked-list, two-pointers

## Task

Return the node where two lists merge, or null. Identity, not value.

## Key insight

The elegant solution: walk pointer A through list A then list B, and B
through B then A. Both travel exactly `lenA + lenB` before the meeting
point, so they arrive together — at the intersection, or at null.

## Invariant

After the switch, the two pointers have equal remaining distance to the
merge point.

## Complexity

time O(n + m)   space O(1)

## Pitfall

Your Go version used a hash set of visited pointers — correct, but O(n)
space. The two-pointer trick is the point of the problem.

Switch each pointer to the OTHER head exactly once. Restarting on its own
list loops forever when there is no intersection; the cross-over is what
makes both hit null simultaneously.

Compare node references with `==`, never values or `.equals`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/160-get-intersection-node.go
