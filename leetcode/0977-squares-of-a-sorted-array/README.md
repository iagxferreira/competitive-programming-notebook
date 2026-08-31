# 977. Squares of a Sorted Array

leetcode | Easy | array, two-pointers, sorting

## Task

Given an integer array `nums` sorted in non-decreasing order, return an
array of the squares of each number, also sorted in non-decreasing
order.

`1 <= nums.length <= 10^4`   `-10^4 <= nums[i] <= 10^4`   `nums` is
sorted in non-decreasing order.

Follow up: squaring each element and sorting is trivial - try an O(n)
solution using a different approach.

## Key insight

Solved the trivial way: map each element to its square, then sort. It is
correct, and at `n <= 10^4` an `Arrays.sort` finishes in well under a
millisecond - the constraints do not punish it.

What it gives up is stated in the problem itself: the input arrives
already sorted, and sorting from scratch throws that away. See the
Pitfall.

## Invariant

None worth naming. The loop is a straight map from `nums[i]` to its
square; the ordering is not maintained as you go, it is re-established
afterwards by the sort.

That absence is itself the tell. A solution that held an ordering
invariant across the pass would not need to sort at all.

## Complexity

time O(n log n)   space O(n) for the output, O(log n) auxiliary

## Pitfall

Overflow is the first box to tick, and it is clear here: `|nums[i]| <=
10^4`, so the largest square is 10^8 - comfortably inside int's
2.1x10^9. Checked, not assumed. A looser bound would not survive: 10^5
squared is 10^10 and needs `long`.

The real one is what the follow-up is pointing at. **The input is already
sorted, and this discards that.** The squares of a sorted array are not
sorted, but they are not arbitrary either - the ordering breaks in
exactly one predictable place, around zero, with the negatives coming out
reversed. Two already-ordered runs can be combined in a single pass
without sorting anything. Redo it that way: the O(n log n) version
carries no lesson, and the O(n) one is a technique you will reuse
constantly.

Minor, and repo-wide: `Arrays.sort(int[])` is dual-pivot quicksort with
adversarial O(n^2) inputs. Not exploitable on LeetCode; it is on
Codeforces. See the note in the README.

## Review

last: 2026-08-31   confidence: ?/5   (set your own)

## Origin

New problem - not in the legacy archive. Added from the pattern study
list.
