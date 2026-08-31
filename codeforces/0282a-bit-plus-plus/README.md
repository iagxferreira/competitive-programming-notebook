# 282A. Bit++

codeforces | 800 | strings, implementation

## Task

n statements, each containing ++ or -- and X in some order. Print the
final value of X, starting from 0.

## Key insight

Do not parse the position of X. Just test whether the statement contains
a '+' - if so add 1, otherwise subtract 1.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

Matching on the exact string "++X" misses "X++", and there are three
forms of each. Testing for a single '+' character handles all of them and
is shorter. Watch the reader: each statement is its own token, so
`next()` is enough - `nextLine()` after `nextInt()` is where this
usually goes wrong.

## Review

last: never   confidence: 0/5
