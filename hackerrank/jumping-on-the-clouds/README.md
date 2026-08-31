# Jumping on the Clouds

hackerrank | easy | greedy, arrays

## Task

Clouds are 0 (safe) or 1 (thunder). From cloud i you may jump to i+1 or
i+2, never onto a 1. Fewest jumps to the end.

## Key insight

Greedy: always take the two-step jump when the landing cloud is safe,
otherwise take one. Because a 1 is never adjacent to another 1 in the
constraints, this is always optimal and no dp is needed.

## Invariant

You are always standing on a safe cloud.

## Complexity

time O(n)   space O(1)

## Pitfall

Reading past the end when checking `c[i + 2]`. Guard the index before
the value. The greedy is only safe because of the no-adjacent-thunder
constraint - state that to yourself before relying on it, because the
general version really is a dp.

## Review

last: never   confidence: 0/5
