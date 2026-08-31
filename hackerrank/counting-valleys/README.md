# Counting Valleys

hackerrank | easy | strings, prefix-sum

## Task

Steps are U or D. A valley is a maximal sequence below sea level; count
them.

## Key insight

Track altitude as a running sum, +1 for U and -1 for D. A valley is
completed exactly when a step brings you FROM -1 back TO 0 - count the
upward sea-level crossings.

## Invariant

Altitude is the prefix sum of the step values.

## Complexity

time O(n)   space O(1)

## Pitfall

Counting every time altitude equals 0 double-counts, since mountains
return to sea level too. The condition is "altitude became 0 on a U step",
which is a transition, not a state.

## Review

last: never   confidence: 0/5
