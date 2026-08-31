# 50A. Domino Piling

codeforces | 800 | math, greedy

## Task

Maximum number of 1 x 2 dominoes fitting in an M x N board without
overlap.

## Key insight

`M * N / 2`, using integer division. Whatever the parity, at most one
cell can be left over, and a tiling achieving that always exists.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Trying to construct or simulate a tiling. This is a counting argument -
the answer is a formula, and reaching for a grid means you have not
finished thinking. The bound is small enough that int is safe here, unlike
1A.

## Review

last: never   confidence: 0/5
