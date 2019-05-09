package set;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class fourSum_18 {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 3; i++){
            if(i > 0 && nums[i] == nums[i - 1]){
                continue;
            }
            for(int j = i + 1; j < nums.length - 2; j++){
                if(j > i + 1 && nums[j] == nums[j - 1]){
                    continue;
                }
                int twoSumTarget = target - nums[i] - nums[j];
                int minTwoSum = nums[j + 1] + nums[j + 2];
                int maxTwoSum = nums[nums.length - 1] + nums[nums.length - 2];
                if(twoSumTarget < minTwoSum || twoSumTarget > maxTwoSum){
                    continue;
                }
                int m = j + 1, n = nums.length - 1;
                while (m < n){
                    int twoSum = nums[m] + nums[n];
                    if(twoSum < twoSumTarget){
                        while (m < n && nums[m] == nums[m + 1]){
                            m ++;
                        }
                        m ++;
                    }
                    else if(twoSum > twoSumTarget){
                        while (m < n && nums[n] == nums[ n - 1]){
                            n --;
                        }
                        n --;
                    }
                    else{
                        result.add(new LinkedList<>(Arrays.asList(nums[i],nums[j],nums[m],nums[n])));
                        while (m < n && nums[m] == nums[m + 1]){
                            m ++;
                        }
                        while (m < n && nums[n] == nums[n - 1]){
                            n --;
                        }
                        m++;
                        n--;
                    }
                }
            }
        }
        return result;
    }
}
