package arrays;

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        // trip [seat, start, end]
        
        int[] remain = new int[1001];
        
        for(int[] trip: trips){
            remain[trip[1]] += trip[0];
            remain[trip[2]] -= trip[0];
        }
        
        
        for(int i = 0; i < 1001; i++){
            capacity -= remain[i];
            if(capacity < 0){
                return false;
            }
        }
        
        return true;
    }
}