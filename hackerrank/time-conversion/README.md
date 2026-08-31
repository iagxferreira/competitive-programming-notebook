# Time Conversion

hackerrank | easy | strings, edge-cases

## Task

Convert a 12-hour time like `07:05:45PM` into 24-hour `19:05:45`.

## Key insight

Only the hour changes. PM adds 12, AM leaves it - except at 12, which
inverts both rules. Slice the string by fixed offsets; there is nothing to
parse.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Midnight and noon are the whole problem. 12:00AM is 00, and 12:00PM is
12 - the naive "+12 for PM" gives 24 and "leave AM alone" gives 12, both
wrong. Format the hour back with `%02d` or you lose the leading zero.

## Review

last: never   confidence: 0/5
