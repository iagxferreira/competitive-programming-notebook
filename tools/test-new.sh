#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

scaffold() {
    local platform="$1" id="$2" slug="$3" language="$4" expected="$5"
    (cd "$tmp" && CP_ROOT="$tmp" "$root/tools/new.sh" "$platform" "$id" "$slug" "$language")
    [[ -f "$tmp/$platform/${id:+$id-}$slug/$language/$expected" ]] || {
        printf 'missing generated source: %s/%s\n' "$platform" "$language/$expected" >&2
        exit 1
    }
}

scaffold leetcode 0146 lru-cache java Solution.java
scaffold codeforces 1900a sample go main.go
scaffold beecrowd 1000 sample python main.py
scaffold hackerrank '' sample kotlin Main.kt
scaffold leetcode 0001 two-sum kotlin Solution.kt
scaffold atcoder abc001 sample rust main.rs
(cd "$tmp" && CP_ROOT="$tmp" "$root/tools/new.sh" beecrowd 1001 default-language)
[[ -f "$tmp/beecrowd/1001-default-language/java/Main.java" ]]

printf '# Keep existing notes\n' > "$tmp/leetcode/0146-lru-cache/README.md"
(cd "$tmp" && CP_ROOT="$tmp" "$root/tools/new.sh" leetcode 0146 lru-cache python)
[[ "$(<"$tmp/leetcode/0146-lru-cache/README.md")" == '# Keep existing notes' ]]

if (cd "$tmp" && CP_ROOT="$tmp" "$root/tools/new.sh" leetcode 0146 lru-cache java); then
    printf 'expected duplicate-language scaffold to fail\n' >&2
    exit 1
fi

printf 'scaffolding tests passed\n'
