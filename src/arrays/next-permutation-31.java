class Solution {
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return;
        }        
        int i = nums.length -1;
        while( i>= 1 && nums[i - 1] >= nums[i]){
            i -= 1;
        }
        if(i == 0){
            reverse(nums, 0, nums.length - 1);
        }
        else{
            int j = nums.length - 1;
            while(nums[j] <= nums[i - 1]){
                j--;
            }
            swap(nums, i - 1, j);
            reverse(nums, i, nums.length - 1);
        }
    }
    
    
    public void reverse(int[] nums, int i, int j){
        while(i < j){
            swap(nums, i++, j--);
        }
    }
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}