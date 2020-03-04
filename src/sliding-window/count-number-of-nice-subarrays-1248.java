class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }
    
    public int atMostK(int[] nums, int k){
        int left = 0, result = 0;
        
        for(int right = 0; right < nums.length; right++){
            k -= nums[right] % 2;
            
            while(k < 0){
                k += nums[left] % 2;
                left += 1;
            }
            // k == 0, find the window 
            result += right - left + 1;
        }
        
        return result;
    }

    public int numberOfSubarrays(int[] A, int k, boolean flag) {
        int result = 0, left = 0,  count = 0;
        
        for(int right = 0; right < A.length; right ++){
            if(A[right] % 2 == 1){
                k -= 1;
                count = 0;
            }
            while(k == 0){
                k += A[left++] % 2;
                count += 1;
            }
            result += count;
        }

        return result;
    }
}