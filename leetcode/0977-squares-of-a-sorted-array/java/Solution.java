import java.util.*;

class Solution {
    public int[] sortedSquares(int[] nums) {
        var answer = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            answer[i] = nums[i] * nums[i];
        }
        Arrays.sort(answer);
        return answer;
    }
}
