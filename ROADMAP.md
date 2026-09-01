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

- [x] [`leetcode/0704-binary-search`](./leetcode/0704-binary-search/)  `*` recursive, with the overflow-prone (lo+hi)/2 midpoint
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
- [x] [`leetcode/0049-group-anagrams`](./leetcode/0049-group-anagrams/)  `*` sorted key; the 26-count key drops the log factor
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

- [x] [`leetcode/0104-maximum-depth-of-binary-tree`](./leetcode/0104-maximum-depth-of-binary-tree/)
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

*8 problems*

Problems added since the plan was written, deliberately left unclassified — naming the pattern here would give away the answer. Once you have solved one, move it up into the phase it belongs to.

- [x] [`leetcode/0383-ransom-note`](./leetcode/0383-ransom-note/)
- [x] [`leetcode/0409-longest-palindrome`](./leetcode/0409-longest-palindrome/)
- [x] [`leetcode/0078-subsets`](./leetcode/0078-subsets/)
- [x] [`leetcode/2236-root-equals-sum-of-children`](./leetcode/2236-root-equals-sum-of-children/)
- [x] [`leetcode/0700-search-in-a-binary-search-tree`](./leetcode/0700-search-in-a-binary-search-tree/)
- [x] [`leetcode/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree`](./leetcode/1379-find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)
- [ ] [`leetcode/2529-maximum-count-of-positive-integer-and-negative-integer`](./leetcode/2529-maximum-count-of-positive-integer-and-negative-integer/)
- [x] [`leetcode/2351-first-letter-to-appear-twice`](./leetcode/2351-first-letter-to-appear-twice/)

---

One problem (`leetcode/2884-modify-columns`) is a LeetCode Pandas
exercise with no meaningful Java form, and is not in this list.

## Blind 75 and Grind 75

*68 problems*

Everything on those two lists that was not already in the repo. The two
overlap by 40, so 110 distinct problems, of which 68 were missing.
Six more are LeetCode Premium (252, 253, 261, 269, 271, 323) and are
left out because you cannot open them.

Left unclassified on purpose, like the Unsorted section above - naming
the phase would name the technique. Move each one up into its phase
once you have solved it.

