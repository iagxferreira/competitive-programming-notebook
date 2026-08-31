# 1015. Distance Between Two Points

beecrowd | trivial | io, floating-point, math

## Task

Read two points as four floats and print the Euclidean distance between
them with four decimal places.

## Key insight

`Math.sqrt((x2-x1)^2 + (y2-y1)^2)`, or `Math.hypot(dx, dy)` which is
written to avoid intermediate overflow and underflow.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

`Math.pow(dx, 2)` for a square is slower and less exact than `dx * dx` -
build the habit of writing the multiplication. And as always, `Locale.US`
on the output.

## Review

last: never   confidence: 0/5
