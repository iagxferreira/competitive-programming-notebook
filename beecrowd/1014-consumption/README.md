# 1014. Consumption

beecrowd | trivial | io, floating-point

## Task

Read a distance in km (integer) and fuel spent in litres (float). Print
the consumption in km/l with three decimal places.

## Key insight

One division and one formatted print. The exercise is the formatting,
not the arithmetic.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

`Locale.US`. On a pt_BR system `%.3f` prints `12,500` instead of
`12.500` and the judge rejects it while it looks perfectly right on your
screen. Pass the locale explicitly to every printf in this whole
directory - make it reflex now.

## Review

last: never   confidence: 0/5
