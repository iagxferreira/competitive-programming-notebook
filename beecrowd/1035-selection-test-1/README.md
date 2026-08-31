# 1035. Selection Test 1

beecrowd | trivial | conditionals, io

## Task

Read four integers A B C D and print whether they satisfy a compound
condition given in the statement.

## Key insight

A single `if` with several `&&` clauses. The exercise is transcribing a
specification into boolean logic without dropping a clause.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Every clause matters, including the easily skipped "B > C", "D > A",
"C + D > A + B", "C and D both positive" and "A is even". Read the list
twice and check them off - a dropped clause passes the sample and fails
the tests, with no hint which one it was.

## Review

last: never   confidence: 0/5
