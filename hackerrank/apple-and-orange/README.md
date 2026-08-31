# Apple and Orange

hackerrank | easy | arrays, simulation

## Task

Apples fall from a tree at `a` and oranges from one at `b`, each with a
signed distance. Count how many land on a house spanning [s, t].

## Key insight

Absolute landing position is `a + d` for apples and `b + d` for oranges.
Count the ones inside the inclusive range. The distances are signed, which
is the only thing to be careful about.

## Invariant

None.

## Complexity

time O(m + n)   space O(1)

## Pitfall

The range is INCLUSIVE at both ends. Also the distances are relative to
the tree, not to the house - adding them to `s` instead of to `a` is the
usual misread.

## Review

last: never   confidence: 0/5
