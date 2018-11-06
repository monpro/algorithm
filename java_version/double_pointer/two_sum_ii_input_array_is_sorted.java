package double_pointer;

public class two_sum_ii_input_array_is_sorted {
    public int[] twoSum(int[] nums, int target) {
        // write your code here
        if(nums.length == 0){
            return new int[0];
        }
        int[] result = new int[2];
        int left = 0, right = nums.length - 1;
        while (left < right){
            if(nums[left] + nums[right] < target){
                left++;
            }
            else if(nums[left] + nums[right] > target){
                right--;
            }
            else if(nums[left] + nums[right] == target){
                result[0] = left;
                result[1] = right;
                return result;
            }
        }
        return result;
    }
}
