import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent

# problems that were solved before but dodged the lesson -> highest value redo
REDO = {
 "leetcode/0004-median-of-two-sorted-arrays":"sorted and merged; the binary search is the entire reason it is Hard",
 "leetcode/0035-search-insert-position":"linear scan where O(log n) was explicitly required",
 "leetcode/0189-rotate-array":"allocated a second array; the O(1) triple-reversal is the point",
 "leetcode/0225-implement-stack-using-queues":"backed the stack with a slice - never honored the queue-only constraint",
 "leetcode/0347-top-k-frequent-elements":"full sort, the one complexity the problem asks you to beat",
 "leetcode/0509-fibonacci-number":"memoised into global mutable state",
 "leetcode/0704-binary-search":"recursive, with the overflow-prone (lo+hi)/2 midpoint",
 "leetcode/0046-permutations":"iterative insertion instead of backtracking",
 "leetcode/0160-intersection-of-two-linked-lists":"hash set; the O(1)-space pointer switch is the lesson",
 "leetcode/0058-length-of-last-word":"trimmed and split the whole string to read its tail",
 "leetcode/3668-restore-finishing-order":"membership test against a list - quietly quadratic",
 "leetcode/0012-integer-to-roman":"table lookup; the greedy subtractive walk is what generalises",
 "leetcode/3467-transform-array-by-parity":"sorted a two-valued array instead of counting",
 "leetcode/3110-score-of-a-string":"floating point for an integer problem",
}
NEVER = {"leetcode/0049-group-anagrams","leetcode/0167-two-sum-ii-input-array-is-sorted",
         "leetcode/0238-product-of-array-except-self",
         "leetcode/0424-longest-repeating-character-replacement"}

