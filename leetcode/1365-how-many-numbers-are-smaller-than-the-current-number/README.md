# 1365. How Many Numbers Are Smaller Than the Current Number

leetcode | Easy | array, hash-table, sorting, counting

## Task

Given the array `nums`, for each `nums[i]` find out how many numbers in
the array are smaller than it. That is, for each `nums[i]` count the
number of valid `j` such that `j != i` and `nums[j] < nums[i]`. Return
the answer in an array.

`2 <= nums.length <= 500`   `0 <= nums[i] <= 100`

## Key insight

Solved the direct way: for each element, scan the whole array and count
the ones below it. At `n <= 500` that is 250k comparisons, comfortably
inside the limit - the constraints are small enough that the obvious
answer is a correct answer.

## Invariant

`count` holds the number of `j` seen so far with `nums[j] < nums[i]`, and
`answer[i]` is final the moment the inner loop ends.

## Complexity

time O(n^2)   space O(1) beyond the output

## Pitfall

The `i != j` guard is dead weight: `nums[i] > nums[i]` is false anyway,
so an element can never count itself. Harmless, but it suggests the
self-comparison felt like a hazard when it is not.

The real one is what the constraints are hinting at, and the reason this
problem exists. `0 <= nums[i] <= 100` bounds the VALUES, not just the
length - a far tighter bound than `n`. Anything with a small, known value
range can be counted into buckets rather than compared pairwise, which
turns this into two linear passes and no nested loop. Worth redoing that
way: the technique carries, the nested scan does not.

## Review

last: 2026-08-31   confidence: ?/5   (set your own)

## Origin

New problem - not in the legacy archive. Added from the pattern study
list.
