import java.util.*;

class Solution {
    public String minWindow(String str, String pattern) {
        Map<Character, Integer> visited = new HashMap<>();
        for(char c: pattern.toCharArray()){
          visited.put(c, visited.getOrDefault(c, 0) + 1);
        }

        int start = 0, smallestLength = Integer.MAX_VALUE;
        int match = 0;
        String result = "";
        char[] arr = str.toCharArray();
        for(int end = 0; end < arr.length; end++){
          if(visited.containsKey(arr[end])){
            visited.put(arr[end],visited.get(arr[end]) - 1);
            if(visited.get(arr[end]) == 0){
              match += 1;
            }
          }

          while(match == visited.size()){
            if(end - start + 1 < smallestLength){
              smallestLength = end - start + 1;
              result = str.substring(start, end + 1);
            }

            if(visited.containsKey(arr[start])){
              if(visited.get(arr[start]) == 0){
                match -= 1;
              }
              visited.put(arr[start], visited.get(arr[start]) + 1);
            }
            start += 1;
          }
        } 
        return result;
    }
}