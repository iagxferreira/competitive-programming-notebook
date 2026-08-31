# 158B. Taxi

codeforces | 1100 | greedy, counting

## Task

Groups of 1 to 4 children must each ride together; a taxi holds 4.
Minimum taxis.

## Key insight

Count how many groups of each size there are, then pair greedily: every
4 rides alone; each 3 takes a 1 with it; 2s pair up; leftovers fill the
rest. Sorting is unnecessary - there are only four possible sizes.

## Invariant

After each pairing step, the remaining groups cannot be combined more
cheaply than the rule applied.

## Complexity

time O(n)   space O(1)

## Pitfall

The leftover arithmetic at the end. After 3s consume 1s and 2s pair off,
an odd 2 leaves 2 free seats that can absorb up to two 1s - forgetting
that overcounts. Work the four counts on paper before writing code; this
is a greedy proof, not an implementation problem.

## Review

last: never   confidence: 0/5
