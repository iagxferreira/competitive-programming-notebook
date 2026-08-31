# 210. Course Schedule II

leetcode | medium | topological-sort, graphs, bfs

## Task

Return any valid order to take all courses given prerequisites,
or an empty array when it is impossible.

## Key insight

Kahn's algorithm: compute in-degrees, seed a queue with every
zero-in-degree vertex, and repeatedly pop one and decrement its
neighbours. 207 only asked whether an order exists; this one wants the
order itself, which is exactly the sequence Kahn pops.

## Invariant

Everything already in the output has all of its
prerequisites in the output before it. A vertex enters the queue only when
its in-degree hits zero, which is precisely that condition.

## Complexity

time O(V + E)   space O(V + E)

## Pitfall

The cycle check is "did I output fewer than numCourses
vertices", not an exception. If you forget it you return a truncated order
that looks valid. Also note the pair is {course, prerequisite}, so the edge
runs prerequisite -> course, not the other way.

## Review

last: never   confidence: 0/5
