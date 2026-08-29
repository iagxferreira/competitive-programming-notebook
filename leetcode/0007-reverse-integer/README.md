# 7. Reverse Integer

leetcode | medium | math, overflow

## Task

Reverse the digits of a signed 32-bit integer. Return 0 if the result
overflows.

## Key insight

`result = result * 10 + x % 10` peels digits off the back and stacks them
on the front.

## Invariant

result holds the reversal of the digits consumed so far.

## Complexity

time O(log x)   space O(1)

## Pitfall

This is an overflow problem wearing a digits costume. Your Go version
computed the full result in 64-bit `int` and range-checked afterwards —
that works in Go, but in C++ `int` IS 32 bits and the overflow is
undefined behaviour before you can test for it. You must check BEFORE
multiplying:

    if (res > INT_MAX / 10 || res < INT_MIN / 10) return 0;

Also `-INT_MIN` overflows, so negating up front (as the Go version does)
is itself unsafe in C++. Work with the negative side, or use long long.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/7-reverse-integer.go
