# 20. Valid Parentheses

leetcode | easy | stack

## Task

Is the bracket string correctly matched and nested?

## Key insight

Nesting means last-opened must be first-closed. That is the definition of
a stack. Push openers; on a closer, the top must be its partner.

## Invariant

The stack holds exactly the openers that are still unmatched, innermost
on top.

## Complexity

time O(n)   space O(n)

## Pitfall

Three ways to fail, and you need all three: wrong partner on top, closer
arriving on an empty stack, and a non-empty stack at the end. Your Go
version covers all three, plus an odd-length early exit.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/20-valid-parenthesis.go
