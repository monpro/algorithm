package strings;

import java.util.*;

class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        Map<String, List<String>> group = new HashMap<>();
        
        if(strings.length == 0){
            return new ArrayList<>();
        }
        
        for(String string: strings){
            char base = string.charAt(0);
            int offset = base - 'a';
            
            StringBuilder build = new StringBuilder();
            for(int i = 0; i < string.length(); i++){
                char ch = string.charAt(i);
                ch = (char)(ch - offset);
                if(ch < 'a'){
                    ch += 26;
                }
                build.append(ch);
            }
            String key = build.toString();
            group.putIfAbsent(key, new ArrayList<>());
            group.get(key).add(string);
        }
        
       return new ArrayList<>(group.values());
        
    }
}