package leetcode

import "testing"

func TestNewPalindrome(t *testing.T) {
	tests := []struct {
		name string
		input string
		want bool
	}{
		{name: "skip trailing punctuation", input: "a,", want: true},
		{name: "all punctuation", input: ".,", want: true},
		{name: "canonical palindrome", input: "A man, a plan, a canal: Panama", want: true},
		{name: "not a palindrome", input: "race a car", want: false},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			if got := isPalindrome(test.input); got != test.want {
				t.Errorf("isPalindrome(%q) = %t, want %t", test.input, got, test.want)
			}
		})
	}
}
