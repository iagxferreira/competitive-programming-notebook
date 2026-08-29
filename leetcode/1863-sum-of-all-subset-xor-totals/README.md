# 1863. Sum of All Subset XOR Totals

leetcode | easy | bit-manipulation, math

## Task

Sum the XOR of every subset.

## Key insight

Consider one bit position. If ANY element has that bit set, then across
all 2^n subsets that bit is set in exactly half of them — 2^(n-1). So the
answer is `OR(all elements) * 2^(n-1)`. No enumeration at all.

## Invariant

Each bit contributes independently.

## Complexity

time O(n)   space O(1) — versus O(2^n) for enumeration

## Pitfall

The counting argument is the entire problem, and it is easy to accept
without understanding. Re-derive WHY exactly half the subsets have the
bit set: fix one element that has it, and pair up subsets by whether they
contain that element — the pairing is a bijection that flips the bit.

Your Python version is the closed form. Write the O(2^n) brute force too
and check they agree on small inputs; that is what `tools/stress.sh` is
for.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/1863.subset-xor.py
