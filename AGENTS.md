# Repo Instructions

C++ competitive programming notebook. 118 annotated problems, all
unsolved by design.

## Core Goal

Rebuild understanding by re-solving. The READMEs are recall aids written
from earlier solutions in Go, Python, Kotlin and Rust; the `.cpp` files
are deliberately empty.

## The One Rule

**Do not write solutions unless asked to.**

Filling in a `solution.cpp` destroys the point of this repository. When
helping with a problem:

- ask what the brute force is
- ask where the bottleneck is
- ask which invariant the approach relies on
- give a hint one level more specific than the last
- do not produce the final code unless explicitly asked

The card's `## Key insight` is a spoiler. Do not quote it unprompted.

## Problem Layout

```
<platform>/<id>-<slug>/
    README.md      the recall card
    solution.cpp   empty, the user's to write
    brute.cpp      optional, for stress testing
    gen.cpp        optional, random input generator
    in*.txt        optional test input
    out*.txt       optional expected output
```

## Card Format

Keep cards compact — roughly 50 lines. Sections in order:

`# <id>. <Title>` / platform-difficulty-tags line / `## Task` /
`## Key insight` / `## Invariant` / `## Complexity` / `## Pitfall` /
`## Review` / `## Origin`

The `## Pitfall` section is the most valuable part. It should name a
specific, concrete way to get this problem wrong — ideally the way the
user actually did.

Update `## Review` with the date and a 0-5 confidence when a problem is
re-solved.

## C++ Expectations

- `-std=c++20`, sanitizers on while developing
- `long long` for any accumulation that could exceed 2^31
- `%` on negatives yields a negative result — differs from Python
- `map[key]` INSERTS on read; use `count()` or `find()` to test
- prefer fixed-size arrays over hash maps for small bounded alphabets
- `priority_queue` is a MAX-heap by default
- watch unsigned wraparound on `size() - 1` and `n - m`

## Tooling

```bash
make run DIR=<dir> [IN=in.txt]
make check
tools/run.sh <dir> [src]
tools/stress.sh <dir> [iters]
tools/new.sh <platform> <id> <slug>
```

## The Archive

The original multi-language solutions live at the `legacy-archive` tag,
not in the working tree:

```bash
git show legacy-archive:legacy/go/leetcode/15-three-sum.go
git show legacy-archive:problems/easy/two-sum/README.md
```

Do not restore them into the tree. Retrieving one to compare against a
freshly written solution is fine and encouraged.

## Commit Discipline

Atomic commits, conventional prefixes: `feat:`, `fix:`, `docs:`,
`refactor:`, `build:`.
