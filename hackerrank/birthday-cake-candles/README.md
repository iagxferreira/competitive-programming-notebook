# Birthday Cake Candles

hackerrank | easy | arrays, counting

## Task

How many candles have the maximum height.

## Key insight

One pass tracking both the max and its count: a bigger value resets the
count to 1, an equal value increments it. No second pass and no sort
needed.

## Invariant

(max, count) always describes the prefix scanned so far.

## Complexity

time O(n)   space O(1)

## Pitfall

Initialising max to 0 works only because heights are positive - make it
`Integer.MIN_VALUE` or the first element, as a habit. Sorting to find the
max is O(n log n) for an O(n) job.

## Review

last: never   confidence: 0/5
