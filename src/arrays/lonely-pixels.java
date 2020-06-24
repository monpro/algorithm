package arrays;

class Solution {
    public int findLonelyPixel(char[][] picture) {
        int m = picture.length, n = picture[0].length;
        int[] rowCount = new int[m];
        int[] colCount = new int[n];
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(picture[i][j] == 'B'){
                    rowCount[i] += 1;
                    colCount[j] += 1;
                }
            }
        }
        
        int result = 0;
        for(int i = 0; i < m; i++){
            if(rowCount[i] != 1){
                continue;
            }
            for(int j = 0; j < n; j++){
                if(picture[i][j] == 'B' && colCount[j] == 1){
                    result += 1;
                    break;

                }
            }
        }
        return result;
    }
}