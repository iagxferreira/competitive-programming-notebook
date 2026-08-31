# 112A. Petya and Strings

codeforces | 800 | strings

## Task

Compare two equal-length strings lexicographically, ignoring case. Print
-1, 0 or 1.

## Key insight

`a.compareToIgnoreCase(b)`, then normalise the sign with
`Integer.signum`. Writing the character loop by hand is worth doing once
too.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

`compareTo` returns the character DIFFERENCE, not -1/0/1 - printing it
raw fails. Use `Integer.signum`, or an explicit three-way branch. Also
note `equalsIgnoreCase` answers a different question and cannot order
them.

## Review

last: never   confidence: 0/5
