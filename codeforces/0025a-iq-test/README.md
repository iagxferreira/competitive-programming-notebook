# 25A. IQ Test

codeforces | 1300 | implementation, parity

## Task

Exactly one number among n has a different parity from the rest. Print
its 1-based index.

## Key insight

Count evens and odds in one pass, then take a second pass for the index
of the minority parity. Or, cheaper: look at the first three numbers -
their majority parity is the answer's parity, since only one number
differs overall.

## Invariant

Exactly one parity class has size 1.

## Complexity

time O(n)   space O(1)

## Pitfall

The output is a 1-BASED index, not the value and not a 0-based index.
Deciding the majority from only the first two numbers is wrong when one of
them is the odd one out - you need three.

## Review

last: never   confidence: 0/5
