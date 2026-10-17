package leetcode

import "sort"

func minSwaps(nums []int) int {
	n := len(nums)
	sorted := make([]int, n)
	copy(sorted, nums)
	sort.Slice(sorted, func(i, j int) bool {
		sa, sb := digitSum(sorted[i]), digitSum(sorted[j])
		if sa != sb {
			return sa < sb
		}
		return sorted[i] < sorted[j]
	})

	pos := make(map[int]int)
	for i, v := range sorted {
		pos[v] = i
	}
	visited := make([]bool, n)
	cycles := 0
	for i := 0; i < n; i++ {
		if !visited[i] {
			cycles++
			j := i
			for !visited[j] {
				visited[j] = true
				j = pos[nums[j]]
			}
		}
	}
	return n - cycles
}

func digitSum(number int) int {
	sum := 0
	for number > 0 {
		sum += number % 10
		number /= 10
	}
	return sum
}
