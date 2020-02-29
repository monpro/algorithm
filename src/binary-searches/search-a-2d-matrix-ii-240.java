class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length == 0 || matrix[0].length == 0)
            return false;
        
        int row = matrix.length, col = matrix[0].length;
        int m = 0, n = col - 1;
        
        while(m < row && n >= 0){
            int mid = matrix[m][n];
            if(mid > target)
                n -= 1;
            else if(mid < target)
                m += 1;
            else
                return true;
        }
        
        return false;
    }
}