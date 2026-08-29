# 347. Top K Frequent Elements

leetcode | medium | heap, bucket-sort, hash-map

## Task

The k most frequent elements. Required better than O(n log n).

## Key insight

Bucket sort. A frequency can never exceed n, so make n+1 buckets indexed
BY frequency and drop each value into its bucket. Walk the buckets from
the top and take k. That is O(n) with no comparison sort at all.

## Invariant

bucket[f] holds exactly the values occurring f times.

## Complexity

bucket O(n)   heap O(n log k)   your sort version O(n log n)   space O(n)

## Pitfall

Your Go version counted then fully sorted, which is O(n log n) — the
exact complexity the problem asks you to beat.

The heap alternative keeps a MIN-heap of size k and evicts the smallest.
Using a max-heap of everything is O(n log n) again and misses the point.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/347-top-k-elements.go
