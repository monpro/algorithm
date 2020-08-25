package strings;

import java.util.*;

class Solution {
    public boolean differByOne(String[] dict) {
        Set<String> set = new HashSet<>();
        int n = dict[0].length();
        for(int i = 0; i < n; i++){
            set = new HashSet<>();
            for(String string: dict){
                String temp = string.substring(0, i) + string.substring(i + 1, n);
                if(set.contains(temp)) {
                    return true;
                }
                set.add(temp);
            }
        }
        return false;
    }
}