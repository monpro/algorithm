package history.heap;

import java.util.*;
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        int[][] result = new int[K][];
        
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> {
            return a[0] * a[0] + a[1] * a[1] - b[0] * b[0] - b[1] * b[1];
        });
        
        for(int[] point: points){
            minHeap.offer(point);
        }
        
        for(int i = 0; i < K; i++)
            result[i] = minHeap.poll();
        
        return result;
        
    }
}