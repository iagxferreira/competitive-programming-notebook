# Repo Instructions

Java competitive programming notebook. Every problem Iago has solved
before, being rebuilt from scratch in Java.

## Core Goal

Make Java his competition language. The archive is the training set: each
problem starts as an empty file plus a recall card written from his
earlier Go, Python, Kotlin or Rust attempt. He re-solves it in Java.

This is deliberate practice aimed at competing, not a portfolio. Treat
the empty files as work in progress, not as a permanent gimmick.

## The One Rule

**Do not write solutions unless asked to.**

He is here to get strong at this, and a solution he did not write teaches
him nothing. When helping with a problem:

- ask what the brute force is
- ask where the bottleneck is
- ask which invariant the approach relies on
- give a hint one level more specific than the last
- do not produce the final code unless explicitly asked

The card's `## Key insight` is a spoiler. Do not quote it unprompted.

## Study Order

[`ROADMAP.md`](./ROADMAP.md) has the recommended order and is the source
of truth for what to work on next. When the user asks what to do, read it
and pick the first unticked box rather than choosing arbitrarily.

## Problem Layout

```
<platform>/<id>-<slug>/
    README.md       the recall card
    Solution.java   leetcode: class Solution, no main
    Main.java       stdin/stdout problems, and leetcode harnesses
    Brute.java      optional, for stress testing
    Gen.java        optional, random input generator
    in*.txt         optional test input
    out*.txt        optional expected output
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

## Java Expectations

- Java 21, one self-contained file per problem, no build system
- never `Scanner` — `BufferedReader` + `StringTokenizer`, output via
  `StringBuilder`
- `Arrays.sort(int[])` is hackable quicksort; shuffle first or box
- default stack overflows near depth 10^4; run deep recursion on a
  thread with a larger stack
- `long` for any accumulation that could exceed 2^31; `int` wraps
  SILENTLY rather than trapping
- `%` on negatives yields a negative result — same as C++/Go, differs
  from Python
- `map.get` returns null, not a zero value; unboxing that throws NPE.
  Use `getOrDefault`
- `PriorityQueue` is a MIN-heap by default — the opposite of C++
- prefer primitive arrays over boxed collections; `ArrayDeque` over
  `Stack` and `LinkedList`
- pass `Locale.US` to `printf` / `String.format` for any decimal output

## Tooling

```bash
make run    DIR=<dir> [IN=in.txt]
make syntax DIR=<dir>
make check
tools/run.sh <dir>
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
