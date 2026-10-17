package leetcode

import "testing"

func TestSumCounts(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{name: "example", nums: []int{1, 2, 1}, want: 15},
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
