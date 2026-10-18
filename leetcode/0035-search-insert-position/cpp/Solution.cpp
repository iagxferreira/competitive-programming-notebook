#include <cstddef>
#include <iterator>
#include <vector>

class Solution {
public:
  int searchInsert(std::vector<int> &nums, int target) {
    std::size_t low = 0;
    std::size_t high = nums.size();

    while (low < high) {
      std::size_t mid = low + (high - low) / 2;
      if (nums[mid] < target) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }

    return static_cast<int>(low);
  }
};
