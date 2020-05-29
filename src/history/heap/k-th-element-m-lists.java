package history.heap;

import java.util.*;

class Node{
  int arrayIndex;
  int elementIndex;

  public Node(int arrayIndex, int elementIndex){
    this.arrayIndex = arrayIndex;
    this.elementIndex = elementIndex;
  }
}
class KthSmallestInMSortedArrays {

  public static int findKthSmallest(List<Integer[]> lists, int k) {
    int index = 0;
    int val = 0;
    PriorityQueue<Node> minHeap = new PriorityQueue<>((n1, n2) -> lists.get(n1.arrayIndex)[n1.elementIndex] - lists.get(n2.arrayIndex)[n2.elementIndex]);
    for(int i = 0; i < lists.size(); i++){
      if(lists.get(i) != null){
        minHeap.add(new Node(i, 0));
      }
    }
    Node node = null;
    while(!minHeap.isEmpty()){
      node = minHeap.poll();
      val = lists.get(node.arrayIndex)[node.elementIndex];
      index += 1;
      if(index == k){
        break;
      }
      if(node.elementIndex + 1<= lists.get(node.arrayIndex).length - 1){
        node.elementIndex += 1;
        minHeap.add(node);
      }
    }
    return val;
  }

  public static void main(String[] args) {
    Integer[] l1 = new Integer[] { 2, 6, 8 };
    Integer[] l2 = new Integer[] { 3, 6, 7 };
    Integer[] l3 = new Integer[] { 1, 3, 4 };
    List<Integer[]> lists = new ArrayList<Integer[]>();
    lists.add(l1);
    lists.add(l2);
    lists.add(l3);
    int result = KthSmallestInMSortedArrays.findKthSmallest(lists, 5);
    System.out.print("Kth smallest number is: " + result);
  }
}
