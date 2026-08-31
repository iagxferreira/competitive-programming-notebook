# Roadmap

A recommended order for every problem in this repo. Pattern-first, not
number-first: each phase installs one idea and the next depends on it.

Tick a box when you have solved it **without** reading past the card's
`## Task` section. Reading `## Key insight` first is fine - it just means
the problem counts as study, not as a rep.

`*` marks a problem worth redoing carefully. `(never solved)` means it was
a `TODO` scaffold in the old Kotlin lab and you have no prior attempt.

## Phase 0 - Toolchain and I/O

*15 problems*

Zero algorithmic content. The point is to make the template, `Locale.US`, and fast reading automatic before anything hard depends on them. If you fumble I/O later you will not know whether your algorithm or your reader is wrong.

- [ ] [`beecrowd/1000-hello-world`](./beecrowd/1000-hello-world/)
- [ ] [`beecrowd/1001-extremely-basic`](./beecrowd/1001-extremely-basic/)
- [ ] [`beecrowd/1002-area-of-a-circle`](./beecrowd/1002-area-of-a-circle/)
- [ ] [`beecrowd/1003-simple-sum`](./beecrowd/1003-simple-sum/)
- [ ] [`beecrowd/1004-simple-product`](./beecrowd/1004-simple-product/)
- [ ] [`beecrowd/1005-average-1`](./beecrowd/1005-average-1/)
- [ ] [`beecrowd/1006-average-2`](./beecrowd/1006-average-2/)
- [ ] [`beecrowd/1007-difference`](./beecrowd/1007-difference/)
- [ ] [`beecrowd/1008-salary`](./beecrowd/1008-salary/)
- [ ] [`beecrowd/1009-salary-with-bonus`](./beecrowd/1009-salary-with-bonus/)
- [ ] [`beecrowd/1010-simple-calculate`](./beecrowd/1010-simple-calculate/)
- [ ] [`beecrowd/1011-sphere`](./beecrowd/1011-sphere/)
- [ ] [`beecrowd/1012-area`](./beecrowd/1012-area/)
- [ ] [`beecrowd/1013-the-greatest`](./beecrowd/1013-the-greatest/)
- [ ] [`hackerrank/simple-addition`](./hackerrank/simple-addition/)

## Phase 1 - Array and string fluency

*24 problems*

Low-thought reps to get Java's array and string idioms under your fingers. Do these fast - if one takes more than ten minutes, the card will tell you what you are missing.

- [ ] [`codeforces/0004a-watermelon`](./codeforces/0004a-watermelon/)
- [ ] [`hackerrank/simple-array-sum`](./hackerrank/simple-array-sum/)
- [ ] [`hackerrank/compare-the-triplets`](./hackerrank/compare-the-triplets/)
- [ ] [`hackerrank/reverse-array`](./hackerrank/reverse-array/)
- [ ] [`hackerrank/plus-minus`](./hackerrank/plus-minus/)
- [ ] [`hackerrank/mini-max-sum`](./hackerrank/mini-max-sum/)
- [ ] [`hackerrank/diagonal-difference`](./hackerrank/diagonal-difference/)
- [ ] [`hackerrank/staircase`](./hackerrank/staircase/)
- [ ] [`leetcode/1929-concatenation-of-array`](./leetcode/1929-concatenation-of-array/)
- [ ] [`leetcode/1920-build-array-from-permutation`](./leetcode/1920-build-array-from-permutation/)
- [ ] [`leetcode/1470-shuffle-the-array`](./leetcode/1470-shuffle-the-array/)
- [ ] [`leetcode/0066-plus-one`](./leetcode/0066-plus-one/)
- [x] [`leetcode/0412-fizz-buzz`](./leetcode/0412-fizz-buzz/)
- [ ] [`leetcode/2011-final-value-of-variable-after-performing-operations`](./leetcode/2011-final-value-of-variable-after-performing-operations/)
- [ ] [`leetcode/2769-find-the-maximum-achievable-number`](./leetcode/2769-find-the-maximum-achievable-number/)
- [ ] [`leetcode/2469-convert-the-temperature`](./leetcode/2469-convert-the-temperature/)
- [ ] [`leetcode/2894-divisible-and-non-divisible-sums-difference`](./leetcode/2894-divisible-and-non-divisible-sums-difference/)
- [ ] [`leetcode/3190-find-minimum-operations-to-make-all-elements-divisible-by-three`](./leetcode/3190-find-minimum-operations-to-make-all-elements-divisible-by-three/)
- [ ] [`leetcode/3512-minimum-operations-to-make-array-sum-divisible-by-k`](./leetcode/3512-minimum-operations-to-make-array-sum-divisible-by-k/)
- [ ] [`leetcode/3110-score-of-a-string`](./leetcode/3110-score-of-a-string/)  `*` floating point for an integer problem
- [ ] [`leetcode/2942-find-words-containing-character`](./leetcode/2942-find-words-containing-character/)
- [ ] [`leetcode/3136-valid-word`](./leetcode/3136-valid-word/)
- [ ] [`leetcode/0058-length-of-last-word`](./leetcode/0058-length-of-last-word/)  `*` trimmed and split the whole string to read its tail
- [ ] [`leetcode/3467-transform-array-by-parity`](./leetcode/3467-transform-array-by-parity/)  `*` sorted a two-valued array instead of counting

