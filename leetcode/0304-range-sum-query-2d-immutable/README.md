# 304. Range Sum Query 2D - Immutable

leetcode | medium | prefix-sum, matrix, design

## Task

Answer many rectangle-sum queries on a fixed matrix.

## Key insight

The 2D version of 303. Build `pre[r+1][c+1]` = sum of the
rectangle from the origin. Each cell adds the one above and the one to the
left, then subtracts the overlap counted twice. A query is then four
lookups: bottom-right - above - left + the doubly-subtracted corner.

## Invariant

`pre[r][c]` is the sum of all cells strictly above row r and left of column c.

## Complexity

time O(rows*cols) build, O(1) per query   space O(rows*cols)

## Pitfall

Inclusion-exclusion signs. Write the four-term formula out on
paper once with a small grid rather than guessing which corner gets added
back. Padding the array by one row and column is what removes every
boundary check - do it.

## Review

last: never   confidence: 0/5
