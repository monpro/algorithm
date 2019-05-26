package Linked_List_Array;

import java.util.Arrays;

public class threeSumClosest_16 {
    public int threeSumClosest(int[] nums, int target) {
        int result = nums[0] + nums[1] + nums[nums.length - 1];
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++){
            int left = i + 1, right = nums.length - 1;
            while (left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == target) return target;
                else if(sum > target) right --;
                else left ++;

                if(Math.abs(sum - target) < Math.abs(result - target))
                    result = sum;
            }
        }
        return result;
    }
}
