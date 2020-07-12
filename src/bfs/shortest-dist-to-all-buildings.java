package bfs;

import java.util.*;

class Solution {
    public int shortestDistance(int[][] grid) {
        int[][] direction = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int numBuildings = 0;
        int m = grid.length, n = grid[0].length;
        int[][] distance = new int[m][n];
        int[][] building = new int[m][n];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    numBuildings += 1;
                    Queue<int[]> queue = new LinkedList<>();
                    queue.offer(new int[]{i, j});
                    
                    boolean[][] visited = new boolean[m][n];
                    
                    int level = 1;
                    
                    while(!queue.isEmpty()){
                        int size = queue.size();
                        for(int k = 0; k < size; k++){
                            int[] cur = queue.poll();
                            for(int[] dir: direction){
                                int nextRow = cur[0] + dir[0];
                                int nextCol = cur[1] + dir[1];
                                
                                if(nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n &&
                                   grid[nextRow][nextCol] == 0 && !visited[nextRow][nextCol]){
                                    visited[nextRow][nextCol] = true;
                                    distance[nextRow][nextCol] += level;
                                    building[nextRow][nextCol] += 1;
                                    queue.offer(new int[]{nextRow, nextCol});
                                }
                            }
                        }
                        level += 1;
                    }
                    
                }
            }
        }
        
        int result = Integer.MAX_VALUE;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(building[i][j] == numBuildings && grid[i][j] == 0){
                    result = Math.min(result, distance[i][j]);
                }
            }
        }
        
        
        return result == Integer.MAX_VALUE? -1: result;
    }
}