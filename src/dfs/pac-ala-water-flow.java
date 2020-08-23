package dfs;

import java.util.*;

class Solution {
    int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        List<List<Integer>> result = new ArrayList<>();
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }
        int m = matrix.length, n = matrix[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        
        for(int i = 0; i < m; i++){
            dfs(matrix, pacific, i, 0, Integer.MIN_VALUE);
            dfs(matrix, atlantic, i, n - 1, Integer.MIN_VALUE);
        }
        
        for(int i = 0; i < n; i++) {
            dfs(matrix, pacific, 0, i, Integer.MIN_VALUE);
            dfs(matrix, atlantic, m - 1, i, Integer.MIN_VALUE);
        }
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(pacific[i][j] && atlantic[i][j]) {
                    result.add(Arrays.asList(new Integer[]{i, j}));
                }
            }
        }
        return result;
    }
    
    public void dfs(int[][] matrix, boolean[][] visited, int i, int j, int minHeight) {
        if(i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length || matrix[i][j] < minHeight || visited[i][j]){
            return;
        }
        visited[i][j] = true;
        for(int[] dir: dirs) {
            dfs(matrix, visited, i + dir[0], j + dir[1], matrix[i][j]);
        }
    }
}