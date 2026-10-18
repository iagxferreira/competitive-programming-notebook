#include <algorithm>
#include <cstddef>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>>
  merge(std::vector<std::vector<int>> &intervals) {
    std::sort(intervals.begin(), intervals.end());
    std::vector<std::vector<int>> merged;
    std::vector<int> prev = intervals[0];

    for (std::size_t i = 1; i < intervals.size(); i++) {
      if (intervals[i][0] <= prev[1]) {
        prev[1] = std::max(prev[1], intervals[i][1]);
        continue;
      }

      merged.push_back(prev);
      prev = intervals[i];
    }
    merged.push_back(prev);

    return merged;
  }
};
