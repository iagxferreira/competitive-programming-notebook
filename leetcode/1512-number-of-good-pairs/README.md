# 1512. Number of Good Pairs

leetcode | easy | hash-map, counting

## Task

Count pairs (i, j) with i < j and nums[i] == nums[j].

## Key insight

When you meet a value for the k-th time, it forms a pair with each of the
k-1 earlier copies. So add the current count, THEN increment.

## Invariant

count[v] is the number of occurrences of v strictly before the current
index — exactly the number of new pairs it closes.

## Complexity

time O(n)   space O(n)

## Pitfall

Add before incrementing. Reversing the two counts each element as a pair
with itself.

Your Python version branches on `seen[number] == 1` and otherwise adds
`seen[number]` — both arms do the same thing, since adding 1 when the
count is 1 IS adding the count. The whole conditional collapses to
`answer += seen[num]++`. Simplify it when you rewrite.

The closed form is sum of c*(c-1)/2 over final counts, if you prefer one
pass to build and one to total.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/1512.good-pairs.py
