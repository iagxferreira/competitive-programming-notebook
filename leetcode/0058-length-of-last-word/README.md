# 58. Length of Last Word

leetcode | easy | strings

## Task

Length of the final word in a string that may have trailing spaces.

## Key insight

Scan from the RIGHT. Skip trailing spaces, then count characters until
the next space or the start of the string. One pass, no allocation.

## Invariant

After the skip phase, the index sits on the last non-space character.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Go version trimmed and split the whole string — O(n) extra space
and a full tokenisation to answer a question about the tail. It also
breaks on runs of interior double spaces, since `Split` on a single space
yields empty tokens.

Trailing whitespace is the entire test here; `"hello   "` must return 5.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/58-length-of-last-string.go
