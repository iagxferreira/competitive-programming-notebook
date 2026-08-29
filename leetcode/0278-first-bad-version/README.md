# 278. First Bad Version

leetcode | easy | binary-search

## Task

Versions are good then bad. Find the first bad one with fewest API calls.

## Key insight

The predicate is monotonic — false...false,true...true — which is the
general precondition for binary search. You are searching for the
boundary, not for a value.

## Invariant

The answer is always in [left, right]; left is never known-good, right is
never known-bad-minus-one.

## Complexity

time O(log n)   space O(1)

## Pitfall

`right = mid` when bad (mid might BE the answer), `left = mid + 1` when
good (mid definitely is not). Writing `right = mid - 1` here skips the
answer.

`(left + right) / 2` overflows when n is near INT_MAX — and this problem
uses exactly that bound. Use `left + (right - left) / 2`. Your Go version
has the overflow-prone form; Go's 64-bit int hid it.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/278-first-bad-version.go
