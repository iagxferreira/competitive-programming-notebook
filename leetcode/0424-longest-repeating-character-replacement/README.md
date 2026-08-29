# 424. Longest Repeating Character Replacement

leetcode | medium | sliding-window

## Task

Longest substring of one repeated letter, given at most k character
replacements.

## Key insight

A window is valid when `windowLength - maxCount <= k`, where maxCount is
the frequency of the most common letter inside it — that difference is
exactly how many characters you would have to replace.

## Invariant

The window never shrinks below the best length found so far; it slides
rather than contracts.

## Complexity

time O(n)   space O(1) — 26 counters

## Pitfall

The famous subtlety: maxCount is never decreased when the window slides.
That looks like a bug — the stored value can be stale and too large — but
it is deliberate. A stale maxCount only ever keeps the window from
shrinking, and since we only care about the MAXIMUM length, a window that
is invalid for a stale reason can never produce a wrong answer larger
than a genuine one.

If that argument does not feel airtight, write the version that
recomputes maxCount honestly and stress-test the two against each other.
Understanding this is worth more than the problem.

## Status

NOT SOLVED. Kotlin lab scaffold with a `TODO` body.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:src/main/kotlin/algorithms/problems/medium/longest_repeating_character_replacement/LongestRepeatingCharacterReplacement.kt
