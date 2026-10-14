package leetcode

func isValid(s string) bool {
	if len(s) == 0 || len(s)%2 == 1 {
		return false
	}

	pairs := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}

	stack := []rune{}

	for _, value := range s {
		if _, ok := pairs[value]; ok {
			stack = append(stack, value)
			continue
		}

		if len(stack) == 0 || pairs[stack[len(stack)-1]] != value {
			return false
		}

		stack = stack[:len(stack)-1]
	}
	return len(stack) == 0
}
