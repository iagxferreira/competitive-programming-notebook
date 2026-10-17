#include <algorithm>
#include <cstddef>
#include <string>
#include <vector>

class Solution {
public:
  bool isAnagram(std::string s, std::string t) {
    if (s.length() != t.length())
      return false;

    std::vector<int> count(26, 0);

    for (std::size_t i = 0; i < s.length(); i++) {
      count[s[i] - 'a']++;
      count[t[i] - 'a']--;
    }

    return std::all_of(count.begin(), count.end(),
                       [](int value) { return value == 0; });
  }
};
