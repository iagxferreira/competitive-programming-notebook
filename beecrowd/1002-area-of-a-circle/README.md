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
`X = `), and you need exactly 4 decimals.

In Java, ALWAYS pass an explicit locale:

    System.out.printf(Locale.US, "A=%.4f%n", area);

Without it the JVM uses the system default, and on a pt_BR machine
`%.4f` prints `12,5664` with a comma. Beecrowd compares bytes, so that
is an instant wrong answer that looks completely correct on your screen.
This is the single most common way Brazilian users lose these problems.
Your Kotlin version dodged it by going through BigDecimal.toString().

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1002.kt
