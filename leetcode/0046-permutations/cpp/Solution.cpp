#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> permute(std::vector<int> &nums) {
    std::vector<std::vector<int>> answer;
    if (nums.size() == 1) {
      std::vector<int> list;
      list.push_back(nums[0]);
      answer.push_back(list);
      return answer;
    }

    for (int i = 0; i < nums.size(); i++) {
      int n = nums[i];
      std::vector<int> remaining;
      for (int j = 0; j < nums.size(); j++) {
        if (j != i) {
          remaining.push_back(nums[j]);
        }
      }

      std::vector<std::vector<int>> permutations = permute(remaining);
      for (std::vector<int> p : permutations) {
        p.insert(p.begin(), n);
        answer.push_back(p);
      }
    }

    return answer;
  }
};
