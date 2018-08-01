package Linked_List_Array;

public class maximum_subarray {
    public int maxSubArray(int[] nums) {
        /*
        Given the array [−2,2,−3,4,−1,2,1,−5,3],
        the contiguous subarray [4,−1,2,1] has the largest sum = 6.
        // write your code here
        */
        if(nums.length == 0){
            return 0;
        }

        int max = Integer.MIN_VALUE, sum = 0;
        for(Integer i: nums){
            sum += i;
            max = Math.max(sum,max);
            sum = Math.max(sum,0);
        }
        return max;



    }
}
