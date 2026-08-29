# 412. Fizz Buzz

leetcode | easy | simulation

## Task

1..n as strings, with multiples of 3 -> Fizz, of 5 -> Buzz, of both ->
FizzBuzz.

## Key insight

Test the combined condition FIRST. Checking `i % 3` before `i % 15` means
15 matches Fizz and exits before FizzBuzz is ever considered.

## Invariant

None.

## Complexity

time O(n)   space O(n) for the output

## Pitfall

Branch order is the entire problem. Your Go version tests
`i%3 == 0 && i%5 == 0` first, which is correct.

`reserve(n)` on the vector avoids repeated reallocation.

## Review

last: 2026-08-29   confidence: ?/5   (set your own)

## Origin

git show legacy-archive:legacy/go/leetcode/412-fizz-buzz.go
git show legacy-archive:legacy/rust/leetcode/412-fizz_buzz.rs
