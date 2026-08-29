# 13. Roman to Integer

leetcode | easy | strings, hash-map

## Task

Convert a Roman numeral to its integer value.

## Key insight

Scan left to right. A symbol worth less than the one after it is
subtractive: subtract instead of add. That single rule handles IV, IX,
XL, XC, CD and CM without special-casing any of them.

## Invariant

total is the correct value of the prefix processed so far.

## Complexity

time O(n)   space O(1)

## Pitfall

The last character has no successor — bound the lookahead, as your Go
version did with `index < len(s)-1`. A fixed 128-entry array beats a
hash map here.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/13-roman-to-integer.go
