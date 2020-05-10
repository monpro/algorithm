class Solution {
    public int firstMissingPositive(int[] nums) {
        if(nums.length == 0){
            return 1;
        }
        int index = 0;
        while(index < nums.length){
          int indexShouldAt = nums[index] - 1;
          if(nums[index] > 0 && nums[index] <= nums.length && nums[index] != nums[nums[index] - 1]){
            swap(nums, index, nums[index] - 1);
          }else{
            index += 1;
          }
        }

        for(int i = 0; i < nums.length; i++){
          if(nums[i] != i + 1){
            return i + 1;
          }
        }
        return nums.length + 1;
    }
    
  public static void swap(int[] array, int i, int j){
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}