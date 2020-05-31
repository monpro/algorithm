package history.heap;

import java.util.*;

class CompareNumber {
  int arrayIndex;
  int elementIndex;

  public CompareNumber(int arrayIndex, int elementIndex){
    this.arrayIndex = arrayIndex;
    this.elementIndex = elementIndex;
  }
}

class SmallestRange {

  public static int[] findSmallestRange(List<Integer[]> lists) {
    int currentStart = 0, currentEnd = Integer.MAX_VALUE, currentMax = Integer.MIN_VALUE;
    PriorityQueue<CompareNumber> minHeap = new PriorityQueue<>((e1, e2) -> lists.get(e1.arrayIndex)[e1.elementIndex] - lists.get(e2.arrayIndex)[e2.elementIndex]);

    for(int i = 0; i < lists.size(); i++){
      minHeap.add(new CompareNumber(i, 0));
      currentMax = Math.max(currentMax, lists.get(i)[0]);
    }

    while(minHeap.size() == lists.size()){
      CompareNumber node = minHeap.poll();

      if(currentEnd - currentStart > currentMax - lists.get(node.arrayIndex)[node.elementIndex]){
        currentStart = lists.get(node.arrayIndex)[node.elementIndex];
        currentEnd = currentMax;
      }

      if(node.elementIndex + 1 <= lists.get(node.arrayIndex).length - 1){
        node.elementIndex += 1;
        minHeap.add(node);
        currentMax = Math.max(lists.get(node.arrayIndex)[node.elementIndex], currentMax);
      }
    }

    return new int[] { currentStart, currentEnd };
  }

  public static void main(String[] args) {
    Integer[] l1 = new Integer[] { 1, 5, 8 };
    Integer[] l2 = new Integer[] { 4, 12 };
    Integer[] l3 = new Integer[] { 7, 8, 10 };
    List<Integer[]> lists = new ArrayList<Integer[]>();
    lists.add(l1);
    lists.add(l2);
    lists.add(l3);
    int[] result = SmallestRange.findSmallestRange(lists);
    System.out.print("Smallest range is: [" + result[0] + ", " + result[1] + "]");
  }
}
