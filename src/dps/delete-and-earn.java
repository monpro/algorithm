class Solution {
    public int deleteAndEarn(int[] nums) {
        int[] bucket = new int[10001];
        
        for(int num: nums){
            bucket[num] += num;
        }
        
        int prev = 0, temp = 0, cur = 0;
        for(int i = 0; i <=10000; i++){
            temp = cur;
            cur = Math.max(bucket[i] + prev, cur);
            prev = temp;
        }
        
        return cur;
        
    }
}