# 1016. Distance

beecrowd | trivial | io, math

## Task

Two cars, one ahead by X km, closing at a known relative speed. Print
how many minutes until they meet, followed by the word from the
statement.

## Key insight

Pure arithmetic on integers - the relative speed is fixed by the
statement, so the answer is a single multiplication. Read the statement for
the exact output wording; getting the label right is half the problem.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Beecrowd output labels are literal and in Portuguese. A trailing space,
a missing one, or an English word is a wrong answer with no diagnostic.
Copy the template string out of the statement rather than retyping it.

## Review

last: never   confidence: 0/5
