class Solution {
    public int consectuiveK(int[] array, int k) {
        if(array.length < k){
            return -1;
        }
        int maxSum = 0;
        for(int i = 0; i < k; i++){
            maxSum += array[i];
        }

        int currentWindow = maxSum;
        for(int i = k; i < array.length; i++){
            currentWindow += array[i] - array[i - k];
            maxSum = Math.max(maxSum, currentWindow);
        }
        
        return maxSum;
    }
}