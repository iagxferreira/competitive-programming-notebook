# Repository Instructions

This is a language-agnostic competitive programming solutions repository.
Solutions may be written in any language; keep each problem's implementations
and tests together under its platform directory.

## Problem layout

```text
<platform>/<problem-id>-<slug>/
    README.md       problem reference, notes, and optional review status
    in*.txt         optional test inputs
    out*.txt        optional expected outputs
    java/           Java source files, if present
    go/             Go source files, if present
    python/         Python source files, if present
    kotlin/         Kotlin source files, if present
    rust/           Rust source files, if present
```

Keep existing Java filenames (`Main.java`, `Solution.java`) as-is under the
problem's `java/` directory. Put each additional implementation under its
language-named subdirectory, using recognizable filenames such as
`solution.go`, `solution.py`, `Solution.kt`, and `solution.rs`. Keep
language-specific tests with their implementation; shared sample input/output
files remain at the problem root. Avoid imposing a single language's build
system on unrelated solutions. Include concise run or test instructions when
needed.

## Helping with problem solving

Do not write a complete solution unless asked. When helping the user reason
through a problem, start with the brute force, identify its bottleneck, and
help establish the invariant before giving progressively more specific hints.
Do not reveal a problem card's key insight unprompted.

## Notes and provenance

Problem notes should be useful and concise. They may describe the task,
approach, invariant, complexity, pitfalls, and review status; adapt to the
problem instead of forcing every section onto every card. Preserve useful
existing notes. If restoring a historical implementation from
`legacy-archive`, preserve its language and mark its origin where that context
matters.

## Language-specific practices

Follow the established conventions of the language used by the solution and
the target judge. Keep implementations self-contained when required by the
platform. Check integer bounds, input/output constraints, and recursion limits
in the chosen runtime. Existing Java tooling and guidance remain applicable to
Java files only.

## Tooling

The Makefile's run/check commands currently support Java. The scaffold tool
supports Java, Go, Python, Kotlin, and Rust using `templates/<language>/`;
choose the right template shape for the target platform. For other language
changes, run the appropriate formatter, compiler, interpreter, or tests. Do
not claim cross-language verification from a Java-only check.

## Historical snapshot

The earlier multi-language solutions are grouped into the current tree by
problem and language. The original layout is preserved at the `legacy-archive`
tag. Retrieve a specific file with `git show legacy-archive:<path>`. When
incorporating another historical implementation, avoid overwriting a
different implementation and verify it using that language's toolchain where
available.

## Commit discipline

Use atomic commits and conventional prefixes: `feat:`, `fix:`, `docs:`,
`refactor:`, `build:`.
