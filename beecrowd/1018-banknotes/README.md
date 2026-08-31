# 1018. Banknotes

beecrowd | easy | greedy, io

## Task

Read a value and print how many notes of each denomination (100, 50, 20,
10, 5, 2, 1) make it up, using as few notes as possible.

## Key insight

Greedy from the largest denomination down: `count = value / note` then
`value %= note`. It is optimal here because each denomination divides
neatly into the pattern - which is NOT true of arbitrary coin systems, and
is exactly why Coin Change is a dp problem.

## Invariant

After processing a denomination, the remaining value is smaller than it.

## Complexity

time O(1)   space O(1)

## Pitfall

Keep everything in integers. The moment you introduce a double for the
money, `0.1 + 0.2` style error creeps in and a note count comes out one
short. Print the original value first - the statement asks for it.

## Review

last: never   confidence: 0/5
