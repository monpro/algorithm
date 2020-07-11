package arrays;

import java.util.Arrays;

class Solution {
    public int minMeetingRooms(int[][] intervals) {
        // when start a meeting, we need a room
        // before adding a room, we need to check whether we could reuse one
        // if curStart < curEnd, the meeting is on going, we need a new room
        // if curStart >= curEnd, prev meeting is ended, we reuse this room
        // when we reuse this room, we move curEnd, because it's already taken
        
        
        int n = intervals.length;
        int[] start = new int[n];
        int[] end = new int[n];
        
        for(int i = 0; i < n; i++){
            start[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }
        
        Arrays.sort(start);
        Arrays.sort(end);
        
        int result = 0;
        int endIndex = 0;
        
        for(int i = 0; i < n; i++){
            if(start[i] < end[endIndex]){
                result += 1;
            }
            else{
                endIndex += 1;
            }
        }
        return result;
        
    }
    
}