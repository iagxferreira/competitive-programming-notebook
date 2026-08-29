#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int current = nums[i];
            int needed = target - current;
            if (seen.find(needed) != seen.end()) {
                return {seen[needed], i};
            }
            seen[current] = i;
        }
        return {};
    }
};
