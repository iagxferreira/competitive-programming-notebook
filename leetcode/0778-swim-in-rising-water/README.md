# 778. Swim in Rising Water

leetcode | hard | dijkstra, binary-search, union-find, grid

## Task

Least time t at which you can walk from the top-left to the
bottom-right of a grid, moving only onto cells with height <= t.

## Key insight

The cost of a path is the MAXIMUM cell on it, not the sum. So
run Dijkstra with `max` in place of `+`: the priority is the largest height
seen so far on the way here. Two other complete solutions - binary search
on t plus a flood fill, and union-find adding cells in height order.

## Invariant

Dijkstra's argument survives the change because max, like
addition, is monotonic: extending a path can never lower its cost.

## Complexity

time O(n^2 log n)   space O(n^2)

## Pitfall

Writing `dist[v] = dist[u] + grid[v]` out of habit. It is
`Math.max(dist[u], grid[v])`. The sum version passes the small examples and
fails the moment a long cheap path beats a short expensive one.

## Review

last: never   confidence: 0/5
