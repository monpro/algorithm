package arrays;

import java.util.*;

class Solution {
    public List<String> commonChars(String[] A) {
        List<String> result = new ArrayList<>();
        int[] common = getCommon(A[0]);
        
        for(int i = 1; i < A.length; i++){
            int[] current = getCommon(A[i]);
            for(int j = 0; j < 26; j++){
                common[j] = Math.min(common[j], current[j]);
            }
        }
        
        for(int i = 0; i < 26; i++){
            for(int j = 0; j < common[i]; j++){
                result.add(String.valueOf((char)('a' + i)));
            }
        }
        return result;
    }
    
    public int[] getCommon(String a){
        int[] common = new int[26];
        
        for(int i = 0; i < a.length(); i++){
            common[a.charAt(i) - 'a'] += 1;
        }
        
        return common;
    }
}