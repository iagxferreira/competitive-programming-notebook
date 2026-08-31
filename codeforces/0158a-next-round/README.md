# 158A. Next Round

codeforces | 800 | implementation, sorting

## Task

Scores are already sorted descending. Count contestants with a score
that is both positive and at least the k-th score.

## Key insight

Read `scores[k-1]` as the threshold, then count entries `>= threshold &&
> 0`. No sorting needed - the input is pre-sorted, which is easy to miss.

## Invariant

The input is non-increasing, so the qualifying set is a prefix.

## Complexity

time O(n)   space O(n)

## Pitfall

The `> 0` condition is the whole problem: a contestant with 0 points
never advances, even if the k-th score is also 0. Checking only
`>= threshold` passes the samples and fails the tests.

## Review

last: never   confidence: 0/5