PHASES = [
("Phase 0", "Toolchain and I/O", 15,
 "Zero algorithmic content. The point is to make the template, `Locale.US`, "
 "and fast reading automatic before anything hard depends on them. If you "
 "fumble I/O later you will not know whether your algorithm or your reader "
 "is wrong.",
 ["beecrowd/1000-hello-world","beecrowd/1001-extremely-basic","beecrowd/1002-area-of-a-circle",
  "beecrowd/1003-simple-sum","beecrowd/1004-simple-product","beecrowd/1005-average-1",
  "beecrowd/1006-average-2","beecrowd/1007-difference","beecrowd/1008-salary",
  "beecrowd/1009-salary-with-bonus","beecrowd/1010-simple-calculate","beecrowd/1011-sphere",
  "beecrowd/1012-area","beecrowd/1013-the-greatest","hackerrank/simple-addition"]),

("Phase 1", "Array and string fluency", 24,
 "Low-thought reps to get Java's array and string idioms under your fingers. "
 "Do these fast - if one takes more than ten minutes, the card will tell you "
 "what you are missing.",
 ["codeforces/0004a-watermelon","hackerrank/simple-array-sum","hackerrank/compare-the-triplets",
  "hackerrank/reverse-array","hackerrank/plus-minus","hackerrank/mini-max-sum",
  "hackerrank/diagonal-difference","hackerrank/staircase",
  "leetcode/1929-concatenation-of-array","leetcode/1920-build-array-from-permutation",
  "leetcode/1470-shuffle-the-array","leetcode/0066-plus-one","leetcode/0412-fizz-buzz",
  "leetcode/2011-final-value-of-variable-after-performing-operations",
  "leetcode/2769-find-the-maximum-achievable-number","leetcode/2469-convert-the-temperature",
  "leetcode/2894-divisible-and-non-divisible-sums-difference",
  "leetcode/3190-find-minimum-operations-to-make-all-elements-divisible-by-three",
  "leetcode/3512-minimum-operations-to-make-array-sum-divisible-by-k",
  "leetcode/3110-score-of-a-string","leetcode/2942-find-words-containing-character",
  "leetcode/3136-valid-word","leetcode/0058-length-of-last-word",
  "leetcode/3467-transform-array-by-parity"]),

("Phase 2", "Binary search", 3,
 "First real primitive, and the one you will reuse most. Own lower-bound "
 "binary search outright - not `Arrays.binarySearch`, the loop. Get the "
 "boundary convention and the overflow-safe midpoint into muscle memory here "
 "and they stay correct forever.",
 ["leetcode/0704-binary-search","leetcode/0035-search-insert-position",
  "leetcode/0278-first-bad-version"]),

("Phase 3", "Two pointers", 8,
 "The second primitive. Every one of these rests on the same exchange "
 "argument: moving a pointer discards only candidates that provably cannot "
 "be the answer. If you cannot state why a move is safe, you have memorised "
 "it rather than understood it.",
 ["leetcode/0125-valid-palindrome","leetcode/0026-remove-duplicates-from-sorted-array",
  "leetcode/0027-remove-element","leetcode/0088-merge-sorted-array",
  "leetcode/0167-two-sum-ii-input-array-is-sorted","leetcode/0011-container-with-most-water",
  "leetcode/0015-3sum","leetcode/0189-rotate-array"]),

("Phase 4", "Hashing and counting", 13,
 "You have already done 0001. The rest drill the same trade - space for time "
 "- plus Java's specific traps: `get` returning null, boxing costs, and when "
 "a plain `int[]` beats a HashMap.",
 ["leetcode/0001-two-sum","leetcode/0217-contains-duplicate","leetcode/0242-valid-anagram",
  "leetcode/0349-intersection-of-two-arrays","leetcode/0387-first-unique-character-in-a-string",
  "leetcode/1512-number-of-good-pairs","leetcode/2956-find-common-elements-between-two-arrays",
  "leetcode/3668-restore-finishing-order","leetcode/3760-count-distinct-characters",
  "leetcode/2325-decode-the-message","leetcode/3541-find-most-frequent-vowel-and-consonant",
  "leetcode/0049-group-anagrams",
  "leetcode/1282-group-the-people-given-the-group-size-they-belong-to"]),

("Phase 5", "Sliding window", 2,
 "Only two problems, but 0424 contains the subtlest argument in the whole "
 "set - why a stale `maxCount` is safe. Do not move on until you can defend "
 "it, or stress-test it against an honest version.",
 ["leetcode/0003-longest-substring-without-repeating-characters",
  "leetcode/0424-longest-repeating-character-replacement"]),

("Phase 6", "Prefix and suffix products", 1,
 "One problem, but the prefix/suffix decomposition it teaches shows up "
 "constantly. Note the division shortcut is banned for a reason.",
 ["leetcode/0238-product-of-array-except-self"]),

("Phase 7", "Stacks and queues", 4,
 "0020 is the base case; 0232 teaches amortised analysis; 0225 you never "
 "actually solved; 0032 is a Hard that falls out of a stack of indices plus "
 "one sentinel.",
 ["leetcode/0020-valid-parentheses","leetcode/0232-implement-queue-using-stacks",
  "leetcode/0225-implement-stack-using-queues","leetcode/0032-longest-valid-parentheses"]),

("Phase 8", "Linked lists", 12,
 "Start with 0206 - reverse is the primitive the rest are built from. Then "
 "the two-pointer trio, then splicing. 0023 at the end is a Hard that needs "
 "the heap or divide-and-conquer you will have by then.",
 ["leetcode/0206-reverse-linked-list","leetcode/0876-middle-of-the-linked-list",
  "leetcode/0141-linked-list-cycle","leetcode/0021-merge-two-sorted-lists",
  "leetcode/0019-remove-nth-node-from-end-of-list","leetcode/0024-swap-nodes-in-pairs",
  "leetcode/0002-add-two-numbers","leetcode/0061-rotate-list",
  "leetcode/0160-intersection-of-two-linked-lists",
  "leetcode/1290-convert-binary-number-in-a-linked-list-to-integer",
  "leetcode/2807-insert-greatest-common-divisors-in-linked-list",
  "leetcode/0023-merge-k-sorted-lists"]),

("Phase 9", "Trees", 14,
 "The largest block. Recursion first (0104 through 0110), then BFS with the "
 "level-size snapshot, then the ordering-dependent ones. 0111 is the trap - "
 "it is not the mirror of 0104.",
 ["leetcode/0104-maximum-depth-of-binary-tree","leetcode/0100-same-tree",
  "leetcode/0226-invert-binary-tree","leetcode/0101-symmetric-tree",
  "leetcode/0110-balanced-binary-tree","leetcode/0094-binary-tree-inorder-traversal",
  "leetcode/0102-binary-tree-level-order-traversal","hackerrank/tree-level-order-traversal",
  "leetcode/0111-minimum-depth-of-binary-tree","leetcode/0098-validate-binary-search-tree",
  "leetcode/0108-convert-sorted-array-to-binary-search-tree","leetcode/0938-range-sum-of-bst",
  "leetcode/1038-binary-search-tree-to-greater-sum-tree","leetcode/1367-linked-list-in-binary-tree"]),

("Phase 10", "Greedy and heaps", 3,
 "Greedy needs an exchange argument, not intuition. For each, write down why "
 "the greedy choice cannot be beaten before you code it. Java's PriorityQueue "
 "is a min-heap by default, which is what both heap problems want.",
 ["leetcode/0121-best-time-to-buy-and-sell-stock","leetcode/0347-top-k-frequent-elements",
  "leetcode/1353-maximum-number-of-events-that-can-be-attended"]),

("Phase 11", "Dynamic programming", 4,
 "Your weakest area by volume - four problems is not much DP. Do these, then "
 "go get more elsewhere. State the recurrence and the base case in words "
 "before writing any array.",
 ["leetcode/0070-climbing-stairs","leetcode/0509-fibonacci-number",
  "leetcode/0096-unique-binary-search-trees",
  "leetcode/3202-find-the-maximum-length-of-valid-subsequence-ii"]),

("Phase 12", "Backtracking and bits", 3,
 "0046 is your only backtracking problem, so make it count - the undo step is "
 "the whole discipline. The bit problems are short but the counting argument "
 "in 1863 is worth deriving rather than accepting.",
 ["leetcode/0046-permutations","leetcode/0136-single-number",
  "leetcode/1863-sum-of-all-subset-xor-totals"]),

("Phase 13", "Math, strings and simulation", 9,
 "The leftovers, and mostly specification-reading exercises. 0007 and 0008 "
 "are really overflow problems; treat them as such.",
 ["leetcode/0009-palindrome-number","leetcode/0007-reverse-integer",
  "leetcode/0008-string-to-integer-atoi","leetcode/0013-roman-to-integer",
  "leetcode/0012-integer-to-roman","leetcode/0014-longest-common-prefix",
  "leetcode/0028-find-the-index-of-the-first-occurrence-in-a-string",
  "leetcode/0006-zigzag-conversion","leetcode/0048-rotate-image"]),

("Phase 14", "The two hard ones left", 2,
 "Save these. 0005 is expand-around-centre with fiddly index recovery. 0004 "
 "is the single biggest gap in the archive - you solved it by sorting, which "
 "ignores the only reason it exists. Do it with the partition binary search.",
 ["leetcode/0005-longest-palindromic-substring","leetcode/0004-median-of-two-sorted-arrays"]),
]

