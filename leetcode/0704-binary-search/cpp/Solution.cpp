#include <cstddef>
#include <vector>

class Solution {
public:
  int search(std::vector<int> &nums, int target) {
    std::size_t low = 0;
    std::size_t high = nums.size();
    while (low < high) {
      const std::size_t mid = low + (high - low) / 2;
      if (nums[mid] == target)
        return static_cast<int>(mid);

      if (nums[mid] < target) {
        low = mid + 1;
        continue;
      }

      high = mid;
    }

    return -1;
  }
};
