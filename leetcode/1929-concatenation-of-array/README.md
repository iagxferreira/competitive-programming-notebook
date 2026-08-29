# 1929. Concatenation of Array

leetcode | easy | arrays

## Task

Return nums concatenated with itself.

## Key insight

Allocate 2n up front and fill index i and i+n in the same iteration.

## Invariant

None.

## Complexity

time O(n)   space O(n)

## Pitfall

Reserve the full size before filling. Repeatedly pushing back into an
unreserved vector reallocates and copies as it grows — the asymptotics
survive but the constant does not.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/1929-array-concatenation.go
