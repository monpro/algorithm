import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

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
}