- [ ] [`leetcode/0017-letter-combinations-of-a-phone-number`](./leetcode/0017-letter-combinations-of-a-phone-number/)
- [ ] [`leetcode/0033-search-in-rotated-sorted-array`](./leetcode/0033-search-in-rotated-sorted-array/)
- [ ] [`leetcode/0039-combination-sum`](./leetcode/0039-combination-sum/)
- [ ] [`leetcode/0042-trapping-rain-water`](./leetcode/0042-trapping-rain-water/)
- [ ] [`leetcode/0053-maximum-subarray`](./leetcode/0053-maximum-subarray/)
- [ ] [`leetcode/0054-spiral-matrix`](./leetcode/0054-spiral-matrix/)
- [ ] [`leetcode/0055-jump-game`](./leetcode/0055-jump-game/)
- [ ] [`leetcode/0056-merge-intervals`](./leetcode/0056-merge-intervals/)
- [ ] [`leetcode/0057-insert-interval`](./leetcode/0057-insert-interval/)
- [ ] [`leetcode/0062-unique-paths`](./leetcode/0062-unique-paths/)
- [ ] [`leetcode/0067-add-binary`](./leetcode/0067-add-binary/)
- [ ] [`leetcode/0073-set-matrix-zeroes`](./leetcode/0073-set-matrix-zeroes/)
- [ ] [`leetcode/0075-sort-colors`](./leetcode/0075-sort-colors/)
- [ ] [`leetcode/0076-minimum-window-substring`](./leetcode/0076-minimum-window-substring/)
- [ ] [`leetcode/0079-word-search`](./leetcode/0079-word-search/)
- [ ] [`leetcode/0084-largest-rectangle-in-histogram`](./leetcode/0084-largest-rectangle-in-histogram/)
- [ ] [`leetcode/0091-decode-ways`](./leetcode/0091-decode-ways/)
- [ ] [`leetcode/0105-construct-binary-tree-from-preorder-and-inorder-traversal`](./leetcode/0105-construct-binary-tree-from-preorder-and-inorder-traversal/)
- [ ] [`leetcode/0124-binary-tree-maximum-path-sum`](./leetcode/0124-binary-tree-maximum-path-sum/)
- [ ] [`leetcode/0127-word-ladder`](./leetcode/0127-word-ladder/)
- [ ] [`leetcode/0128-longest-consecutive-sequence`](./leetcode/0128-longest-consecutive-sequence/)
- [x] [`leetcode/0133-clone-graph`](./leetcode/0133-clone-graph/)
- [ ] [`leetcode/0139-word-break`](./leetcode/0139-word-break/)
- [ ] [`leetcode/0143-reorder-list`](./leetcode/0143-reorder-list/)
- [ ] [`leetcode/0146-lru-cache`](./leetcode/0146-lru-cache/)
- [ ] [`leetcode/0150-evaluate-reverse-polish-notation`](./leetcode/0150-evaluate-reverse-polish-notation/)
- [ ] [`leetcode/0152-maximum-product-subarray`](./leetcode/0152-maximum-product-subarray/)
- [ ] [`leetcode/0153-find-minimum-in-rotated-sorted-array`](./leetcode/0153-find-minimum-in-rotated-sorted-array/)
- [ ] [`leetcode/0155-min-stack`](./leetcode/0155-min-stack/)
- [ ] [`leetcode/0169-majority-element`](./leetcode/0169-majority-element/)
- [ ] [`leetcode/0190-reverse-bits`](./leetcode/0190-reverse-bits/)
- [ ] [`leetcode/0191-number-of-1-bits`](./leetcode/0191-number-of-1-bits/)
- [ ] [`leetcode/0198-house-robber`](./leetcode/0198-house-robber/)
- [ ] [`leetcode/0199-binary-tree-right-side-view`](./leetcode/0199-binary-tree-right-side-view/)
- [ ] [`leetcode/0200-number-of-islands`](./leetcode/0200-number-of-islands/)
- [ ] [`leetcode/0207-course-schedule`](./leetcode/0207-course-schedule/)
- [ ] [`leetcode/0208-implement-trie-prefix-tree`](./leetcode/0208-implement-trie-prefix-tree/)
- [ ] [`leetcode/0211-design-add-and-search-words-data-structure`](./leetcode/0211-design-add-and-search-words-data-structure/)
- [ ] [`leetcode/0212-word-search-ii`](./leetcode/0212-word-search-ii/)
- [ ] [`leetcode/0213-house-robber-ii`](./leetcode/0213-house-robber-ii/)
- [ ] [`leetcode/0224-basic-calculator`](./leetcode/0224-basic-calculator/)
- [ ] [`leetcode/0230-kth-smallest-element-in-a-bst`](./leetcode/0230-kth-smallest-element-in-a-bst/)
- [ ] [`leetcode/0235-lowest-common-ancestor-of-a-binary-search-tree`](./leetcode/0235-lowest-common-ancestor-of-a-binary-search-tree/)
- [ ] [`leetcode/0236-lowest-common-ancestor-of-a-binary-tree`](./leetcode/0236-lowest-common-ancestor-of-a-binary-tree/)
- [x] [`leetcode/0268-missing-number`](./leetcode/0268-missing-number/)
- [ ] [`leetcode/0295-find-median-from-data-stream`](./leetcode/0295-find-median-from-data-stream/)
- [ ] [`leetcode/0297-serialize-and-deserialize-binary-tree`](./leetcode/0297-serialize-and-deserialize-binary-tree/)
- [ ] [`leetcode/0300-longest-increasing-subsequence`](./leetcode/0300-longest-increasing-subsequence/)
- [ ] [`leetcode/0310-minimum-height-trees`](./leetcode/0310-minimum-height-trees/)
- [ ] [`leetcode/0322-coin-change`](./leetcode/0322-coin-change/)
- [ ] [`leetcode/0338-counting-bits`](./leetcode/0338-counting-bits/)
- [ ] [`leetcode/0371-sum-of-two-integers`](./leetcode/0371-sum-of-two-integers/)
- [ ] [`leetcode/0416-partition-equal-subset-sum`](./leetcode/0416-partition-equal-subset-sum/)
- [ ] [`leetcode/0417-pacific-atlantic-water-flow`](./leetcode/0417-pacific-atlantic-water-flow/)
- [ ] [`leetcode/0435-non-overlapping-intervals`](./leetcode/0435-non-overlapping-intervals/)
- [ ] [`leetcode/0438-find-all-anagrams-in-a-string`](./leetcode/0438-find-all-anagrams-in-a-string/)
- [ ] [`leetcode/0542-01-matrix`](./leetcode/0542-01-matrix/)
- [ ] [`leetcode/0543-diameter-of-binary-tree`](./leetcode/0543-diameter-of-binary-tree/)
- [ ] [`leetcode/0572-subtree-of-another-tree`](./leetcode/0572-subtree-of-another-tree/)
- [ ] [`leetcode/0621-task-scheduler`](./leetcode/0621-task-scheduler/)
- [ ] [`leetcode/0647-palindromic-substrings`](./leetcode/0647-palindromic-substrings/)
- [ ] [`leetcode/0721-accounts-merge`](./leetcode/0721-accounts-merge/)
- [ ] [`leetcode/0733-flood-fill`](./leetcode/0733-flood-fill/)
- [ ] [`leetcode/0973-k-closest-points-to-origin`](./leetcode/0973-k-closest-points-to-origin/)
- [x] [`leetcode/0981-time-based-key-value-store`](./leetcode/0981-time-based-key-value-store/)
- [ ] [`leetcode/0994-rotting-oranges`](./leetcode/0994-rotting-oranges/)
- [ ] [`leetcode/1143-longest-common-subsequence`](./leetcode/1143-longest-common-subsequence/)
- [ ] [`leetcode/1235-maximum-profit-in-job-scheduling`](./leetcode/1235-maximum-profit-in-job-scheduling/)

