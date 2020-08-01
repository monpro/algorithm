package strings;

import java.util.*;

class Solution {
    public String arrangeWords(String text) {
        TreeMap<Integer, List<String>> map = new TreeMap<>();
        String[] strings = text.toLowerCase().split(" ");
        Arrays.sort(strings, (s1, s2) -> s1.length() - s2.length());
        StringBuilder result = new StringBuilder();
        for(String string: strings) {
            result.append(string).append(" ");
        }
        
        result.setCharAt(0, Character.toUpperCase(result.charAt(0)));
        return result.toString().trim();
        /**
        for(String string: strings) {
            map.putIfAbsent(string.length(), new ArrayList<>());
            map.get(string.length()).add(string);
        }
        
        StringBuilder result = new StringBuilder();
        
        for(int i: map.keySet()) {
            for(String word: map.get(i)) {
                result.append(word).append(" ");
            }
        }
        
        result.setCharAt(0, Character.toUpperCase(result.charAt(0)));
        return result.toString().trim();
        **/
    }
}