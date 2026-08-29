# 66. Plus One

leetcode | easy | arrays, math

## Task

Increment a number represented as a digit array.

## Key insight

Walk from the last digit. Any digit below 9 absorbs the carry and you
return immediately. A 9 becomes 0 and the carry continues.

## Invariant

Every digit already passed is 0, meaning the carry is still live.

## Complexity

time O(n)   space O(1), or O(n) in the all-nines case

## Pitfall

The only case that grows the array is all nines: 999 -> 1000. The result
is then a 1 followed by n zeros — your Go version handles it by
allocating a fresh n+1 array, which is exactly right since the rest are
already zeroed.

Never convert to an integer. The array can be far longer than 64 bits;
that is the whole reason the input is given as digits.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/66-plus-one.go