## Pattern study list

*23 problems*

Everything on the pattern-grouped study list that the repo did not
already have. The other forty-odd entries on that list were already here,
scattered across the phases above.

Left unclassified like the two sections above, and for a sharper reason:
the list you took these from states the pattern next to each problem.
Reading them here, stripped of that label, is the harder and more useful
version. Move each one up into its phase once you have solved it.

- [ ] [`leetcode/0077-combinations`](./leetcode/0077-combinations/)
- [ ] [`leetcode/0092-reverse-linked-list-ii`](./leetcode/0092-reverse-linked-list-ii/)
- [ ] [`leetcode/0112-path-sum`](./leetcode/0112-path-sum/)
- [ ] [`leetcode/0203-remove-linked-list-elements`](./leetcode/0203-remove-linked-list-elements/)
- [ ] [`leetcode/0209-minimum-size-subarray-sum`](./leetcode/0209-minimum-size-subarray-sum/)
- [ ] [`leetcode/0215-kth-largest-element-in-an-array`](./leetcode/0215-kth-largest-element-in-an-array/)
- [ ] [`leetcode/0219-contains-duplicate-ii`](./leetcode/0219-contains-duplicate-ii/)
- [ ] [`leetcode/0234-palindrome-linked-list`](./leetcode/0234-palindrome-linked-list/)
- [ ] [`leetcode/0303-range-sum-query-immutable`](./leetcode/0303-range-sum-query-immutable/)
- [x] [`leetcode/0448-find-all-numbers-disappeared-in-an-array`](./leetcode/0448-find-all-numbers-disappeared-in-an-array/)
- [ ] [`leetcode/0450-delete-node-in-a-bst`](./leetcode/0450-delete-node-in-a-bst/)
- [ ] [`leetcode/0530-minimum-absolute-difference-in-bst`](./leetcode/0530-minimum-absolute-difference-in-bst/)
- [ ] [`leetcode/0653-two-sum-iv-input-is-a-bst`](./leetcode/0653-two-sum-iv-input-is-a-bst/)
- [ ] [`leetcode/0701-insert-into-a-binary-search-tree`](./leetcode/0701-insert-into-a-binary-search-tree/)
- [ ] [`leetcode/0784-letter-case-permutation`](./leetcode/0784-letter-case-permutation/)
- [ ] [`leetcode/0787-cheapest-flights-within-k-stops`](./leetcode/0787-cheapest-flights-within-k-stops/)
- [ ] [`leetcode/0845-longest-mountain-in-array`](./leetcode/0845-longest-mountain-in-array/)
- [x] [`leetcode/0977-squares-of-a-sorted-array`](./leetcode/0977-squares-of-a-sorted-array/)  `*` sorted from scratch; the input already being sorted is the whole follow-up
- [ ] [`leetcode/1200-minimum-absolute-difference`](./leetcode/1200-minimum-absolute-difference/)
- [ ] [`leetcode/1266-minimum-time-visiting-all-points`](./leetcode/1266-minimum-time-visiting-all-points/)
- [x] [`leetcode/1365-how-many-numbers-are-smaller-than-the-current-number`](./leetcode/1365-how-many-numbers-are-smaller-than-the-current-number/)  `*` O(n^2) pairwise scan; the bounded value range makes it linear
- [ ] [`leetcode/1382-balance-a-binary-search-tree`](./leetcode/1382-balance-a-binary-search-tree/)
- [ ] [`leetcode/2073-time-needed-to-buy-tickets`](./leetcode/2073-time-needed-to-buy-tickets/)

