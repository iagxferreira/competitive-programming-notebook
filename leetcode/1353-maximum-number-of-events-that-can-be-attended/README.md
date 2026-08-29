# 1353. Maximum Number of Events That Can Be Attended

leetcode | medium | greedy, heap

## Task

Each event spans [start, end]. Attend at most one per day. Maximise the
number attended.

## Key insight

Sweep days forward. On each day, add every event that has now started to
a MIN-heap keyed by end date, discard events already expired, and attend
the one that expires soonest. Earliest-deadline-first is the exchange
argument: taking a later-ending event can never beat taking the one about
to disappear.

## Invariant

The heap holds exactly the events currently available, ordered by
urgency.

## Complexity

time O(n log n)   space O(n)

## Pitfall

Discard expired events (`top < today`) BEFORE attending, or you attend an
event whose window has closed.

Your Go version loops days 1..100000 unconditionally — safe given the
constraints, but it does fixed work regardless of input size. Jumping to
the next relevant day is the better shape.

Note this file is named 1363 in the archive; the problem is 1353.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/1363-maximum-meetings.go
