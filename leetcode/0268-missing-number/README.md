# 268. Missing Number

leetcode | Easy | array, hash-table, math

## Task

Given an array `nums` containing `n` distinct numbers in the range `[0,
n]`, return the only number in the range that is missing from the array.

`n == nums.length`   `1 <= n <= 10^4`   `0 <= nums[i] <= n`

Follow up: Could you implement a solution using only `O(1)` extra space
complexity and `O(n)` runtime complexity?

## Key insight

Sort, then walk the array: the first index where `nums[i] != i` is the
missing value. If the scan runs to the end, the gap is `n` itself.

## Invariant

Everything scanned so far is exactly `0..i-1`, so the first mismatch is
the first value that never appears.

## Complexity

time O(n log n)   space O(1)

## Pitfall

The tail case is the one to get wrong: when nothing is missing inside the
array the answer is `nums.length`, not `-1` and not `nums.length - 1`.
The loop cannot return it, so the return after the loop carries it.

`Arrays.sort(int[])` is dual-pivot quicksort with adversarial O(n^2)
inputs. Harmless here, hackable on Codeforces - shuffle first or sort a
boxed `Integer[]` if you reuse this shape under a contest clock.

The follow-up is still open: O(n) time, O(1) space, no sorting. You have
n+1 candidate values and exactly n of them present - identify the odd one
out in a single pass instead of imposing an order first.

## Review

last: 2026-08-31   confidence: ?/5   (set your own)

## Origin

New problem - not in the legacy archive. Added from the Blind 75 and
Grind 75 lists.