## Contest gaps - added 2026-08-31

*72 problems*

Two things at once. Twelve moved in from `algorithm-studies`, which has
been narrowed to building and using data structures and no longer holds
anything judge-shaped. The other sixty fill holes that were visible from
the section below: no number theory, no union-find, no minimum spanning
tree, no Fenwick tree, no monotonic deque, and one single Codeforces
problem on a repo whose stated goal is competing.

Unclassified like the sections above, except the two I/O ladders, which
simply continue Phase 0 and Phase 1 and have no technique to spoil.

### Moved from algorithm-studies

- [ ] [`leetcode/0022-generate-parentheses`](./leetcode/0022-generate-parentheses/)
- [ ] [`leetcode/0025-reverse-nodes-in-k-group`](./leetcode/0025-reverse-nodes-in-k-group/)
- [ ] [`leetcode/0045-jump-game-ii`](./leetcode/0045-jump-game-ii/)
- [ ] [`leetcode/0051-n-queens`](./leetcode/0051-n-queens/)
- [ ] [`leetcode/0072-edit-distance`](./leetcode/0072-edit-distance/)
- [ ] [`leetcode/0134-gas-station`](./leetcode/0134-gas-station/)
- [ ] [`leetcode/0567-permutation-in-string`](./leetcode/0567-permutation-in-string/)
- [ ] [`leetcode/0739-daily-temperatures`](./leetcode/0739-daily-temperatures/)
- [ ] [`leetcode/0743-network-delay-time`](./leetcode/0743-network-delay-time/)
- [ ] [`leetcode/1004-max-consecutive-ones-iii`](./leetcode/1004-max-consecutive-ones-iii/)
- [ ] [`leetcode/1046-last-stone-weight`](./leetcode/1046-last-stone-weight/)
- [ ] [`leetcode/1094-car-pooling`](./leetcode/1094-car-pooling/)  the free stand-in for the premium Meeting Rooms II

### Union-find, spanning trees and weighted grids

The roadmap used to say there was no union-find and no shortest path in
here. These close that.

- [ ] [`leetcode/0210-course-schedule-ii`](./leetcode/0210-course-schedule-ii/)  207 asks whether; this asks which
- [ ] [`leetcode/0547-number-of-provinces`](./leetcode/0547-number-of-provinces/)  `*` write union-find here first
- [ ] [`leetcode/0684-redundant-connection`](./leetcode/0684-redundant-connection/)  union-find as a cycle detector
- [ ] [`leetcode/1584-min-cost-to-connect-all-points`](./leetcode/1584-min-cost-to-connect-all-points/)  `*` the repo's first minimum spanning tree
- [ ] [`leetcode/0778-swim-in-rising-water`](./leetcode/0778-swim-in-rising-water/)  Dijkstra with max in place of sum

