# 239. Sliding Window Maximum

leetcode | hard | monotonic-deque, sliding-window

## Task

Maximum of every window of size k.

## Key insight

Monotonic deque of INDICES, values decreasing from front to
back. Before pushing i, pop every index whose value is <= nums[i] - they
can never be the maximum again while i is in the window. The front is
always the answer.

## Invariant

The deque holds the indices of the current window that could
still be the maximum of some future window, in decreasing value order. The
front is inside the window because you evict `i - k` first.

## Complexity

time O(n)   space O(k)

## Pitfall

A heap gives O(n log n) and is accepted, so it is tempting -
but this problem exists to teach the deque, and the deque is what you need
when the window has to be O(n). Storing values instead of indices makes
the "has it fallen out of the window" check impossible.

## Review

last: never   confidence: 0/5
