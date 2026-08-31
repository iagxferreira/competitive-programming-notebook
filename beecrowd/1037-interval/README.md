# 1037. Interval

beecrowd | easy | conditionals, io

## Task

Read a float and print which of several half-open intervals it falls
into, or the out-of-range message.

## Key insight

A cascade of `if / else if`, ordered so each test only has to check the
upper bound - the lower one is implied by the branches already rejected.

## Invariant

On reaching branch k, the value is known to exceed every earlier bound.

## Complexity

time O(1)   space O(1)

## Pitfall

The intervals are half-open, `(a, b]`, so a value exactly on a boundary
belongs to the LOWER interval - `<=` not `<`. Boundary values are exactly
what the hidden tests contain. Copy the bracket notation from the
statement into the output verbatim.

## Review

last: never   confidence: 0/5
