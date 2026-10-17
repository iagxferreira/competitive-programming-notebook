package leetcode

import "testing"

func TestMinSwaps(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{name: "already sorted", nums: []int{1, 2, 3}, want: 0},
		{name: "two swaps", nums: []int{13, 10, 21}, want: 2},
		{name: "one cycle", nums: []int{22, 14, 3}, want: 2},
		{name: "single element", nums: []int{42}, want: 0},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			if got := minSwaps(test.nums); got != test.want {
				t.Errorf("minSwaps(%v) = %d, want %d", test.nums, got, test.want)
			}
		})
	}
}
