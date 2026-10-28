// 1695. Maximum Erasure Value
// sliding window (hard shrink-on-duplicate)
// TODO: solve

#include <unordered_set>
#include <vector>

class Solution {
public:
  int maximumUniqueSubarray(std::vector<int> &nums) {
    int result = 0;
    std::unordered_set<int> seen;
    for (int i = 0, j = 0, win = 0; j < nums.size(); j++) {
      while (seen.find(nums[j]) != seen.end()) {
        seen.erase(nums[i]);
        win -= nums[i];
        i++;
      }

      seen.insert(nums[j]);
      win += nums[j];
      result = std::max(result, win);
    }
    return result;
  }
};
