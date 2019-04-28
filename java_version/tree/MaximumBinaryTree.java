package tree;

import java.util.Arrays;

public class MaximumBinaryTree {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if(nums.length == 0){
            return null;
        }

        int digit = getMaxDigit(nums);
        TreeNode root = new TreeNode(nums[digit]);
        int[] leftArray = Arrays.copyOfRange(nums,0,digit);
        int[] rightArray = Arrays.copyOfRange(nums, digit + 1,nums.length);
        root.left = constructMaximumBinaryTree(leftArray);
        root.right = constructMaximumBinaryTree(rightArray);
        return root;

    }

    private int getMaxDigit(int[] nums){
        int maximum = Integer.MIN_VALUE;
        int digit = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] > maximum){
                maximum = nums[i];
                digit = i;
            }
        }
        return digit;
    }
}
