#include <cctype>
#include <cstddef>
#include <string>

class Solution {
public:
  bool isPalindrome(std::string s) {
    std::size_t start = 0;
    std::size_t end = s.size() - 1;
    while (start < end) {
      if (!std::isalnum(s[start])) {
        start++;
        continue;
      }

      if (!std::isalnum(s[end])) {
        end--;
        continue;
      }

      if (std::tolower(s[start]) != std::tolower(s[end]))
        return false;

      start++;
      end--;
    }
    return true;
  }
};
