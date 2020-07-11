package arrays;

import java.util.*;

class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        String cur = folder[0];
        List<String> result = new ArrayList<>();
        result.add(cur);
        
        for(int i = 1; i < folder.length; i++){
            if(!folder[i].startsWith(cur + "/")){
                result.add(folder[i]);
                cur = folder[i];
            }
        }
        
        return result;
    }
}