## Phase 2 - Binary search

*6 problems*

First real primitive, and the one you will reuse most. Own lower-bound binary search outright - not `Arrays.binarySearch`, the loop. Get the boundary convention and the overflow-safe midpoint into muscle memory here and they stay correct forever.

- [ ] [`leetcode/0704-binary-search`](./leetcode/0704-binary-search/)  `*` recursive, with the overflow-prone (lo+hi)/2 midpoint
- [ ] [`leetcode/0035-search-insert-position`](./leetcode/0035-search-insert-position/)  `*` linear scan where O(log n) was explicitly required
- [ ] [`leetcode/0278-first-bad-version`](./leetcode/0278-first-bad-version/)

## Phase 3 - Two pointers

*8 problems*

The second primitive. Every one of these rests on the same exchange argument: moving a pointer discards only candidates that provably cannot be the answer. If you cannot state why a move is safe, you have memorised it rather than understood it.

- [ ] [`leetcode/0125-valid-palindrome`](./leetcode/0125-valid-palindrome/)
- [ ] [`leetcode/0026-remove-duplicates-from-sorted-array`](./leetcode/0026-remove-duplicates-from-sorted-array/)
- [ ] [`leetcode/0027-remove-element`](./leetcode/0027-remove-element/)
- [ ] [`leetcode/0088-merge-sorted-array`](./leetcode/0088-merge-sorted-array/)
- [ ] [`leetcode/0167-two-sum-ii-input-array-is-sorted`](./leetcode/0167-two-sum-ii-input-array-is-sorted/)  `(never solved)`
- [ ] [`leetcode/0011-container-with-most-water`](./leetcode/0011-container-with-most-water/)
- [ ] [`leetcode/0015-3sum`](./leetcode/0015-3sum/)
- [ ] [`leetcode/0189-rotate-array`](./leetcode/0189-rotate-array/)  `*` allocated a second array; the O(1) triple-reversal is the point

## Phase 4 - Hashing and counting

*13 problems*

You have already done 0001. The rest drill the same trade - space for time - plus Java's specific traps: `get` returning null, boxing costs, and when a plain `int[]` beats a HashMap.

