# 547. Number of Provinces

leetcode | medium | union-find, graphs, dfs

## Task

Count connected components in an undirected graph given as an
adjacency matrix.

## Key insight

The plainest possible union-find problem, and the right place
to write DSU for the first time. Union every connected pair, then count
distinct roots - or keep a counter and decrement on each successful union.
A DFS from each unvisited node works equally well; write both.

## Invariant

After processing edge (i, j), i and j have the same root.
find() with path compression keeps every lookup near O(1).

## Complexity

time O(n^2 * alpha(n))   space O(n)

## Pitfall

Union by size or rank is not optional decoration: without it,
a chain of unions builds a linked list and find() degrades to O(n).
Path compression alone is usually enough in practice, but write both -
this is the template you will reuse for 684 and 1584.

## Review

last: never   confidence: 0/5
