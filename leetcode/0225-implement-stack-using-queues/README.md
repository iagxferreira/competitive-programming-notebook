# 225. Implement Stack using Queues

leetcode | easy | stack, queue, design

## Task

Implement a LIFO stack using ONLY queue operations: push to back, pop
from front, size, empty.

## Key insight

Make push do the work. Push onto the queue, then rotate the queue
`size - 1` times — dequeue and re-enqueue each older element — so the
newest element ends up at the front. Pop and top then become plain queue
operations.

## Invariant

The queue is always ordered newest-first, so its front is the stack top.

## Complexity

push O(n)   pop O(1)   top O(1)   space O(n)

## Pitfall

Your Go version did NOT solve this problem. It backed `MyStack` with a
slice and used append / truncate — that is just a stack implemented as a
stack. The entire constraint is that you may only use queue operations.
This one needs a genuine redo, not a port.

Rotate `size - 1` times, not `size` — a full rotation returns the queue
to where it started.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/225-stacks-using-queue.go
