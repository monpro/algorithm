package dps;

import java.util.*;

class Solution {
    public int longestStrChain(String[] words) {
        Map<String, Integer> dps = new HashMap<>();
        Arrays.sort(words, (w1, w2) -> w1.length() - w2.length());
        int result = 0;
        for(String word: words){
            int value = 0;
            for(int i = 0; i < word.length(); i++){
                String string = word.substring(0, i) + word.substring(i + 1);
                value = Math.max(value, dps.getOrDefault(string, 0) + 1);
            }
            dps.put(word, value);
            result = Math.max(value, result);
        }
        
        return result;
    }
}