# 46. Permutations

leetcode | medium | backtracking

## Task

All permutations of an array of distinct integers.

## Key insight

Two valid routes. Your Go version built them iteratively: hold every
permutation of the first k elements, then insert element k+1 into all
k+2 possible gaps of each. Correct, and pleasantly free of recursion.

The route the problem is actually teaching is backtracking: swap index i
with each j >= i, recurse on i+1, swap back.

## Invariant

Backtracking: nums[0..i) is a fixed prefix; the recursion permutes the
rest and restores the array before returning.

## Complexity

time O(n * n!)   space O(n) recursion, O(n * n!) output

## Pitfall

The undo step is the whole discipline of backtracking. Forget the second
swap and the array is silently corrupted for every sibling branch.

The insertion approach allocates a fresh vector per permutation — fine
here, but it does not generalise to the pruning that harder backtracking
problems need. Redo this one recursively.

## Review

last: 2026-08-29   confidence: ?/5   (set your own)

## Origin

git show legacy-archive:legacy/go/leetcode/46-permutations.go
