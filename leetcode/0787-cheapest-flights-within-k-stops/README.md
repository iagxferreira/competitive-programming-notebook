# 787. Cheapest Flights Within K Stops

leetcode | Medium | graph, dynamic-programming, shortest-path, heap

## Task

There are `n` cities connected by some number of flights, given as
`flights[i] = [from_i, to_i, price_i]`. Given `src`, `dst` and `k`,
return the cheapest price from `src` to `dst` with at most `k` stops. If
there is no such route, return `-1`.

`1 <= n <= 100`   `0 <= flights.length <= (n * (n - 1) / 2)`   `0 <=
from_i, to_i < n`, `from_i != to_i`   `1 <= price_i <= 10^4`   No
duplicate edges.   `0 <= src, dst, k < n`   `src != dst`

## Key insight

<!-- Fill in AFTER solving, in your own words. Name the technique and say
     what it buys you over the brute force. -->

## Invariant

<!-- What is true at every step of your loop or recursion? May be "none"
     for a pure simulation - say so rather than inventing one. -->

## Complexity

time O(?)   space O(?)

## Pitfall

<!-- Fill in AFTER solving: the specific way you got this wrong, or the
     one you had to think hardest to avoid. Check the constraints for
     overflow, empty input and the largest case before writing "none". -->

## Review

last: never   confidence: 0/5

## Origin

New problem - not in the legacy archive. Added from the pattern study
list.
