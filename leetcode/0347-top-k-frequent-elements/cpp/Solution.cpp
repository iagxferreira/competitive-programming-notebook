#include <functional>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
  std::vector<int> topKFrequent(std::vector<int> &nums, int k) {
    std::unordered_map<int, int> seen;
    std::vector<int> answer;

    for (int num : nums)
      ++seen[num];

    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        std::greater<std::pair<int, int>>>
        queue;

    for (const auto &[num, frequency] : seen) {
      std::pair<int, int> item = {frequency, num};

      if (queue.size() < k) {
        queue.push(item);
      } else if (frequency > queue.top().first) {
        queue.pop();
        queue.push(item);
      }
    }

    while (!queue.empty()) {
      answer.push_back(queue.top().second);
      queue.pop();
    }

    return answer;
  }
};
