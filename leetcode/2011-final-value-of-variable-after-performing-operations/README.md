# 2011. Final Value of Variable After Performing Operations

leetcode | easy | strings, simulation

## Task

Apply operations like `++X` and `--X`; return the final value from 0.

## Key insight

Only the MIDDLE character distinguishes increment from decrement — it is
`+` in both `++X` and `X++`, and `-` in both decrement forms. Inspect
index 1 and ignore the rest.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

Checking the first character fails, since `X++` starts with X. Index 1 is
always the operator in all four legal forms. Your Python version uses
exactly that.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/2011.final-value.py
