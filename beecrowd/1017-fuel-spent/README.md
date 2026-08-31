# 1017. Fuel Spent

beecrowd | trivial | io, floating-point

## Task

Read a driving time in hours and an average speed. Assuming the car does
12 km per litre, print the litres used with three decimals.

## Key insight

Distance is time * speed; litres is distance / 12.0.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Dividing by `12` rather than `12.0` when the numerator is an int does
INTEGER division and truncates before you ever get to the formatting.
Force one operand to double.

## Review

last: never   confidence: 0/5
