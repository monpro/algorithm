class Solution {
    public int findLucky(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        int result = -1;
        for(int i : arr)
            map.put(i, map.getOrDefault(i, 0) + 1);
        
        for(int i : arr){
            if(map.get(i) == i)
                result = Math.max(result, i);
        }
        
        return result;
    }
}