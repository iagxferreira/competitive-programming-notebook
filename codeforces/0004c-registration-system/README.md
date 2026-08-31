# 4C. Registration System

codeforces | 1300 | hashing, maps

## Task

For each requested name: print OK if unused, otherwise print the name
with the smallest unused suffix number and register that.

## Key insight

A HashMap from name to "how many times this base name has been taken".
On a hit, the answer is `name + count` and the count increments. Do not
scan for a free suffix - store it.

## Invariant

map[name] is always the next free suffix for that base name.

## Complexity

time O(n) expected   space O(n)

## Pitfall

Registering only the base name is the bug: after emitting `abacaba1` you
must be able to emit `abacaba2` next time, so the counter has to advance.
With n up to 1e5, build the output in a StringBuilder - a println per line
is a real TLE risk here.

## Review

last: never   confidence: 0/5
