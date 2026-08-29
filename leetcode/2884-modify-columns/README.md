# 2884. Modify Columns

leetcode | easy | pandas | NOT A JAVA PROBLEM

## Task

Double every value in the `salary` column of a DataFrame.

## Key insight

`employees["salary"] = employees["salary"] * 2` — a vectorised column
operation, mutating in place and returning the frame.

## Invariant

None.

## Complexity

time O(n)   space O(1) in place

## Pitfall

This is from LeetCode's PANDAS track, not the algorithms track. It has no
meaningful Java translation — there is no DataFrame to modify, and
rewriting it as a loop over an array teaches nothing the rest of this
repo does not already cover.

`Solution.java` is intentionally absent. The card is kept so the archive
stays complete and you can see why this one is excluded. If you want to
keep the Pandas skill alive, re-solve it in `solution.py`.

## Review

last: never   confidence: n/a

## Origin

git show legacy-archive:legacy/python/leetcode/2884.double-salary.py
