package arrays;

class Solution {
    public int[] runningSum(int[] nums) {
        int[] prefix = new int[nums.length];
        prefix[0] = nums[0];
        for(int i = 1; i < nums.length; i++){
            prefix[i] = prefix[i - 1];
            prefix[i] += nums[i];
        }
        
        return prefix;
    }
}