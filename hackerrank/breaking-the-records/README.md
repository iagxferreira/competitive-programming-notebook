# Breaking the Records

hackerrank | easy | arrays, counting

## Task

Count how many times a running maximum and a running minimum are broken
across a season of scores.

## Key insight

Seed both records with the FIRST score, then scan from index 1,
incrementing a counter each time a score strictly beats the record it
updates.

## Invariant

(min, max) describe the prefix scanned so far; the counters describe how often each changed.

## Complexity

time O(n)   space O(1)

## Pitfall

Game one sets the records but does not count as breaking them - starting
the scan at index 0 with sentinel records reports one break too many on
each side. "Strictly" matters: tying a record is not breaking it.

## Review

last: never   confidence: 0/5
