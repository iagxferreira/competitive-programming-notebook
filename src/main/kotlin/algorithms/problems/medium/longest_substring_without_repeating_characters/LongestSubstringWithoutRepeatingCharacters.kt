package algorithms.problems.medium.longest_substring_without_repeating_characters

fun lengthOfLongestSubstring(s: String): Int {
    val lastIndex = IntArray(128)
    var left = 0
    var best = 0

    for (right in s.indices) {
        val current = s[right].code

        if (lastIndex[current] > left) {
            left = lastIndex[current]
        }

        best = maxOf(best, right - left + 1)
        lastIndex[current] = right + 1
    }

    return best
}
