# 1A. Theatre Square

codeforces | 1000 | math, overflow

## Task

Cover an n x m square with a x a flagstones; stones may overhang and
cannot be broken. Minimum number of stones.

## Key insight

Rows and columns are independent: `ceil(n/a) * ceil(m/a)`. There is no
geometry here at all - the entire problem is integer arithmetic done
carefully.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

The single most famous Java trap on Codeforces. n, m, a go up to 1e9, so
the product reaches 1e18 - it MUST be `long`. Read as long, multiply as
long. An int overflow here wraps silently and prints a plausible negative.
Second trap: integer ceiling is `(n + a - 1) / a`, never
`Math.ceil((double) n / a)` - a double loses precision above 2^53 and gives
the wrong answer for large inputs.

## Review

last: never   confidence: 0/5
