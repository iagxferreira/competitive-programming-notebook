# 121. Best Time to Buy and Sell Stock

Platform: LeetCode
Problem URL: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
Difficulty: Easy
Pattern: Array Scan / Running State
Status: Solved

Started: August 27, 2026
Solved: August 28, 2026

Worksheet: [`../problem.md`](/home/iago/workspace/algorithm-solutions/problems/problem.md)

## Session Notes

This problem is about tracking a useful state while scanning the array once.

The key question is:

- as I move through the prices, what is the cheapest buy point I have seen so far, and what profit can I already guarantee?

That is the idea to keep in mind while working through the sections below.

## 1. Understanding

The problem asks for the maximum profit from one buy and one sell.

My own wording:

- Scan the prices in order.
- Buy on one day and sell on a later day.
- Return the maximum profit possible.
- If no profit is possible, return `0`.

What the output represents:

- the best positive difference between a later sell price and an earlier buy price
- or `0` if the prices never go up enough to create profit

What I need to keep in mind:

- I must buy before I sell
- I am not allowed to choose multiple transactions
- the answer depends on the best pair of days, not just the highest price

## 2. Constraints

From the prompt:

- Input size: `1 <= prices.length <= 10^5`
- Value range: reasonable integer prices
- Duplicates allowed: yes
- Sorted: no guarantee
- Negative values: not relevant for the problem setting
- Empty input: not allowed by the usual constraints, but useful to think about defensively
- Time constraints: suggest a single pass
- Memory constraints: no need for extra storage if I can keep running state

What do these constraints tell me about the possible complexity?

- I should aim for `O(n)` time.
- I can likely solve this with constant extra space.
- The interesting part is not storing everything, but tracking only what matters.

## 3. Examples

Example 1:

- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `5`
- Why? Buy at `1`, sell at `6`.

Example 2:

- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`
- Why? No later price beats an earlier buy price.

My own example:

- Input: `prices = [2, 4, 1]`
- Output: `2`
- Why? Buy at `2`, sell at `4`.

Relevant edge cases:

- Strictly decreasing prices
- Repeated prices
- Single day
- Best profit happens early
- Best profit happens late

## 4. Brute Force

Approach:

- Try every possible buy day.
- For each buy day, try every later sell day.
- Compute the profit for every pair.
- Return the maximum profit found.

Why does it work?

- Every valid buy-sell pair is checked.

Time Complexity:

- `O(n^2)`

Space Complexity:

- `O(1)`

## 5. Bottleneck

What makes the brute-force solution slow?

- It recomputes the profit for many pairs.

What operation happens repeatedly?

- Comparing future prices against earlier buy prices.

What information am I recomputing?

- The cheapest price seen so far.
- Whether a later price creates a better profit.

Can I store something?

- Yes, I can store the lowest price seen so far.

Can I eliminate unnecessary work?

- Yes, by updating the running minimum instead of rescanning the past.

Can ordering help?

- Yes, because the sell day must come after the buy day.

Can I process the input only once?

- Yes, that is the best direction here.

Can I maintain some state?

- Yes, the current minimum buy price and the best profit so far.

## 6. Pattern Recognition

Pattern:

- Array scan
- Running minimum
- State update

Why:

- The answer depends on a prefix summary: the cheapest buy point seen up to now.

Recognition signals:

- “Buy before sell”
- “Maximum profit”
- “Single transaction”
- “One pass”
- “Track the best so far”

## 7. Data Structure

What data structure am I using?

- The array itself, plus a few scalar variables

Why?

- I only need the current minimum price and the best profit.

What operation does it optimize?

- It avoids storing all past prices or all possible pairs.

What is its complexity?

- Constant-time updates.

What would happen if I used another data structure?

- A list or map would store more information than I need.
- Sorting would destroy the day order and would not directly solve the “buy before sell” rule.

## 8. Invariant

What must always remain true while my algorithm runs?

- `minBuy` is the lowest price seen so far.
- `maxProfit` is the best profit seen so far.
- Any profit I compute uses a buy day that comes before the current day.

## 9. Algorithm

1. Start with the highest possible buy price.
2. Scan each price from left to right.
3. If the price is lower than the current buy price, update the buy price.
4. Otherwise, check the profit if I sold today.
5. If that profit is better, update the best profit.
6. Return the best profit at the end.

## 10. Correctness

Why does this algorithm always produce the correct result?

- The scan considers every day as a possible sell day.
- The running minimum ensures I always know the cheapest valid buy day before the current day.
- For each sell day, the profit uses the best possible buy price from the past.
- Therefore, the algorithm never misses a better valid pair.

What cases does it handle?

- Increasing arrays
- Decreasing arrays
- Flat arrays
- Profit appearing near the start or near the end

Why can I safely discard certain information?

- I do not need to remember every past price.
- Only the cheapest past price matters for future profit.

Why does the state represent the required subproblem?

- The subproblem is: “what is the best buy point before today?”
- The running minimum is exactly that summary.

## 11. Kotlin Implementation

Implementation notes:

- A single pass is enough.
- The loop should update state, not build collections.
- The current code uses a `when`-driven state update to avoid extra checks.

Final Kotlin solution:

- Track the minimum buy price and the best profit while scanning once.

## 12. Tests

Tests:

- Increasing prices
- Decreasing prices
- Best profit in the middle
- Single-day input
- Repeated values

Test scaffold:

- Kotlin test file: [`BestTimeToBuyAndSellStockTest.kt`](/home/iago/workspace/algorithm-solutions/src/test/kotlin/algorithms/problems/easy/best_time_to_buy_and_sell_stock/BestTimeToBuyAndSellStockTest.kt)
- What should this test prove?

  - The function returns the best profit, not just the biggest price.
  - The function returns `0` when no profitable trade exists.
  - The function handles one-pass state updates correctly.

## 13. Complexity

Time:

- `O(n)`

Space:

- `O(1)` extra space

Notes on JVM behavior:

- This style keeps allocations low.
- It relies on primitive `Int` state rather than extra collections.

## 14. Reflection

What did I initially misunderstand?

- I first thought about tracking too many values.

What is the reusable lesson?

- Sometimes the best answer is just a running minimum plus a running best.

What should I remember next time?

- Before reaching for a data structure, ask whether a single pass with a small state summary is enough.
