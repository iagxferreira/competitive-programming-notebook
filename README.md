# competitive-programming-notebook

Every algorithm problem I have solved — across LeetCode, Beecrowd,
HackerRank and Codeforces — being rebuilt from scratch in Java.

The goal is not a solutions archive. It is to make Java the language I
compete in: fast enough under a clock, familiar enough that I am thinking
about the problem and never about the syntax.

Each problem starts as an empty file and an annotated card — the key
insight, the invariant, the complexity, and the specific way I got it
wrong the first time. I solve it again, in Java, properly.

Sisyphus got strong pushing that rock. That is the point.

## How this works

Every problem is a directory:

```
leetcode/0015-3sum/
    README.md       what the problem teaches, and where you went wrong
    Solution.java   empty. you write this.
```

The README is not a solution write-up. It is a **recall card**: the key
insight, the invariant that makes it work, the complexity, and the
specific pitfall — written from your own earlier attempt in Go, Python,
Kotlin or Rust. Read the card, close it, then solve from scratch.

Nothing arrives pre-solved. Every one gets earned in Java.

**Start here: [`ROADMAP.md`](./ROADMAP.md)** — every problem in a
recommended order, pattern by pattern, with the eighteen highest-value
ones called out. Tick the boxes as you go.

## The archive

These problems were originally solved between 2023 and 2026 in four
languages. The code is not in the working tree, but none of it is lost —
every card ends with the command to retrieve the original:

```bash
git show legacy-archive:legacy/go/leetcode/15-three-sum.go
```

`legacy-archive` is a tag on the last commit before the rewrite. Use it
to diff your new solution against what you wrote the first time.

## Layout

| Directory | Holds |
|---|---|
| `leetcode/` | the bulk of it |
| `beecrowd/` | the I/O and formatting drills |
| `hackerrank/` | early warmups |
| `codeforces/` | contest problems |
| `lib/` | reusable snippets |
| `tools/` | run, stress-test, scaffold |

LeetCode ids are zero-padded to four digits so they sort correctly.

## Running

```bash
make run    DIR=beecrowd/1000-hello-world
make run    DIR=... IN=in.txt           # feed a test file
make syntax DIR=leetcode/0015-3sum      # compile only (leetcode has no main)
make check                              # compile every problem

tools/run.sh beecrowd/1000-hello-world  # run against all in*.txt, diff vs out*.txt
tools/stress.sh codeforces/0004a-watermelon 1000
tools/new.sh leetcode 0146 lru-cache    # scaffold a new problem
```

Two problem shapes, and they build differently:

- **stdin/stdout** (beecrowd, codeforces, hackerrank) — `Main.java` or
  `Solution.java` has a `main`, so `make run` works directly.
- **`class Solution`** (leetcode) — no `main`, nothing to execute. Use
  `make syntax`, or add a `Main.java` harness to the directory and
  `make run` will find and use it.

No Gradle, no Maven. Every problem is one self-contained file, exactly
what you paste into the judge.

## Java in contests

Java is a first-class contest language — Codeforces, AtCoder, ICPC,
LeetCode, HackerRank and Beecrowd all take it. Four things cost people
problems, and all four are handled in `Template.java`:

**Scanner is too slow.** It is the most common cause of a Java TLE on a
solution that is algorithmically correct. Use `BufferedReader` +
`StringTokenizer` (what the template does), and build output into a
`StringBuilder` rather than calling `println` in a loop.

**`Arrays.sort(int[])` is hackable.** It is dual-pivot quicksort with
adversarial O(n²) inputs, and people on Codeforces construct them
deliberately. Shuffle before sorting, or sort a boxed `Integer[]`, which
uses TimSort. The template has a `sort` helper that shuffles.

**Recursion overflows early.** The default stack dies around depth 10⁴,
which a DFS over 10⁵ nodes will hit. Run your work on a thread with a
bigger stack — the template starts one with 256MB.

**No extra time limit.** Most judges, Codeforces included, apply the same
limit to every language, and Java runs roughly 1.5–2.5× slower than C++.
Setters normally ensure the intended solution passes in Java, but you
have less headroom, so constant factors matter: prefer primitive arrays
over boxed collections, and `ArrayDeque` over `Stack` or `LinkedList`.

One more, specific to the Beecrowd set: **always pass `Locale.US`** to
`printf` / `String.format`. On a pt_BR system `%.2f` prints a decimal
comma, which is an instant wrong answer that looks perfectly correct on
screen.

## Stress testing

For any problem where you are unsure, write three files and let the
machine find your counterexample:

- `Brute.java` — obviously correct, too slow
- `Gen.java` — random input, seeded from `args[0]`
- `Main.java` — the real one

Then `tools/stress.sh <dir>`. This is the single highest-leverage habit
in competitive programming and it is why `Brute.java` is worth writing
even when you are confident.

## Status

Every card is written. Most solutions are still empty — that is the work
in front of me, not a permanent state. Solved ones stay solved, and the
Review line on each card tracks when to come back to it.

Four problems (`0049`, `0167`, `0238`, `0424`) were never solved in the
first place — they were `TODO` scaffolds in the old Kotlin lab, and their
cards say so.

One (`2884`) is a LeetCode Pandas problem with no meaningful Java form;
it has a card but intentionally no `Solution.java`.
