# 684. Redundant Connection

leetcode | medium | union-find, graphs

## Task

A tree plus one extra edge. Return the edge to delete; if several
qualify, the one latest in the input.

## Key insight

Union-find as a cycle detector. Process the edges in order and
the first union that FAILS - both endpoints already share a root - is the
edge that closes a cycle. Because you scan in order, that is automatically
the last valid answer.

## Invariant

Before processing edge e, the DSU represents exactly the
forest built from the edges before e. A union fails iff e connects two
vertices already joined, i.e. iff e closes a cycle.

## Complexity

time O(n * alpha(n))   space O(n)

## Pitfall

Nodes are labelled 1..n. Size the parent array n + 1 or every
index is off by one. Returning the FIRST cycle edge found by a DFS is a
different answer from what the problem asks - the DSU scan gets the
tie-break right for free.

## Review

last: never   confidence: 0/5
