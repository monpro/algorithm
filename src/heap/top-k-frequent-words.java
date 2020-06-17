package heap;

import java.util.*;


class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        List<String> result = new ArrayList<>();
        Map<String, Integer> count = new HashMap<>();
        for(String word: words)
            count.put(word, count.getOrDefault(word, 0) + 1);
        
        PriorityQueue<String> maxHeap = new PriorityQueue<>((s1, s2) -> {
            if(count.get(s2) == count.get(s1))
                return s1.compareTo(s2);
            return count.get(s2) - count.get(s1);
        });
        
        for(String word: count.keySet()){
            maxHeap.offer(word);
        }
        
        for(int i = 0; i < k; i++)
            result.add(maxHeap.poll());
        return result;
        
    }
}