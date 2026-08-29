#!/usr/bin/env bash
# Compile and run one problem, feeding it every in*.txt it has.
#   tools/run.sh leetcode/0015-three-sum [solution.cpp|practice.cpp]
set -euo pipefail

dir="${1:?usage: tools/run.sh <problem-dir> [src]}"
src="${2:-solution.cpp}"
bin="$(mktemp -d)/a.out"

g++ -std=c++20 -O2 -Wall -Wextra -Wshadow -fsanitize=address,undefined -g \
    "$dir/$src" -o "$bin"

shopt -s nullglob
inputs=("$dir"/in*.txt)
if (( ${#inputs[@]} == 0 )); then
    "$bin"
    exit 0
fi

for in in "${inputs[@]}"; do
    expected="${in/in/out}"
    echo "=== $(basename "$in") ==="
    if [[ -f "$expected" ]]; then
        if diff -u <("$bin" < "$in") "$expected"; then
            echo "PASS"
        else
            echo "FAIL"
        fi
    else
        "$bin" < "$in"
    fi
done
