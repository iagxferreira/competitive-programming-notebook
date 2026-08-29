#!/usr/bin/env bash
# Differential test: run Brute against the real solution on random input
# until they disagree. Gen takes a seed on argv[0].
#
# Needs three extra files in the problem directory:
#   Brute.java  - obviously correct, too slow
#   Gen.java    - random input generator, seeded from args[0]
#   Main.java   - the real solution (or Solution.java with a main)
#
#   tools/stress.sh codeforces/0004a-watermelon [iterations]
set -euo pipefail

dir="${1:?usage: tools/stress.sh <problem-dir> [iters]}"
iters="${2:-1000}"
out="$(mktemp -d)"

for f in Gen Brute; do
    [[ -f "$dir/$f.java" ]] || { echo "missing $dir/$f.java"; exit 1; }
done

javac -d "$out" "$dir"/*.java

main=$(grep -lE 'static void main' "$dir"/Main.java "$dir"/Solution.java 2>/dev/null | head -1 || true)
[[ -n "$main" ]] || { echo "no Main.java or Solution.java with a main in $dir"; exit 1; }
cls=$(basename "$main" .java)

for ((i = 1; i <= iters; i++)); do
    java -cp "$out" Gen "$i"            > "$out/in.txt"
    java -cp "$out" "$cls" < "$out/in.txt" > "$out/fast.txt"
    java -cp "$out" Brute  < "$out/in.txt" > "$out/slow.txt"
    if ! diff -q "$out/fast.txt" "$out/slow.txt" >/dev/null; then
        echo "MISMATCH on iteration $i (seed $i)"
        echo "--- input ---";    cat "$out/in.txt"
        echo "--- solution ---"; cat "$out/fast.txt"
        echo "--- brute ---";    cat "$out/slow.txt"
        exit 1
    fi
    (( i % 100 == 0 )) && echo "ok $i/$iters"
done
echo "no mismatch in $iters iterations"
