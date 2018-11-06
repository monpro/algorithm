package double_pointer;

import dfs.N_Queens;

import java.util.*;

public class two_sum_unique_pairs {
    /*
    Given nums = [1,1,2,45,46,46], target = 47
    return 2
    1 + 46 = 47
    2 + 45 = 47
     */
    public int twoSum6(int[] nums, int target) {
        // write your code here
        //对result进行最终去重才可以 [1,1]-- 2
        if(nums.length == 0){
            return 0;
        }
        Arrays.sort(nums);
        int result = 0, left = 0, right = nums.length - 1;
        Map<Integer, Integer> list = new HashMap<>();
        while (left < right){
            if(nums[left] + nums[right] == target){
                if(!list.containsKey(nums[left])){
                    result+= 1;
                    list.put(nums[left],0);
                }
                left++;
                right--;
            }
            else if(nums[left] + nums[right] < target){
                left++;
            }
            else if(nums[left] + nums[right] > target){
                right--;
            }

        }
        //remove duplicates
        return result;
    }
}
