# 2529. Maximum Count of Positive Integer and Negative Integer

leetcode | easy | binary-search

## Task

`nums` is sorted in non-decreasing order. Let `pos` be how many values
are strictly greater than zero and `neg` how many are strictly less than
zero. Return `max(pos, neg)`.

Zeros count toward neither.

`1 <= nums.length <= 2000`, `-2000 <= nums[i] <= 2000`.
Follow-up asks for O(log n).

## Key insight

<!-- Fill in AFTER solving, in your own words. The array is sorted, so
     say what that buys you here — and name the two boundaries you are
     actually looking for. -->

## Invariant

<!-- Write the loop invariant for your search: what is true of everything
     left of `lo`, and of everything at or right of `hi`, at the top of
     every iteration? If you cannot state it, the off-by-one below is
     waiting for you. -->

## Complexity

time O(?)   space O(?)

## Pitfall

<!-- The linear scan passes inside these constraints, so the judge will
     not catch a bad search. What is the failure mode you have to test
     for yourself? Consider: all-negative, all-positive, all-zero, and a
     long run of zeros in the middle. -->

## Review

last: never   confidence: 0/5

## Origin

New problem — not in the legacy archive.
