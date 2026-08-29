#!/usr/bin/env bash
# Compile and run one problem, feeding it every in*.txt it has.
# Diffs against the matching out*.txt when one exists.
#   tools/run.sh leetcode/0015-3sum [solution.cpp|practice.cpp]
# Set SAN=1 for sanitizers (needs libasan/libubsan, or CXX=clang++).
set -euo pipefail

dir="${1:?usage: tools/run.sh <problem-dir> [src]}"
src="${2:-solution.cpp}"
cxx="${CXX:-g++}"
bin="$(mktemp -d)/a.out"

flags=(-std=c++20 -O2 -Wall -Wextra -Wshadow)
[[ -n "${SAN:-}" ]] && flags+=(-fsanitize=address,undefined -g)

"$cxx" "${flags[@]}" "$dir/$src" -o "$bin"

shopt -s nullglob
inputs=("$dir"/in*.txt)
if (( ${#inputs[@]} == 0 )); then
    "$bin"
    exit 0
fi

status=0
for in in "${inputs[@]}"; do
    expected="${in/in/out}"
    echo "=== $(basename "$in") ==="
    if [[ -f "$expected" ]]; then
        if diff -u <("$bin" < "$in") "$expected"; then
            echo "PASS"
        else
            echo "FAIL"
            status=1
        fi
    else
        "$bin" < "$in"
    fi
done
exit $status
