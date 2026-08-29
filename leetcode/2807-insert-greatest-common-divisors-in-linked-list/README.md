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

Your Go version allocates `gcdNode` as a stack value and stores its
address (`&gcdNode`), relying on escape analysis to heap-allocate it.
That line is a dangling-pointer bug in C++ — but in Java the whole
hazard disappears: every object is heap-allocated and reachable nodes
are never collected. `new ListNode(gcd)` inside the loop is simply
correct.

Worth noting because it is the one place the language choice removes a
real trap rather than adding one.

Handle the single-node list, which has no pairs.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/2807-insert-gcd.go
