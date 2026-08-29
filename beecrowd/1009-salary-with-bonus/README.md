# 1009. Salary with Bonus

beecrowd | trivial | io, floating-point

## Task

Read a seller's name, fixed salary, and total sales. Print
`TOTAL = R$ ` followed by salary + 15% of sales, 2 decimals.

## Key insight

The name is read and discarded. Consuming input you never use is normal.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Reading the name with `cin >>` stops at whitespace. If a test ever has a
two-word name, `>>` silently desynchronises everything after it. Prefer
`getline` when a field is textual.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1009.kt
