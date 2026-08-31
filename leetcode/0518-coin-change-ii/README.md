# 518. Coin Change II

leetcode | medium | dp, counting, knapsack

## Task

Number of distinct COMBINATIONS of coins summing to amount.

## Key insight

The unbounded knapsack counting variant. Loop coins on the
OUTSIDE and amounts on the inside. That order is the entire problem: it
counts each multiset once, because coins are only ever considered in a
fixed order.

## Invariant

After processing the first k coins, `dp[a]` is the number of
combinations of those k coins summing to a. `dp[0] = 1` - the empty
combination.

## Complexity

time O(amount * coins)   space O(amount)

## Pitfall

Swap the two loops and you count PERMUTATIONS instead:
{1,2} and {2,1} become two answers. It still compiles, still runs, and
gives a larger wrong number. If you ever want permutations (as in
Combination Sum IV) the swapped order is exactly right - so learn which is
which rather than memorising one.

## Review

last: never   confidence: 0/5
