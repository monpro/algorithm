package dfs;

import java.util.*;

class Solution {
    int diff = Integer.MAX_VALUE;
    String result = "";
    public String nextClosestTime(String time) {
        Set<Integer> set = new HashSet<>();
        set.add(Character.getNumericValue(time.charAt(0)));
        set.add(Character.getNumericValue(time.charAt(1)));
        set.add(Character.getNumericValue(time.charAt(3)));
        set.add(Character.getNumericValue(time.charAt(4)));
        if(set.size() == 1){
            return time;
        }
        int minutes = Integer.parseInt(time.substring(0, 2)) * 60 + Integer.parseInt(time.substring(3, 5));
        
        dfs(new ArrayList<>(set), "", 0, minutes);
        return result;
    }
    
    public void dfs(List<Integer> set, String cur, int pos, int minutes) {
        if(pos == 4) {
            int curMins = Integer.parseInt(cur.substring(0, 2)) * 60 + Integer.parseInt(cur.substring(2, 4));
            if(curMins == minutes) {
                return;
            }
            int curDiff = curMins > minutes ? curMins - minutes : 1440 - (minutes - curMins);
            
            if(curDiff < diff) {
                diff = curDiff;
                result = cur.substring(0, 2) + ":" + cur.substring(2, 4);
            }
        } else {
            for(int i = 0; i < set.size(); i++){
                if(pos == 0 && set.get(i) > 2) continue;
                if(pos == 1 && Integer.parseInt(cur) * 10 + set.get(i) > 23) continue;
                if(pos == 2 && set.get(i) > 5) continue;
                
                dfs(set, cur + set.get(i), pos + 1, minutes);
            }
        }
    }
}