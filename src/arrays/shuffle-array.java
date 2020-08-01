package arrays;

class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[nums.length];
        int pointerX = 0;
        int pointerY = n;
        int index = 0;
        
        while(index < nums.length) {
            result[index++] = nums[pointerX++];
            result[index++] = nums[pointerY++];
        } 
        
        return result; 
    }
}