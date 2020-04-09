class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {

        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int cur = 0;
        for(int i = 0; i < nums.length; i++){
            cur += nums[i];
            if(k != 0)
                cur %= k;
            if(map.containsKey(cur)){
                Integer prev = map.get(cur);
                if(i - prev > 1)
                    return true;
            }else{
                map.put(cur, i);
            }
        }
        
        return false;
    }
}