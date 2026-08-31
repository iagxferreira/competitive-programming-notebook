# 64. Minimum Path Sum

leetcode | medium | dp, grid

## Task

Cheapest path from the top-left to the bottom-right, moving only right or down.

## Key insight

The plainest grid dp there is, and the right rung before 221.
Every cell is entered from above or from the left, so
`dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])`. One row of state is
enough if you update it left to right in place.

## Invariant

dp[r][c] is the cheapest cost to reach (r, c) from the origin.

## Complexity

time O(rows*cols)   space O(cols)

## Pitfall

The first row and first column have only one predecessor each.
Handle them before the main loop rather than special-casing inside it -
`Math.min` against an uninitialised 0 quietly returns 0 and poisons the
whole table.

## Review

last: never   confidence: 0/5
