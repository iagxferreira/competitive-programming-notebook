# 131. Palindrome Partitioning

leetcode | medium | backtracking, dp, strings

## Task

All ways to cut a string so every piece is a palindrome.

## Key insight

Backtracking over cut positions: try every prefix, recurse on
the rest when the prefix is a palindrome. The refinement worth making is
precomputing an `isPalindrome[i][j]` table with dp so the check inside the
search is O(1) instead of O(n).

## Invariant

Everything already on the path is a palindrome, so any completed path is valid.

## Complexity

time O(n * 2^n)   space O(n^2) with the table

## Pitfall

Forgetting to undo the choice after the recursive call, which
is the one discipline backtracking actually asks for. Adding
`new ArrayList<>(path)` rather than `path` itself when recording an answer
matters just as much - otherwise every recorded answer aliases the same
list and ends up empty.

## Review

last: never   confidence: 0/5
