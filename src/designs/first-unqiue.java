package designs;

import java.util.*;

class FirstUnique {
    Queue<Integer> queue = new LinkedList<>();
    Map<Integer, Integer> map = new HashMap<>();
    public FirstUnique(int[] nums) {
        for(int num: nums){
            add(num);
        }
    }
    
    public int showFirstUnique() {
        while(!queue.isEmpty() && map.get(queue.peek()) > 1){
            queue.poll();
        }
        return queue.isEmpty() ? -1: queue.peek();
    }
    
    public void add(int value) {
        map.put(value, map.getOrDefault(value, 0) + 1);
        queue.add(value);
    }
}
