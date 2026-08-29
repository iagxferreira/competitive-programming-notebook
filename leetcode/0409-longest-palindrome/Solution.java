import java.util.*;

class Solution {
    public int longestPalindrome(String s) {
        Set<Character>set = new HashSet<>();
        var n = 0;
        for(int i = 0; i <s.length(); i++){
            var ch = s.charAt(i);

            if (set.contains(ch)){
               n++;
              set.remove(ch);
            }else {
                set.add(ch);
            }
        }
        return n * 2 == s.length() ? n* 2 : n*2 + 1;
    }
}
