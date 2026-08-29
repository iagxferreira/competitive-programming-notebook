# 61. Rotate List

leetcode | medium | linked-list

## Task

Rotate the list right by k places.

## Key insight

Close the list into a ring, then cut it open at the right place. Walk to
the tail counting the length, link tail to head, advance
`length - k % length - 1` steps from the head, and sever there.

## Invariant

After closing the ring, every node has a successor, so the cut point
fully determines the result.

## Complexity

time O(n)   space O(1)

## Pitfall

`k % length` first — k can be far larger than the list, and rotating by a
multiple of the length is a no-op. Without the modulus this walks off the
end or spins pointlessly.

Empty list must return early; `k % 0` is a crash.

Sever the ring. Forgetting `temp->next = nullptr` leaves a circular list
that hangs whatever traverses it next.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/61.rotate-list.py
