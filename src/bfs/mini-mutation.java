package bfs;

import java.util.*;

class Solution {
    public int minMutation(String start, String end, String[] bank) {
       if(start.equals(end)){
           return 0;
       }
        int result = 0;
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        Set<String> banks = new HashSet<>();
        for(String string: bank){
            banks.add(string);
        }
        char[] candidate = new char[]{'A', 'C', 'G', 'T'};
        queue.offer(start);
        visited.add(start);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                String string = queue.poll();
                if(string.equals(end)){
                    return result;
                }
                char[] chars = string.toCharArray();
                for(int j = 0; j < chars.length; j++){
                    char original = chars[j];
                    for(char ch: candidate){
                        chars[j] = ch;
                        String cdString = new String(chars);
                        if(banks.contains(cdString) && !visited.contains(cdString)){
                            visited.add(cdString);
                            queue.offer(cdString);
                        }
                    }
                    
                    
                    chars[j] = original;
                }
            }
            result += 1;
        } 
        return -1;
    }
}