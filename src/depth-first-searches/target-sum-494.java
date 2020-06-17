class Solution {
    int result = 0;
    public int findTargetSumWays(int[] nums, int S) {
        if(nums.length == 0)
            return 0;
        
        dfs(nums, S, 0, 0);
        return result;
    }
    
    public void dfs(int[] nums, int S, int temp, int k){

        if(k == nums.length){
            if(temp == S){
                result += 1;
            }
            return;
        }
        
        dfs(nums, S, temp + nums[k], k + 1);
        dfs(nums, S, temp - nums[k], k + 1);
    }
}