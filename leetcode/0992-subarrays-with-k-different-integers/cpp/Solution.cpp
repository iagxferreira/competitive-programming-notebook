// 992. Subarrays with K Different Integers
// sliding window (exactly-k trick: exactly(k) = atMost(k) - atMost(k-1))
// TODO: solve

#include <unordered_map>
#include <vector>

class Solution {
private:
  int atMost(const std::vector<int> &nums, int limit) {
    std::unordered_map<int, int> freq;
    int left = 0, answer = 0;
    for (int right = 0; right < (int)nums.size(); ++right) {
      ++freq[nums[right]];
      while ((int)freq.size() > limit) {
        if (--freq[nums[left]] == 0)
          freq.erase(nums[left]);
        ++left;
      }
      answer += right - left + 1;
    }
    return answer;
  };

public:
  int subarraysWithKDistinct(std::vector<int> &nums, int k) {
    return atMost(nums, k) - atMost(nums, k - 1);
  }
};
