# 28. Find the Index of the First Occurrence in a String

leetcode | easy | strings

## Task

Index of the first occurrence of needle in haystack, or -1.

## Key insight

Naive: try every start position and compare. Optimal: KMP, which
precomputes the longest proper prefix that is also a suffix so a mismatch
never rewinds the haystack pointer.

## Invariant

KMP: the prefix function lps[i] is the length of the longest proper
prefix of needle[0..i] that is also its suffix.

## Complexity

naive O(n * m)   KMP O(n + m)   space O(m)

## Pitfall

The loop bound is `i <= n - m`. In C++ that subtraction is on `size_t`,
so when m > n it wraps to a huge unsigned value and the loop runs off the
end. Cast to `int` or check `m > n` first. Your Go version was safe
because Go's `len` returns a signed int — this is exactly the kind of bug
the language change introduces.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/28-first-string-occurrence.go
