package heap;

import java.util.*;

class Solution {
    public String frequencySort(String s) {
        // priorityQueue
        PriorityQueue<Map.Entry<Character, Integer>>maxHeap = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        Map<Character, Integer> map = new HashMap<>();
        
        StringBuilder result = new StringBuilder();
        for(char c: s.toCharArray())
            map.put(c, map.getOrDefault(c, 0) + 1);
        
        maxHeap.addAll(map.entrySet());
        while(!maxHeap.isEmpty()){
            Map.Entry e = maxHeap.poll();
            for(int i = 0; i < (int)e.getValue(); i++)
                result.append(e.getKey());
        }
        
        return result.toString();  
    }

    public String frequencySortBucketSort(String s) {
        // bucket sort
        int[] count = new int[256];
        int maxCount = 0;
        for(char c: s.toCharArray()){
            count[c] += 1;
            maxCount = Math.max(count[c], maxCount);
        }
        ArrayList<Character>[] bucket = new ArrayList[maxCount + 1];
        
        for(int i = 255; i >= 0; i--){
            if(count[i] == 0)
                continue;
            if(bucket[count[i]] == null)
                bucket[count[i]] = new ArrayList<>();
            bucket[count[i]].add((char)i);
        }
            
        StringBuilder result = new StringBuilder();
        for(int i = maxCount; i > 0; i--){
            if(bucket[i] == null) continue;
            for(char c: bucket[i]){
                for(int j = 0; j < i; j++){
                    result.append(c);
                }
            }
        }
        return result.toString();
    }
}