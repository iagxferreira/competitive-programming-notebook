#!/usr/bin/env bash
# Differential test: run brute.cpp against solution.cpp on random input
# until they disagree. gen.cpp takes a seed argument on argv[1].
#   tools/stress.sh leetcode/0015-three-sum [iterations]
set -euo pipefail

dir="${1:?usage: tools/stress.sh <problem-dir> [iters]}"
iters="${2:-1000}"
tmp="$(mktemp -d)"

for f in gen solution brute; do
    [[ -f "$dir/$f.cpp" ]] || { echo "missing $dir/$f.cpp"; exit 1; }
    g++ -std=c++20 -O2 "$dir/$f.cpp" -o "$tmp/$f"
done

for ((i = 1; i <= iters; i++)); do
    "$tmp/gen" "$i" > "$tmp/in.txt"
    "$tmp/solution" < "$tmp/in.txt" > "$tmp/fast.txt"
    "$tmp/brute"    < "$tmp/in.txt" > "$tmp/slow.txt"
    if ! diff -q "$tmp/fast.txt" "$tmp/slow.txt" >/dev/null; then
        echo "MISMATCH on iteration $i (seed $i)"
        echo "--- input ---";    cat "$tmp/in.txt"
        echo "--- solution ---"; cat "$tmp/fast.txt"
        echo "--- brute ---";    cat "$tmp/slow.txt"
        exit 1
    fi
    (( i % 100 == 0 )) && echo "ok $i/$iters"
done
echo "no mismatch in $iters iterations"
