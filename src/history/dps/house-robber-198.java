class Solution {
    public int rob(int[] nums) {
        //dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        //dp[i + 1] = max(dp[i - 1] + nums[i + 1], dp[i])
        //...
        // temp = max(prev + nums[i], cur)
        // prev = cur
        //  cur = temp
        //return cur
        
        int temp = 0, cur = 0, prev = 0;
        
        for(int i = 0; i < nums.length; i++){
            temp = Math.max(prev + nums[i], cur);
            prev = cur;
            cur = temp;
        }
        
        return cur;
    }
}