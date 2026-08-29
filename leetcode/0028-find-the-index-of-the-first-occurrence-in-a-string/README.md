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

The loop bound is `i <= n - m`. This is one of the few places Java is
SAFER than the alternatives: `String.length()` returns a signed `int`, so
when m > n the bound goes negative and the loop simply does not run,
returning -1 correctly. In C++ the same expression is unsigned and wraps
to a huge value, running off the end of the string.

Worth knowing you are protected here, because the equivalent protection
does not exist for array index arithmetic elsewhere.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/28-first-string-occurrence.go
