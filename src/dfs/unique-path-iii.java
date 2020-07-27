package dfs;

class Solution {
    int result = 0;
    int empty = 1;
    public int uniquePathsIII(int[][] grid) {
        int startX = 0, startY = 0;
        
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 0){
                    empty += 1;
                } else if (grid[i][j] == 1){
                    startX = i;
                    startY = j;
                }
            }
        }
        
        dfs(grid, startX, startY);
        return result;
    }
    
    public void dfs(int[][] grid, int x, int y){
        if(x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == -1){
            return;
        }
        
        if(grid[x][y] == 2){
            if(empty == 0){
                result += 1;
            }
            return;
        }
        
        grid[x][y] = -1;
        empty -= 1;
        dfs(grid, x + 1, y);
        dfs(grid, x - 1, y);
        dfs(grid, x, y + 1);
        dfs(grid, x, y - 1);
        grid[x][y] = 0;
        empty += 1;
    }
}