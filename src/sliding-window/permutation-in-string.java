import java.util.*;

class Solution {
    public boolean checkInclusion(String pattern, String str) {
        Map<Character, Integer> count = new HashMap<>();
        for(char c: pattern.toCharArray()){
          count.put(c, count.getOrDefault(c, 0) + 1);
        }
        char[] arr = str.toCharArray();
        int start = 0, match = 0;
        for(int end = 0; end < arr.length; end++){
          char ch = arr[end];
            
          if(count.containsKey(ch)){
            count.put(ch, count.get(ch) - 1);
            if(count.get(ch) == 0){
              match += 1;
            }
          }

          if(match == count.size()){
            return true;
          }

          if(end >= pattern.length() - 1){
            if(count.containsKey(arr[start])){
              if(count.get(arr[start]) == 0){
                match -= 1;
              }
              count.put(arr[start], count.get(arr[start]) + 1);
            }
              start += 1;
          }
        }
        return false;
    }
}