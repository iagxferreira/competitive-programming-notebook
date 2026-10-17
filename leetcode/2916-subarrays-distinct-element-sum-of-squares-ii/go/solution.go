package leetcode

// MOD keeps the answer within the limit required by LeetCode.
const MOD int64 = 1_000_000_007

// FenwickTree is a helper that can quickly add a value to a whole range
// and quickly find the sum of a range. It uses two internal trees (b1, b2)
// to do both jobs efficiently.
type FenwickTree struct {
	n      int
	b1, b2 []int64
}

// Make an empty helper that can store n positions.
func newFenwickTree(n int) *FenwickTree {
	return &FenwickTree{
		n:  n,
		b1: make([]int64, n+1),
		b2: make([]int64, n+1),
	}
}

// Add val to one position in one of the helper's internal trees.
func (f *FenwickTree) add(bit []int64, idx int, val int64) {
	for i := idx; i <= f.n; i += i & -i {
		bit[i] += val
	}
}

// Record one change in both internal trees.
func (f *FenwickTree) update(i int, val int64) {
	f.add(f.b1, i, val)
	f.add(f.b2, i, int64(i-1)*val)
}

// Add val to every position from l through r (positions start at 1).
// The second update marks where this range change should stop.
func (f *FenwickTree) rangeAdd(l, r int, val int64) {
	f.update(l, val)
	f.update(r+1, -val)
}

// Add up the pieces in one internal tree that are needed for positions 1..idx.
func (f *FenwickTree) query(bit []int64, idx int) int64 {
	var sum int64
	for i := idx; i > 0; i -= i & -i {
		sum += bit[i]
	}
	return sum
}

// Find the sum of all values from position 1 through i.
func (f *FenwickTree) prefixSum(i int) int64 {
	s1 := f.query(f.b1, i)
	s2 := f.query(f.b2, i)
	return int64(i)*s1 - s2
}

// Find the sum of all values from position l through r.
func (f *FenwickTree) rangeSum(l, r int) int64 {
	return f.prefixSum(r) - f.prefixSum(l-1)
}

func sumCounts(nums []int) int {
	n := len(nums)
	fw := newFenwickTree(n)

	// Remember the most recent position where each number appeared.
	last := make(map[int]int)

	// sq is the sum of squared distinct counts for subarrays ending here.
	// ans is the total answer for all subarrays seen so far.
	var sq, ans int64

	for r, x := range nums {
		p, seen := last[x]
		if !seen {
			// Pretend a never-seen number appeared just before the array began.
			p = -1
		}

		// Only subarrays starting after x's previous appearance gain a new
		// distinct number. Convert their positions to 1-based Fenwick indices.
		l, right := p+2, r+1

		// These are the old distinct counts in the affected subarrays.
		oldSum := fw.rangeSum(l, right)
		length := int64(right - l + 1)

		// Each affected count d becomes d+1, whose square grows by 2*d+1:
		// (d+1)^2 - d^2 = 2*d + 1. Add that growth to sq.
		sq = (sq + 2*oldSum + length) % MOD

		// Save the increased distinct counts for the next array position.
		fw.rangeAdd(l, right, 1)

		// All subarrays ending at r now contribute to the final answer.
		ans = (ans + sq) % MOD
		last[x] = r
	}

	return int(ans)
}
