# 231A. Team

codeforces | 800 | implementation, io

## Task

Three friends each say whether they are sure about a problem. They
implement it if at least two are sure. Count such problems.

## Key insight

Read three ints per line, count the lines whose sum is >= 2. The whole
exercise is reading n lines of three tokens cleanly with the fast
reader.

## Invariant

None.

## Complexity

time O(n)   space O(1)

## Pitfall

Nothing algorithmic - this is an I/O rep. Do it with
BufferedReader + StringTokenizer and no Scanner, so the template becomes
automatic before a problem depends on it.

## Review

last: never   confidence: 0/5
