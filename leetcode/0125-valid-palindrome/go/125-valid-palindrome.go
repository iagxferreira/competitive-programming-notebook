package leetcode

import "strings"

func isValidChar(value string) bool {
	if (value >= "A" && value <= "Z") || (value >= "a" && value <= "z") || (value >= "0" && value <= "9") {
		return true
	}
	return false
}

func isPalindrome(s string) bool {
	for left, right := 0, len(s)-1; left <= right; {
		if !isValidChar(string(s[left])) {
			left++
			continue
		}

		if !isValidChar(string(s[right])) {
			right--
			continue
		}

		if !strings.EqualFold(string(s[left]), string(s[right])) {
			return false
		}

		left++
		right--
	}

	return true
}
