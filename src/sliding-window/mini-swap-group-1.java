class Solution {
    public int minSwaps(int[] data) {
        int window = 0;
        for(int num: data){
            if(num == 1){
                window += 1;
            }
        }
        
        int left = 0;
        int count = 0;
        int maxCount = Integer.MIN_VALUE;
        for(int right = 0; right < data.length; right++){
            if(data[right] == 1){
                count += 1;
            }
            
            maxCount = Math.max(count, maxCount);
            
            if(right - left + 1 == window){
                if(data[left] == 1){
                    count -= 1;
                }
                left += 1;
            }
            
        }
        
        return window - maxCount;
    }
}