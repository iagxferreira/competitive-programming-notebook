# 70. Climbing Stairs

leetcode | easy | dynamic-programming

## Task

Number of ways to climb n stairs taking 1 or 2 steps at a time.

## Key insight

To arrive at step i you came from i-1 or i-2, and those route sets are
disjoint. So `dp[i] = dp[i-1] + dp[i-2]` — this is Fibonacci with
different seeds. Recognising a known recurrence in disguise is the skill
being trained.

## Invariant

dp[i] is the number of distinct paths from 0 to i.

## Complexity

time O(n)   space O(n) as written, O(1) with two rolling variables

## Pitfall

`dp[0] = dp[1] = 1` is the seeding that matters — dp[0] = 1 encodes "one
way to stand still", which is what makes dp[2] come out as 2.

Your Go version allocates the full table. Only the last two values are
ever read, so two variables suffice. Also note it indexes dp[1]
unconditionally, which is out of bounds if n were 0.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/70-climbing-stairs.go
