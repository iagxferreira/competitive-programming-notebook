# 1004. Simple Product

beecrowd | trivial | io

## Task

Read two integers, print `PROD = ` followed by their product.

## Key insight

Same shape as 1003, multiplication instead of addition.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Check the stated bounds before using `int` — a product overflows far
sooner than a sum does. When in doubt, `long`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1004.kt
