package bfs;

import java.util.*;

class Solution {
    public int minTotalDistance(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        
        List<Integer> row = new ArrayList<>();
        List<Integer> col = new ArrayList<>();
        
        // for(int i = 0; i < m; i++){
        //     for(int j = 0; j < n; j++){
        //         if(grid[i][j] == 1){
        //             row.add(i);
        //             col.add(j);
        //         }
        //     }
        // }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    row.add(i);
                }
            }
        }
        
        for(int j = 0; j < n; j++){
            for(int i = 0; i < m; i++){
                if(grid[i][j] == 1){
                    col.add(j);
                }
            }
        }
        
        return getMedian(row) + getMedian(col);
    }
    
    public int getMedian(List<Integer> nums){
        // Collections.sort(nums);
        
        // x1 x2 m x3 x4 -> x4 - m + x3 - m + m - x2 + m - x1 -> x4 - x1 + x3 - x2
        
        int i = 0, j = nums.size() - 1;
        int result = 0;
        while(i < j){
            result += nums.get(j--) - nums.get(i++);
        }
        
        return result;
    }
}