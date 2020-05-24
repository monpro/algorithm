package history.heap;

import java.util.*;
class Entry {
    int key;
    int value;
  
    public Entry(int key, int value) {
      this.key = key;
      this.value = value;
    }
  }
  
  class Solution {
      public List<Integer> findClosestElements(int[] arr, int K, int X) {
          List<Integer> result = new ArrayList<>();
          PriorityQueue<Entry> maxHeap = new PriorityQueue<>((n1, n2) -> n2.value - n1.value);
          int index = binarySearch(arr, X);
          int low = Math.max(index - K, 0);
          int high = Math.min(index + K, arr.length - 1);
          for(int i = low; i < low + K; i++){
            maxHeap.add(new Entry(arr[i], Math.abs(arr[i] - X)));
          }
          for(int i = low + K; i <= high; i++){
              Entry entry = new Entry(arr[i], Math.abs(arr[i] - X));
              if(maxHeap.peek().value > entry.value){
                  maxHeap.poll();
                  maxHeap.add(entry);
              }
          }
          
          maxHeap.forEach((val) -> result.add(val.key));
          Collections.sort(result);
          return result;
      }
      
      public int binarySearch(int[] arr, int X){
          int low = 0, high = arr.length - 1;
          
          while(low <= high){
              int mid = low + (high - low) / 2;
              if(arr[mid] == X){
                  return mid;
              }
              else if(arr[mid] < X){
                  low = mid + 1;
              }else{
                  high = mid - 1;
              }
          }
          return low;
          
      }
  }