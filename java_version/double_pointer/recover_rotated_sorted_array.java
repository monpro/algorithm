package double_pointer;

import java.util.List;

public class recover_rotated_sorted_array {
    /*
    Given a rotated sorted array, recover it to sorted array in-place.
    Example
    [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
    Challenge
    In-place, O(1) extra space and O(n) time.
     */
    public void recoverRotatedSortedArray(List<Integer> nums) {
        // write your code here
        //[4,5,1,2,3] -- [5,4,1,2,3] == [5,4,3,2,1] -= [1,2,3,4,5]
        int left = 0;
        while (left < nums.size() - 1){
            if(nums.get(left) > nums.get(left + 1)){
                break;
            }
            left++;
        }
        //left is target
        rotate(nums,0,left);
        rotate(nums, left+1, nums.size() -1);
        rotate(nums,0,nums.size() -1);

    }

    private void rotate(List<Integer> nums, int start, int end){
        while (start < end){
            int temp = nums.get(start);
            nums.set(start,nums.get(end));
            nums.set(end,temp);
            start++;
            end--;
        }
    }
}
