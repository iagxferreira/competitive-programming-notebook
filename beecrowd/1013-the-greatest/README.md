# 1013. The Greatest

beecrowd | trivial | math

## Task

Read three integers, print `<max> eh o maior`.

## Key insight

The intended lesson is the branchless identity

    max(a, b) = (a + b + |a - b|) / 2

Apply it to A and B, then to that result and C. Your Kotlin version did
exactly this, which is why it is worth keeping rather than replacing
with `Math.max`.

## Invariant

After the first step the running value is max(A, B); after the second it
is max of all three.

## Complexity

time O(1)   space O(1)

## Pitfall

The identity relies on exact integer arithmetic — `a + b` can overflow
for large inputs even when the true max fits. In real code just use
`Math.max(a, Math.max(b, c))` — Java has no varargs max for primitives.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1013.kt
