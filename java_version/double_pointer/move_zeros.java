package double_pointer;

public class move_zeros {
    public void moveZeroes(int[] nums) {
        // write your code here
        /*
        Given nums = [0, 1, 0, 3, 12],
        after calling your function,
        nums should be [1, 3, 12, 0, 0].
         */
        int index = 0;
        for(int i = 0; i < nums.length;i++){
            if(nums[i] != 0){
                nums[index] = nums[i];
                index++;
            }
        }
        for(int i = index; i < nums.length;i++){
            nums[i] = 0;
        }
    }
}
