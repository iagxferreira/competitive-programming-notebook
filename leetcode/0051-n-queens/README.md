# 51. N-Queens

leetcode | hard | backtracking, sets

## Task

All distinct placements of n queens on an n x n board with none attacking.

## Key insight

One queen per row, so rows can never conflict. Track columns
and both diagonal directions in sets: a '\' diagonal shares `row - col`,
a '/' diagonal shares `row + col`. Conflict checks become O(1).

## Invariant

The three sets hold exactly the columns and diagonals used by
queens in rows 0..row-1. Every add on the way down has a matching remove
on the way out.

## Complexity

time O(n!)   space O(n^2) for the boards

## Pitfall

`row - col` goes negative, so it cannot index an array
directly - offset by n - 1, or use a HashSet. Getting this wrong gives an
ArrayIndexOutOfBounds that looks like a logic bug.

## Review

last: never   confidence: 0/5
