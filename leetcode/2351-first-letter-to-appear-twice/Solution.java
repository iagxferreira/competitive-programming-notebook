import java.util.*;

class Solution {
    public char repeatedCharacter(String s) {
        var seen = new boolean[26];
        for(var c: s.toCharArray()){
            if(seen[c-'a']) return c;
            seen[c-'a'] = true;
        }
        return 'a';
    }
}
