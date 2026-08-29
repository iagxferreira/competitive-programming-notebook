# 1010. Simple Calculate

beecrowd | trivial | io, floating-point

## Task

Two lines, each: product code, quantity, unit price. Print
`VALOR A PAGAR: R$ ` followed by the total, 2 decimals.

## Key insight

Two structurally identical records. Read them in a loop rather than
duplicating the parse.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

The product code is read and thrown away, like the name in 1009. Your
Kotlin version destructured it to `_` — in C++ just read into a scratch
variable.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1010.kt
