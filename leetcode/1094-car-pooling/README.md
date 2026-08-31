# 1094. Car Pooling

leetcode | medium | intervals, difference-array, sweep-line

## Task

Trips are {passengers, from, to}. Can the car carry them all
without ever exceeding capacity?

## Key insight

The free version of Meeting Rooms II. Two ways, both worth
writing: a difference array over the 1001 possible stops (+p at `from`, -p
at `to`), then a prefix sum; or sort the events and sweep. The difference
array is O(n + range) and about four lines.

## Invariant

After prefix-summing, position i holds the number of
passengers on board over the segment starting at i.

## Complexity

time O(n + range)   space O(range)

## Pitfall

A passenger leaving at `to` frees the seat AT `to`, so the
decrement goes at index `to`, not `to + 1`. Off by one here silently
rejects valid inputs where one trip ends exactly where the next begins.

## Review

last: never   confidence: 0/5
