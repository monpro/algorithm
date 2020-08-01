package heap;

import java.util.Arrays;

class Solution {
    /**
    public int[] getStrongest(int[] arr, int k) {
        Arrays.sort(arr);
        int median = arr[(arr.length - 1) / 2];
        
        PriorityQueue<Integer> heap = new PriorityQueue<>((n1, n2) -> {
            if(Math.abs(n1 - median) > Math.abs(n2 - median)) {
                return -1;
            } else if(Math.abs(n1 - median) == Math.abs(n2 - median)) {
                return n2 - n1;
            } else {
                return 1;
            }
        });
        for(int num: arr) {
            heap.add(num);
        }
        
        int[] result = new int[k];
        for(int i = 0; i < k; i++) {
            result[i] = heap.poll();
        }
        return result;
    }
    
    **/
    
    public int[] getStrongest(int[] arr, int k) {
        Arrays.sort(arr);
        int[] result = new int[k];
        int median = arr[(arr.length - 1) / 2];
        
        int start = 0, end = arr.length - 1, index = 0;
        
        while(index < k) {
            if(median - arr[start] > arr[end] - median) {
                result[index++] = arr[start++];
            } else {
                result[index++] = arr[end--];
            }
        }
        return result;
    }
}