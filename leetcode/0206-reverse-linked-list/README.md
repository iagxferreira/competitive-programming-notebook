# 206. Reverse Linked List

leetcode | easy | linked-list

## Task

Reverse a singly linked list.

## Key insight

Three pointers: prev, curr, and a saved next. Flip curr's link to prev,
then shuffle all three forward. The saved next is mandatory — overwriting
`curr->next` destroys your only route to the rest of the list.

## Invariant

prev heads the reversed prefix; curr heads the untouched suffix.

## Complexity

time O(n)   space O(1)

## Pitfall

Save `next` BEFORE reassigning. Getting that order wrong is the single
most common linked-list bug and it strands the remainder of the list.

Return prev, not curr — curr is null when the loop ends. Your Go version
gets both right.

This is the primitive behind palindrome-list, reorder-list, and
reverse-in-k-groups. Make it muscle memory.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/206-reverse-linked-list.go
