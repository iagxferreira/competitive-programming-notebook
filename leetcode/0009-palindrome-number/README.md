# 9. Palindrome Number

leetcode | easy | math

## Task

Is the integer a palindrome, without converting to a string?

## Key insight

Reverse the number and compare. Negatives are never palindromes because
of the leading minus.

## Invariant

reverse holds the digits consumed so far, in reversed order.

## Complexity

time O(log x)   space O(1)

## Pitfall

Reversing the whole number can overflow for large 32-bit inputs. The
robust version reverses only the second half and stops when
`rev >= x` — it also halves the work.

Your Go version reversed everything, which is safe in Go's 64-bit int but
not in Java's 32-bit one — it wraps silently.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/9-is-palindrome.go
