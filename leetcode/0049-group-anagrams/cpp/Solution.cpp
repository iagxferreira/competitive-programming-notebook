#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<std::vector<std::string>>
  groupAnagrams(std::vector<std::string> &strs) {
    std::unordered_map<std::string, std::vector<std::string>> answer;
    for (std::string &s : strs) {
      std::string key = s;
      std::sort(key.begin(), key.end());
      answer[key].push_back(s);
    }

    std::vector<std::vector<std::string>> result;
    for (const auto &entry : answer) {
      result.push_back(entry.second);
    }

    return result;
  }
};
