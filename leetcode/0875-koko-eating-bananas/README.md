# 875. Koko Eating Bananas

leetcode | medium | binary-search-on-answer

## Task

Smallest eating speed that finishes all piles within h hours.

## Key insight

Binary search the ANSWER, not an array. "Can she finish at
speed k?" is monotonic - true for every k above some threshold - so search
[1, max(piles)] for the first true. Recognising that a predicate is
monotonic is the whole skill, and it generalises to capacity, distance and
time-limit problems.

## Invariant

feasible(k) is false, false, ..., true, true. Keep the search
range as the smallest interval still containing the boundary.

## Complexity

time O(n log maxPile)   space O(1)

## Pitfall

Hours per pile is a CEILING: `(pile + k - 1) / k`, not
`pile / k`. And the total can exceed int when the piles are large - sum
into a long. Both mistakes give an answer that is merely slightly wrong,
which is harder to spot than a crash.

## Review

last: never   confidence: 0/5
