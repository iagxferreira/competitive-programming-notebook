# 118A. String Task

codeforces | 1000 | strings

## Task

Delete vowels, insert a '.' before each remaining consonant, and
lowercase everything.

## Key insight

Single pass over the lowercased string: skip vowels (a e i o u y),
otherwise append '.' then the character. A StringBuilder keeps it O(n).

## Invariant

None.

## Complexity

time O(n)   space O(n)

## Pitfall

'y' counts as a vowel in this problem, which the statement mentions once
and everyone misses. Building the result with `result += c` in the loop is
O(n^2) - fine at n = 100, but the habit is what you are training here, so
use a StringBuilder.

## Review

last: never   confidence: 0/5
