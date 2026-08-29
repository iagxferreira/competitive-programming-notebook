# 242. Valid Anagram

leetcode | easy | hash-map, counting

## Task

Is t a rearrangement of s?

## Key insight

Anagrams have identical character multisets. Count s, decrement with t,
and require every count to land on zero.

## Invariant

The counter holds (occurrences in s) minus (occurrences in t so far).

## Complexity

time O(n)   space O(1) for a 26-entry array

## Pitfall

Compare lengths first — it is an O(1) rejection that also makes the
single-pass decrement sound.

For lowercase-only input, use `array<int, 26>` rather than a hash map:
same asymptotics, far better constant. That constant factor is exactly
what separates a comfortable submission from a TLE in contests.

Your Go version's delete-on-zero bookkeeping is clever but unnecessary;
just scan the counts at the end.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/242-is-anagram.go

Full study essay from the Kotlin lab (~300 lines):

    git show legacy-archive:problems/easy/valid-anagram/README.md
