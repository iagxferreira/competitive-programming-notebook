# 1282. Group the People Given the Group Size They Belong To

leetcode | medium | hash-map, greedy

## Task

Person i must be in a group of size groupSizes[i]. Return any valid
grouping.

## Key insight

Bucket people by their required size. The moment a bucket reaches that
size it is a complete valid group — emit it and start a fresh one. No
lookahead or backtracking is needed, because group membership is
unconstrained beyond the size.

## Invariant

Every bucket holds strictly fewer people than its key, so it is always
still fillable.

## Complexity

time O(n)   space O(n)

## Pitfall

CLEAR the bucket after emitting. Your Python version used `hashmap.pop`,
which removes and returns in one step; in C++ you must copy the vector
out and then `clear()` it, or you keep appending to a group you already
emitted.

Any valid answer is accepted, so there is nothing to optimise — the
greedy first-fit is provably correct here.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/1282.group-the-people.py
