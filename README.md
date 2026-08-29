# competitive-programming-notebook

C++ notebook for competitive programming and DSA. 118 problems across
four platforms, each one an annotated card plus an empty file to solve
into.

## How this works

Every problem is a directory:

```
leetcode/0015-3sum/
    README.md      what the problem teaches, and where you went wrong
    solution.cpp   empty. you write this.
```

The README is not a solution write-up. It is a **recall card**: the key
insight, the invariant that makes it work, the complexity, and the
specific pitfall — written from your own earlier attempt in Go, Python,
Kotlin or Rust. Read the card, close it, then solve from scratch.

Nothing here is pre-solved. That is deliberate.

## The archive

These problems were originally solved between 2023 and 2026 in four
languages. The code is not in the working tree, but none of it is lost —
every card ends with the command to retrieve the original:

```bash
git show legacy-archive:legacy/go/leetcode/15-three-sum.go
```

`legacy-archive` is a tag on the last commit before the C++ rewrite. Use
it to diff your new solution against what you wrote the first time.

## Layout

| Directory | Problems |
|---|---|
| `leetcode/` | 94 |
| `beecrowd/` | 14 |
| `hackerrank/` | 9 |
| `codeforces/` | 1 |
| `lib/` | reusable snippets |
| `tools/` | run, stress-test, scaffold |

LeetCode ids are zero-padded to four digits so they sort correctly.

## Running

```bash
make run DIR=leetcode/0015-3sum            # build and run
make run DIR=leetcode/0015-3sum IN=in.txt  # feed a test file
make check                                 # syntax-check every solution

tools/run.sh leetcode/0015-3sum            # run against all in*.txt, diff vs out*.txt
tools/stress.sh leetcode/0015-3sum 1000    # brute vs fast on random input
tools/new.sh leetcode 0146 lru-cache       # scaffold a new problem
```

Builds use `-std=c++20 -O2 -Wall -Wextra -Wshadow` with address and
undefined-behaviour sanitizers on. The sanitizers catch the class of bug
that costs you a contest — turn them off only when timing.

## Stress testing

For any problem where you are unsure, write three files and let the
machine find your counterexample:

- `brute.cpp` — obviously correct, too slow
- `solution.cpp` — the real one
- `gen.cpp` — random input, seeded from `argv[1]`

Then `tools/stress.sh <dir>`. This is the single highest-leverage habit
in competitive programming and it is why `brute.cpp` is worth writing
even when you are confident.

## Status

All 118 cards are written. All 118 solutions are empty.

Four of them (`0049`, `0167`, `0238`, `0424`) were never solved in the
first place — they were `TODO` scaffolds in the old Kotlin lab, and their
cards say so.

One (`2884`) is a LeetCode Pandas problem with no meaningful C++ form; it
has a card but intentionally no `solution.cpp`.
