# 2351. First Letter to Appear Twice

leetcode | easy | strings, hashing, bits

## Task

Given a string `s` of lowercase English letters, return the first letter
to appear twice.

Read the definition carefully, because it is the whole problem: a letter
`a` appears twice before a letter `b` if the **second** occurrence of `a`
comes before the second occurrence of `b`. So you are ordering by where
each letter's second occurrence lands, not by where its first one does.

`2 <= s.length <= 100`   lowercase English letters only   `s` is
guaranteed to contain at least one repeated letter.

## Key insight

A `boolean[26]` of letters seen so far, scanned left to right. The first
letter whose flag is already set is the answer.

The reason this needs no extra thought about the ordering rule: walking
positions in order means you meet every letter's *second* occurrence in
order too, so the first one you trip over is by definition the earliest.
The definition and the loop line up for free.

## Invariant

Before reading position `i`, `seen` holds exactly the distinct letters of
`s[0..i)` and no second occurrence has been reached yet.

## Complexity

time O(n)   space O(1) - 26 flags, independent of n

## Pitfall

The trap is counting frequencies first and then picking a letter. A
frequency map throws away position, so you end up answering "which
repeated letter appears earliest", which is a different question.
`"abccba"` separates them: every letter repeats, `a` appears first, but
`c` is the answer because its second occurrence comes before `b`'s and
`a`'s. Tested.

`return 'a'` at the end is unreachable - the constraints guarantee a
repeat - but Java needs it to compile. Worth knowing it is dead rather
than believing it is a fallback.

If you want O(1) space with no array at all, the 26 flags fit in a single
`int` used as a bitmask: test with `(seen >> (c - 'a') & 1) == 1`, set
with `seen |= 1 << (c - 'a')`. Same complexity, one register - a good
five-line exercise once the array version is green.

## Review

last: 2026-09-01   confidence: ?/5   (set your own)

## Origin

New problem - not in the legacy archive. Added on request.
