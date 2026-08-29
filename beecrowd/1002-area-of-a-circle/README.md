# 1002. Area of a Circle

beecrowd | trivial | io, floating-point

## Task

Read radius R, print `A=` followed by pi*R^2 with 4 decimal places.

## Key insight

The problem hands you pi = 3.14159 explicitly. Use *that* constant, not
`M_PI` — the expected output was generated with the truncated value and
a more accurate pi produces a wrong answer.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Two traps. `A=` has NO space before the number here (unlike 1001's
`X = `), and you need exactly 4 decimals: `printf("A=%.4f\n", area)`.
Your Kotlin version reached for BigDecimal to get this rounding; in C++
`printf` does it natively.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1002.kt
