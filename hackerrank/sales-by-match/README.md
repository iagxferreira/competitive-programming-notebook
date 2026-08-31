# Sales by Match

hackerrank | easy | hashing, counting

## Task

Count matching pairs of socks by colour.

## Key insight

Count each colour with a map (or an int[] over the small colour range),
then sum `count / 2` over the colours. Integer division discards the
unpaired sock for free.

## Invariant

None.

## Complexity

time O(n)   space O(distinct colours)

## Pitfall

Do not use a set and toggle membership unless you are sure of it - it
works, but the counting version generalises to "groups of k" and the
toggle does not. `map.get` returns null for an unseen key; use
`getOrDefault` or `merge`.

## Review

last: never   confidence: 0/5
