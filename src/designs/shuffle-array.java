package designs;

import java.util.Random;

class Solution {
    int[] originalArray;
    Random r;
    public Solution(int[] nums) {
        originalArray = nums;
        r = new Random();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return originalArray;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int[] shuffelArray = originalArray.clone();
        for(int i = shuffelArray.length - 1; i >= 0; i--){
            int j = r.nextInt(i + 1);
            
            int temp = shuffelArray[i];
            shuffelArray[i] = shuffelArray[j];
            shuffelArray[j] = temp;
        }
        
        return shuffelArray;
    }
}