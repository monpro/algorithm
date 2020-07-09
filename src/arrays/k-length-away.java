package arrays;

class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        if(nums == null){
            return true;
        }
        int prev = -1;
        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                if(prev != -1 && i - prev <= k){
                    return false;
                }
                prev = i;
            }
        }
        
        return true;
    }
}