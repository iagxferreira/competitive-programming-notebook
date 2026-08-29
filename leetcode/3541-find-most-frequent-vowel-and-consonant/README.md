# 3541. Find Most Frequent Vowel and Consonant

leetcode | easy | counting, strings

## Task

Sum of the highest vowel frequency and the highest consonant frequency.

## Key insight

Count all 26 letters, then take the max over the vowel set and the max
over the consonant set separately and add them.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

Both maxima start at 0 and stay there when a category is absent — a
string of only vowels must contribute 0 for consonants, not skip the
term. Your Go version handles this correctly by initialising both to 0.

Counting into a 26-entry array and taking the two maxima afterwards is
cleaner than tracking maxima inside the loop.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/go/leetcode/3541-most-frequent.go
