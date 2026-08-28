# 125. Valid Palindrome

Platform: LeetCode
Problem URL: [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)
Difficulty: Easy
Pattern: Two Pointers / String Cleanup
Status: Solved

Started: August 28, 2026
Solved: August 28, 2026

Worksheet: [`../problem.md`](/home/iago/workspace/algorithm-solutions/problems/problem.md)

## Session Notes

This problem is a good fit for a two-pointer scan because I want to compare the string from both ends while ignoring characters that do not matter.

The key question is:

- after filtering out punctuation, spaces, and case differences, do the remaining characters read the same forward and backward?

## 1. Understanding

The problem asks whether a string is a palindrome when I ignore non-alphanumeric characters and case.

My own wording:

- Look at the string from both ends.
- Skip characters that are not letters or digits.
- Compare the remaining characters without caring about uppercase vs lowercase.
- Return `true` if the cleaned sequence reads the same in both directions.

What the output represents:

- `true` means the normalized string is the same forward and backward.
- `false` means a mismatch appears after normalization.

What I need to keep in mind:

- punctuation does not matter
- spaces do not matter
- case does not matter
- the comparison is symmetric

## 2. Constraints

From the prompt:

- Input size: not huge enough to force a heavy precomputation trick
- Character set: general ASCII-style text with letters, digits, spaces, and punctuation

What do these constraints tell me about the possible complexity?

- I can solve this in one pass with two pointers.
- I do not need to build a fully cleaned copy of the string unless I want the simpler but less memory-efficient version.

## 3. Examples

Example 1:

- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `true`
- Why? After normalization, the string reads the same forward and backward.

Example 2:

- Input: `s = "race a car"`
- Output: `false`
- Why? The normalized characters do not mirror each other.

My own example:

- Input: `s = "0P"`
- Output: `false`
- Why? `0` and `p` are different after normalization.

Relevant edge cases:

- Empty string
- Single character
- Only punctuation
- Mixed case
- Digits mixed with letters

## 4. Brute Force

Approach:

- Remove every character that is not a letter or digit.
- Convert the remaining characters to one case.
- Reverse the result.
- Compare it to the original normalized string.

Why does it work?

- A palindrome reads the same forward and backward.
- Normalization makes the comparison fair by ignoring irrelevant characters.

Time Complexity:

- `O(n)`

Space Complexity:

- `O(n)` because the cleaned copy and reversed copy need storage.

## 5. Bottleneck

What makes the brute-force solution less attractive?

- It allocates extra strings.

What operation happens repeatedly?

- Cleaning, copying, and reversing the whole string.

What information am I recomputing?

- Whether the next meaningful character on the left matches the next meaningful character on the right.

Can I store something?

- I can avoid storage by comparing in place.

Can I eliminate unnecessary work?

- Yes, by skipping ignored characters directly in the original string.

Can ordering help?

- Yes, because palindrome comparison is naturally a left-right symmetry problem.

Can I process the input only once?

- Yes, with two pointers.

Can I maintain some state?

- Yes, the left and right scan positions.

## 6. Pattern Recognition

Pattern:

- Two pointers
- Normalization in place

Why:

- I need to compare mirrored positions while skipping irrelevant characters.

Recognition signals:

- “Read the string as a palindrome”
- “Ignore non-alphanumeric characters”
- “Case insensitive”
- “Compare from both ends”

## 7. Data Structure

What data structure am I using?

- The original string plus two indexes

Why?

- The string itself already contains the data I need.

What operation does it optimize?

- Mirrored comparison without allocation.

What is its complexity?

- Pointer movement is `O(1)` per step.

What would happen if I used another data structure?

- A cleaned `StringBuilder` or filtered list would be easier to reason about but would use extra memory.

## 8. Invariant

What must always remain true while my algorithm runs?

- Every character outside the current `[left, right]` window has already been validated.
- The characters being compared are the next meaningful characters from each side.

## 9. Algorithm

1. Set one pointer at the start and one at the end.
2. Move the left pointer forward until it reaches a letter or digit.
3. Move the right pointer backward until it reaches a letter or digit.
4. Compare the normalized characters.
5. If they differ, return `false`.
6. Move both pointers inward and continue.
7. If the pointers cross, return `true`.

## 10. Correctness

Why does this algorithm always produce the correct result?

- It compares the next meaningful character from the left with the next meaningful character from the right.
- Any ignored character is skipped, so punctuation and spaces cannot affect the answer.
- If every mirrored pair matches, the normalized string is symmetric.
- If any mirrored pair differs, the string is not a palindrome after normalization.

What cases does it handle?

- Empty string
- Single-character string
- Strings with punctuation
- Strings with mixed case
- Strings with digits

Why can I safely discard certain information?

- Non-alphanumeric characters do not affect the result.
- Case differences do not affect the result.

## 11. Kotlin Implementation

Implementation notes:

- Use `Char.isLetterOrDigit()` to skip irrelevant characters.
- Use `Char.lowercaseChar()` to normalize comparisons.
- Keep the scan in the original string to avoid extra allocations.

Final Kotlin solution:

- Two pointers, skipping non-alphanumeric characters, comparing lowercase values.

## 12. Tests

Tests:

- Classic palindrome with punctuation
- Non-palindrome with spaces
- Empty string
- Single character
- Mixed case and punctuation

Test scaffold:

- Kotlin test file: [`ValidPalindromeTest.kt`](/home/iago/workspace/algorithm-solutions/src/test/kotlin/algorithms/problems/easy/valid_palindrome/ValidPalindromeTest.kt)
- What should this test prove?

  - The function ignores punctuation and spaces.
  - The function ignores case.
  - The function returns the correct result for short and empty inputs.

## 13. Complexity

Time:

- `O(n)`

Space:

- `O(1)` extra space

Notes on JVM behavior:

- The two-pointer version avoids building extra strings.
- It keeps allocations low compared with a normalize-then-reverse approach.

## 14. Reflection

What did I initially misunderstand?

- I might first think of reversing a cleaned string, but that is not required.

What is the reusable lesson?

- If the comparison is symmetric, two pointers are usually the cleanest shape.

What should I remember next time?

- First ask whether I can ignore characters in place instead of creating a filtered copy.
