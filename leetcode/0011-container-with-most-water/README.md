# 11. Container With Most Water

leetcode | medium | two-pointers, greedy

## Task

Pick two lines maximising `min(h[i], h[j]) * (j - i)`.

## Key insight

Start at the widest pair and always move the SHORTER wall inward. Moving
the taller one can only lose: width shrinks and the height is still
capped by the shorter wall, so no better answer is discarded.

## Invariant

The optimal pair is always still inside [left, right].

## Complexity

time O(n)   space O(1)

## Pitfall

Your Go version tracked `width` as a separate counter decremented once
per iteration. That happens to stay correct because exactly one pointer
moves each step — but it is a second source of truth that silently breaks
the moment the loop changes. Use `right - left` directly.

On ties move either pointer; both are safe.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/11-container-water.go
