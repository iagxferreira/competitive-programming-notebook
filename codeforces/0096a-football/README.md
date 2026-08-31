# 96A. Football

codeforces | 900 | strings, implementation

## Task

A situation is dangerous if seven or more players of the same team stand
consecutively. Print YES or NO.

## Key insight

One pass tracking the current run length, resetting whenever the
character changes. Or simply test `s.contains("0000000") ||
s.contains("1111111")`, which is completely legitimate here.

## Invariant

The run counter always equals the length of the current maximal run ending at i.

## Complexity

time O(n)   space O(1)

## Pitfall

Resetting the counter to 0 rather than 1 when the character changes -
the new character is itself the start of a run of length one. The
threshold is at least seven, not more than seven.

## Review

last: never   confidence: 0/5
