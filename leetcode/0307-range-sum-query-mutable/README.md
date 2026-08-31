# 307. Range Sum Query - Mutable

leetcode | medium | fenwick-tree, segment-tree, design

## Task

Support point updates and range-sum queries, interleaved.

## Key insight

Once updates are in the mix, a prefix-sum array costs O(n) per
update and a plain array costs O(n) per query. A Fenwick tree (binary
indexed tree) makes both O(log n) in about fifteen lines; a segment tree is
more code but generalises to min, max and gcd.

## Invariant

Fenwick node i covers the `i & -i` values ending at i. Walk
up by `i += i & -i` when updating, down by `i -= i & -i` when querying.

## Complexity

time O(log n) per operation   space O(n)

## Pitfall

A Fenwick tree is 1-indexed - the bit trick does not work from
zero, since `0 & -0` is 0 and the loop never advances. Convert at the
boundary. Also `update` takes a DELTA; this problem gives you an absolute
new value, so pass `value - current` and keep the raw array around.

## Review

last: never   confidence: 0/5
