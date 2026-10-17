package leetcode

func sumCounts(nums []int) int {
	result := 0

	for left := range nums {
		seen := make(map[int]bool)
		for right := left; right < len(nums); right++ {
			seen[nums[right]] = true
			distinct := len(seen)
			result += distinct * distinct
		}
	}

	return result
}
