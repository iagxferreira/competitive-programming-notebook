#include <vector>

class Solution {
public:
  std::vector<int> targetIndices(std::vector<int> &nums, int target) {
    int less = 0, equal = 0;
    std::vector<int> answer;
    for (int x : nums) {
      if (x < target) {
        less++;
        continue;
      }
      if (x == target)
        equal++;
    }

    for (int i = 0; i < equal; i++) {
      answer.push_back(less + i);
    }

    return answer;
  }
};