### Range queries and monotonic structures

- [ ] [`leetcode/0560-subarray-sum-equals-k`](./leetcode/0560-subarray-sum-equals-k/)  `*` the single most reused counting trick
- [ ] [`leetcode/0239-sliding-window-maximum`](./leetcode/0239-sliding-window-maximum/)  `*` monotonic deque
- [ ] [`leetcode/0496-next-greater-element-i`](./leetcode/0496-next-greater-element-i/)  monotonic stack, gentlest form
- [ ] [`leetcode/0304-range-sum-query-2d-immutable`](./leetcode/0304-range-sum-query-2d-immutable/)
- [ ] [`leetcode/0307-range-sum-query-mutable`](./leetcode/0307-range-sum-query-mutable/)  `*` the repo's first Fenwick tree
- [ ] [`leetcode/0315-count-of-smaller-numbers-after-self`](./leetcode/0315-count-of-smaller-numbers-after-self/)  Fenwick or merge-sort inversions

### Number theory, sorting and binary search on the answer

- [ ] [`leetcode/0204-count-primes`](./leetcode/0204-count-primes/)  `*` the sieve
- [ ] [`leetcode/0050-powx-n`](./leetcode/0050-powx-n/)  `*` fast exponentiation, and modPow's twin
- [ ] [`leetcode/0875-koko-eating-bananas`](./leetcode/0875-koko-eating-bananas/)  `*` binary search over the answer
- [ ] [`leetcode/0912-sort-an-array`](./leetcode/0912-sort-an-array/)  `*` anti-quicksort tests, by design
- [ ] [`leetcode/0179-largest-number`](./leetcode/0179-largest-number/)  the comparator contract
- [ ] [`leetcode/0201-bitwise-and-of-numbers-range`](./leetcode/0201-bitwise-and-of-numbers-range/)
- [ ] [`leetcode/0287-find-the-duplicate-number`](./leetcode/0287-find-the-duplicate-number/)  Floyd cycle detection on an array

### Grid dp, knapsack counting and backtracking

- [ ] [`leetcode/0064-minimum-path-sum`](./leetcode/0064-minimum-path-sum/)
- [ ] [`leetcode/0221-maximal-square`](./leetcode/0221-maximal-square/)
- [ ] [`leetcode/0518-coin-change-ii`](./leetcode/0518-coin-change-ii/)  `*` loop order decides combinations vs permutations
- [ ] [`leetcode/0090-subsets-ii`](./leetcode/0090-subsets-ii/)
- [ ] [`leetcode/0131-palindrome-partitioning`](./leetcode/0131-palindrome-partitioning/)
- [ ] [`leetcode/0703-kth-largest-element-in-a-stream`](./leetcode/0703-kth-largest-element-in-a-stream/)

### Codeforces ladder - rated 800 to 1300

The biggest gap of the lot. Contest problems are stated as stories and
judged on a clock, which is a different skill from anything on LeetCode.
Each has its sample as `in1.txt` / `out1.txt`, so `tools/run.sh` works.

- [ ] [`codeforces/0001a-theatre-square`](./codeforces/0001a-theatre-square/)  `*` long overflow and integer ceiling
- [ ] [`codeforces/0004c-registration-system`](./codeforces/0004c-registration-system/)
- [ ] [`codeforces/0025a-iq-test`](./codeforces/0025a-iq-test/)
- [ ] [`codeforces/0050a-domino-piling`](./codeforces/0050a-domino-piling/)
- [ ] [`codeforces/0071a-way-too-long-words`](./codeforces/0071a-way-too-long-words/)  char + int is addition, not concatenation
- [ ] [`codeforces/0096a-football`](./codeforces/0096a-football/)
- [ ] [`codeforces/0112a-petya-and-strings`](./codeforces/0112a-petya-and-strings/)
- [ ] [`codeforces/0118a-string-task`](./codeforces/0118a-string-task/)
- [ ] [`codeforces/0158a-next-round`](./codeforces/0158a-next-round/)
- [ ] [`codeforces/0158b-taxi`](./codeforces/0158b-taxi/)  `*` a greedy whose leftovers need proving
- [ ] [`codeforces/0231a-team`](./codeforces/0231a-team/)
- [ ] [`codeforces/0282a-bit-plus-plus`](./codeforces/0282a-bit-plus-plus/)

