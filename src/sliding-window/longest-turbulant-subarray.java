class Solution {
    public int maxTurbulenceSize(int[] A) {
        int inc = 1, desc = 1, result = 1;
        
        for(int i = 1; i < A.length; i++){
            if(A[i - 1] < A[i]){
                inc = desc + 1;
                desc = 1;
            }
            else if(A[i - 1] > A[i]){
                desc = inc + 1;
                inc = 1;
            }
            else{
                inc = 1;
                desc = 1;
            }
            
            result = Math.max(result, Math.max(inc, desc));
        }
        return result;
    }
}