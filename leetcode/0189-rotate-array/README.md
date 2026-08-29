# 189. Rotate Array

leetcode | medium | arrays

## Task

Rotate the array right by k steps, in place. Follow-up demands O(1) extra
space.

## Key insight

Triple reversal. Reverse the whole array, then reverse the first k
elements, then reverse the rest. The two local reversals undo the
scrambling that the global one introduced, leaving a clean rotation.

## Invariant

After the full reverse, the last k elements are at the front but in
reversed order — reversing that block restores them.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Python version allocated a second array. It is correct and easy to
reason about, but it fails the O(1) follow-up — this one is worth redoing
with the reversal trick, which is a genuinely reusable technique.

`k %= n` first: k can exceed n.

The alternative cyclic-replacement method needs a gcd-based cycle count
to avoid revisiting the same orbit. The triple reversal avoids that
entirely, which is why it is the one to remember.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/189.rotate-array.py
