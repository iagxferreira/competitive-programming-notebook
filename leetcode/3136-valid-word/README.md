# 3136. Valid Word

leetcode | easy | strings

## Task

Valid if: at least 3 characters, only letters and digits, at least one
vowel, and at least one consonant.

## Key insight

A single pass collecting three booleans, plus a length check up front.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

A specification problem — every clause is graded. The easiest to miss:
digits are ALLOWED but count as neither vowel nor consonant, so a word of
only digits fails on both flags.

Case-insensitive vowel test. In C++ cast to `unsigned char` before
`isalpha` / `tolower` to avoid undefined behaviour on negative chars.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3136-valid-word.go
