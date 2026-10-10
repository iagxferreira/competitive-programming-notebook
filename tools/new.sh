#!/usr/bin/env bash
# Scaffold a problem or add a language implementation to an existing problem.
#   tools/new.sh leetcode 0146 lru-cache java
#   tools/new.sh codeforces 1900a some-problem go
#   tools/new.sh hackerrank '' simple-array-sum python
set -euo pipefail

usage() {
    printf 'usage: %s <platform> <id> <slug> [java|go|python|kotlin|rust]\n' "$0" >&2
    exit 2
}

[[ $# -ge 3 && $# -le 4 ]] || usage
platform="$1"
id="$2"
slug="$3"
language="${4:-java}"
case "$language" in
    java|go|python|kotlin|rust) ;;
    *) printf 'unsupported language: %s\n' "$language" >&2; usage ;;
esac

script_dir="$(cd "$(dirname "$0")" && pwd)"
root="${CP_ROOT:-$(dirname "$script_dir")}"
problem="$root/$platform/${id:+$id-}$slug"
template_dir="$script_dir/../templates/$language"

if [[ "$platform" == "leetcode" ]]; then
    case "$language" in
        java) template="Solution.java" ;;
        go) template="solution.go" ;;
        python) template="Solution.py" ;;
        kotlin) template="Solution.kt" ;;
        rust) template="Solution.rs" ;;
    esac
else
    case "$language" in
        java) template="Main.java" ;;
        go) template="main.go" ;;
        python) template="main.py" ;;
        kotlin) template="Main.kt" ;;
        rust) template="main.rs" ;;
    esac
fi

source="$problem/$language/$template"
[[ -f "$template_dir/$template" ]] || { printf 'missing template: %s\n' "$template_dir/$template" >&2; exit 1; }
[[ ! -e "$source" ]] || { printf 'source already exists: %s\n' "$source" >&2; exit 1; }

mkdir -p "$(dirname "$source")"
cp "$template_dir/$template" "$source"

if [[ ! -e "$problem/README.md" ]]; then
    heading_id="$(printf '%s' "$id" | sed 's/^0*\([0-9]\)/\1/')"
    heading_name="$(printf '%s' "${slug//-/ }" | sed 's/\b\(.[^ ]*\)/\u\1/g')"
    heading="${heading_id:+$heading_id. }$heading_name"
    cat > "$problem/README.md" <<TPL
# $heading

$platform | ? | ?

## Task

## Notes

## Review

last: never   confidence: 0/5
TPL
fi

printf 'created %s\n' "$source"