def pid(d):
    m = re.match(r"^(\d+)", pathlib.Path(d).name)
    return m.group(1) if m else ""

def title(d):
    p = R / d / "README.md"
    return p.read_text().splitlines()[0].lstrip("# ").strip()

lines = []
A = lines.append
A("# Roadmap")
A("")
A("A recommended order for the 117 solvable problems. Pattern-first, not")
A("number-first: each phase installs one idea and the next depends on it.")
A("")
A("Tick a box when you have solved it **without** reading past the card's")
A("`## Task` section. Reading `## Key insight` first is fine - it just means")
A("the problem counts as study, not as a rep.")
A("")
A("`*` marks a problem worth redoing carefully. `(never solved)` means it was")
A("a `TODO` scaffold in the old Kotlin lab and you have no prior attempt.")
A("")

total = 0
for name, heading, _, why, items in PHASES:
    A(f"## {name} - {heading}")
    A("")
    A(f"*{len(items)} problems*")
    A("")
    for w in [why]:
        A(w)
    A("")
    for d in items:
        mark = ""
        if d in NEVER: mark = "  `(never solved)`"
        elif d in REDO: mark = f"  `*` {REDO[d]}"
        done = " already solved, ported from your C++" if d == "leetcode/0001-two-sum" else ""
        A(f"- [ ] [`{d}`](./{d}/){mark}{done}")
    A("")
    total += len(items)

