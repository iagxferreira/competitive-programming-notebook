# 1008. Salary

beecrowd | trivial | io, floating-point

## Task

Read an employee number, hours worked, and hourly rate. Print the number
on one line and `SALARY = U$ ` plus hours*rate on the next, 2 decimals.

## Key insight

First multi-line output of the set. Both lines are graded.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

The `$` needs no escaping in a C++ string literal (it did in Kotlin's
template strings). Watch the exact spacing in `U$ `.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/beecrowd/1008.kt
