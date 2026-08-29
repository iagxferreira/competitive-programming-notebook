# 2942. Find Words Containing Character

leetcode | easy | strings

## Task

Indices of the words that contain character x.

## Key insight

Linear scan with an early break once found.

## Invariant

None.

## Complexity

time O(total characters)   space O(1) extra

## Pitfall

Break on the first match, or a word containing x twice is recorded twice.
Your Go version breaks correctly.

`string::find(x) != string::npos` expresses this in one line.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2942-find-words-containing.go
