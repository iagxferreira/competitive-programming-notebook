# 102. Binary Tree Level Order Traversal

leetcode | medium | trees, bfs, queue

## Task

Return node values grouped by level.

## Key insight

BFS, but snapshot `queue.size()` at the top of each round. That count is
exactly the width of the current level, so the inner loop consumes one
level and everything pushed during it belongs to the next.

## Invariant

At the start of each outer iteration the queue holds exactly one complete
level.

## Complexity

time O(n)   space O(width)

## Pitfall

Capture the size BEFORE the inner loop. Reading `queue.size()` inside the
loop sees the children being pushed and merges all the levels into one.
Your Go version captures it correctly into `currentLevel`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/102-binary-tree-level-order.go
