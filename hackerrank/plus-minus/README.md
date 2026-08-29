# Plus Minus

hackerrank | easy | arrays

## Task

Print the fraction of positive, negative, and zero elements, each on its
own line with 6 decimal places.

## Key insight

One pass, three counters. The only real content is the division and the
output format.

## Invariant

pos + neg + zero == number of elements processed so far.

## Complexity

time O(n)   space O(1)

## Pitfall

Two traps. Divide counters by `(double) n` — integer division yields 0
for every ratio. And use `double`, not `float`: your Rust version used
f32, which carries ~7 significant digits and can round wrong at the 6th
decimal the grader checks.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/rust/hackerrank/plus_minus.rs
