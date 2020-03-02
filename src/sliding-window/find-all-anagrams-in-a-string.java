import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] count = new int[26];
        for(int i = 0; i < p.length(); i++){
            count[p.charAt(i) - 'a'] += 1;
        }
        List<Integer> result = new ArrayList<>();
        for(int left = 0, right = 0; right < s.length(); right++){
            int rightPos = s.charAt(right) - 'a';
            count[rightPos] -= 1;
            
            while(count[rightPos] < 0){
                int leftPos = s.charAt(left) - 'a';
                count[leftPos] += 1;
                left += 1;
            }
            
            if(right - left + 1 == p.length()){
                result.add(left);
            }
            
        }
        return result;
    }
}