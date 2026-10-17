#include <vector>

class Solution {
public:
  void merge(std::vector<int> &first, int firstLimit, std::vector<int> &second,
             int secondLimit) {
    int left = firstLimit - 1;
    int right = secondLimit - 1;
    int write = firstLimit + secondLimit - 1;
    while (right >= 0) {
      if (left >= 0 && first[left] > second[right]) {
        first[write] = first[left];
        left--;
        write--;
        continue;
      }

      first[write] = second[right];
      right--;
      write--;
    }
  }
};
