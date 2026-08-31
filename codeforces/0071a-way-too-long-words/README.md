# 71A. Way Too Long Words

codeforces | 800 | strings, io

## Task

Words longer than 10 characters become first letter + count of letters
between + last letter. Others are unchanged.

## Key insight

Direct implementation. The abbreviation is
`s.charAt(0) + (s.length() - 2) + s.charAt(s.length() - 1)`.

## Invariant

None.

## Complexity

time O(total length)   space O(1)

## Pitfall

In Java, `char + int` is INTEGER ADDITION, not concatenation - building
the answer as `s.charAt(0) + (s.length() - 2) + ...` silently produces a
number. Start the expression with a String, or use a StringBuilder. The
threshold is strictly greater than 10, so a 10-letter word is left
alone.

## Review

last: never   confidence: 0/5
