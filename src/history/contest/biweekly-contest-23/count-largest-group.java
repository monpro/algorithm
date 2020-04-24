class Solution {
    public int countLargestGroup(int n) {
        // 9 + 9 + 9 + 9 = 36 
        int[] count = new int[37];
        int maxSum = 0;
        for(int i = 1; i <= n; i++){
            int numSum = getSum(i);
            count[numSum] += 1;
            maxSum = Math.max(maxSum, count[numSum]);
        }
        
        int result = 0;
        for(int i = 0; i < 36; i++){
            if(count[i] == maxSum)
                result += 1;
        }
        
        return result;
    }
    
    public int getSum(int num){
        String numString = Integer.toString(num);
        int result = 0;
        for(char ch: numString.toCharArray()){
            result += Character.getNumericValue(ch);
        }
        return result;
    }
}