class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixSum = new HashMap<>();
        prefixSum.put(0, 1);
        int cur = 0;
        int result = 0;
        for(int i = 0; i < nums.length; i++){
            cur += nums[i];
            if(prefixSum.containsKey(cur - k)){
                result += prefixSum.get(cur - k);
            }
            
            prefixSum.put(cur, prefixSum.getOrDefault(cur, 0) + 1);
        }
        
        return result;
    }
}