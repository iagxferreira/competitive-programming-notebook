# 6. Zigzag Conversion

leetcode | medium | strings, simulation

## Task

Write the string in a zigzag over numRows rows, then read it off row by
row.

## Key insight

Index arithmetic beats simulation. One full zigzag cycle spans
`2 * (numRows - 1)` characters. Row 0 and the last row contribute one
character per cycle; every middle row contributes two, the second offset
by `cycle - 2*row`.

## Invariant

Within a cycle, row r is visited at offsets r and cycle - r.

## Complexity

time O(n)   space O(n) for the output

## Pitfall

`numRows == 1` makes the cycle length 0 and the loop never advances —
guard it up front, as your Go version did.

Building the result with `rows += ...` reallocates repeatedly; reserve n
bytes instead.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/6-zigzag.go
