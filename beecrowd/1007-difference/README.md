# 1007. Difference

beecrowd | trivial | io

## Task

Read four integers A B C D. Print `DIFERENCA = ` followed by
(A*B - C*D).

## Key insight

Pure integer arithmetic — no rounding needed, unlike its neighbours.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Your Kotlin version ran this through Double and BigDecimal with
`setScale(0)`. That was unnecessary and it is how precision bugs get in.
The result is an integer; compute it as one.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1007.kt
