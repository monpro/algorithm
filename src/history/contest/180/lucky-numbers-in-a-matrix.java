class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        int[] minRow = new int[50];
        int[] maxCol = new int[50];
        for(int i = 0; i < m; i++){
            int val = matrix[i][0];
            for(int j = 0; j < n; j++){
                val = Math.min(val, matrix[i][j]);
            }
            minRow[i] = val;
            // System.out.println(val);
        }
        
        for(int i = 0; i < n; i++){
            int val = matrix[0][i];
            for(int j = 0; j < m; j++){
                val = Math.max(val, matrix[j][i]);
            }
            maxCol[i] = val;
            // System.out.println("col" + val);
        }
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(minRow[i] == maxCol[j]){
                    result.add(minRow[i]);
                }
            }
        }
        
        return result;
    }
}