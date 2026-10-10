# Competitive Programming Solutions

A language-agnostic collection of competitive programming problems, solutions,
notes, and tests. Problems are organized by platform; implementations may use
whatever language best fits the problem or the author's current practice.

The repository brings together Java solutions and earlier solutions in Go,
Python, Kotlin, and Rust. Those language implementations have been grouped by
problem in the current tree. The `legacy-archive` tag remains an immutable
historical snapshot of the original layout.

## Repository layout

```text
<platform>/<problem-id>-<slug>/
    README.md              problem statement/reference and notes
    in*.txt / out*.txt     sample or regression tests
    java/                  Java implementation(s)
    go/                    Go implementation(s), when present
    python/                Python implementation(s), when present
    kotlin/                Kotlin implementation(s), when present
    rust/                  Rust implementation(s), when present
```

Each problem directory is the shared home for all implementations of that
problem. Add a language-named subdirectory and keep that language's sources
and language-specific tests there. Keep judge-ready implementations
self-contained when required by the platform. If a language needs a compiler,
runtime, or test harness, document its command next to the solution or in the
platform's tooling docs. Shared `in*.txt` / `out*.txt` samples and problem
notes stay at the problem-directory root.

Platforms currently represented include `leetcode/`, `beecrowd/`,
`hackerrank/`, and `codeforces/`. Shared algorithms and utilities belong in
`lib/` with the language included in the path when needed, for example
`lib/go/` or `lib/python/`.

## Working with problems

Problem cards can record the task, approach, invariant, complexity, pitfalls,
references, and review status. They are useful study notes, not a mandatory
format: retain meaningful existing cards and avoid duplicating a full solution
in prose. Record the language and any non-obvious assumptions when they help a
reader understand an implementation.

## Running solutions

There is no repository-wide build system across languages. The existing
Makefile and scripts support the Java solutions:

```bash
make run    DIR=beecrowd/1000-hello-world
make run    DIR=codeforces/0001a-theatre-square IN=in1.txt
make syntax DIR=leetcode/0015-3sum
make check
tools/run.sh codeforces/0001a-theatre-square
tools/stress.sh codeforces/0004a-watermelon 1000
```

Java implementations live in each problem's `java/` directory. For other
languages, use the relevant compiler/runtime directly and add problem-specific
instructions when a command is not obvious. Tests should be kept close to the
problem they exercise.

## Scaffolding a problem

`templates/` contains stdin/stdout and judge-class starting points for Java,
Go, Python, Kotlin, and Rust. `make new` creates a problem directory (or adds
an implementation to an existing one) and never overwrites an existing source:

```bash
make new P=leetcode ID=0146 SLUG=lru-cache L=python
make new P=codeforces ID=1900a SLUG=some-problem L=java
make new P=hackerrank ID= SLUG=simple-array-sum L=kotlin
make scaffold-test
```

`L` defaults to `java`. LeetCode receives a judge-class template; other
platforms receive a stdin/stdout template. Direct use is also available as
`tools/new.sh <platform> <id> <slug> [language]`.

## Historical solutions

The original multi-language work is available without checking out the tag:

```bash
git show legacy-archive:legacy/go/leetcode/15-three-sum.go
git show legacy-archive:problems/easy/two-sum/README.md
```

The Go, Python, Kotlin, and Rust implementations are imported under their
matching platform/problem directories and language subdirectories. When
restoring another historical implementation, preserve its language and mark
its origin where relevant; do not overwrite an existing implementation just
because the problem matches.
