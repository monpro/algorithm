package bfs;

import java.util.*;

class Solution {
    public int maximumMinimumPath(int[][] A) {
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int m = A.length, n = A[0].length;
        Queue<int[]> queue = new PriorityQueue<>((n1, n2) -> n2[2] - n1[2]);
        
        queue.offer(new int[]{0, 0, A[0][0]});
        boolean[][] visited = new boolean[m][n];
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            if(cur[0] == m - 1 && cur[1] == n - 1){
                return cur[2];
            }
            for(int[] dir: directions){
                int nextRow = cur[0] + dir[0];
                int nextCol = cur[1] + dir[1];
                
                if(nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n && !visited[nextRow][nextCol]){
                    visited[nextRow][nextCol] = true;
                    queue.offer(new int[]{nextRow, nextCol, Math.min(cur[2], A[nextRow][nextCol])});
                }
            }
        }
        
        return -1;
    }
}