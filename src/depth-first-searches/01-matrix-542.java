class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        if(matrix.length == 0 || matrix[0].length == 0)
            return matrix;
        int row = matrix.length, col = matrix[0].length;
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(matrix[i][j] == 1){
                    if(!hasZeroNeighbor(matrix, i, j)){
                        matrix[i][j] = Integer.MAX_VALUE;
                    }
                }
            }
        }
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(matrix[i][j] == 1){
                    dfs(matrix, i, j, 1);
                }
            } 
        }
        
        return matrix;
    }
    
    public boolean hasZeroNeighbor(int[][] matrix, int i, int j){
        if(i - 1 >= 0 && matrix[i - 1][j] == 0)
            return true;
        if(i + 1 < matrix.length && matrix[i + 1][j] == 0)
            return true;
        if(j - 1 >= 0 && matrix[i][j - 1] == 0)
            return true;
        if(j + 1 < matrix[0].length && matrix[i][j + 1] == 0)
            return true;
        return false;    
    }
    
    public void dfs(int[][] matrix, int i, int j, int distance){
        if(i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length || matrix[i][j] < distance)
            return;
        
        matrix[i][j] = distance;
        
        dfs(matrix, i + 1, j, distance + 1);
        dfs(matrix, i - 1, j, distance + 1);
        dfs(matrix, i, j + 1, distance + 1);
        dfs(matrix, i, j - 1, distance + 1);
    }
}