package heap;

import java.util.*;

class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        Map<Character, Queue<String>> map = new HashMap<>();
        for(char ch = 'a'; ch <= 'z'; ch++){
            map.putIfAbsent(ch, new LinkedList<>());
        }
        
        for(String word: words){
            map.get(word.charAt(0)).add(word);
        }
        
        int result = 0;
        
        for(char c: S.toCharArray()){
            Queue<String> queue = map.get(c);
            int size = queue.size();
            for(int i = 0; i < size; i++){
                String word = queue.poll();
                if(word.length() == 1){
                    result += 1;
                }else{
                    map.get(word.charAt(1)).add(word.substring(1));
                }
            }
        }
        return result;
    }
}