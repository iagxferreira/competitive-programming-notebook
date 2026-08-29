# 2956. Find Common Elements Between Two Arrays

leetcode | easy | hash-map

## Task

Return [count of nums1 elements present in nums2, count of nums2 elements
present in nums1].

## Key insight

Two sets. For each element of nums1 ask whether nums2 contains it, and
vice versa. Note this counts OCCURRENCES on each side, not distinct
values.

## Invariant

None.

## Complexity

time O(n + m)   space O(n + m)

## Pitfall

Your Go version reads `hashmap2[key] != 0` on a map, relying on the zero
value for a missing key. Java's `map.get` returns `null` there, and
comparing or unboxing that throws. Use `getOrDefault(key, 0)`.

Its accumulation is also subtly wrong in shape: it adds `hashmap2[key]`
per distinct key of nums1, which happens to give the right total but
reads as if it were symmetric when the two answers are computed
differently. Rewrite it as two explicit passes; a set of each array and a
count over the other is clearer and just as fast.

Since values are bounded and small, two boolean arrays beat hash sets.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2956-find-intersection.go
