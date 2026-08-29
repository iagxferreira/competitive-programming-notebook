# 232. Implement Queue using Stacks

leetcode | easy | stack, queue, design

## Task

Implement a FIFO queue using only stack operations.

## Key insight

Two stacks. Push onto `in`. To pop, if `out` is empty, drain `in` into
`out` — that single transfer reverses the order, turning LIFO into FIFO.
Then pop from `out`.

## Invariant

`out` holds the oldest elements in pop order; `in` holds the newest in
push order. Their concatenation is the queue.

## Complexity

push O(1)   pop amortised O(1)   space O(n)

## Pitfall

Transfer ONLY when `out` is empty. Moving elements early interleaves the
two halves and destroys the ordering.

The amortised bound is the interesting part: each element is moved
exactly once, so n operations cost O(n) even though a single pop can be
O(n).

Your Go version is correct but duplicates the transfer loop in both Pop
and Peek — factor it into one helper.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/232-queue-using-stack.go
