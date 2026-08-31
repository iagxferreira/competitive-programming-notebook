# 221. Maximal Square

leetcode | medium | dp, grid

## Task

Area of the largest square of 1s in a binary matrix.

## Key insight

`dp[r][c]` is the side of the largest square whose BOTTOM-RIGHT
corner is (r, c). If the cell is 1 it is
`1 + min(up, left, up-left)` - all three must support the square, so the
smallest one caps it. Track the running maximum side, and square it at the
end.

## Invariant

Every dp value is the side of a square that genuinely fits, ending at that cell.

## Complexity

time O(rows*cols)   space O(cols)

## Pitfall

Two. The answer is the AREA, so square the side before
returning. And the grid holds chars '0'/'1', not ints - comparing against
0 rather than '0' makes every cell look like a 1.

## Review

last: never   confidence: 0/5
