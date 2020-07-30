package heap;

import java.util.*;

class FreqNumber {
    int num;
    int freq;
    
    public FreqNumber(int num, int freq) {
        this.num = num;
        this.freq = freq;
    }
}

class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num: arr){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        PriorityQueue<FreqNumber> heap = new PriorityQueue<FreqNumber>((n1, n2) -> n1.freq - n2.freq);
        
        map.forEach((key, val) -> heap.add(new FreqNumber(key, val)));
        
        while(k > 0){
            k -= heap.poll().freq;
            
        }

        return k < 0 ? heap.size() + 1: heap.size();
        
    }
}