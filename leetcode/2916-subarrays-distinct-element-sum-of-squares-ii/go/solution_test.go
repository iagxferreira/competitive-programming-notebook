package leetcode

import "testing"

func TestSumCounts(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{name: "example", nums: []int{1, 2, 1}, want: 15},
		{name: "all distinct", nums: []int{1, 2, 3}, want: 20},
		{name: "repeated values", nums: []int{2, 2}, want: 3},
		{name: "empty", nums: []int{}, want: 0},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			if got := sumCounts(test.nums); got != test.want {
				t.Errorf("sumCounts(%v) = %d, want %d", test.nums, got, test.want)
			}
		})
	}
}

func TestSumCountsAgainstBruteForce(t *testing.T) {
	for length := 0; length <= 6; length++ {
		for mask := 0; mask < 1<<length; mask++ {
			nums := make([]int, length)
			for i := range nums {
				nums[i] = (mask >> i) & 1
			}
			if got, want := sumCounts(nums), bruteSumCounts(nums); got != want {
				t.Fatalf("sumCounts(%v) = %d, want %d", nums, got, want)
			}
		}
	}
}

func bruteSumCounts(nums []int) int {
	var total int
	for left := range nums {
		seen := make(map[int]struct{})
		for right := left; right < len(nums); right++ {
			seen[nums[right]] = struct{}{}
			total = (total + len(seen)*len(seen)) % int(MOD)
		}
	}
	return total
}
