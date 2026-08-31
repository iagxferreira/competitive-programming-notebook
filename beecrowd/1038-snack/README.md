# 1038. Snack

beecrowd | trivial | arrays, io

## Task

Read an item code and a quantity, look the price up in the menu given by
the statement, and print the total with two decimals.

## Key insight

A price table as a `double[]` indexed by code (pad index 0) beats a
switch, and it is the first time in this ladder that an array replaces
branching.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Codes start at 1, so either pad the array or subtract 1 - mixing the two
gives an off-by-one that shifts every price. `Locale.US` on the total, and
the exact `Total: R$ ` prefix from the statement.

## Review

last: never   confidence: 0/5
