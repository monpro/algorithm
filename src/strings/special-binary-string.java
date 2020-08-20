package strings;

import java.util.*;

class Solution {
    public String makeLargestSpecial(String S) {
        int count = 0;
        int left = 0;
        List<String> result = new ArrayList<>();
        for(int right = 0; right < S.length(); right++) {
            if(S.charAt(right) == '0') {
                count -= 1;
            } else {
                count += 1;
            }
            
            if(count == 0) {
                result.add("1" + makeLargestSpecial(S.substring(left + 1, right))+ "0");
                left = right + 1;
            }
        }
        
        Collections.sort(result, Collections.reverseOrder());
        return String.join("", result);
    }
}