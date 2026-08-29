# 1012. Area

beecrowd | trivial | io, floating-point

## Task

Read three reals A B C. Print five labelled areas, 3 decimals each:
triangle (A*C/2), circle (pi*C^2), trapezium ((A+B)*C/2),
square (B^2), rectangle (A*B).

## Key insight

Five formulas, one input line. The work is bookkeeping, not maths.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Each line has its own label and all five are graded. Getting four right
scores zero. Note the circle uses C as its radius, not A.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1012.kt
