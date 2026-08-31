# 25. Reverse Nodes in k-Group

leetcode | hard | linked-list, pointers

## Task

Reverse the list in consecutive blocks of k. A trailing block
shorter than k is left as it is.

## Key insight

Check a full block exists BEFORE reversing anything, by
walking k nodes ahead. Then reverse exactly k nodes and reconnect three
things: the previous block's tail to the new head, and the new tail to
whatever follows.

## Invariant

`groupPrev` always points at the node immediately before the
block being reversed, so the reconnection is the same three assignments
every iteration. A dummy head makes the first block obey it too.

## Complexity

time O(n)   space O(1)

## Pitfall

Reversing first and discovering the block was short. Once you
have reversed a partial block you have to reverse it back, which is where
this goes wrong. Count first, then commit.

## Review

last: never   confidence: 0/5
