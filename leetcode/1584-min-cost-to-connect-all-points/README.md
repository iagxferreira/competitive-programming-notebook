# 1584. Min Cost to Connect All Points

leetcode | medium | mst, union-find, heap, greedy

## Task

Connect all points at minimum total cost, where the cost between
two points is their Manhattan distance.

## Key insight

A minimum spanning tree on a complete graph. Kruskal: build
all n^2/2 edges, sort, and add one whenever union-find says the endpoints
are not yet connected. Prim with a heap avoids materialising the edges and
is the better fit for a dense graph like this one.

## Invariant

Kruskal: the chosen edges always form a forest, and each
added edge is the cheapest that reduces the component count. Prim: the
heap holds the cheapest known edge from the built tree to each outside
vertex.

## Complexity

time O(n^2 log n)   space O(n^2) for Kruskal, O(n) for Prim

## Pitfall

The first MST problem in this repo, so the point is the
template, not the answer. With n up to 1000 the edge list is ~500k entries
- sorting boxed Integer objects there will hurt; sort an int[][] with a
comparator on the weight column, or use Prim.

## Review

last: never   confidence: 0/5
