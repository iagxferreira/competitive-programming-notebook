package algorithms.problems.easy.valid_palindrome

import org.junit.jupiter.api.Assertions.assertFalse
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

class ValidPalindromeTest {
    @Test
    fun `returns true for the classic palindrome`() {
        assertTrue(isPalindrome("A man, a plan, a canal: Panama"))
    }

    @Test
    fun `returns false when the normalized characters differ`() {
        assertFalse(isPalindrome("race a car"))
    }

    @Test
    fun `returns true for an empty string`() {
        assertTrue(isPalindrome(""))
    }

    @Test
    fun `returns true for a single character`() {
        assertTrue(isPalindrome("a"))
    }

    @Test
    fun `returns false for mixed letters and digits that do not mirror`() {
        assertFalse(isPalindrome("0P"))
    }
}
