# 72. Edit Distance

leetcode | medium | dp, strings

## Task

Fewest insert / delete / replace operations turning word1 into word2.

## Key insight

Same table shape as longest common subsequence, three
predecessors instead of two. `dp[i][j]` is the distance between the first i
and the first j characters. Equal characters cost nothing and move
diagonally; otherwise 1 + min(insert, delete, replace).

## Invariant

Row 0 is `j` (insert everything), column 0 is `i` (delete
everything). Fill those before the loop or every answer is off.

## Complexity

time O(n*m)   space O(min(n,m)) with rolling rows

## Pitfall

Confusing which neighbour means insert and which means delete.
It does not affect the answer here because the cost is the same, but it
will the moment the operations are weighted differently - so get the
meaning right now rather than memorising the min of three.

## Review

last: never   confidence: 0/5
