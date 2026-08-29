# 3. Longest Substring Without Repeating Characters

leetcode | medium | sliding-window

## Task

Length of the longest substring with no repeated character.

## Key insight

A window [start, i]. When s[i] was last seen inside the window, the
window cannot keep its left edge — jump start to just past that previous
occurrence. Jumping, rather than shrinking one step at a time, is what
keeps this linear.

## Invariant

[start, i] always contains distinct characters, and `last[c]` holds the
index just after c's most recent appearance.

## Complexity

time O(n)   space O(1) — 128-entry table

## Pitfall

`start` must never move backwards. The guard `if (last[c] > start)` is
essential: a repeat that sits left of the window is irrelevant, and
without the test `abba` gives the wrong answer. Your Go version had this
right, storing index+1 so the comparison stays a clean `>`.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3-longest-substring.go
git show legacy-archive:legacy/rust/leetcode/3-longest_substring.rs
