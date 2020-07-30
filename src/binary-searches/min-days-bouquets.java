class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        if(bloomDay.length < m * k) {
            return -1;
        }
        int maxValue = Integer.MIN_VALUE;
        int minValue = Integer.MAX_VALUE;
        
        for(int val: bloomDay) {
            maxValue = Math.max(val, maxValue);
            minValue = Math.min(val, minValue);
        }
        
        int start = minValue, end = maxValue;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            
            int bouquets = getBouquets(bloomDay, mid, k);
            if(bouquets < m) {
                start = mid;
            }
            else {
                end = mid;
            }
        }
        // System.out.println(start);
        // System.out.println(end);
        // System.out.println(getBouquets(bloomDay, start, k));
        if(getBouquets(bloomDay, start, k) == m) {
            return start;
        } else {
            return end;
        }
    }
    
    public int getBouquets(int[] bloomDay, int day, int k) {
        int flowers = 0, bouquets = 0;
        
        for(int value: bloomDay) {
            
            if(value <= day) {
                flowers += 1;
            } else {
                flowers = 0;
            }
            
            if(flowers == k) {
                bouquets += 1;
                flowers = 0;
            }
            
        }
        
        return bouquets;
    }
}