package permutation;

import java.util.*;

class Solution {
    public List<String> wordSubsets(String[] A, String[] B) {
        List<String> result = new ArrayList<>();
        int[] count = new int[26];
        int[] temp;
        
        for(String string: B){
            temp = getCounter(string);
            for(int i = 0; i < 26; i++){
                count[i] = Math.max(count[i], temp[i]);
            }
        }
        
        for(String string: A){
            temp = getCounter(string);
            
            for(int i = 0; i < 26; i++){
                if(temp[i] < count[i]){
                    break;
                }
                if(i == 25){
                    result.add(string);
                }
            }
            
        }
        
        return result;
    }
    
    
    public int[] getCounter(String string){
        int[] result = new int[26];
        for(char ch: string.toCharArray()){
            result[ch - 'a'] += 1;
        }
        return result;
    }
}