# 14. Longest Common Prefix

leetcode | easy | strings

## Task

Longest common prefix of an array of strings.

## Key insight

Your Go version used a genuinely elegant trick: sort the array, then
compare only the FIRST and LAST strings. Any prefix shared by those two
lexicographic extremes is shared by everything between them.

The plain alternative is vertical scanning: compare column j across all
strings, stop at the first mismatch.

## Invariant

Sorted version: result is a prefix of both strs[0] and strs[n-1], hence
of all of them.

## Complexity

sorted trick O(n log n * m)   vertical scan O(n * m)   space O(1)

## Pitfall

Handle the empty array before indexing. Vertical scanning must also stop
when j reaches the length of the shortest string — that is the more
common off-by-one, and it is why the sorted trick is easier to get right
even though it is asymptotically worse.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/14-longest-common-prefix.go