- [x] [`leetcode/0001-two-sum`](./leetcode/0001-two-sum/) already solved, ported from your C++
- [x] [`leetcode/0217-contains-duplicate`](./leetcode/0217-contains-duplicate/)
- [x] [`leetcode/0242-valid-anagram`](./leetcode/0242-valid-anagram/)
- [ ] [`leetcode/0349-intersection-of-two-arrays`](./leetcode/0349-intersection-of-two-arrays/)
- [ ] [`leetcode/0387-first-unique-character-in-a-string`](./leetcode/0387-first-unique-character-in-a-string/)
- [ ] [`leetcode/1512-number-of-good-pairs`](./leetcode/1512-number-of-good-pairs/)
- [ ] [`leetcode/2956-find-common-elements-between-two-arrays`](./leetcode/2956-find-common-elements-between-two-arrays/)
- [ ] [`leetcode/3668-restore-finishing-order`](./leetcode/3668-restore-finishing-order/)  `*` membership test against a list - quietly quadratic
- [ ] [`leetcode/3760-count-distinct-characters`](./leetcode/3760-count-distinct-characters/)
- [ ] [`leetcode/2325-decode-the-message`](./leetcode/2325-decode-the-message/)
- [ ] [`leetcode/3541-find-most-frequent-vowel-and-consonant`](./leetcode/3541-find-most-frequent-vowel-and-consonant/)
- [ ] [`leetcode/0049-group-anagrams`](./leetcode/0049-group-anagrams/)  `(never solved)`
- [ ] [`leetcode/1282-group-the-people-given-the-group-size-they-belong-to`](./leetcode/1282-group-the-people-given-the-group-size-they-belong-to/)

## Phase 5 - Sliding window

*3 problems*

Only two problems, but 0424 contains the subtlest argument in the whole set - why a stale `maxCount` is safe. Do not move on until you can defend it, or stress-test it against an honest version.

- [x] [`leetcode/0003-longest-substring-without-repeating-characters`](./leetcode/0003-longest-substring-without-repeating-characters/)
- [ ] [`leetcode/0424-longest-repeating-character-replacement`](./leetcode/0424-longest-repeating-character-replacement/)  `(never solved)`

## Phase 6 - Prefix and suffix products

*2 problems*

One problem, but the prefix/suffix decomposition it teaches shows up constantly. Note the division shortcut is banned for a reason.

- [ ] [`leetcode/0238-product-of-array-except-self`](./leetcode/0238-product-of-array-except-self/)  `(never solved)`

## Phase 7 - Stacks and queues

*4 problems*

0020 is the base case; 0232 teaches amortised analysis; 0225 you never actually solved; 0032 is a Hard that falls out of a stack of indices plus one sentinel.

- [ ] [`leetcode/0020-valid-parentheses`](./leetcode/0020-valid-parentheses/)
- [ ] [`leetcode/0232-implement-queue-using-stacks`](./leetcode/0232-implement-queue-using-stacks/)
- [ ] [`leetcode/0225-implement-stack-using-queues`](./leetcode/0225-implement-stack-using-queues/)  `*` backed the stack with a slice - never honored the queue-only constraint
- [ ] [`leetcode/0032-longest-valid-parentheses`](./leetcode/0032-longest-valid-parentheses/)

## Phase 8 - Linked lists

*12 problems*

Start with 0206 - reverse is the primitive the rest are built from. Then the two-pointer trio, then splicing. 0023 at the end is a Hard that needs the heap or divide-and-conquer you will have by then.

- [ ] [`leetcode/0206-reverse-linked-list`](./leetcode/0206-reverse-linked-list/)
- [ ] [`leetcode/0876-middle-of-the-linked-list`](./leetcode/0876-middle-of-the-linked-list/)
- [ ] [`leetcode/0141-linked-list-cycle`](./leetcode/0141-linked-list-cycle/)
- [ ] [`leetcode/0021-merge-two-sorted-lists`](./leetcode/0021-merge-two-sorted-lists/)
- [ ] [`leetcode/0019-remove-nth-node-from-end-of-list`](./leetcode/0019-remove-nth-node-from-end-of-list/)
- [ ] [`leetcode/0024-swap-nodes-in-pairs`](./leetcode/0024-swap-nodes-in-pairs/)
- [x] [`leetcode/0002-add-two-numbers`](./leetcode/0002-add-two-numbers/)
- [ ] [`leetcode/0061-rotate-list`](./leetcode/0061-rotate-list/)
- [ ] [`leetcode/0160-intersection-of-two-linked-lists`](./leetcode/0160-intersection-of-two-linked-lists/)  `*` hash set; the O(1)-space pointer switch is the lesson
- [ ] [`leetcode/1290-convert-binary-number-in-a-linked-list-to-integer`](./leetcode/1290-convert-binary-number-in-a-linked-list-to-integer/)
- [ ] [`leetcode/2807-insert-greatest-common-divisors-in-linked-list`](./leetcode/2807-insert-greatest-common-divisors-in-linked-list/)
- [ ] [`leetcode/0023-merge-k-sorted-lists`](./leetcode/0023-merge-k-sorted-lists/)

