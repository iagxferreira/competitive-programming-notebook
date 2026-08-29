# Mini-Max Sum

hackerrank | easy | arrays, greedy

## Task

Given 5 integers, print the minimum and maximum sums obtainable by adding
exactly 4 of them.

## Key insight

Summing 4 of 5 is the same as dropping exactly 1. So the answers are
total - max and total - min. No sorting and no subset enumeration.

## Invariant

total is the sum of every element seen so far; min and max bound that
same prefix.

## Complexity

time O(n)   space O(1)

## Pitfall

Five values near the int limit overflow a 32-bit total. Accumulate in
`long` — your Go version was right to use int64 for the sum while
keeping the elements int32. In Java `int + int` stays int and wraps
silently, so widen the ACCUMULATOR, not just the result:
`long sum = 0;` not `long sum = a + b;`.

Your Go version also sorted the array and then computed min/max in the
loop anyway. The sort was dead work; drop it.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/hackerrank/min-max-sum.go
