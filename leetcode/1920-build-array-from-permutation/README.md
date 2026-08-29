# 1920. Build Array from Permutation

leetcode | easy | arrays

## Task

Return ans where `ans[i] = nums[nums[i]]`.

## Key insight

A direct transcription of the formula. The follow-up asks for O(1) extra
space, which needs the encoding trick: store both old and new values in
one slot as `nums[i] += n * (nums[nums[i]] % n)`, then divide by n in a
second pass.

## Invariant

Encoded version: each slot holds `old + n * new`, recoverable because
both are < n.

## Complexity

time O(n)   space O(n), or O(1) with encoding

## Pitfall

The encoding trick only works because every value is < n, so the two
numbers never collide. Read the old value with `% n` — reading it
directly gives you an already-encoded slot.

Encoded values can exceed int range for large n; use `long long`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/1920-build-array-from-permutation.go
