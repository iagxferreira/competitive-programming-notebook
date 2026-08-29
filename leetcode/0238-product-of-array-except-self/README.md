# 238. Product of Array Except Self

leetcode | medium | prefix-products

## Task

ans[i] = product of every element except nums[i]. No division, O(n).

## Key insight

Prefix and suffix products. `ans[i] = (product of everything left of i) *
(product of everything right of i)`. Two passes: fill ans with prefix
products going right, then multiply by a running suffix product coming
back left.

## Invariant

After pass one, ans[i] is the product of nums[0..i-1]. During pass two,
the running variable holds the product of nums[i+1..n-1].

## Complexity

time O(n)   space O(1) excluding output

## Pitfall

Division is banned, and for good reason — it breaks on zeros. Reaching
for total-product-divided-by-element is the trap.

Keep the suffix product in a single VARIABLE rather than a second array;
that is what gets you to O(1) auxiliary space.

Seed both running products at 1, the multiplicative identity. Seeding at
0 zeroes everything.

## Status

NOT SOLVED. Kotlin lab scaffold with a `TODO` body.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:src/main/kotlin/algorithms/problems/medium/product_of_array_except_self/ProductOfArrayExceptSelf.kt
