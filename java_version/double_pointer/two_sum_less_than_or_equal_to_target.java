package double_pointer;

import java.util.Arrays;

public class two_sum_less_than_or_equal_to_target {
    public int twoSum5(int[] nums, int target) {
        // write your code here
        /**
         *Given nums = [2, 7, 11, 15], target = 24.
         Return 5.
         2 + 7 < 24
         2 + 11 < 24
         2 + 15 < 24
         7 + 11 < 24
         7 + 15 < 25
         **/
        int result = 0;
        Arrays.sort(nums);
        int left = 0, right = nums.length - 1;
        while (left < right){
            if(nums[left] + nums[right] <= target){
                result += right- left;
                left++;
            }
            else{
                right--;
            }
        }
        return result;

    }
}
