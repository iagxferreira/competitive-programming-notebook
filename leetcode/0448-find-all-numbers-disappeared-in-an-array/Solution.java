import java.util.*;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> present = new HashSet<>();
        for (int value: nums) present.add(value);

        List<Integer> answer = new ArrayList<>();
        for(int i = 1; i <= nums.length; i++){
            if(!present.contains(i))
                answer.add(i);
        }
        return answer;
    }
}
