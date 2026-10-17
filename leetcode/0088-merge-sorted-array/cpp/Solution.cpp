#include <algorithm>
#include <cstddef>
#include <vector>

class Solution {
public:
  void merge(std::vector<int> &nums1, int m, std::vector<int> &nums2, int n) {
    for (std::size_t i = m, j = 0; j < n; j++) {
      nums1[i] = nums2[j];
      i++;
    }
    std::sort(nums1.begin(), nums1.end());
  }
};
