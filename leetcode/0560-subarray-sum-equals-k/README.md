# 560. Subarray Sum Equals K

leetcode | medium | prefix-sum, hashing

## Task

Number of contiguous subarrays summing to exactly k.

## Key insight

Prefix sums plus a hash map of counts. At index j, the number
of valid starts is how many times `prefix[j] - k` has already been seen.
One pass, no window - a sliding window does NOT work here because the
values may be negative, so the sum is not monotonic in the window size.

## Invariant

The map holds the frequency of every prefix sum strictly
before the current index. Seeding it with `{0: 1}` accounts for subarrays
that start at index 0.

## Complexity

time O(n)   space O(n)

## Pitfall

Two, both common. Forgetting the `{0: 1}` seed loses every
subarray beginning at the start. And updating the map BEFORE querying it
counts the empty subarray when k is 0 - query first, then insert.

## Review

last: never   confidence: 0/5
