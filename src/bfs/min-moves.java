package bfs;

import java.util.Arrays;

class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        
        int i = 0, j = nums.length - 1;
        int result = 0;
        
        while(i < j){
            result += nums[j--] - nums[i++];
        }
        
        return result;
    }
}