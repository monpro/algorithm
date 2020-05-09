class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();
        int index = 0;
        while(index < nums.length){
            int indexShouldAt = nums[index] - 1;
            if(nums[index] != nums[indexShouldAt]){
                swap(nums, index, indexShouldAt);
            }else{
                index += 1;
            }
        }
        
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != i + 1){
                result.add(nums[i]);
            }
        }
        return result;
    }
    
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}