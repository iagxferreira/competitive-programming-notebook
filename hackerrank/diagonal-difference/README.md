# Diagonal Difference

hackerrank | easy | matrix

## Task

Given an n x n matrix, return the absolute difference between the sums of
its two diagonals.

## Key insight

Both diagonals are indexable directly — no search required:

    primary   cell i is (i, i)
    secondary cell i is (i, n - 1 - i)

So one loop over i, not a nested scan.

## Invariant

After iteration i, each accumulator holds the sum of the first i+1 cells
of its diagonal.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Kotlin version scanned all n^2 cells with `if (i == j)` tests, and
its outer loop read `for (i in 0..array.size)` — inclusive, so i reached
n. That is an out-of-bounds index that only escaped because neither
diagonal condition can be true when i == n. It was a latent crash, not a
correct program. Indexing the diagonals directly removes the whole class
of error, and drops O(n^2) to O(n).

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/kotlin/hackerrank/diagonal-difference.kt
