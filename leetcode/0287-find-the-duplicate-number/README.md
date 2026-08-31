# 287. Find the Duplicate Number

leetcode | medium | floyd-cycle, two-pointers, binary-search

## Task

One repeated value in an array of n+1 integers in [1, n]. Find it
without modifying the array and in O(1) space.

## Key insight

Read `i -> nums[i]` as a linked list. Since every value is a
valid index and two indices share a value, that list must contain a cycle,
and its entrance is the duplicate. Floyd's tortoise and hare finds it -
the same routine as 141 and 142, applied to an array.

## Invariant

After the pointers meet, restarting one at index 0 and
advancing both one step at a time makes them meet at the cycle entrance.

## Complexity

time O(n)   space O(1)

## Pitfall

The constraints ("do not modify", "O(1) space") exist to rule
out sorting and a HashSet - both work and both miss the point. Binary
search on the value range, counting how many elements are <= mid, is the
other intended solution and is worth writing too.

## Review

last: never   confidence: 0/5
