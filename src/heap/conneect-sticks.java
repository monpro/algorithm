package heap;

import java.util.*;

class Solution {
    public int connectSticks(int[] sticks) {
        Queue<Integer> queue = new PriorityQueue<>();
        
        for(int num: sticks){
            queue.offer(num);
        }
        
        int result = 0;
        while(queue.size() > 1){
            int first = queue.poll(), second = queue.poll();
            result += first + second;
            queue.offer(first + second);
        }
        
        return result;
    }
}