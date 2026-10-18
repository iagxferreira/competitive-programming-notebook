#include <cstddef>
#include <vector>

class Solution {
public:
  std::vector<int> productExceptSelf(std::vector<int> &nums) {
    std::vector<int> answer(nums.size(), 1);

    int prefix = 1;
    for (std::size_t i = 0; i < nums.size(); i++) {
      answer[i] = prefix;
      prefix *= nums[i];
    }

    int suffix = 1;
    for (std::size_t i = nums.size(); i > 0; i--) {
      answer[i - 1] *= suffix;
      suffix *= nums[i - 1];
    }

    return answer;
  }
};
