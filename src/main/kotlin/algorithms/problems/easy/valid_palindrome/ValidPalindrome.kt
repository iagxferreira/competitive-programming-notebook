package algorithms.problems.easy.valid_palindrome

fun isPalindrome(s: String): Boolean {
    if (s.isEmpty()) {
        return true
    }
    var left = 0
    var right = s.lastIndex

    while (left < right) {
        while (left < right && !s[left].isLetterOrDigit()) {
            left++
        }

        while (left < right && !s[right].isLetterOrDigit()) {
            right--
        }

        if (s[left].lowercaseChar() != s[right].lowercaseChar()) {
            return false
        }

        left++
        right--
    }
    return true
}
