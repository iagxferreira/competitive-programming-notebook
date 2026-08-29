# Tree: Level Order Traversal

hackerrank | medium | trees, bfs, queue

## Task

Insert the given values into a BST in order, then print the node values
in level order (breadth-first), space separated.

## Key insight

Level order is BFS, and BFS is a queue. Pop the front, print it, push its
children left-then-right. The queue enforces the level ordering for free
— you never need to track depth explicitly for this variant.

## Invariant

The queue holds nodes in non-decreasing depth, and within a depth in
left-to-right order. Popping preserves both.

## Complexity

time O(n)   space O(n) for the queue (O(width) at peak)

## Pitfall

Two things. Push children only if non-null, or you dequeue null and
dereference it. And your Go version used `queue = queue[1:]` to pop,
which never releases the underlying array — fine at this size, but
`std::queue` is the right tool and pops in O(1) without the leak.

Building the BST is half the problem: values go left when strictly less,
right otherwise, which is what puts duplicates on the right.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/hackerrank/level_order.go
