package bfs;

public class search_a_2d_matrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        boolean result = false;
        if(matrix.length == 0 || matrix[0].length == 0){
            return false;
        }

        for(int i = 0; i < matrix.length;i++){
            if( target >= matrix[i][0] && target <= matrix[i][matrix[i].length - 1]){
                result = binary_search(target, matrix[i]);
                return result;

            }
        }

        return false;
    }

    private boolean binary_search(int target, int[] t){
        System.out.println(t[0]);
        System.out.println(t[t.length - 1]);
        int start = 0, end = t.length - 1;
        while(start + 1 < end){
            int mid = start + (end - start)/2;

            if(target > t[mid]){
                start = mid;
            }
            else{
                end = mid;

            }

            System.out.println(mid);
        }
        if(t[start] == target){
            return true;
        }
        else if(t[end] == target){
            return true;
        }
        return false;
    }
}
