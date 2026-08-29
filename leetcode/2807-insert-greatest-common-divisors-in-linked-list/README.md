# 2807. Insert Greatest Common Divisors in Linked List

leetcode | medium | linked-list, math

## Task

Insert a node holding gcd(a, b) between every adjacent pair.

## Key insight

Walk with two pointers over the ORIGINAL pairs, splicing a new node
between them. Euclid's algorithm gives the gcd: `gcd(a, b) = gcd(b, a%b)`
until b is 0.

## Invariant

node1 and node2 always straddle an original adjacent pair; the inserted
node never becomes a traversal target.

## Complexity

time O(n log V)   space O(1) extra

## Pitfall

After splicing, advance to the ORIGINAL next node, not the node you just
inserted — otherwise you compute gcds of gcds forever. Your Go version
steps `node1 = node2` correctly, skipping past the insertion.

That version allocates `gcdNode` as a stack value and stores its address
(`&gcdNode`). In Go the escape analysis heap-allocates it and it is safe.
In C++ this is a dangling pointer the moment the loop iterates — you MUST
use `new ListNode(...)`. This is the most dangerous line to port
literally in the whole archive.

Handle the single-node list, which has no pairs.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2807-insert-gcd.go
