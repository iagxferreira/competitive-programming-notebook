# 23. Merge k Sorted Lists

leetcode | hard | linked-list, heap, divide-and-conquer

## Task

Merge k sorted linked lists into one.

## Key insight

Two good routes. Your Python version used pairwise divide and conquer:
merge lists in pairs, halving k each round, log k rounds over n total
nodes.

The other is a min-heap of the k current heads: pop the smallest, append
it, push its successor.

## Invariant

Divide and conquer: after round r, each surviving list is a correct merge
of 2^r originals.

## Complexity

both O(n log k)   space O(1) pairwise, O(k) for the heap

## Pitfall

Merging one list at a time into an accumulator is O(nk) — that is the
trap this problem exists to catch, and it is the intuitive thing to do.

The empty input must be handled before indexing `lists[0]`. An odd count
per round leaves one list unpaired; your version handles it with the
`i + 1 < len` guard.

For the heap version, C++ `priority_queue` is a MAX-heap — pass
`greater<>` or the comparison is inverted.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/23.merge-k-lists.py
