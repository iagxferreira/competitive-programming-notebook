# 1020. Age in Days

beecrowd | trivial | io, math

## Task

Read an age in days and print it as years, months and days, taking every
year as 365 days and every month as 30.

## Key insight

Successive division and remainder, largest unit first - the same shape
as 1018 with different denominations.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

The 365/30 simplification is given by the statement; using real calendar
lengths produces a wrong answer. Beecrowd problems are specifications
first and arithmetic second - implement what is written, not what is
true.

## Review

last: never   confidence: 0/5
