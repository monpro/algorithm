package strings;

import java.util.List;

class Solution {
    public int findMinDifference(List<String> timePoints) {
        boolean[] buckets = new boolean[24 * 60];
        for(String time: timePoints){
            String[] t = time.split(":");
            int hour = Integer.parseInt(t[0]);
            int min = Integer.parseInt(t[1]);
            int point = hour * 60 + min;
            if(buckets[point]){
                return 0;
            }
            buckets[point] = true;
        }
        
        int firstTime = Integer.MAX_VALUE, lastTime = Integer.MIN_VALUE;
        int diff = Integer.MAX_VALUE, prev = -1;
        
        for(int i = 0; i < 24 * 60; i++){
            if(buckets[i]){
                if(prev != -1){
                    diff = Math.min(diff, i - prev);
                }
                firstTime = Math.min(firstTime, i);
                lastTime = Math.max(lastTime, i);
                prev = i;
            }
        }
        
        return Math.min(diff, 24 * 60 + firstTime - lastTime);
        
        
    }
}