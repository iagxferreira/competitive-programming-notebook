# 8. String to Integer (atoi)

leetcode | medium | strings, overflow

## Task

Parse a leading integer from a string: skip whitespace, take an optional
sign, consume digits, clamp to the int32 range.

## Key insight

Four strictly ordered phases — whitespace, sign, digits, stop. The
problem is a specification-reading exercise; the difficulty is obeying
the order exactly.

## Invariant

result holds the value of the digits consumed so far, clamped.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Go version has a real precedence bug:

    if index < n && s[index] == '-' || s[index] == '+'

`&&` binds tighter than `||`, so this parses as
`(index < n && s[index]=='-') || (s[index]=='+')` — the bounds check does
not guard the `'+'` branch. It only survives because the empty string
returns earlier. Port it with explicit parentheses.

Clamp to INT_MAX / INT_MIN, do not return 0 on overflow — that is the
difference from problem 7.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/8-atoi.go
