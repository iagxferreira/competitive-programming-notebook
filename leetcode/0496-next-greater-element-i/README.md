# 496. Next Greater Element I

leetcode | easy | monotonic-stack, hashing

## Task

For each value of nums1, find its next greater element to the
right within nums2, or -1.

## Key insight

The gentlest monotonic stack there is, and the right one to
write before 739 and 84. Sweep nums2 once with a decreasing stack; when a
larger value arrives it is the answer for everything it pops. Store those
answers in a map, then read nums1 off it.

## Invariant

Values on the stack are decreasing; each is still waiting for its answer.

## Complexity

time O(n + m)   space O(n)

## Pitfall

The brute force is O(n*m) and passes here, which is exactly why
this is worth doing properly - you are buying the pattern, not the verdict.
Anything left on the stack at the end has no greater element and maps
to -1.

## Review

last: never   confidence: 0/5
