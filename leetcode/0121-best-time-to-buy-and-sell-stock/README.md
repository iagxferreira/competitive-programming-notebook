# 121. Best Time to Buy and Sell Stock

leetcode | easy | greedy, dynamic-programming

## Task

One buy and one later sell. Maximum profit, or 0.

## Key insight

Track the minimum price seen so far. At each day the best sale today is
`price - minSoFar`, and the answer is the best of those. One pass, no
lookahead.

## Invariant

minSoFar is the lowest price in [0, i], so it is always a legal buy day
strictly at or before the sell day.

## Complexity

time O(n)   space O(1)

## Pitfall

Update the minimum and the profit in the correct relationship. Your Go
version updates `price = min(price, current)` first and then computes
`current - price`, which allows a same-day buy and sell — that yields 0,
never a negative, so the answer stays correct.

Profit floors at 0 for a monotonically falling series; do not report a
loss.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/121-max-profit.go

Full study essay from the Kotlin lab (~300 lines):

    git show legacy-archive:problems/easy/best-time-to-buy-and-sell-stock/README.md