## Phase 9 - Trees

*14 problems*

The largest block. Recursion first (0104 through 0110), then BFS with the level-size snapshot, then the ordering-dependent ones. 0111 is the trap - it is not the mirror of 0104.

- [ ] [`leetcode/0104-maximum-depth-of-binary-tree`](./leetcode/0104-maximum-depth-of-binary-tree/)
- [ ] [`leetcode/0100-same-tree`](./leetcode/0100-same-tree/)
- [x] [`leetcode/0226-invert-binary-tree`](./leetcode/0226-invert-binary-tree/)
- [ ] [`leetcode/0101-symmetric-tree`](./leetcode/0101-symmetric-tree/)
- [ ] [`leetcode/0110-balanced-binary-tree`](./leetcode/0110-balanced-binary-tree/)
- [ ] [`leetcode/0094-binary-tree-inorder-traversal`](./leetcode/0094-binary-tree-inorder-traversal/)
- [ ] [`leetcode/0102-binary-tree-level-order-traversal`](./leetcode/0102-binary-tree-level-order-traversal/)
- [ ] [`hackerrank/tree-level-order-traversal`](./hackerrank/tree-level-order-traversal/)
- [ ] [`leetcode/0111-minimum-depth-of-binary-tree`](./leetcode/0111-minimum-depth-of-binary-tree/)
- [ ] [`leetcode/0098-validate-binary-search-tree`](./leetcode/0098-validate-binary-search-tree/)
- [ ] [`leetcode/0108-convert-sorted-array-to-binary-search-tree`](./leetcode/0108-convert-sorted-array-to-binary-search-tree/)
- [ ] [`leetcode/0938-range-sum-of-bst`](./leetcode/0938-range-sum-of-bst/)
- [ ] [`leetcode/1038-binary-search-tree-to-greater-sum-tree`](./leetcode/1038-binary-search-tree-to-greater-sum-tree/)
- [ ] [`leetcode/1367-linked-list-in-binary-tree`](./leetcode/1367-linked-list-in-binary-tree/)

## Phase 10 - Greedy and heaps

*3 problems*

Greedy needs an exchange argument, not intuition. For each, write down why the greedy choice cannot be beaten before you code it. Java's PriorityQueue is a min-heap by default, which is what both heap problems want.

- [ ] [`leetcode/0121-best-time-to-buy-and-sell-stock`](./leetcode/0121-best-time-to-buy-and-sell-stock/)
- [ ] [`leetcode/0347-top-k-frequent-elements`](./leetcode/0347-top-k-frequent-elements/)  `*` full sort, the one complexity the problem asks you to beat
- [ ] [`leetcode/1353-maximum-number-of-events-that-can-be-attended`](./leetcode/1353-maximum-number-of-events-that-can-be-attended/)

## Phase 11 - Dynamic programming

*4 problems*

Your weakest area by volume - four problems is not much DP. Do these, then go get more elsewhere. State the recurrence and the base case in words before writing any array.

- [ ] [`leetcode/0070-climbing-stairs`](./leetcode/0070-climbing-stairs/)
- [ ] [`leetcode/0509-fibonacci-number`](./leetcode/0509-fibonacci-number/)  `*` memoised into global mutable state
- [ ] [`leetcode/0096-unique-binary-search-trees`](./leetcode/0096-unique-binary-search-trees/)
- [ ] [`leetcode/3202-find-the-maximum-length-of-valid-subsequence-ii`](./leetcode/3202-find-the-maximum-length-of-valid-subsequence-ii/)

