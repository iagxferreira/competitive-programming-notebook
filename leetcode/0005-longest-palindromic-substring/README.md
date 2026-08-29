# 5. Longest Palindromic Substring

leetcode | medium | strings, two-pointers

## Task

The longest palindromic substring.

## Key insight

Expand around centres. Every palindrome has a centre, and there are
2n-1 of them — n single characters for odd lengths, n-1 gaps for even
ones. Try both at each index and keep the longest.

## Invariant

expand(l, r) returns the length of the maximal palindrome centred at that
position; the returned length is `r - l - 1` after the loop overshoots by
one on each side.

## Complexity

time O(n^2)   space O(1)

## Pitfall

The index recovery is the fiddly part:

    start = i - (len - 1) / 2
    end   = i + len / 2

The asymmetric rounding is what makes one formula serve both the odd and
even cases. Your Python version has it exactly right — re-derive it
rather than copying it, because it is the only hard line in the problem.

Empty input must return "" before the loop indexes anything.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/5.longest-palindromic-substring.py
