class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if(intervals.length < 2){
            return 0;
        }
        
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        int count = 0;
        
        int end = intervals[0][1];
        
        for(int i = 1; i < intervals.length; i++){
            int[] interval = intervals[i];
            if(interval[0] >= end){
                end = interval[1];
            }
            else{
                count += 1;
            }
        }
        return count;
    }
}