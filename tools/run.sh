#!/usr/bin/env bash
# Compile and run one problem, feeding it every in*.txt it has.
# Diffs against the matching out*.txt when one exists.
#   tools/run.sh beecrowd/1000-hello-world
set -euo pipefail

dir="${1:?usage: tools/run.sh <problem-dir>}"
out="$(mktemp -d)"

javac -d "$out" "$dir"/*.java

main=$(grep -lE 'static void main' "$dir"/*.java | head -1 || true)
if [[ -z "$main" ]]; then
    echo "no main in $dir (leetcode problems have none) - compiled only"
    exit 0
fi
cls=$(basename "$main" .java)

shopt -s nullglob
inputs=("$dir"/in*.txt)
if (( ${#inputs[@]} == 0 )); then
    java -Xss256m -cp "$out" "$cls"
    exit 0
fi

status=0
for in in "${inputs[@]}"; do
    expected="${in/in/out}"
    echo "=== $(basename "$in") ==="
    if [[ -f "$expected" ]]; then
        if diff -u <(java -Xss256m -cp "$out" "$cls" < "$in") "$expected"; then
            echo "PASS"
        else
            echo "FAIL"
            status=1
        fi
    else
        java -Xss256m -cp "$out" "$cls" < "$in"
    fi
done
exit $status
