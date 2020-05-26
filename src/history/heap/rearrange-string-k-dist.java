package history.heap;

import java.util.*;

class RearrangeStringKDistanceApart {

  public static String reorganizeString(String str, int k) {
    if(k <= 1){
        return str;
    }
    Map<Character, Integer> count = new HashMap<>();
    for(char ch: str.toCharArray()){
        count.put(ch, count.getOrDefault(ch, 0) + 1);
    }
    PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<>((e1, e2) -> e2.getValue() - e1.getValue());

    maxHeap.addAll(count.entrySet());
    Queue<Map.Entry<Character, Integer>> queue = new LinkedList<>();

    StringBuilder result = new StringBuilder(str.length());

    while(!maxHeap.isEmpty()){
        Map.Entry<Character, Integer> entry = maxHeap.poll();
        result.append(entry.getKey());
        entry.setValue(entry.getValue() - 1);

        queue.offer(entry);

        if(queue.size() == k){
            Map.Entry<Character, Integer> entryFromQueue = queue.poll();
            if(entryFromQueue.getValue() > 0){
                maxHeap.add(entryFromQueue);
            }
        }
    }

    return result.length() == str.length() ? result.toString(): "";
  }

  public static void main(String[] args) {
    System.out.println("Reorganized string: " + 
            RearrangeStringKDistanceApart.reorganizeString("mmpp", 2));
    System.out.println("Reorganized string: " + 
            RearrangeStringKDistanceApart.reorganizeString("Programming", 3));
    System.out.println("Reorganized string: " + 
            RearrangeStringKDistanceApart.reorganizeString("aab", 2));
    System.out.println("Reorganized string: " + 
            RearrangeStringKDistanceApart.reorganizeString("aappa", 3));
  }
}