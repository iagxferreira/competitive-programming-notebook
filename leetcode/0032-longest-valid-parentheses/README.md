# 32. Longest Valid Parentheses

leetcode | hard | stack, dynamic-programming

## Task

Length of the longest well-formed parentheses substring.

## Key insight

Stack of INDICES, not characters, seeded with -1 as a base. On `(` push
the index. On `)` pop; if the stack empties, the current index becomes
the new base — otherwise the length is `i - stack.top()`.

## Invariant

The stack top is always the index just before the current valid run, so
the subtraction yields a length directly.

## Complexity

time O(n)   space O(n)

## Pitfall

The -1 sentinel is the entire trick — without it the first valid run
computes one short. Understanding *why* a popped-empty stack means "this
`)` is unmatched, restart from here" is the difference between recalling
this solution and being able to rebuild it.

Your Go version also redefines a local `max` helper; Java has `Math.max`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/32-longest-valid-parenthesis.go
