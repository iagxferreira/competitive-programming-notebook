# 96. Unique Binary Search Trees

leetcode | medium | dynamic-programming, combinatorics

## Task

How many structurally distinct BSTs hold values 1..n?

## Key insight

Pick a root j. Then 1..j-1 must form the left subtree and j+1..n the
right, independently. So

    dp[i] = sum over j of dp[j-1] * dp[i-j]

These are the Catalan numbers.

## Invariant

dp[i] counts BSTs over any i consecutive values — only the count matters,
not which values, which is why the subproblems compose.

## Complexity

time O(n^2)   space O(n)

## Pitfall

dp[0] = 1, not 0. The empty subtree is one valid arrangement, and setting
it to 0 collapses the entire product to zero.

Your Go version writes `memo[0], memo[1] = 1, 1` before checking n — for
n = 0 the slice has length 1 and indexing memo[1] panics. Only the
constraint n >= 1 saves it.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/96-unique-bst.go