A("---")
A("")
A(f"**{total} problems.** One (`leetcode/2884-modify-columns`) is a Pandas")
A("problem with no Java form and is not in this list.")
A("")
A("## The short version")
A("")
A("If you only do eighteen problems, do these. Fourteen are ones where your")
A("old solution passed but sidestepped the lesson; four you never solved at")
A("all. This is the highest-value work in the repo.")
A("")
listed_all = [x for _,_,_,_,its in PHASES for x in its]
for d, why in sorted(REDO.items()):
    assert d in listed_all, f"redo path not in roadmap: {d}"
    A(f"- [ ] [`{d}`](./{d}/) - {why}")
for d in sorted(NEVER):
    assert d in listed_all, f"never path not in roadmap: {d}"
    A(f"- [ ] [`{d}`](./{d}/) - never solved")
A("")
A("## How to use the Review line")
A("")
A("Every card ends with:")
A("")
A("```")
A("last: never   confidence: 0/5")
A("```")
A("")
A("Set the date and a confidence when you solve it. Then revisit anything at")
A("3 or below after a week, and anything at 1 or 2 after two days. That is the")
A("whole spaced-repetition system - the cards exist to make a revisit cost two")
A("minutes instead of twenty.")
A("")
A("A problem you re-solve correctly from a cold start is worth more than three")
A("you read the solution to.")
A("")
A("## One honest caveat")
A("")
A("This archive is interview-style DSA, not competitive programming. The two")
A("overlap in fundamentals and diverge after that: contests want speed under")
A("time pressure, problems stated as stories, and topics barely represented")
A("here - number theory, graphs, geometry, combinatorics. There is not a single")
A("graph traversal in these 117 problems.")
A("")
A("So run a second track in parallel. Do Codeforces Div. 2 A and B on the")
A("actual clock, starting now rather than after Phase 14. This repo builds the")
A("foundation; contests build the thing you said you wanted. Neither substitutes")
A("for the other.")
A("")

(R / "ROADMAP.md").write_text("\n".join(lines))
print(f"ROADMAP.md written: {total} problems across {len(PHASES)} phases")
print(f"flagged: {len(REDO)} redo + {len(NEVER)} never = {len(REDO)+len(NEVER)}")

# sanity: every solvable problem appears exactly once
allp = {str(p.parent.relative_to(R)) for p in R.glob("*/*/README.md")}
allp.discard("leetcode/2884-modify-columns")
listed = [x for _,_,_,_,its in PHASES for x in its]
assert len(listed) == len(set(listed)), "DUPLICATE in roadmap"
missing = allp - set(listed)
extra = set(listed) - allp
assert not missing, f"MISSING: {sorted(missing)}"
assert not extra, f"BAD PATH: {sorted(extra)}"
print("verified: all 117 covered exactly once, all paths exist")
