# 2913. Subarrays Distinct Element Sum of Squares I

leetcode | easy | array, hash-table

## Task

Given an integer array `nums`, sum the square of the number of distinct
elements over every contiguous subarray.

## Notes

For each left endpoint, extend the right endpoint while maintaining the set
of values in the current subarray. This takes O(n²) expected time and O(n)
extra space.

## Review

last: never   confidence: 0/5
