# 2D Array - DS

hackerrank | easy | matrix, brute-force

## Task

Maximum hourglass sum in a 6x6 grid, where an hourglass is the fixed
3x3 pattern with the middle row's outer cells removed.

## Key insight

Only 16 hourglass positions exist, so a double loop over top-left
corners with the seven cells summed inline is the whole solution. No
cleverness required, and none available.

## Invariant

None.

## Complexity

time O(1) for the fixed 6x6   space O(1)

## Pitfall

Initialising the maximum to 0. Values range down to -9, so an all-
negative grid has a negative answer and 0 is not a valid starting point -
use `Integer.MIN_VALUE` or the first hourglass. This is the single most
common failure on this problem.

## Review

last: never   confidence: 0/5
