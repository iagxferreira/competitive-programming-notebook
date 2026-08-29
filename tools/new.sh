#!/usr/bin/env bash
# Scaffold a new problem directory.
#   tools/new.sh leetcode 0146 lru-cache        -> Solution.java (no main)
#   tools/new.sh codeforces 1900a some-problem  -> Main.java from the template
set -euo pipefail

platform="${1:?usage: tools/new.sh <platform> <id> <slug>}"
id="${2:?}"
slug="${3:?}"
dir="$platform/$id-$slug"
root="$(cd "$(dirname "$0")/.." && pwd)"

[[ -d "$dir" ]] && { echo "$dir already exists"; exit 1; }
mkdir -p "$dir"

if [[ "$platform" == "leetcode" ]]; then
    cat > "$dir/Solution.java" <<'TPL'
import java.util.*;

class Solution {
    public int solve() {
        // TODO: solve
        return 0;
    }
}
TPL
else
    sed -e 's/^public class Template {/public class Main {/' \
        -e 's/Template::run/Main::run/' \
        -e 's|^// Contest template.*|// Solution.|' \
        "$root/Template.java" > "$dir/Main.java"
fi

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
