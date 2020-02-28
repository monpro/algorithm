class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length == 0 || matrix[0].length == 0)
            return false;
        int row = matrix.length, col = matrix[0].length;
        //corner case
        int left = -1, right = row * col;
        
        while(left + 1 < right){
            int mid = left + (right - left) / 2;
            int midRow = mid / col, midCol = mid % col;
            if(matrix[midRow][midCol] < target)
                left = mid;
            else if(matrix[midRow][midCol] > target)
                right = mid;
            else
                return true;
        }
        
        return false;
        
    }
}