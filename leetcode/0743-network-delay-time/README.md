# 743. Network Delay Time

leetcode | medium | dijkstra, graphs, heap

## Task

Time for a signal from node k to reach every node in a weighted
directed graph, or -1 if some node is unreachable.

## Key insight

Plain Dijkstra, with the twist that the answer is the MAXIMUM
of the distances, not one of them: the signal is done when the slowest node
has it. Java's PriorityQueue is a min-heap, which is what you want here.

## Invariant

Once a node is polled off the heap its distance is final -
that is the whole correctness argument, and it depends on every weight
being non-negative.

## Complexity

time O(E log V)   space O(V + E)

## Pitfall

Nodes are labelled 1..n, not 0..n-1. Either size the arrays
n + 1 and ignore index 0, or subtract 1 everywhere - mixing the two is the
usual off-by-one. Also skip stale heap entries with a `if (d > dist[u])
continue;` guard instead of trying to decrease-key.

## Review

last: never   confidence: 0/5
