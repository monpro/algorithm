package heap;

import java.util.*;

class LargestPairs {

  public static List<int[]> findKLargestPairs(int[] nums1, int[] nums2, int k) {
    PriorityQueue<int[]> minHeap = new PriorityQueue<>((p1, p2) -> p1[0] + p1[1] - p2[0] - p2[1]);

    for(int i = 0; i < k && i < nums1.length; i++){
      for(int j = 0; j < k && j < nums2.length; j++){
        if(minHeap.size() < k){
          minHeap.add(new int[]{nums1[i], nums2[j]});
        }else{
          if(nums1[i] + nums2[j] < minHeap.peek()[0] + minHeap.peek()[1]){
            break;
          }else{
            minHeap.poll();
            minHeap.add(new int[]{nums1[i], nums2[j]});
          }
        }
      }
    }    
    return new ArrayList<>(minHeap);
  }

  public static void main(String[] args) {
    int[] l1 = new int[] { 9, 8, 2 };
    int[] l2 = new int[] { 6, 3, 1 };
    List<int[]> result = LargestPairs.findKLargestPairs(l1, l2, 3);
    System.out.print("Pairs with largest sum are: ");
    for (int[] pair : result)
      System.out.print("[" + pair[0] + ", " + pair[1] + "] ");
  }
}