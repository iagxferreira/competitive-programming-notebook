#include <algorithm>
#include <cstdlib>
#include <utility>
#include <vector>

class Solution {
public:
  std::vector<int> sortArray(std::vector<int> &nums) {
    radixSort(nums);
    return nums;
  }

private:
  void radixCountingSort(std::vector<int> &nums, int factor) {
    int frequenceSize = 10, size = nums.size();
    std::vector<int> frequence(frequenceSize, 0), sorted(size, 0);

    for (int ind = 0; ind < size; ind++)
      frequence[getDigit(nums[ind], factor)]++;

    for (int ind = 1; ind < frequenceSize; ind++)
      frequence[ind] += frequence[ind - 1];

    for (int ind = size - 1; ind >= 0; ind--)
      sorted[frequence[getDigit(nums[ind], factor)]-- - 1] = nums[ind];
    nums = sorted;
  }

  void radixSort(std::vector<int> &nums) {
    if (nums.empty())
      return;

    int minValue = *std::min_element(nums.begin(), nums.end());

    for (auto &num : nums)
      num -= minValue;

    int factor = 1, maxValue = *std::max_element(nums.begin(), nums.end());

    while (maxValue / factor) {
      radixCountingSort(nums, factor);
      factor *= 10;
    }

    for (auto &num : nums)
      num += minValue;
  }

  int getDigit(int num, int factor) {
    return (std::abs(num) / std::abs(factor)) % 10;
  }
};
