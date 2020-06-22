package arrays;

class Solution {
    /**
    public int smallestCommonElement(int[][] mat) {
        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;
        // val, count
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int[] row: mat){
            for(int val: row){
                minVal = Math.min(minVal, val);
                maxVal = Math.max(maxVal, val);
                map.put(val, map.getOrDefault(val, 0) + 1);
            }
        }
        
        for(int i = minVal; i< maxVal; i++){
            if(map.containsKey(i)){
                if(map.get(i) == mat.length){
                    return i;
                }
            }    
        }
        return -1;
    }
    **/
    public int smallestCommonElement(int[][] mat) {
        int[] count = new int[10001];
        for(int[] row: mat){
            for(int val: row){
                count[val] += 1;
                if(count[val] == mat.length){
                    return val;
                }
            }
        }
        return -1;
    }
}