## Phase 12 - Backtracking and bits

*3 problems*

0046 is your only backtracking problem, so make it count - the undo step is the whole discipline. The bit problems are short but the counting argument in 1863 is worth deriving rather than accepting.

- [x] [`leetcode/0046-permutations`](./leetcode/0046-permutations/)  `*` iterative insertion instead of backtracking
- [ ] [`leetcode/0136-single-number`](./leetcode/0136-single-number/)
- [ ] [`leetcode/1863-sum-of-all-subset-xor-totals`](./leetcode/1863-sum-of-all-subset-xor-totals/)

## Phase 13 - Math, strings and simulation

*9 problems*

The leftovers, and mostly specification-reading exercises. 0007 and 0008 are really overflow problems; treat them as such.

- [ ] [`leetcode/0009-palindrome-number`](./leetcode/0009-palindrome-number/)
- [ ] [`leetcode/0007-reverse-integer`](./leetcode/0007-reverse-integer/)
- [ ] [`leetcode/0008-string-to-integer-atoi`](./leetcode/0008-string-to-integer-atoi/)
- [ ] [`leetcode/0013-roman-to-integer`](./leetcode/0013-roman-to-integer/)
- [ ] [`leetcode/0012-integer-to-roman`](./leetcode/0012-integer-to-roman/)  `*` table lookup; the greedy subtractive walk is what generalises
- [ ] [`leetcode/0014-longest-common-prefix`](./leetcode/0014-longest-common-prefix/)
- [ ] [`leetcode/0028-find-the-index-of-the-first-occurrence-in-a-string`](./leetcode/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [ ] [`leetcode/0006-zigzag-conversion`](./leetcode/0006-zigzag-conversion/)
- [ ] [`leetcode/0048-rotate-image`](./leetcode/0048-rotate-image/)

## Phase 14 - The two hard ones left

*2 problems*

Save these. 0005 is expand-around-centre with fiddly index recovery. 0004 is the single biggest gap in the archive - you solved it by sorting, which ignores the only reason it exists. Do it with the partition binary search.

- [ ] [`leetcode/0005-longest-palindromic-substring`](./leetcode/0005-longest-palindromic-substring/)
- [ ] [`leetcode/0004-median-of-two-sorted-arrays`](./leetcode/0004-median-of-two-sorted-arrays/)  `*` sorted and merged; the binary search is the entire reason it is Hard

## Unsorted - Recently added

*7 problems*

Problems added since the plan was written, deliberately left unclassified — naming the pattern here would give away the answer. Once you have solved one, move it up into the phase it belongs to.

- [x] [`leetcode/0383-ransom-note`](./leetcode/0383-ransom-note/)
- [x] [`leetcode/0409-longest-palindrome`](./leetcode/0409-longest-palindrome/)
- [x] [`leetcode/0078-subsets`](./leetcode/0078-subsets/)
- [x] [`leetcode/2236-root-equals-sum-of-children`](./leetcode/2236-root-equals-sum-of-children/)
- [x] [`leetcode/0700-search-in-a-binary-search-tree`](./leetcode/0700-search-in-a-binary-search-tree/)
- [x] [`leetcode/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree`](./leetcode/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [ ] [`leetcode/2529-maximum-count-of-positive-integer-and-negative-integer`](./leetcode/2529-maximum-count-of-positive-integer-and-negative-integer/)

---

One problem (`leetcode/2884-modify-columns`) is a LeetCode Pandas
exercise with no meaningful Java form, and is not in this list.

## The short version

If you only do eighteen problems, do these. Fourteen are ones where your
old solution passed but sidestepped the lesson; four you never solved at
all. This is the highest-value work in the repo.

- [ ] [`leetcode/0004-median-of-two-sorted-arrays`](./leetcode/0004-median-of-two-sorted-arrays/) - sorted and merged; the binary search is the entire reason it is Hard
- [ ] [`leetcode/0012-integer-to-roman`](./leetcode/0012-integer-to-roman/) - table lookup; the greedy subtractive walk is what generalises
- [ ] [`leetcode/0035-search-insert-position`](./leetcode/0035-search-insert-position/) - linear scan where O(log n) was explicitly required
- [ ] [`leetcode/0046-permutations`](./leetcode/0046-permutations/) - iterative insertion instead of backtracking
- [ ] [`leetcode/0058-length-of-last-word`](./leetcode/0058-length-of-last-word/) - trimmed and split the whole string to read its tail
- [ ] [`leetcode/0160-intersection-of-two-linked-lists`](./leetcode/0160-intersection-of-two-linked-lists/) - hash set; the O(1)-space pointer switch is the lesson
- [ ] [`leetcode/0189-rotate-array`](./leetcode/0189-rotate-array/) - allocated a second array; the O(1) triple-reversal is the point
- [ ] [`leetcode/0225-implement-stack-using-queues`](./leetcode/0225-implement-stack-using-queues/) - backed the stack with a slice - never honored the queue-only constraint
- [ ] [`leetcode/0347-top-k-frequent-elements`](./leetcode/0347-top-k-frequent-elements/) - full sort, the one complexity the problem asks you to beat
- [ ] [`leetcode/0509-fibonacci-number`](./leetcode/0509-fibonacci-number/) - memoised into global mutable state
- [ ] [`leetcode/0704-binary-search`](./leetcode/0704-binary-search/) - recursive, with the overflow-prone (lo+hi)/2 midpoint
- [ ] [`leetcode/3110-score-of-a-string`](./leetcode/3110-score-of-a-string/) - floating point for an integer problem
- [ ] [`leetcode/3467-transform-array-by-parity`](./leetcode/3467-transform-array-by-parity/) - sorted a two-valued array instead of counting
- [ ] [`leetcode/3668-restore-finishing-order`](./leetcode/3668-restore-finishing-order/) - membership test against a list - quietly quadratic
- [ ] [`leetcode/0049-group-anagrams`](./leetcode/0049-group-anagrams/) - never solved
- [ ] [`leetcode/0167-two-sum-ii-input-array-is-sorted`](./leetcode/0167-two-sum-ii-input-array-is-sorted/) - never solved
- [ ] [`leetcode/0238-product-of-array-except-self`](./leetcode/0238-product-of-array-except-self/) - never solved
- [ ] [`leetcode/0424-longest-repeating-character-replacement`](./leetcode/0424-longest-repeating-character-replacement/) - never solved

## How to use the Review line

Every card ends with:

```
last: never   confidence: 0/5
```

Set the date and a confidence when you solve it. Then revisit anything at
3 or below after a week, and anything at 1 or 2 after two days. That is the
whole spaced-repetition system - the cards exist to make a revisit cost two
minutes instead of twenty.

A problem you re-solve correctly from a cold start is worth more than three
you read the solution to.

## This repo is not enough on its own

Say it plainly: this archive is interview-style DSA, not competitive
programming. The two share fundamentals and then diverge hard. Contests
want speed under a clock, problems stated as stories you have to decode,
and whole topics that barely appear here — graphs, number theory,
combinatorics, geometry. **There is not a single graph traversal anywhere
in this repo.** No BFS on a grid, no shortest path, no union-find. Those
are table stakes for Div. 2 C and above.

So this is the training block, not the sport. Two tracks, in parallel:

**Track 1 — this repo.** Rebuild the fundamentals in Java until the
language is invisible. Follow the phases above.

**Track 2 — actual contests, starting now.** Codeforces Div. 2, virtual
if the timing is bad, but on the real clock. Do not wait for Phase 14 —
the whole point of Track 1 is to make Track 2 go better, and you only
find out what is missing by competing. Expect the early ones to hurt.
Rating is the only honest feedback signal here; the tick boxes above are
not.

When a contest exposes a gap — you could not model it as a graph, you
did not know the sieve — that becomes a new problem directory in here.
That is the loop. The rock gets heavier and so do you.
