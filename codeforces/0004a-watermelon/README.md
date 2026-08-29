# 4A. Watermelon

codeforces | 800 | math, parity

## Task

Given weight w, decide whether it can be split into two positive even
parts. Print YES or NO.

## Key insight

Two even numbers always sum to an even number, so w must be even. But
w = 2 fails: the only split is 1 + 1, and both parts must be even and
positive. So the answer is `w % 2 == 0 && w > 2`.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

The `w > 2` guard is the whole problem — checking parity alone passes the
samples and fails the tests. This is the canonical example of a Div 2 A
where the edge case, not the idea, is what is being tested.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/codeforces/4a.py
