# 22. Generate Parentheses

leetcode | medium | backtracking, pruning

## Task

All well-formed strings of n pairs of parentheses.

## Key insight

Do not generate all 2^(2n) strings and filter. Prune at the
point of choice: place '(' only while some remain, and ')' only while it
would not outnumber the '(' already placed. Every leaf is then a valid
answer and nothing is wasted.

## Invariant

At every node, close <= open <= n. The string is a valid
prefix of a balanced string at all times, never merely at the end.

## Complexity

time O(4^n / sqrt(n))   space O(n) recursion

## Pitfall

Backtracking with a String instead of a StringBuilder. Each
concatenation copies, which quietly adds a factor of n. Use a
StringBuilder and delete the last character on the way out - and make sure
you delete exactly the character you appended.

## Review

last: never   confidence: 0/5
