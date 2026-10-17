#include <cstddef>
#include <utility>
#include <vector>

class Solution {
  public:
    void moveZeroes(std::vector<int>& nums){
      std::size_t fast = 0;
      for (std::size_t slow = 0; slow < nums.size(); slow++) {
        if(nums[slow] != 0){
          std::swap(nums[slow], nums[fast]);
          fast++;
        }
      }
    }
};
