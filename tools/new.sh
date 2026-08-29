#!/usr/bin/env bash
# Scaffold a new problem directory from the template.
#   tools/new.sh leetcode 0217 contains-duplicate
set -euo pipefail

platform="${1:?usage: tools/new.sh <platform> <id> <slug>}"
id="${2:?}"
slug="${3:?}"
dir="$platform/$id-$slug"

[[ -d "$dir" ]] && { echo "$dir already exists"; exit 1; }
mkdir -p "$dir"
cp template.cpp "$dir/solution.cpp"

cat > "$dir/README.md" <<TPL
# $id. ${slug//-/ }

$platform | ? | ?

## Task

## Key insight

## Invariant

## Complexity

time O(?)   space O(?)

## Pitfall

## Review

last: never   confidence: 0/5
TPL

echo "created $dir"
