# Array Manipulation

hackerrank | hard | difference-array, prefix-sum

## Task

m operations each add a value to an inclusive range of a zero-filled
array of size n. Return the maximum final value.

## Key insight

The difference array, and the reason it is worth knowing. Instead of
touching every element of every range, record `+v` at `a` and `-v` at
`b + 1`, then prefix-sum once at the end and take the running maximum.
O(n + m) instead of O(n * m).

## Invariant

After the sweep, the running sum at index i is exactly the final value at
i, because each range contributes from its start until its cancellation.

## Complexity

time O(n + m)   space O(n)

## Pitfall

n is up to 1e7 and values up to 1e9, so the running sum reaches ~1e13 -
it MUST be `long`. The naive nested loop is 1e12 operations and times out;
this problem exists specifically to force the difference array. Watch the
`b + 1` index and size the array n + 2.

## Review

last: never   confidence: 0/5
