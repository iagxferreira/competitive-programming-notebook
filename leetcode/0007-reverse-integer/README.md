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
that works in Go, but Java's `int` IS 32 bits. Overflow is not undefined
here — it wraps silently, which is arguably worse, because the wrapped
value looks like a legitimate answer. Check BEFORE multiplying:

    if (res > Integer.MAX_VALUE / 10 || res < Integer.MIN_VALUE / 10) return 0;

Also `-Integer.MIN_VALUE` is still `Integer.MIN_VALUE`, so negating up
front (as the Go version does) is unsafe. Work with the negative side,
or accumulate in `long` and range-check at the end.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/7-reverse-integer.go
