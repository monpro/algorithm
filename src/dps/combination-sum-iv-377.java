class Solution {
    public int combinationSum4(int[] nums, int target) {
        
        int[] dp = new int[target + 1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        
        return helper(nums, target, dp);
    }
    
    private int helper(int[] nums, int target, int[] dp){
        if(target == 0)
            return dp[0];
        
        if(dp[target] != -1)
            return dp[target];
        int result = 0;
        for(int i = 0; i < nums.length; i++){
            if(target >= nums[i])
                result += helper(nums, target - nums[i], dp); 
        }
        dp[target] = result;
        
        return result;
    }
}