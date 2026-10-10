import java.util.*;

class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        var answer = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            var count = 0;
            for(int j = 0; j < nums.length; j++){
                if(i != j && nums[i] > nums[j]) count += 1;
            }
            answer[i] = count;
        }
        return answer;
    }
}
