class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n = nums.length;
        int low = 0, high = n / 2;
        
        while(low < high){
            int mid = low + (high - low) / 2;
            if(nums[2* mid] != nums[2* mid + 1]){
                high = mid;
            }else{
                low = mid + 1;
            }
        } 
        return nums[2 * low];
    }
}