package dfs;

import java.util.*;

class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        Map<String, List<String>> map = new HashMap<>();
        for(String string: allowed){
            map.putIfAbsent(string.substring(0, 2), new ArrayList<>());
            map.get(string.substring(0, 2)).add(string.substring(2));
        }
        
        return helper(1, bottom, "", map);
    }
    
    public boolean helper(int index, String curLevel, String nextLevel, Map<String, List<String>> map){
        if(curLevel.length() == 1){
            return true;
        }
        if(nextLevel.length() + 1 == curLevel.length()){
            return helper(1, nextLevel, "", map);
        }
        
        List<String> list = map.getOrDefault(curLevel.substring(index - 1, index + 1), new ArrayList<>());
        
        for(String triple: list){
            if(helper(index + 1, curLevel, nextLevel + triple, map)){
                return true;
            }
        }
        return false;
    }
}