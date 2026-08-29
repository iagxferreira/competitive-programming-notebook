import java.util.*;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(ransomNote.length() > magazine.length()) return false;
        var counter = new int[128];

        for(var letter :  magazine.toCharArray()){
            ++counter[letter];
        }

        for(var letter :  ransomNote.toCharArray()){
            if(--counter[letter]<0) return false;
        }

        return true;
    }
}
