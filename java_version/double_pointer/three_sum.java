package double_pointer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class three_sum {
    public List<List<Integer>> threeSum(int[] numbers) {
        // write your code here
        /*

        Given an array S of n integers, are there elements a, b, c in S
        such that a + b + c = 0?
        Find all unique triplets in the array which gives the sum of zero.
        Example
        For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
        (-1, 0, 1)
        (-1, -1, 2)
                 */

        List<List<Integer>> result = new ArrayList<>();
        if(numbers.length == 0){
            return result;
        }
        Arrays.sort(numbers);
        for(int i = 0; i < numbers.length;i++){
            if(i > 0 && numbers[i - 1] == numbers[i]){
                continue;
            }
            int left = i + 1, right = numbers.length - 1;
            int target = - numbers[i];
            twoSum(target,left,right,numbers,result);

        }
        return result;
    }
    private void twoSum(int target, int left, int right, int[] numbers, List<List<Integer>> result){
        while (left < right){
            if(numbers[left] + numbers[right] < target){
                left++;
            }
            else if(numbers[left] + numbers[right] > target){
                right--;
            }
            else if(numbers[left] + numbers[right] == target){
                List<Integer> mid = new ArrayList<>();
                mid.add(-target);
                mid.add(numbers[left]);
                mid.add(numbers[right]);
                left++;
                right--;
                result.add(mid);

                while(left < right && numbers[left] == numbers[left - 1]){
                    left++;
                }
                while(left < right && numbers[right] == numbers[right + 1]){
                    right--;
                }
            }
        }
    }
}
