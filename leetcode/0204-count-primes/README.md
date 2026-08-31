# 204. Count Primes

leetcode | medium | sieve, math, number-theory

## Task

How many primes are strictly less than n.

## Key insight

Sieve of Eratosthenes. Mark multiples of each prime as
composite; whatever survives is prime. Start marking from p*p, because
every smaller multiple already had a smaller prime factor, and stop the
outer loop at sqrt(n).

## Invariant

When the outer loop reaches p, every composite with a factor
below p is already marked, so an unmarked p must be prime.

## Complexity

time O(n log log n)   space O(n)

## Pitfall

`p * p` overflows int when n is near 2^31 - use `long`, or loop
while `p <= n / p`. Testing each number with trial division is O(n sqrt n)
and times out; the sieve is the point, and it is the tool you will reuse
for factorisation and totients.

## Review

last: never   confidence: 0/5
