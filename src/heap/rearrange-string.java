package heap;

import java.util.*;

class RearrangeString {

  public static String rearrangeString(String str) {
    Map<Character, Integer> count = new HashMap<>();
    for(char ch: str.toCharArray()){
      count.put(ch, count.getOrDefault(ch, 0) + 1);
    }

    PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<>((e1, e2) -> e2.getValue() - e1.getValue());

    for(Map.Entry<Character, Integer> entry: count.entrySet()){
      maxHeap.add(entry);
    }

    StringBuilder result = new StringBuilder();
    Map.Entry<Character, Integer> previous = null;
    while(!maxHeap.isEmpty()){
      Map.Entry<Character, Integer> current = maxHeap.poll();
      if(previous != null && previous.getValue() > 0){
        maxHeap.offer(previous);
      }
      result.append(current.getKey());
      current.setValue(current.getValue() - 1);
      previous = current;
    }
    return result.toString();
  }

  public static void main(String[] args) {
    System.out.println("Rearranged string: " + RearrangeString.rearrangeString("aappp"));
    System.out.println("Rearranged string: " + RearrangeString.rearrangeString("Programming"));
    System.out.println("Rearranged string: " + RearrangeString.rearrangeString("aapa"));
  }
}