package arrays;

class Solution {
    /**
    public int arrayNesting(int[] nums) {
        // that is -> dfs 
        int n = nums.length;
        int maxLength = Integer.MIN_VALUE;
        boolean[] visited = new boolean[n];
        
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                maxLength = Math.max(maxLength, helper(nums, i, visited));
            }
        }
        
        return maxLength;
    }
    
    public int helper(int[] nums, int index, boolean[] visited){
        int count = 0;
        int start = index;
        while(count == 0 || index != start){
            count += 1;
            visited[index] = false;
            index = nums[index];
        }
        
        return count;
    }
    **/
    public int arrayNesting(int[] nums) {
        int n = nums.length;
        int maxLength = Integer.MIN_VALUE;
        boolean[] visited = new boolean[n];
        
        for(int num: nums){
            int length = 0;
            while(!visited[num]){
                visited[num] = true;
                length += 1;
                num = nums[num];
            }
            maxLength = Math.max(maxLength, length);
        }
        
        return maxLength;
    }
    
    
}