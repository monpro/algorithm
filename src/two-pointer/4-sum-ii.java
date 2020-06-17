class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int i = 0; i < A.length; i ++){
            for(int j = 0; j < B.length; j++){
                count.put(-A[i] - B[j], count.getOrDefault(-A[i] - B[j], 0) + 1);
            }
        }
        
        int result = 0;
        for(int i = 0; i < C.length; i++){
            for(int j = 0; j < D.length; j++){
                result += count.getOrDefault(C[i] + D[j], 0);
            }
        }
        
        return result;
    }
}