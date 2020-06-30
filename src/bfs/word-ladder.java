package bfs;

import java.util.*;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        int result = 0;
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer(beginWord);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            result += 1;
            for(int i = 0; i < size; i++){
                String word = queue.poll();
                if(word.equals(endWord)){
                    return result;
                }
                for(String string: wordList){
                    if(!visited.contains(string)){
                        if(countWordDiff(word, string) == 1){
                            visited.add(string);
                            queue.offer(string);
                        }
                    }
                }
            }
        }
        
        return 0;
    }
    
    
    public int countWordDiff(String word1, String word2){
        int diff = 0;
        char[] chars1 = word1.toCharArray();
        char[] chars2 = word2.toCharArray();
        for(int i = 0; i < chars1.length; i++){
            if(chars1[i] != chars2[i]){
                diff += 1;
            }
        }
        
        return diff;
    }
}