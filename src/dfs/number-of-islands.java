package dfs;

import java.util.*;

class Solution {
    int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public int numDistinctIslands(int[][] grid) {
        Set<String> set = new HashSet<>();
        int result = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    StringBuilder sb = new StringBuilder();
                    helper(grid, i, j, 0, 0, sb);
                    String string = sb.toString();
                    if(!set.contains(string)){
                        set.add(string);
                        result += 1;
                    }
                    
                }
            }
        }
        
        return result;
    }
    
    public void helper(int[][] grid, int i, int j, int xDir, int yDir, StringBuilder sb){
        grid[i][j] = 0;
        sb.append(xDir + "" + yDir);
        for(int[] dir: directions){
            int x = i + dir[0];
            int y = j + dir[1];
            
            if(x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == 0){
                continue;
            }
            
            helper(grid, x, y, xDir + dir[0], yDir + dir[1], sb);
        }
    }
    
}