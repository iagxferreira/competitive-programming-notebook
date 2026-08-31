import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs == null || strs.length == 0) return new ArrayList<>();
        Map<String, List<String>> seen = new HashMap<>();
        for(String s: strs){
            char[] arr = s.toCharArray();
            Arrays.sort(arr);
            var sorted = String.valueOf(arr);
            if(!seen.containsKey(sorted)) seen.put(sorted, new ArrayList<>());
            seen.get(sorted).add(s);
        }
        return new ArrayList<>(seen.values());
    }
}
