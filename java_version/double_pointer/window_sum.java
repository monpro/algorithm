package double_pointer;

public class window_sum {
    public int[] winSum(int[] nums, int k) {

        /*
        For array [1,2,7,8,5], moving window size k = 3.
        1 + 2 + 7 = 10
        2 + 7 + 8 = 17
        7 + 8 + 5 = 20
        return [10,17,20]
         */
        if(k > nums.length || nums.length == 0){
            return new int[0];
        }
        int[] result = new int[nums.length - k + 1];
        int left = 0, right = k - 1, sum = 0;
        for(int i = left; i <= right; i++){
            sum += nums[i];
        }
        result[left] = sum;
        while (left + 1 + k <= nums.length){
            sum = sum - nums[left];
            right += 1;
            sum = sum + nums[right];
            left += 1;
            result[left] = sum;
        }
        return result;
    }
}
