# 2469. Convert the Temperature

leetcode | easy | math

## Task

Return [kelvin, fahrenheit] for a Celsius input.

## Key insight

kelvin = c + 273.15, fahrenheit = c * 1.80 + 32.00.

## Invariant

None.

## Complexity

time O(1)   space O(1)

## Pitfall

Use `double`, not `float` — the answer is checked to within 1e-5 and
float's ~7 significant digits are marginal at that tolerance.

Write the constants as `1.80` and `32.00`, not `9/5` — integer division
gives 1.

## Review

last: never   confidence: 0/5

## Origin

git show legacy-archive:legacy/python/leetcode/2469.convert-temperature.py
