import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        var left = 0;
        var max = 0;
        var seen = new HashSet<Character>();

        for(int right = 0; right < s.length(); right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(s.charAt(right));
            max = Math.max(max, right - left + 1);
        }
        return max;
    }
}
