import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        var seen = new int[128];
        Arrays.fill(seen, -1);
        var left = 0; var max = 0;

        for(int right = 0; right < s.length(); right++){
            var value = s.charAt(right);
            if(seen[value] >= left){
                left = seen[value] + 1;
            }
            seen[value] = right;
            max = Math.max(max, right - left + 1);
        }
        return max;
    }
}
