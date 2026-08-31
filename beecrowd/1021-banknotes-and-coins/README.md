# 1021. Banknotes and Coins

beecrowd | medium | floating-point, greedy, io

## Task

Decompose a monetary value into notes (100 down to 2) and coins (1.00
down to 0.01), using as few pieces as possible.

## Key insight

Do the whole thing in integer CENTS. Read the value as a string or
multiply by 100 and round, then run the same greedy as 1018 over a
denomination table in cents.

## Invariant

After each denomination the remainder is strictly smaller than it.

## Complexity

time O(1)   space O(1)

## Pitfall

The classic floating-point failure, and the reason this problem is rated
above its neighbours. `(int)(value * 100)` on a value like 576.73 can land
on 57672 because the double is really 576.7299999... Use
`Math.round(value * 100)` and hold the result in a long. Every currency
problem you ever meet has this bug available.

## Review

last: never   confidence: 0/5
