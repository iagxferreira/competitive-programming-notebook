# 125. Valid Palindrome

leetcode | easy | two-pointers, strings

## Task

Is the string a palindrome, considering only alphanumerics and ignoring
case?

## Key insight

Two pointers converging, each skipping non-alphanumeric characters
independently before comparing.

## Invariant

Everything outside [left, right] has already been matched.

## Complexity

time O(n)   space O(1)

## Pitfall

Your Go version wrapped every character in a `string(...)` and compared
with `strings.ToLower` — an allocation per character, and the range test
`value >= "A" && value <= "Z"` is doing lexicographic STRING comparison
where a byte comparison was meant. In C++ use `isalnum` and `tolower` on
the char directly. Cast to `unsigned char` first: passing a negative
char to those functions is undefined behaviour.

The empty string is a palindrome. The `flag` variable in the Go version
is dead weight — return true directly.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/125-valid-palindrome.go

Full study essay from the Kotlin lab (~300 lines):

    git show legacy-archive:problems/easy/valid-palindrome/README.md