### HackerRank - the rest of the prep kit

Continues Phase 1. Low-thought reps, except the last three.

- [ ] [`hackerrank/time-conversion`](./hackerrank/time-conversion/)
- [ ] [`hackerrank/birthday-cake-candles`](./hackerrank/birthday-cake-candles/)
- [ ] [`hackerrank/grading-students`](./hackerrank/grading-students/)
- [ ] [`hackerrank/apple-and-orange`](./hackerrank/apple-and-orange/)
- [ ] [`hackerrank/number-line-jumps`](./hackerrank/number-line-jumps/)
- [ ] [`hackerrank/breaking-the-records`](./hackerrank/breaking-the-records/)
- [ ] [`hackerrank/sales-by-match`](./hackerrank/sales-by-match/)
- [ ] [`hackerrank/counting-valleys`](./hackerrank/counting-valleys/)
- [ ] [`hackerrank/jumping-on-the-clouds`](./hackerrank/jumping-on-the-clouds/)
- [ ] [`hackerrank/repeated-string`](./hackerrank/repeated-string/)  long overflow at n = 1e12
- [ ] [`hackerrank/2d-array-ds`](./hackerrank/2d-array-ds/)  the negative-initialisation trap
- [ ] [`hackerrank/array-manipulation`](./hackerrank/array-manipulation/)  `*` the difference array

### Beecrowd - the ladder past 1013

Continues Phase 0. I/O and specification drills; every card carries a
different formatting failure rather than repeating `Locale.US` twelve
times.

- [ ] [`beecrowd/1014-consumption`](./beecrowd/1014-consumption/)
- [ ] [`beecrowd/1015-distance-between-two-points`](./beecrowd/1015-distance-between-two-points/)
- [ ] [`beecrowd/1016-distance`](./beecrowd/1016-distance/)
- [ ] [`beecrowd/1017-fuel-spent`](./beecrowd/1017-fuel-spent/)
- [ ] [`beecrowd/1018-banknotes`](./beecrowd/1018-banknotes/)
- [ ] [`beecrowd/1019-time-conversion`](./beecrowd/1019-time-conversion/)
- [ ] [`beecrowd/1020-age-in-days`](./beecrowd/1020-age-in-days/)
- [ ] [`beecrowd/1021-banknotes-and-coins`](./beecrowd/1021-banknotes-and-coins/)  `*` money in integer cents
- [ ] [`beecrowd/1035-selection-test-1`](./beecrowd/1035-selection-test-1/)
- [ ] [`beecrowd/1036-bhaskaras-formula`](./beecrowd/1036-bhaskaras-formula/)
- [ ] [`beecrowd/1037-interval`](./beecrowd/1037-interval/)
- [ ] [`beecrowd/1038-snack`](./beecrowd/1038-snack/)

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
- [x] [`leetcode/0704-binary-search`](./leetcode/0704-binary-search/) - recursive, with the overflow-prone (lo+hi)/2 midpoint
- [ ] [`leetcode/3110-score-of-a-string`](./leetcode/3110-score-of-a-string/) - floating point for an integer problem
- [ ] [`leetcode/3467-transform-array-by-parity`](./leetcode/3467-transform-array-by-parity/) - sorted a two-valued array instead of counting
- [ ] [`leetcode/3668-restore-finishing-order`](./leetcode/3668-restore-finishing-order/) - membership test against a list - quietly quadratic
- [x] [`leetcode/0049-group-anagrams`](./leetcode/0049-group-anagrams/) - solved fresh, sorted key
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
and whole topics that barely appear here. Graphs used to be the glaring
one — that is now covered: grid BFS, topological order, Dijkstra,
union-find and a minimum spanning tree all have directories. Number
theory is down to two problems, and **combinatorics and geometry are
still absent entirely**. Those are table stakes for Div. 2 C and above.

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
